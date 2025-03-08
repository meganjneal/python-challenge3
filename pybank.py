 # PyBank Analysis Script  
 # This script reads the budget_data.csv file, performs financial analysis,  
 # prints the results to the terminal, and exports the analysis to a text file.  
 # Important: Always commit your work and back it up on GitHub or GitLab!  
 import pandas as pd  
   
 # Load the CSV and store the header  
 budget_df = pd.read_csv("budget_data.csv")  
 header = budget_df.columns.tolist()  # Storing the header row (for assignment requirements)  
   
 # Calculate total number of months and net total amount  
 total_months = len(budget_df)  
 net_total = budget_df["Profit/Losses"].sum()  
   
 # Calculate monthly changes in "Profit/Losses"  
 budget_df["Change"] = budget_df["Profit/Losses"].diff()  
 average_change = budget_df["Change"].mean()  
   
 # Determine greatest increase and decrease in profits  
 max_increase = budget_df["Change"].max()  
 max_decrease = budget_df["Change"].min()  
 max_date = budget_df.loc[budget_df["Change"].idxmax(), "Date"]  
 min_date = budget_df.loc[budget_df["Change"].idxmin(), "Date"]  
   
 # Create output string for the analysis  
 output = (  
     "Financial Analysis\n"  
     "----------------------------\n"  
     "Total Months: " + str(total_months) + "\n" +  
     "Total: $" + format(net_total, ",") + "\n" +  
     "Average Change: $" + format(average_change, ",.2f") + "\n" +  
     "Greatest Increase in Profits: " + max_date + " ($" + format(max_increase, ",.0f") + ")\n" +  
     "Greatest Decrease in Profits: " + min_date + " ($" + format(max_decrease, ",.0f") + ")\n"  
 )  
   
 # Print the analysis to terminal  
 print(output)  
   
 # Export the results to a text file  
 with open("pybank_analysis.txt", "w") as file:  
     file.write(output)  