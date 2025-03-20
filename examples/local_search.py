from langchain_ollama import ChatOllama
from browser_use import Agent
from pydantic import SecretStr
import asyncio

llm = ChatOllama(
    model="qwen2.5:7b",
    base_url="http://localhost:11434",
    #base_url="http://10.239.140.101:8000",
    num_ctx=20000,
    request_timeout=30
)

try:
    response = llm.invoke("请用一句话证明你已成功连接")
    print(f"连接成功！模型响应：{response.content}")
except Exception as e:
    print(f"连接失败，错误信息：{str(e)}")

agent = Agent(
    task="使用百度查一查谁是intel的新CEO?",
    llm=llm,
    save_conversation_path=r"C:\model_deploy\workspace-li\browser-use\examples\logs\conversation",
    max_failures=3
)
async def main():
    result = await agent.run()

asyncio.run(main())