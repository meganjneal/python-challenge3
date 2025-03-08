 # PyPoll Analysis Script  
 # This script reads the election_data.csv file, counts votes,  
 # calculates each candidate's total votes and percentage,  
 # prints the results to the terminal, and exports the analysis to a text file.  
 # Important: Always commit your work and back it up on GitHub or GitLab!  
 import pandas as pd  
   
 # Load the CSV and store the header  
 election_df = pd.read_csv("election_data.csv")  
 header = election_df.columns.tolist()  # Storing the header row (for assignment requirements)  
   
 # Calculate total votes cast  
 total_votes = len(election_df)  
   
 # Get the total votes and percentages for each candidate  
 vote_counts = election_df["Candidate"].value_counts()  
 vote_percentages = (vote_counts / total_votes) * 100  
   
 # Determine the winner based on the highest vote count  
 winner = vote_counts.idxmax()  
   
 # Create output string for the election analysis  
 output = "Election Results\n"  
 output += "-------------------------\n"  
 output += "Total Votes: " + format(total_votes, ",") + "\n"  
 output += "-------------------------\n"  
 for candidate in vote_counts.index:  
     output += candidate + ": " + format(vote_percentages[candidate], ".3f") + "% (" + format(vote_counts[candidate], ",") + ")\n"  
 output += "-------------------------\n"  
 output += "Winner: " + winner + "\n"  
 output += "-------------------------\n"  
   
 # Print the analysis to terminal  
 print(output)  
   
 # Export the results to a text file  
 with open("pypoll_analysis.txt", "w") as file:  
     file.write(output)  