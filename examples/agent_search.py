from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
import os
load_dotenv()

import asyncio

api_key = os.getenv('Silicon_Cloud_API_KEY')
base_url = os.getenv('Base_URL')
model = os.getenv('Model')

llm = ChatOpenAI(model=model, api_key=api_key, base_url=base_url)

async def main():
    agent = Agent(
        task="使用百度搜索告诉我intel最新的CEO是谁？",
        llm=llm,
        use_vision=False,
        save_conversation_path=r"C:\model_deploy\workspace-li\browser-use\examples\logs\conversation_3"
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
