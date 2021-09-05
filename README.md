# Election Audit

## Overview of Election Audit: 
The purpose of this election audit was to get familiar with using Python programming. We learned about the basics of creating and executing Python files, different data types, and performing calculations. Additionally, we also became familiar with data structures such as lists, tuples, and dictionaries, and reviewed concepts from previous VBA experience, like for loops.

## Election-Audit Results: 
Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.
- How many votes were cast in this congressional election?
  - A total of 369,711 votes were cast in this congressional election. 
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  - Jefferson County had 10.5% of the votes, Denver County had 82.8% of the votes, and Arapahoe had 6.7% of the votes. 

![County Vote Breakdown](https://github.com/li-emily/Election_Analysis/blob/main/Resources/county_votes.png)
- Which county had the largest number of votes?
  - The county with the largest number of votes was Denver, with 306,055 votes.
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - Stockham had 23% of the votes, DeGette had 73.8% of the votes, and Doane had 3.1% of the votes.

![Candidate Vote Breakdown](https://github.com/li-emily/Election_Analysis/blob/main/Resources/candidate_results.png)
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  - Diana DeGette was the winner of the election. Her vote count and percentage are as follows.

![Winning Candidate Vote Breakdown](https://github.com/li-emily/Election_Analysis/blob/main/Resources/winning_candidate.png)
  - The winner was found by putting the following code into a for loop that went through each of the candidates, using it to determine the winning vote count, percentage, and candidate.
```        
if (votes > winning_count) and (vote_percentage > winning_percentage):
  winning_count = votes
  winning_candidate = candidate_name
  winning_percentage = vote_percentage
```

## Election-Audit Summary: 
This script is highly adaptable, and can be modified to be used in several other possibilities. Larger state elections should be able to take advantage of this script without much editing needed, as perhaps there may just be more candidates or counties being counted. Additionally, with simple modifications by adding a state variable, the script could definitely be used for nationwide elections as well. Ballot proposition that may allow individuals to vote directly in an initiative can also be analyzed, as by adding a support variable, the script can also take a look at how voting would break down.
