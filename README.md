Linux Bug Analysis
====================

***

A project bringing together some work I did for University analysing the bug reports from the Linux kernel bugzilla and correlating them to the commits made to the files in the kernel.
Initially I did this only on the ext4 sub-project, but I'm extending it to the entire Linux kernel with an attempt at automating the process.

The code in this repo is originally designed to work just for the Linux kernel project, although I will be working on it with the intention of making it possible to analyse any git project with a bug csv file.


Hopefully its useful to someone one day!


Using
======
*** 
At the moment. Don't, but heres the dependancys anyway.

(Git2Neo)[http://github.com/samathy/git2neo
(git Python)[https://github.com/python-git/python]
(Neo4J)[http://neo4j.com/]

