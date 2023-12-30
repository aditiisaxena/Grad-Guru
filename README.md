# Grad-Guru
## Introduction
Grad Guru is a comprehensive 'College Decision Support System' designed to simplify and streamline the college selection process for students globally. This README provides an overview of the project, its objectives, features, and technical aspects.
## Table of Contents
- [Grad-Guru](#grad-guru)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Problem Statement](#problem-statement)
  - [Use Case](#use-case)
  - [Why Do You Need Grad Guru?](#why-do-you-need-grad-guru)
  - [For Whom is Grad Guru Beneficial?](#for-whom-is-grad-guru-beneficial)
  - [Technical Overview](#technical-overview)
  - [Data Sources](#data-sources)
  - [Schema Matching \& Mapping](#schema-matching--mapping)
  - [ETL/Data Exchange/Propagation](#etldata-exchangepropagation)
  - [Data Management](#data-management)
  - [Prerequisites](#prerequisites)
## Problem Statement
In the modern, globalized world, students often find it challenging to select the right institution and program of study due to the overwhelming amount of information available. Grad Guru aims to provide a one-stop solution by integrating data from colleges worldwide, assisting students in making informed decisions.
## Use Case
The application offers several features:
1. User Registration: Creation of user accounts with essential information.
2. Profile Creation: Input academic, financial, and personal preferences.
3. College Search: Explore colleges based on various criteria.
4. Comparative Analysis: Compare institutions side by side.
5. Career Exploration: Research potential career paths.
6. Shortlisting: Curate a list of preferred institutions.
7. Communication: Engage with current students/alumni.
8. Decision-Making: Finalize the choice based on gathered insights.
## Why Do You Need Grad Guru?
Grad Guru addresses the challenges of information overload, the globalization of education, the importance of informed decision-making, financial considerations, career preparation, and the need for transparency and accessibility in higher education.
## For Whom is Grad Guru Beneficial?
Stakeholders include students, parents, colleges/universities, educational counselors, government bodies, employers, and system administrators. Each group derives specific benefits from the system, ranging from informed decision-making to improved recruitment strategies.
## Technical Overview
Open Source Tools & Data Persistence Software:
1. Beautiful Soup: Web scraping tool for data extraction.
2. Pandas: Data processing and transformation.
3. PostgreSQL: Database management system for data storage and retrieval.
## Data Sources
The project utilizes datasets from platforms like Kaggle, Education.com, and Collegedunia.com, covering aspects like university rankings, program details, fee structures, and more. Additionally, the News API is used to fetch relevant news articles.
## Schema Matching & Mapping
Scripts have been developed for college search, program search, fee structure mapping, admission requirements mapping, and salary expectation mapping. These scripts employ linguistic matching algorithms and SQL queries to extract relevant data from the database.
## ETL/Data Exchange/Propagation
The Extract, Transform, Load (ETL) process involves:
1. Extract: Data extraction from sources like CSV files.
2. Transform: Data cleaning and processing.
3. Load: Loading transformed data into the PostgreSQL database.
Data exchange is automated using the Windows Task Scheduler, ensuring timely updates.
## Data Management
The system supports the addition and deletion of data sources. New datasets can be added using the 'central.py' script, while the 'delete.py' script facilitates the removal of existing datasets, ensuring efficient data management.
## Prerequisites
To run the Grad Guru program, ensure the following prerequisites are met:
1. Python 3.x installed on the system.
2. Required Python libraries: Beautiful Soup, Pandas, and psycopg2.
3. PostgreSQL database setup and credentials available.
4. Access to the datasets mentioned in the data sources section.
5. Internet connectivity for fetching real-time data and news.
***
Made By: [Aditi Saxena](https://github.com/aditiisaxena) | [Aditi Singla]() | [Kanishk Kukreja](https://github.com/kanishk393) | [Yash Dhiman](https://github.com/yashhhhhhhhh504)
