import time

from prefect import flow, task


@task
def print_values(values, sleep=2):
    time.sleep(sleep)
    print(values, end="\r")


@flow
def concurrent_flow():
    print_values.submit(["AAAA"] * 15, sleep=1.5)
    print_values.submit(["BBBB"] * 10, sleep=0.5)


concurrent_flow()
