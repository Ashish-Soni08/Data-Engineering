---
id: 4yxgrwyjr1xgf2kcv50lz88
title: 'Lesson1:Introduction to Data Modeling'
desc: ''
updated: 1658263767732
created: 1658259711098
---
**Q. What is a Data Model?**

Ans: At a high level "an abstraction that organizes elements of data and how they will relate to each other".

The process of creating data models for a particular information system.
Data modeling can easily translate to database modeling, as this is the essential end state.(home of the data)
Data modeling can be considered an abstract (existing in thought or as an idea but not having a physical or concrete existence ) process.

The purpose of data modeling is to organize data into a database system to ensure that your data is persisted and easily usable in your organization.

Data modeling is a process to support both your business and your user applications.

**For example:** Lets say we owned an online store, we will need to store that data to understand how much stock we sold of a particular item.

**Steps to take:**

- This is a busines process and we will also need to store information about our customers as they'd log onto our website, a user application.
- To begin the data modeling process, the team must gather requirements from the application team, the business users and our end users to understand that data must be retained and served to the business or end users.
- First we need to map out that our data must be stored and persisted and how that data will relate to each other.
- Conceptual Data Modeling: Actual data modeling starts with conceptual data modeling with entity mapping. Mapping the concepts of the data that you have or will have. The relationship between your data will be organized in this process.
- Logical Data Modeling: Conceptual data models are mapped to logical data models using the concept of tables, schemas and columns.
- Physical Data Modeling: Transforming the logical data model to the databases data definition language or DDL, to be able to create the databases, the tables and the schemas.
- Then we start writing code: We will writing our DDLs to create tables in the way that the database understands.

**Q. Correct Order of Data Modeling process?**

Ans: Conceptual -> Logical -> Physical

Thinking about the concept data model always comes first before logical and actual implementation of the data modeling.

**Q.Why can't everything be stored in a giant Excel spreadsheet?**

Ans: There are limitations to the amount of data that can be stored in an Excel sheet. So, a database helps organize the elements into tables - rows and columns, etc. Also reading and writing operations on a large scale is not possible with an Excel sheet, so it's better to use a database to handle most business functions.

**Q: Does data modeling happen before you create a database, or is it an iterative process?**

Ans: It's definitely an iterative process. Data engineers continually reorganize, restructure, and optimize data models to fit the needs of the organization.

**Q. How is data modeling different from machine learning modeling?**

Ans: Machine learning includes a lot of data wrangling to create the inputs for machine learning models, but data modeling is more about how to structure data to be used by different people within an organization. You can think of data modeling as the process of designing data and making it available to machine learning engineers, data scientists, business analytics, etc., so they can make use of it easily.

Example of Why Data Modeling is Important:
Let's take an example from Udacity. Here, a Udacity data engineer would help structure the data so it can be used by different people within Udacity for further analysis and also shared with the learner on the website. For instance, when we want to track the students' progress within a Nanodegree program, we want to aggregate data across students and projects within a Nanodegree. In a relational database, this requires the data to be structured in ways that each student's data is tracked across all Nanodegree programs that s/he has ever enrolled in. The data also needs to track the student's progress within each of those Nanodegree programs.

