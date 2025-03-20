import asyncio
from examples.functions import run_browser_task

async def batch_run_tasks():
    tasks = []
    for i in range(8, 50):  # 创建50个任务
        print(f"start task {i}")
        task = "用百度查一查intel新的CEO是?"
        save_path = fr"C:\model_deploy\workspace-li\browser-use\examples\logs\batch_log_3_20\conversation_{i}"
        tasks.append(
            run_browser_task(
                task=task,
                save_path=save_path,
                max_failures=3
            )
        )

    # 顺序执行所有任务
    results = []
    for idx, task in enumerate(tasks, 1):
        result = await task
        results.append(result)
        print(f"任务 {idx}/50 完成，保存路径: conversation_{idx}")

    return results


if __name__ == "__main__":
    print("开始批量执行浏览器任务...")
    asyncio.run(batch_run_tasks())
    print("所有50个任务执行完成！")