##
## Name: Caleb Rogers
## Prog2Rogers.py
##
## Purpose:
## This program replicates the twitter program used to
## calculate the score that determines where promoted  
## tweets appear in search results
##
## Inputs:
## Number of re-tweets, number of @ replies, and number of days
##
## Output:
## Score that ranks the search result placement of a promoted tweet
##
## Certification of Authenticity:
## I certify that this lab is entirely my own work.
##

def main():
    print("This program will compute the score for a promoted tweet.")

    # input for re-tweets, @ replies, and days
    numReTweets = int(input("Enter the number of re-tweets: "))
    numAtReplies = int(input("Enter the number of @ replies: "))
    numDays = int(input("Enter number of days since tweeted: "))

    # calculate day score
    dayScore = (2/(numDays**3))

    # calculate total score
    score = (.3333*numReTweets+.3333*numAtReplies+.3333*dayScore)

    # output score
    print("Your tweet's score is", score)
main()
    
    