The data model is critical for accurately representing each data object. For instance, a data table would track a student's progress on project submissions, i.e., whether they passed or failed a specific rubric requirement. Furthermore, the data model should ensure that a student's progress is updated and aggregated to provide an indicator of whether the student passed all the rubric requirements and successfully finished the project. Data modeling is critical to track all of these pieces of data so the tables are speaking to each other, updating the tables correctly (e.g., updating a student's progress on a project submission), and meeting defined rules (e.g., project completed when all rubric requirements are passed).
 Data modeling affects everyone who deals with data. The more they know about data modeling, the more they can contribute to an effective, data-driven organization.

Data Modeling Stakeholders
If you will be working with data, you want to have the fundamentals of data modeling in your toolkit. Stakeholders involved in data modeling include:

Data Engineers
Data Scientists
Software Engineers
Product Owners
Business Users

Relational and Non-Relational databases do data modeling differntly.

## Relational Model

This model organizes data into one or more tables(or relations) of columns and rows with a unique key identifying each row. Generally, each table represents one "entity type"(such as customer or product).

Introduction to Relational Databases
The relational model and the relational database were invented by IBM and Edgar Codd in the late 60’s early 70’s. RD is a digital database based on the relational model of data. The software system used to maintain a relational database is referred to as an RDBMS which stands for the relational database management system.
At a basic level, a table is a collection of rows and columns.

Examples of RDBMS include in order of Production readiness:

Oracle - used as a system of truth to handle asset transactions. e.g-banks
Teradata
MySql
PostgreSQL
Sqlite - is a database in file format, is generally used in devlopment of extremely simple tasks in an application.
Microsoft SQL Server

SQL is the language used across almost all relational databases system for querying and maintaining the database. So SQL is the language, used to interact with the database.

The Basics:

- Database/Schema: is a collection of tables
- Tables/Relation: A group of rows sharing the same labeled elements or columns
- Columns/Attribute: Labeled element(name, city or email)
- Rows/Tuple: A single item(Amanda, jdoe@xyc.com, NYC)

A table holds multiple columns with data in them.
The data stored in a column is an attribute of data within a row
Relational databases include a schema of tables that are linked to each other.

**Q. When to use a relational database?**
Ans: Advantages of Using a Relational Database

- Ease of use - SQL
- Flexibility for writing in SQL queries: With SQL being the most common database query language.
- Modeling the data not modeling queries, data modeling is independent in regard to your queries i.e not modeling your data to the queries.
- Ability to do JOINS(Unique to relational databases)
- Ability to do aggregations and analytics(Relational databases were built for this purpose along with being a persistent datastore)
- Secondary Indexes available : You have the advantage of being able to add another index to help with quick searching. efficently structure your data by an index that is not your primary key.
- Smaller data volumes: If you have a smaller data volume (and not big data) you can use a relational database for its simplicity.
- ACID Transactions: Allows you to meet a set of properties of database transactions intended to guarantee validity even in the event of errors, power failures, and thus maintain data integrity(that your data is correct)
- Easier to change to business requirements as you can perform ad hoc queries on your database with ease.

## ACID Transactions

Properties of database transactions intended to guarantee validity even in the event of errors or power failures.

1. Atomicity: The whole transaction is processed or nothing is processed. A commonly cited example of an atomic transaction is money transactions between two bank accounts. The transaction of transferring money from one account to the other is made up of two operations. First, you have to withdraw money in one account, and second you have to save the withdrawn money to the second account. An atomic transaction, i.e., when either all operations occur or nothing occurs, keeps the database in a consistent state. This ensures that if either of those two operations (withdrawing money from the 1st account or saving the money to the 2nd account) fail, the money is neither lost nor created. Source Wikipedia for a detailed description of this example.

2. Consistency: Only transactions that abide by constraints and rules are written into the database, otherwise the database keeps the previous state. The data should be correct across all rows and tables. Check out additional information about consistency on Wikipedia.

3. Isolation: Transactions are processed independently and securely, order does not matter. A low level of isolation enables many users to access the data simultaneously, however this also increases the possibilities of concurrency effects (e.g., dirty reads or lost updates). On the other hand, a high level of isolation reduces these chances of concurrency effects, but also uses more system resources and transactions blocking each other. Source: Wikipedia

4. Durability: Completed transactions are saved to database even in cases of system failure. A commonly cited example includes tracking flight seat bookings. So once the flight booking records a confirmed seat booking, the seat remains booked even if a system failure occurs. Source: Wikipedia.

Non-volatile memory (NVM) or non-volatile storage is a type of computer memory that can retain stored information even after power is removed. In contrast, volatile memory needs constant power in order to retain data.
