from airflow.decorators import dag, task
import pendulum
import asyncio
from airflow.decorators import task
from my_utils.optimized_crawling_crawling import crawling_main
from my_utils.upload_sql_aftercrawling import upload_main
from my_utils.summary import process_card_summaries
from airflow.operators.python import PythonOperator
import json

@dag(
    dag_id='03_crawling_cardData_pipline',
    tags=['crawling', 'cardData', 'cardGorila', 'taskflow'],
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    schedule="0 1 * * *", # 매 새벽 1시에 진행하도록
    catchup=False,
)
def getData_pipeline_weekly():
    @task
    def get_cardData():
        crawling_main()

    @task
    def upload_cardData():
        upload_main()

    @task
    def summarized_cardmaster_temp():
        asyncio.run(process_card_summaries())
        
    crwaling = get_cardData()
    upload = upload_cardData()
    summary = summarized_cardmaster_temp()

    crwaling >> upload >> summary

    
getData_pipeline_weekly()