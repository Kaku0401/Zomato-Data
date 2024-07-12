import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# File path to the CSV file
file_path = "Zomato data .csv"
# Attempt to load the dataset
try:
    dataframe = pd.read_csv(file_path)
    print("File loaded successfully!")
    print(dataframe.head())
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please check the file path and try again.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_path}' is empty.")
except pd.errors.ParserError:
    print(f"Error: The file '{file_path}' contains parsing errors.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Proceed with further operations only if the dataframe is successfully loaded
if 'dataframe' in locals():
    # Handle 'rate' column, converting to float and handling non-numeric values
    def handleRate(value):
        try:
            value = str(value).split('/')[0]
            return float(value)
        except ValueError:
            return np.nan

    dataframe['rate'] = dataframe['rate'].apply(handleRate)
    print(dataframe.head())

    # Check the DataFrame information
    dataframe.info()

    # Plotting the count of 'listed_in(type)'
    plt.figure(figsize=(10, 6))
    sns.countplot(x=dataframe['listed_in(type)'])
    plt.xlabel("Type of restaurant")
    plt.xticks(rotation=45)
    plt.title("Count of Restaurant Types")
    plt.show()

    # Grouping data and plotting votes by type of restaurant
    grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
    result = pd.DataFrame({'votes': grouped_data})

    plt.figure(figsize=(10, 6))
    plt.plot(result, c="green", marker="o")
    plt.xlabel("Type of restaurant", color="red", size=20)
    plt.ylabel("Votes", color="red", size=20)
    plt.title("Votes by Type of Restaurant")
    plt.xticks(rotation=45)
    plt.show()

    # Finding the restaurant(s) with the maximum votes
    max_votes = dataframe['votes'].max()
    restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
    print("Restaurant(s) with the maximum votes:")
    print(restaurant_with_max_votes)

    # Plotting the count of 'online_order'
    plt.figure(figsize=(10, 6))
    sns.countplot(x=dataframe['online_order'])
    plt.xlabel("Online Order")
    plt.title("Count of Online Orders")
    plt.show()

    # Plotting the distribution of ratings
    plt.figure(figsize=(10, 6))
    plt.hist(dataframe['rate'].dropna(), bins=5, edgecolor='black')
    plt.title("Ratings Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.show()

    # Plotting the count of approximate cost for two people
    plt.figure(figsize=(10, 6))
    sns.countplot(x=dataframe['approx_cost(for two people)'])
    plt.xticks(rotation=45)
    plt.title("Approximate Cost for Two People")
    plt.show()

    # Boxplot for online orders vs rate
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='online_order', y='rate', data=dataframe)
    plt.title("Boxplot of Online Order vs Rate")
    plt.show()

    # Heatmap of pivot table for 'listed_in(type)' and 'online_order'
    pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
    plt.title("Heatmap of Online Orders by Restaurant Type")
    plt.xlabel("Online Order")
    plt.ylabel("Listed In (Type)")
    plt.show()
