from airflow import DAG 
import airflow
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id = "sparking_flow",
    default_args = {
        "owner": "Raj Salvi",
        "start_date": airflow.utils.dates.days_ago(1)
    },
    schedule_interval = "@daily"
)

start = PythonOperator(
    task_id = "start",
    python_callable=lambda: print("Job Started"),
    dag = dag
)
spark_job = SparkSubmitOperator(
    task_id = "spark-job",
    conn_id= "spark-conn",
    application= "jobs/python/wordcount.py",
    dag = dag
)

end = PythonOperator(
    task_id = "end",
    python_callable=lambda: print("Job Completed Successfully"),
    dag = dag
)

start >> spark_job >> end