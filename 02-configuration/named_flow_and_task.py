from time import sleep

from prefect import flow, task


@task(
    name="My Example Task",
    description="An example task for a tutorial.",
    tags=["tutorial", "tag-test"],
)
def my_task():
    print("doing some work...")
    sleep(4)
    print("done!")


@flow(
    name="My Example Flow",
    description="An example flow for a tutorial.",
)
def my_flow():
    my_task()


my_flow()
