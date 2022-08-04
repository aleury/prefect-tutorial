import time

from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner


@task
def print_values(values, sleep=1):
    time.sleep(sleep)
    print(values, end="\r")


@flow(task_runner=SequentialTaskRunner())
def sequential_flow():
    print_values.submit(["AAAA"] * 15, sleep=5)
    print_values.submit(["BBBB"] * 10, sleep=2)


sequential_flow()
