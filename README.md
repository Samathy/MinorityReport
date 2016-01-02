Minority Report
====================

***

Bring together bug reports over time and Git commits to predict files at high risk of being buggy.

A project bringing together some work I did for University analysing the bug reports from the Linux kernel bugzilla and correlating them to the commits made to the files in the kernel.
Initially I did this only on the ext4 sub-project, but I'm extending it to the entire Linux kernel with an attempt at automating the process.

The code in this repo is originally designed to work just for the Linux kernel project, although I will be working on it with the intention of making it possible to analyse any git project with a bug list csv file.


Hopefully its useful to someone one day!


Using
======
*** 
At the moment. Don't, but heres the dependancys anyway.

[Git2Neo](http://github.com/samathy/git2neo)
[Git Python](https://github.com/python-git/python)
[Neo4J](http://neo4j.com/)



TODO
=======
***

- [x] Write description of the process
- [ ] Remove project specific stuff
- [ ] Clean up, rename, describe, and comment code 
- [ ] Add master script for automating it all
- [ ] Write tests for things
- [ ] Write Auto-install script for getting the dependancies.
- [ ] Write something that displays the data in a graph nicely.
- [ ] Package code better, maybe as a module with a single config/process script




