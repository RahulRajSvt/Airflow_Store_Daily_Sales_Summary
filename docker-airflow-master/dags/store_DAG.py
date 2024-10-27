from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.email_operator import EmailOperator
from data_cleaner import data_cleaner

# define dag 
default_args = {
    "owner": "Airflow",
    "start_date": datetime(2024,10,26),
    "retries": 1, 
    "retry_delay": timedelta(seconds=5)
}

dag= DAG('store_dag', default_args=default_args, schedule_interval='@daily',template_searchpath=[
    '/usr/local/airflow/sql_files'], catchup=False)

    # task1: check if the source file exists in the input directory
    # note that the file in airflow container.
t1 = BashOperator(
        task_id="check_file_exists",
        bash_command="shasum ~/store_files_airflow/raw_store_transactions.csv",
        retries=2,
        retry_delay=timedelta(seconds=15), dag=dag)

# task 2: clean data (remove special characters)
    # task 2: clean data (remove special characters)
t2 = PythonOperator( 
        task_id="clean_raw_csv", python_callable =data_cleaner, dag=dag)

    # task 3: create table
t3 = MySqlOperator(
        task_id="create_mysql_table",
        mysql_conn_id="mysql_conn",
        sql="create_table.sql", dag=dag)
 
t4 = MySqlOperator(
        task_id="insert_into_table",
        mysql_conn_id="mysql_conn",
        sql="insert_into_table.sql", dag=dag)
    # task 5: calculate store-wise and location-wise profit (yesterday) and save results as csv
t5 = MySqlOperator(
        task_id="select_from_table",
        mysql_conn_id="mysql_conn",
        sql="select_from_table.sql",dag=dag)

yesterday_date = datetime.strftime(datetime.now() - timedelta(1), "%Y-%m-%d")
    # task 6: rename the location profit output file by adding date
t6 = BashOperator(
        task_id="move_loc_file",
        bash_command="cat ~/store_files_airflow/location_wise_profit.csv && mv "
                     "~/store_files_airflow/location_wise_profit.csv "
                     f"~/store_files_airflow/location_wise_profit_{yesterday_date}.csv",dag=dag)

    # task 7: rename the store profit output file by adding date
t7 = BashOperator(
        task_id="move_store_file",
        bash_command="cat ~/store_files_airflow/store_wise_profit.csv && mv "
                     "~/store_files_airflow/store_wise_profit.csv "
                     f"~/store_files_airflow/store_wise_profit_{yesterday_date}.csv",dag=dag)


    # task 8: send email
t8 = EmailOperator(
        task_id="send_email",
        to="rrj0062@gmail.com",
        subject="Daily report generated",
        html_content="""<h2>Congratulations! Rahul your store "Adhbuth" reports are ready.</h2>                  
                        <p>Please find attached the details in attachment:</p>
                         <img src="cid:my_image" alt="Image description" />""",
        files=[f"/usr/local/airflow/store_files_airflow/location_wise_profit_{yesterday_date}.csv",
               f"/usr/local/airflow/store_files_airflow/store_wise_profit_{yesterday_date}.csv",
               f"/usr/local/airflow/store_files_airflow/rep_img.png"],dag=dag)

    # task 9: rename the raw files as well because it will be updated tomorrow again
t9 = BashOperator(
        task_id="rename_raw",
        bash_command="mv ~/store_files_airflow/raw_store_transactions.csv "
                     f"~/store_files_airflow/raw_store_transactions_{yesterday_date}.csv", dag=dag)


t1 >> t2 >> t3 >> t4 >> t5 >> [t6,t7] >> t8 >> t9