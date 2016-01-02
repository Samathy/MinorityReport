Process
==============

***
This document describes what the process is for generating the graph database and doing the analyitics.

Its partly for my own use to track what order things need to go in.



1: Add Git commit data to Neo4J graphDB
    * Should be done using Git2Neo but scripted based on a script with the predefined componant sections specified as these can't really be reliably computed.cjjjc
2: Add bug csv
    * Done using csv_to_neo
ForEach sub-componant/project
{

    3: Get high bug months 
        1: First get the count of bugs in all the months
        2: Find the the highest months.
        3: Find the 2 months prior to the highest months
        4: Store the months we're going to analyse.
    4: Get number of commits applied to every file during those months
        * I think thats done using MapReduce_Files.py
    5: Sort those into highest first
}

6: Gather all sorted files together for the entire project to identify highest risk files in the project.
    * Currently no script for this
