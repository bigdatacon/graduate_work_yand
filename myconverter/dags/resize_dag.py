import os
from airflow.decorators import dag, task


@dag(schedule_interval="@hourly")
def etl():
    @task()
    def resize() -> str:
        film_uuid = os.getenv("FILM_UUID")
        answer = requests.post(f"http://127.0.0.1:8001/api/v1/modelhandlerapi/resize_full/?file_id={film_uuid}")
        return f'Answer {answer.status_code}: {answer.json()}'


elt_dag = etl()
