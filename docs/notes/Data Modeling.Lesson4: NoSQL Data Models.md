---
id: 4y3vjkjh7ngwwkgkh5q38zq
title: 'Lesson4: NoSQL Data Models'
desc: ''
updated: 1659383761597
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
