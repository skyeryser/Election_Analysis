# Election Analysis

## Project Overview
An employee of the Colorado Board of Elections has requested an audit of the results of the tabulated results for a U.S. congressional precinct election. The project requirements are to:
1. Tally the total number of votes cast in the election
2. Report the total number of votes cast for each county
3. Calculate the percentage of votes cast in each county
4. Report the total number of votes cast for each candidate
5. Calculate the percentage of votes each candidate recieved
6. Announce the winner of the election

## Resources
- Source File: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.72.2

## Election Audit Results
The review of the election shows that:
 - There was a total of 369,711 votes cast.
 - All votes were cast in one of three counties:
    1. Jefferson
    2. Denver
    3. Arapahoe
 - Each county had a different voter turnout:
    - 10.5% of the total vote was cast in Jefferson County, with 38,855 votes.
    - 82.8% of the total vote was cast in Denver County, with 306,055 votes.
    - 6.7% of the total vote was cast in Arapahoe County, with 24,801 votes.
 - Three candidates ran in the election:
    - Charles Casper
    - Diana DeGette
    - Raymon Anthony Doane
 - Each candidate received a different amount of votes:
    - Charles Casper Stockham received 85,213 votes, accounting for 23.0% of the total votes.
    - Diana DeGette received 272,892 votes, accounting for 73.8% of the total votes.
    - Raymon Anthony Doane received 11,606 votes, accounting for 3.1% of the total votes.
 - The winner of the election was:
    - Diana DeGette with 73.8% of the total vote.
   
## Challenge Summary
I wrote this script to analyze the results of a specific election, but it can still be refactored to investigate a different election in the future. All the Colorado Board of Elections would need to do is set up a repository to store the election results, a copy of this script, and a text file for the analysis output to print. Once this repository is set up, all the board would need to do is normalize the references in the script to match the election results CSV input file name and the text file output.

![file_names.png](https://github.com/skyeryser/Election_Analysis/blob/main/Resources/file_names.png)
