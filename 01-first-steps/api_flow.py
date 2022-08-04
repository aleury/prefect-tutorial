import requests
from prefect import flow, task


@task
def call_api(url: str) -> dict:
    response = requests.get(url)
    print(response.status_code)
    return response.json()


@task
def parse_fact(fact_data: dict) -> str:
    fact = fact_data["fact"]
    print(fact)
    return fact


@flow
def api_flow(url: str) -> dict:
    fact_json = call_api(url)
    fact = parse_fact(fact_json)
    return fact


api_flow("https://catfact.ninja/fact")
