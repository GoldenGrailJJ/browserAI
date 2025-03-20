from browser_use import Agent, Browser, BrowserConfig
from langchain_openai import ChatOpenAI
import asyncio
from pydantic import SecretStr
from key.deepseek import *

api_key = get_key()

# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
    )
)

async def run_search():
    agent = Agent(
        task=(

            # "1. 在搜索框中输入抖音并搜索"
            # '2. 点击搜索结果中的第一个链接'
            # '3. 关闭扫码登录'
            # '3. 返回第一个视频的内容'

            '1.在浏览器的地址栏输入 https://www.baidu.com/'
        ),
        llm=ChatOpenAI(
            base_url='https://api.deepseek.com/v1',
            #base_url='http://localhost:8899/v1/chat/completions',
            model='gpt-4o',
            # api_key=SecretStr(api_key),
            api_key = "1"
        ),
        use_vision=False,
    )

    await agent.run()

# Create the agent with your configured browser
# agent = Agent(
#     task="Your task here",
#     llm=ChatOpenAI(model='gpt-4o'),
#     browser=browser,
# )



if __name__ == '__main__':
    asyncio.run(run_search())