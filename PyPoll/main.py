#Objective is to help a small, rural U.S. town modernise its vote-counting process
#Dependencies, Importing the Modules
import os
import csv

election_csv_path = os.path.join('Resources', 'election_data.csv')
#print (csv_path)
with open(election_csv_path) as elec_csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    elect_csv_reader = csv.reader(elec_csvfile, delimiter=',')
     # Read the header row first
    elect_csv_header = next(elect_csv_reader)
    
    # Initialise variables
    cnt0=0
    cnt1=0
    cnt2=0
    total_votes=0
    Candidates=["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]

    #Storing the number of votes for each candidate in variable cnt
    #adding the number of votes in the variable total_votes

    for row in elect_csv_reader:
        total_votes+=1
        if row[2]==Candidates[0]:
            cnt0=cnt0+1  
        elif row[2]==Candidates[1]:  
            cnt1=cnt1+1
        elif row[2]==Candidates[2]:  
            cnt2=cnt2+1  

    # Initialise writer to txt file
    with open(os.path.join("analysis", "output.txt"), "w") as f:       

        print("Election Results\n")
        print("Election Results\n",file=f)

        print("---------------------\n")
        print("---------------------\n",file=f)

        #The total number of votes cast

        print("Total Votes: "+str(total_votes)+"\n")
        print("Total Votes: "+str(total_votes)+"\n",file=f)

        print("---------------------\n")
        print("---------------------\n",file=f)

        #Total no of votes each candidate won,percentage of votes each candidate won
        #and total number of votes each candidate won

        print(Candidates[0]+": "+str(round(float((cnt0/total_votes)*100),3))+"% ("+str(cnt0)+")\n")
        print(Candidates[0]+": "+str(round(float((cnt0/total_votes)*100),3))+"% ("+str(cnt0)+")\n",file=f)

        print(Candidates[1]+": "+str(round(float((cnt1/total_votes)*100),3))+"% ("+str(cnt1)+")\n")
        print(Candidates[1]+": "+str(round(float((cnt1/total_votes)*100),3))+"% ("+str(cnt1)+")\n",file=f)

        print(Candidates[2]+": "+str(round(float((cnt2/total_votes)*100),3))+"% ("+str(cnt2)+")\n")
        print(Candidates[2]+": "+str(round(float((cnt2/total_votes)*100),3))+"% ("+str(cnt2)+")\n",file=f)

        print("---------------------\n")
        print("---------------------\n",file=f)

        #The winner of the election based on number of votes
    
        if max(cnt0,cnt1,cnt2) == cnt0:
            winner=Candidates[0]
        elif max(cnt0,cnt1,cnt2) == cnt1:
             winner=Candidates[1]
        else:
             winner=Candidates[2]

        print("Winner: "+winner)
        print("Winner: "+winner+"\n",file=f)

        print("\n---------------------\n")
        print("\n---------------------\n",file=f)
        #Closing the text file
        f.close()