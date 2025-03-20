import asyncio
from langchain_ollama import ChatOllama
from browser_use import Agent


async def run_browser_task(
        task: str,
        save_path: str = r"C:\model_deploy\workspace-li\browser-use\examples\logs\conversation_8",
        max_failures: int = 3
) -> str:
    """执行浏览器自动化任务的封装函数

    Args:
        task: 需要执行的浏览器操作指令
        save_path: 对话记录保存路径(默认使用项目示例路径)
        max_failures: 最大容错次数(默认5次)

    Returns:
        str: 任务执行结果或错误信息

    功能特性：
    - 集成Ollama本地模型服务连接验证
    - 自动处理异步执行和异常捕获
    - 支持自定义日志保存路径
    """
    # 初始化本地模型连接
    llm = ChatOllama(
        model="qwen2.5:7b",
        base_url="http://localhost:11434",  # 网页1推荐的本地部署地址格式
        num_ctx=20000,  # 上下文长度与量化模型匹配
        request_timeout=30
    )

    try:
        response = llm.invoke("请用一句话证明你已成功连接")
        print(f"连接成功！模型响应：{response.content}")
    except Exception as e:
        print(f"连接失败，错误信息：{str(e)}")

    agent = Agent(
        task=task,
        llm=llm,
        use_vision=False,
        save_conversation_path=save_path,
        max_failures=max_failures,
        max_actions_per_step=30
    )

    try:
        result = await agent.run()
        return result
    except Exception as e:
        return f"任务执行失败: {str(e)}"

def query_intel_ceo() -> str:
    """封装为同步调用的查询接口"""
    #task = "使用百度查一查谁是Intel的新CEO?"
    task = "Please use baidu to search the latest CEO of intel"
    return asyncio.run(run_browser_task(task))

# async def main():
#     result = await run_browser_task("用百度查一查intel新的CEO是？")
#     print(result)
#     extracted_data = result.extracted_content()
#     print(extracted_data[-1])
#     print(type(extracted_data[-1]))
#
# asyncio.run(main())