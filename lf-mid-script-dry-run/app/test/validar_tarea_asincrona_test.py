import asyncio

pending_tasks = asyncio.all_tasks()
for task in pending_tasks:
    print(task)