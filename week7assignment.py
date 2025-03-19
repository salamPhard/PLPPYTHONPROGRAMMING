import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#load the csv file
def task1(file):
    try:
        df = pd.read_csv(file)
        first5rows = df.head(5) #Reading the first 4 lines
        dt = df.dtypes #exploring data type
        info = df.info #checking the data information

        #Checking for missing values
        print(df.isnull().sum()) #check for missing value
        print('Values missing in dataset?',df.isnull().values.any()) #check if missing value exist
        print("Total missing value = ", df.isnull().sum().sum())  # Total missing values in the dataset

        #Cleaning the dataset
        new_df = df.dropna(how="any") #remove any rows that have rows empty
        print("Dataset missing value dropped and cleaned")
        print(new_df.isnull().sum())  # check for missing value
        print('Values missing in dataset after cleaning?', new_df.isnull().values.any())  # check if missing value exist
        print("Total missing value after cleaning = ", new_df.isnull().sum().sum())  # Total missing values in the dataset

        #Statistics on column
        num_colum = df['Unit price']
        print(num_colum.describe()) #Statistics of column data_value computed

        #Performing grouping on a categorical column
        df_group = df.groupby('Payment')['Total'].mean() #group by period and find the mean of data value of each
        print(df_group)
    except FileNotFoundError:
        print("File not found")


def create_plot_graph(file):
    try:
        df = pd.read_csv(file)

        plt.figure(figsize=(12, 6))
        plt.plot(df["Date"], df["Rating"], color="blue", linewidth=1)
        plt.xlabel("Date")
        plt.ylabel("Rating")
        plt.ylim(4, 10) #minimum and maximum scale of y axis
        plt.title("Rating over time")
        plt.show()


    except FileNotFoundError:
        print("File not found")


def create_bar_chart(file):
    try:
        df = pd.read_csv(file)

        plt.figure(figsize=(12, 6))
        plt.bar(df["Branch"], df["Rating"], color="blue", linewidth=1)
        plt.xlabel("Branch")
        plt.ylabel("Rating")
        plt.ylim(4, 10)  # minimum and maximum scale of y axis
        plt.title("Branch rating")
        plt.show()

    except FileNotFoundError:
        print("File not found")


def create_histogram(file):
    try:
        df = pd.read_csv(file)

        plt.figure(figsize=(12, 6))
        plt.hist(df["Branch"], df["Rating"], color="blue", linewidth=1)
        plt.xlabel("Branch")
        plt.ylabel("Rating")
        plt.ylim(4, 10)  # minimum and maximum scale of y axis
        plt.title("Branch rating")
        plt.show()

    except FileNotFoundError:
        print("File not found")


def create_scatter_plot(file):
    try:
        df = pd.read_csv(file)

        plt.figure(figsize=(12, 6))
        plt.scatter(df["Branch"], df["Rating"], color="blue", linewidth=1)
        plt.xlabel("Branch")
        plt.ylabel("Rating")
        plt.ylim(4, 10)  # minimum and maximum scale of y axis
        plt.title("Branch rating")
        plt.show()

    except FileNotFoundError:
        print("File not found")

