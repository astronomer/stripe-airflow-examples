"""
### Consuming Downstream Datasets

This is an example of a DAG that consumes two datasets.
The DAG only runs once dag1_dataset and dag2_dataset have been updated.

Airflow 2.4 introduced the concept of data driven scheduling. This can be used to have DAGs run based 
on updates to underlying datasets, not cron schedules.
"""

import pendulum

from airflow import DAG, Dataset
from airflow.operators.bash import BashOperator



dag1_dataset = Dataset('s3://dataset1/output_1.txt')
dag2_dataset = Dataset('s3://dataset2/output_2.txt')

with DAG(
    dag_id='dataset_downstream_1_2',
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=[dag1_dataset, dag2_dataset],
    tags=['downstream', "2.4"],
    doc_md=__doc__
) as dag3:

    BashOperator(
        task_id='downstream_2',
        bash_command="sleep 5",
        outlets=[Dataset('s3://downstream_dataset/another_dataset.txt')]
    )