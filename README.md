# Adbhut Project Documentation

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Docker Setup](#docker-setup)
  - [Airflow Setup](#airflow-setup)
  - [MySQL Setup](#mysql-setup)
- [Airflow Workflows](#airflow-workflows)
  - [Workflow Structure](#workflow-structure)
  - [Task Descriptions](#task-descriptions)
- [Database Structure](#database-structure)
- [Data Management](#data-management)
- [Monitoring and Notifications](#monitoring-and-notifications)
- [Conclusion](#conclusion)

## Project Overview
The Adbhut project is dedicated to enhancing the operational efficiency of an online store. It automates critical processes such as data management, report generation, and database interactions. By streamlining these tasks, we ensure that the store can focus on delivering an excellent customer experience.

## Technologies Used
This project utilizes several key technologies:
- **Docker**: A powerful platform that enables us to create, deploy, and manage applications within lightweight containers. This ensures consistency across different environments.
- **Apache Airflow**: A versatile workflow management tool that orchestrates complex data pipelines, making it easy to schedule and automate tasks.
- **MySQL**: A robust relational database management system that stores and manages data related to store transactions and analytics.

## Architecture
The Adbhut project is built on a modular architecture, comprising three main components:
- **Docker Containers**: Each component of the system (Airflow and MySQL) operates within its own container, ensuring isolation and reliability.
- **Airflow**: Manages and automates workflows, ensuring tasks are executed in a timely and organized manner.
- **MySQL**: Serves as the backbone for data storage, holding essential information about transactions, profits, and other metrics.

## Setup Instructions

### Prerequisites
To set up the Adbhut project, ensure you have the following installed on your machine:
- **Docker**: For managing the application containers.
- **Docker Compose**: To handle multi-container applications smoothly.
- **Python**: Required for running Apache Airflow.

### Docker Setup
1. Create a configuration file named `Dockerfile` to set up the Airflow environment.
2. Define a `docker-compose.yml` file to specify how the various containers interact with one another.

### Airflow Setup
1. Initialize the Airflow database to prepare it for storing workflow data.
2. Launch the Airflow web server and scheduler to manage and execute the defined workflows.

### MySQL Setup
1. Access the MySQL database to create the necessary tables that will hold transaction data.
2. Define the structure of these tables according to your data requirements.

## Airflow Workflows

### Workflow Structure
The core workflow, known as `store_dag`, automates a series of tasks related to managing store transactions, ensuring smooth operations on a daily basis.

### Task Descriptions
- **Check for Transaction File**: This task verifies whether the file containing raw transaction data is present in the specified directory.
- **Clean Transaction Data**: Utilizes a Python function to clean the raw data, removing any unwanted characters and formatting issues.
- **Create Database Table**: Executes a SQL script to set up a new table in MySQL for storing the cleaned data.
- **Insert Data into Database**: Saves the processed data into the MySQL table for future analysis and reporting.
- **Calculate Profits**: Computes the store's profits by location and overall from the previous day’s data.
- **Rename Output Files**: Organizes output files by renaming them to include the date, making it easier to track historical records.
- **Send Notification Email**: Sends an email to the store owner, attaching reports of the day’s transactions for their review.
- **Organize Raw Files**: Renames the raw transaction files to include the date, preparing for the next day’s data processing.

## Database Structure
The database is structured to effectively manage various types of data, including:
- **Raw Transactions**: Stores original transaction data received from the store.
- **Cleaned Data**: Contains data that has been processed and cleaned for analysis.
- **Profit Reports**: Holds the calculated results of profits, enabling quick access to important financial metrics.

## Data Management
The project employs a systematic approach to data management, ensuring that data is collected, processed, stored, and reported efficiently. Automated checks are in place to confirm the availability and integrity of necessary files, reducing the risk of errors.

## Monitoring and Notifications
To keep stakeholders informed, the project incorporates a notification system that sends daily email reports to the store owner. This feature allows for real-time insights into the store’s performance, facilitating timely decision-making.

## Conclusion
The Adbhut project leverages modern technologies to streamline the management of an online store. By automating data processing and reporting, it enhances operational efficiency and provides valuable insights, enabling the store to thrive in a competitive marketplace.
