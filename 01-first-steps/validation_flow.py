from prefect import flow, task


@task
def printer(obj: any) -> None:
    print(f"Received a {type(obj)} with value {obj}")


@flow
def validation_flow(x: int, y: str):
    printer(x)
    printer(y)


validation_flow(x="42", y=100)
