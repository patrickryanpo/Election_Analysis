### Election_Analysis

## Overview of Election Audit 
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast.
2. Get a complete list of the candidates who received votes. 
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote. 

## Overview of Election-Audit
A Colorado Board of Elections employee requested for some additional data in order to complete the audit. This report provides election data based on counties. 

1. Calculate the voter turnout for each county
2. Respresentation of the percentage of county votes our of the total count
3. Shows the county with the highest vote turnout

# Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election-Audit Results

![Summary of Election Results](https://github.com/patrickryanpo/Election_Analysis/blob/main/Resources/Screen%20Shot%202020-12-05%20at%201.26.40%20PM.png)

The analysis of the election show that:
- There were 369,711 cast in the election.
- The candidated were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was: 
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes. 

The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The counties were:
    - Jefferson
    - Denver
    - Arapahoe
- The candidate results were:
    - Jefferson county represented 10.5% of the total votes with 38,855 number of votes.
    - Denver county represented 82.8% of the total votes with 306,055 number of votes.
    - Arapahoe county represented 6.7% of the total votes with 24,801 number of votes.
- The county with the highest turnout of votes was: 
    - **Denver** county with 306,055 (82.8%) votes. 
 
 ![Image of Dever Map](https://github.com/patrickryanpo/Election_Analysis/blob/main/Resources/denver%20map.jpg)

## Challenge Summary
The current script runs through each row of the provided election file classifying votes by candidate and by county. The script can be modified to cater to municipal elections by changing the candidate names and changing counties to cities. In the same manner, the script may be used for Presidential general elections by changing the candidate names and broadening the geographical classification to states. 