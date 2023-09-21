Overview
========

Welcome to Astronomer! This project was generated after you ran 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine.


Project Contents
================

Your Astro project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes two example DAGs:
    - `example_dag_basic`: This DAG shows a simple ETL data pipeline example with three TaskFlow API tasks that run daily.
    - `example_dag_advanced`: This advanced DAG showcases a variety of Airflow features like branching, Jinja templates, task groups and several Airflow operators.
- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

# DAGs

The following sections list the DAGs shown sorted by the feature that they showcase. You can filter DAGs in the UI by their `tags`.

### Datasets and Data-Aware Scheduling

DAGs that demonstrate how upstream DAGs and trigger a downstream DAG based on data availability.  For further details see our how-to [documentation](https://docs.astronomer.io/learn/airflow-datasets)

Five DAGs:

- `dataset_upstream1`: Upstream DAG 1 with a simple `BashOperator` as an Outlet
- `dataset_upstream2`: Upstream DAG 2 with two simple `BashOperator`s as Outlets
- `datasets_downstream1`: Simple DAG that is schedule based on the completion of the two upstream Datasets
- `downstream_dataset_taskflow_toy`: Upstream DAG with Outlet using the Taskflow API
- `upstream_dataset_taskflow_toy.py`: Taskflow downstream DAG schedule based on the completion of the above DAG

### Setup/ teardown

DAGs that showcase the `setup` and `teardown` tasks added in Airflow 2.7. For further information see the [setup/teardown guide](https://docs.astronomer.io/learn/airflow-setup-teardown).

Three toy DAGs:

- `toy_setup_teardown_simple`: Shows a very simple setup/ teardown workflow to nest setup/ teardown tasks with empty `@task` tasks.
- `toy_setup_teardown_nesting`: Shows how to nest setup/ teardown tasks with empty `@task` tasks.

### Dynamic Task Mapping

DAGS that highlight how to dynamically generate parallel tasks at runtime with dynamic task mapping.  For further details see the [Dynamic Task Mapping Documentation](https://docs.astronomer.io/learn/dynamic-tasks)

- `dynamic_task_mapping`: This DAG shows 5 different examples for Airflow's dynamic mapping features.
- `task_group_mapping_usecase`: Dynamic tasks mapping in a task group

### Fail/Stop

DAG to demonstrate new parameter that stops DAG execution as soon as one task in this DAG fails.

- `fail_stop`: DAG that has `fail_stop` enabled with tasks that take different amounts of time to finish.

### Other

DAGs that showcase other features.

- `pythonsensor_example`: DAG showing how to create a custom Sensor with the PythonSensor
- `sensor_decorator`: DAG showing how to create a custom Sensor with the Sensor Decorator
- `toy_deferrable_operators_config`: Shows how to use the `deferrable` parameter in the `TriggerDagRunOperator` to defer the execution of a DAG. The config that was added in 2.7 is set to `True` in the Dockerfile `ENV AIRFLOW__OPERATORS__DEFAULT_DEFERRABLE=True`.
- `helper_dag_wait_30_seconds`: DAG that is triggered by the TriggerDagRunOperator in the `toy_deferrable_operators_config` DAG. It waits 30 seconds before completing.

Deploy Your Project Locally
===========================

1. Start Airflow on your local machine by running 'astro dev start'.

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

2. Verify that all 4 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either [stop your existing Docker containers or change the port](https://docs.astronomer.io/astro/test-and-troubleshoot-locally#ports-are-not-available).

3. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.

You should also be able to access your Postgres Database at 'localhost:5432/postgres'.

Deploy Your Project to Astronomer
=================================

If you have an Astronomer account, pushing code to a Deployment on Astronomer is simple. For deploying instructions, refer to Astronomer documentation: https://docs.astronomer.io/cloud/deploy-code/

Contact
=======

The Astronomer CLI is maintained with love by the Astronomer team. To report a bug or suggest a change, reach out to our support.
# stripe-airflow-examples
