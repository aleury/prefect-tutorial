import asyncio

from prefect import flow, task


@task
async def print_values(values):
    for value in values:
        await asyncio.sleep(1)
        print(value, end=" ")


@flow
async def async_flow():
    await print_values([1, 2, 3, 4, 5])

    coros = [print_values("abcd"), print_values("6789")]
    await asyncio.gather(*coros)


asyncio.run(async_flow())
