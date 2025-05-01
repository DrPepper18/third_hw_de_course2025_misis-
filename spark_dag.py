import os
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from pyspark.sql import SparkSession


def create_spark_session():
    """Создаёт Spark-сессию и выводит её параметры."""
    print(f"hadoop conf dir: {os.environ['HADOOP_CONF_DIR']}")
    spark = (
        SparkSession.builder.appName("SparkHiveExample")
        .enableHiveSupport()
        .getOrCreate()
    )

    print(f"Spark master: {spark.sparkContext.master}")
    print("Spark Session создана!")
    print(f"Версия Spark: {spark.version}")
    spark.stop()
    print("Spark Session остановлена!")


with DAG(
    dag_id="simple_spark_session",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,  # Запускается вручную
    catchup=False,
) as dag:
    # Задача 1: Создать Spark-сессию
    create_session = PythonOperator(
        task_id="create_spark_session",
        python_callable=create_spark_session,
    )
