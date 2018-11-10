# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:27:53 2018

@author: Hema
"""

import os
import csv

ttl_votes=[]
Num_votes=0
dict_candidates={}
count =0
names=[]
file_to_output="Vote_analysis"
winner=0
winner_Name=""
#Open file to read the data
with open("election_data.csv", 'r') as csvfile :
    csvreader =csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    
    #Creating two variables to store the data
    for row in csvreader:
        ttl_votes.append(row)
        Num_votes=len(ttl_votes)
        names.append(row)
    #Converting the columns to row to get the canditates names
    # and creating a dictonary to store the names so that we can
    # iterate through the other list for the total vote counts
    test_data=list(zip(*names))
    candidates =set(test_data[2])
    #print(Num_votes)

    #calcualtion of canditates votes, percentages and display it on text and 
    #output terminal
    for individual in candidates:
        dict_candidates.update({individual: 0})

# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes: " + str(Num_votes))
    txt_file.write("\n")
    txt_file.write("-------------------------------------")
    txt_file.write("\n")
    print("Election Results")
    print("\n")  
    print("-------------------------------------")
    print("Total Votes: " + str(Num_votes))
    print("-------------------------------------") 
       
    for key in dict_candidates:
        for votes in ttl_votes:
            if key == votes[2]:
                count+=1
        dict_candidates[key]=count 
        percentage= round((count/Num_votes)*100)
        if (winner < count):
            winner=count
            winner_Name=key
        count=0
        txt_file.write("\n")
        txt_file.write( str(key) + " : " + f'{percentage:.3f}%' + " ("+ str(dict_candidates[key]) + ")" )
        print( str(key) + " : "  + f'{percentage:.3f}%' + " ("+str(dict_candidates[key]) + ")" )
    print("------------------------------------------------")
    print("Winner: " + winner_Name)
    txt_file.write("\n")
    txt_file.write("-------------------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner_Name))
    txt_file.write("\n")

   
   