import time

from prefect import flow, task
from prefect_dask.task_runners import DaskTaskRunner


@task
def print_values(values, sleep=1):
    time.sleep(sleep)
    print(values, end="\r")


@flow(task_runner=DaskTaskRunner())
def dask_flow():
    print_values.submit(["AAAA"] * 15, sleep=10)
    print_values.submit(["BBBB"] * 10, sleep=5)


if __name__ == "__main__":
    dask_flow()
