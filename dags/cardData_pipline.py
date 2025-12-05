from airflow.decorators import dag, task
import pendulum
from airflow.decorators import task
from my_utils.optimized_crawling_crawling import crawling_main
from my_utils.upload_sql_aftercrawling import upload_main
from airflow.operators.python import PythonOperator
import json

@dag(
    dag_id='03_crawling_cardData_pipline',
    tags=['crawling', 'cardData', 'cardGorila', 'taskflow'],
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    schedule="0 9 * * 1", # 월요일마다.
    catchup=False,
)
def getData_pipeline_weekly():
    @task
    def get_cardData():
        crawling_main()

    @task
    def upload_cardData():
        upload_main()


    # @task
    # def get_user_id_list() -> list :
    #     uid_list = get_all_user_id_list()
        
    #     return uid_list


    # @task
    # def update_To_DB(user_list, date_interval):
    #     """알림 DB를 최신화 합니다."""
    #     for user_id in user_list:
    #         try:
                
    #             usage = get_seven_days_usage(user_id)
    #             info = {"title": "주간지출", "content": f"{date_interval}에 총 {usage}원을 썼어요. {'어디에 많이 썼는지 확인하세요' if usage != '0' else ''}"}
    #             json_string = json.dumps(info, ensure_ascii=False)
    #             insert_val_notification(user_id, 3, json_string)
    #         except Exception as error:
    #             print(f"에러가 발생했습니다: {error}")
    #             raise error
        
    crwaling = get_cardData()
    upload = upload_cardData()
    crwaling >> upload
getData_pipeline_weekly()