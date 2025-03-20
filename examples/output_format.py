import asyncio
from typing import List

from pydantic import BaseModel
from browser_use import Controller, Agent
from langchain_ollama import ChatOllama
# Define the output format as a Pydantic model
class Post(BaseModel):
	post_title: str
	post_url: str
	num_comments: int
	hours_since_post: int


class Posts(BaseModel):
	posts: List[Post]


controller = Controller(output_model=Posts)


async def main():
	task = '使用百度查一查谁是intel的新CEO?'
	model = ChatOllama(
        model="qwen2.5:latest",
        base_url="http://10.239.140.101:8000",
        num_ctx=20000,
        request_timeout=30
    )
	agent = Agent(task=task, llm=model, controller=controller)

	history = await agent.run()

	result = history.final_result()
	if result:
		parsed: Posts = Posts.model_validate_json(result)

		for post in parsed.posts:
			print('\n--------------------------------')
			print(f'Title:            {post.post_title}')
			print(f'URL:              {post.post_url}')
			print(f'Comments:         {post.num_comments}')
			print(f'Hours since post: {post.hours_since_post}')
	else:
		print('No result')


if __name__ == '__main__':
	asyncio.run(main())