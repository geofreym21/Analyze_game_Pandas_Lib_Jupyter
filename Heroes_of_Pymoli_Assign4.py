#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Depedencies and Setup
import pandas as pd
import numpy as np


# In[2]:


# File to Load 
file_to_load = "..\Assignment\purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# In[3]:


# Assign the unique players
unique_players = purchase_data["SN"].unique
# Display the unique players
unique_players


# In[4]:


# count the number of unique players
number_of_unique_players = len(purchase_data["SN"].unique())
number_of_unique_players


# In[5]:


# create a data frame in order to show the total players
total_df = pd.DataFrame({"Total Players": [number_of_unique_players]})
total_df["Total Players"] = total_df["Total Players"].map("{:<}".format)
total_df


# In[6]:


# compute number of unique items, average price, number of purchases and total revenue
# number of unique items
unique_items = len(purchase_data["Item ID"].unique())

# number of purchases
num_of_purchases = len(purchase_data)

# average price 
ave_price = purchase_data["Price"].mean()

#total revenue 
total_revenue = sum(purchase_data["Price"])


# In[7]:


# Data Frame for purchasing analysis information
purchasing_df = pd.DataFrame({"Number of Unique Items":[unique_items], "Average Price":[ave_price], "Number of Purchases":[num_of_purchases],"Total Revenue":[total_revenue]})
purchasing_df["Number of Unique Items"] = purchasing_df["Number of Unique Items"].map("{:<}".format)
purchasing_df["Average Price"] = purchasing_df["Average Price"].map("${:<.2f}".format)
purchasing_df["Number of Purchases"] = purchasing_df["Number of Purchases"].map("{:<}".format)
purchasing_df["Total Revenue"] = purchasing_df["Total Revenue"].map("${:<,.2f}".format)
purchasing_df


# In[20]:


# Gender Demographics
# Drop the duplicates in column SN
gender_group = purchase_data.drop_duplicates('SN')
gender_count = gender_group["Gender"].value_counts
#gender_count()


# In[9]:


# gender count to data frame
gender_df = pd.DataFrame(gender_count())
#gender_df


# In[10]:


# get the percentage per gender and add to the gender Count
# rename the column Gender to Total Count
gender_perct = gender_df["Gender"]/number_of_unique_players
gender_df["Percent of Players"] = gender_perct

gender_df_renamed = gender_df.rename(columns={"Gender": "Total Count"})
gender_df_renamed.head()


# In[11]:


# Purchasing Analysis (Gender)
pur_count_df = purchase_data[["Purchase ID", "Gender"]]
pur_count = pur_count_df["Gender"].value_counts()
#pur_count


# In[12]:


# Create a data frame for the Analysis
pur_gender = pd.DataFrame(pur_count)
#pur_gender


# In[13]:


# Get data that is grouped by Gender
group_gender_df = purchase_data.groupby(["Gender"])

# get the average purchase per gender and add to the data frame
ave_pur_gender = group_gender_df["Price"].mean()
pur_gender["Average Purchase Price"] = ave_pur_gender

# get the total purchase value and add to the data frame
tot_pur_gender = group_gender_df["Price"].sum()
pur_gender["Total Purchase Value"] = tot_pur_gender

# rename the column
pur_gender_renamed = pur_gender.rename(columns={"Gender": "Total Count"})
pur_gender_renamed
#avg_tot_person = 
#pur_gender


# In[14]:


# Get data taht is group per person
# group_per_person = purchase_data.groupby(["SN","Gender"])
# ave_tot_person = group_per_person["Price"].mean()
# ave_tot_person_df = pd.DataFrame(ave_tot_person)
# ave_tot_group_df = ave_tot_person_df.groupby(["Gender"])
# average_per_person = ave_tot_group_df["Price"].mean()
# average_per_person
# add to the data frame that is group by gender
#group_gender_df["Pur Person"] = ave_tot_person


# In[15]:


print(purchase_data["Age"].max())
print(purchase_data["Age"].min())


# In[16]:


# Create bins
bins = [0, 10, 15, 20, 25, 30, 35, 40, 45]

# names for the bins
bin_names = ["<10", "10-14","15-19","20-24","25-29","30-34","35-39","40+"]

#purchase_data["Total Count"] = pd.cut(purchase_data["Age"], bins, labels=bin_names)
#purchase_data
pd.cut(gender_group["Age"], bins, labels=bin_names).head()


# In[17]:


# Place the data series into a new column inside of the DataFrame
gender_group["Total Count"] = pd.cut(gender_group["Age"], bins, labels=bin_names)
gender_group.head()


# In[18]:


# Create a GroupBy object based upon "View Group"
purchase_data_group = gender_group.groupby("Total Count")

# Find how many rows fall into each bin
print(purchase_data_group["SN"].count())

# Get the average of each column within the GroupBy object
purchase_data_group[["Price"]].count()


# In[ ]:




