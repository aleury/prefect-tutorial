from datetime import timedelta

from prefect import flow, task
from prefect.tasks import task_input_hash


@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(minutes=1))
def sum_to(n: int) -> int:
    print(f"Summing from 0 to {n}...")

    total = 0
    for x in range(n + 1):
        total += x
    return total


@flow
def sum_flow(n: int) -> int:
    total = sum_to(n)
    return total


print(sum_flow(100_000_000))
