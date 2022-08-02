---
id: 4y3vjkjh7ngwwkgkh5q38zq
title: 'Lesson4: NoSQL Data Models'
desc: ''
updated: 1659465484114
created: 1659380683380
---

When to Use NoSQL:
Need high Availability in the data: Indicates the system is always up and there is no downtime
Have Large Amounts of Data
Need Linear Scalability: The need to add more nodes to the system so performance will increase linearly
Low Latency: Shorter delay before the data is transferred once the instruction for the transfer has been received.
Need fast reads and write

Basics of NoSQL Database Design:

distributed Databases: In a distributed database, in order to have high availability, you will need copies of your data.

CAP Theorem:
Consistency: Every read from the database gets the latest (and correct) piece of data or an error

Availability: Every request is received and a response is given -- without a guarantee that the data is the latest update

Partition Tolerance: The system continues to work regardless of losing network connectivity between nodes.

Cassandra Query Language
Cassandra query language is the way to interact with the database and is very similar to SQL. The following are not supported by CQL

JOINS
GROUP BY
Subqueries

Primary Key
Must be unique
The PRIMARY KEY is made up of either just the PARTITION KEY or may also include additional CLUSTERING COLUMNS
A Simple PRIMARY KEY is just one column that is also the PARTITION KEY. A Composite PRIMARY KEY is made up of more than one column and will assist in creating a unique value and in your retrieval queries
The PARTITION KEY will determine the distribution of data across the system

Clustering Columns:
The clustering column will sort the data in sorted ascending order, e.g., alphabetical order.*
More than one clustering column can be added (or none!)
From there the clustering columns will sort in order of how they were added to the primary key
Commonly Asked Questions:
How many clustering columns can we add?

You can use as many clustering columns as you would like. You cannot use the clustering columns out of order in the SELECT statement. You may choose to omit using a clustering column in your SELECT statement. That's OK. Just remember to use them in order when you are using the SELECT statement.

WHERE clause
Data Modeling in Apache Cassandra is query focused, and that focus needs to be on the WHERE clause
Failure to include a WHERE clause will result in an error

Why do we need to use a WHERE statement since we are not concerned about analytics? Is it only for debugging purposes?
The WHERE statement is allowing us to do the fast reads. With Apache Cassandra, we are talking about big data -- think terabytes of data -- so we are making it fast for read purposes. Data is spread across all the nodes. By using the WHERE statement, we know which node to go to, from which node to get that data and serve it back. For example, imagine we have 10 years of data on 10 nodes or servers. So 1 year's data is on a separate node. By using the WHERE year = 1 statement we know which node to visit fast to pull the data from.
