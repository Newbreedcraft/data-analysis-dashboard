import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data from CSV files
def load_data():
    # Load data from datafile1.csv
    df1 = pd.read_csv('data\\datafile1.csv')
    
    # Load data from datafile2.csv
    df2 = pd.read_csv('data\\datafile2.csv')
    
    return df1, df2

# Function to perform data analysis and visualization
def analyze_and_visualize(df1, df2):
    # Example: Calculate total tasks completed per project
    tasks_completed = df1.groupby('project_name')['tasks_completed'].sum()
    
    # Example: Calculate total revenue per project
    revenue = df2.groupby('project_name')['revenue'].sum()
    
    # Example: Plotting tasks completed and revenue using Matplotlib
    plt.figure(figsize=(12, 6))
    
    # Plot tasks completed
    plt.subplot(1, 2, 1)
    tasks_completed.plot(kind='bar', color='skyblue')
    plt.title('Total Tasks Completed')
    plt.xlabel('Project')
    plt.ylabel('Tasks Completed')
    plt.xticks(rotation=45)
    
    # Plot revenue
    plt.subplot(1, 2, 2)
    revenue.plot(kind='bar', color='lightgreen')
    plt.title('Total Revenue')
    plt.xlabel('Project')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

# Main function to run the dashboard
def main():
    # Load data
    df1, df2 = load_data()
    
    # Perform analysis and visualization
    analyze_and_visualize(df1, df2)

# Entry point of the script
if __name__ == "__main__":
    main()
