---
id: i1s9c5xcr4urpj3514mxliu
title: 'Lesson2: Relational Data Models'
desc: ''
updated: 1658612393824
created: 1658610705797
---

Learn the fundamentals of how to do relational data modeling by focusing on:

- Normalization
- Denormalization
- Fact/dimension tables
- Different schema models

Database: A set of related data and the way it is organized

Database Management System: Computer software that allows users to interact with the database and provides access to all of the data.

The term database is often used to refer to both the database and the DBMS used.

Rule 1: The information rule: what we are trying to achive with relational modeling.

All information in a relational database is represented explicitly at the logical level and in exactly one way – by values in tables.

Importance of Relational Databases:
Standardization of data model: Once your data is transformed into the rows and columns format, your data is standardized and you can query it with SQL
Flexibility in adding and altering tables: Relational databases gives you flexibility to add tables, alter tables, add and remove data.
Data Integrity: Data Integrity is the backbone of using a relational database.
Structured Query Language (SQL): A standard language can be used to access the data with a predefined language.
Simplicity : Data is systematically stored and modeled in tabular format.
Intuitive Organization: The spreadsheet format is intuitive but intuitive to data modeling in relational databases.

Online Analytical Processing (OLAP):

Databases optimized for these workloads allow for complex analytical and ad hoc queries, including aggregations. These type of databases are optimized for reads.

Online Transactional Processing (OLTP):

Databases optimized for these workloads allow for less complex queries in large volume. The types of queries for these databases are read, insert, update, and delete.

The key to remember the difference between OLAP and OLTP is analytics (A) vs transactions (T). If you want to get the price of a shoe then you are using OLTP (this has very little or no aggregations). If you want to know the total stock of shoes a particular store sold, then this requires using OLAP (since this will require aggregations)
