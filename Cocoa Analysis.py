
# coding: utf-8

# # Flavors of Cocoa
The questions that this case study will delve deeper into are: 

1) Which country has the highest chocolate consumption?
2) When were the reviews captured?
3) Is there a link between the cocoa percentage and the ratings?
4) Which countries have the highest ratings?
5) Which countries have the lowest ratings?

We'll begin by loading the required libraries and the dataset. 
# In[5]:


import numpy as np
import os
import pandas as pd
import sys
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set(color_codes=True)

Next we'll load the dataset, located on my desktop:
# In[8]:


cocoa = pd.read_csv("C:/Users/tgameiro/Desktop/flavors_of_cacao.csv")


# In[9]:


cocoa.head()


# In[10]:


cocoa.dtypes


# In[11]:


#We'll convert the Cocoa Percent from a string to a float
cocoa['Cocoa\nPercent'] = cocoa['Cocoa\nPercent'].apply(lambda row: row[:-1]).astype('float')


# In[12]:


cocoa.dtypes


# In[13]:


cocoa.corr()


# In[14]:


cocoa.columns = cocoa.columns.str.replace(' ', '_')


# In[15]:


cocoa.head()


# In[16]:


print("Table 1: Summary of Statistical Measurements")
cocoa.describe(include='all').T

The summary table is very interesting to review. 

With this table, we're able to see that the average percent of cocoa in a chocolate bar is around 70%, and the average rating for the chocolate bars is 3.1. 

We can see that most of the chocolate bars were reviewed in 2014-16, with the data collection starting in 2006, up until 2017. 

The main location for the cocoa companies is in the U.S.A. 

We can also see that the top country that produces the cocoa beans is Venezuela.
# In[17]:


#We will verify if there are any NA's in the dataset
cocoa.isnull().sum(axis=0)

We found that two columns have a single null value in each. This is not significant enough to make a change. 

Let's visualize some of the data. 

We'll take a look at the countries with the highest amount of chocolate vendors
# In[18]:


cocoa['Company\nLocation'].value_counts().head(15).plot.bar()
plt.xlabel('Countries of Distribution')
plt.ylabel('Count of Chocolate Bars')
print("Companies with the Highest Chocolate Vendors")


# In[19]:


cocoa['Company\nLocation'].value_counts().head(15).plot('barh')
plt.xlabel('Count of Chocolate Bars')
plt.ylabel('Countries of Distribution')
print("Companies with the Highest Chocolate Vendors")

The data clearly shows that the US consumes chocolate far more than any other country of the world.

Let's take a look at the review data
# In[20]:


sns.distplot(cocoa['Review\nDate'])
plt.xlabel('Review Date')
plt.ylabel('Count')
print("Quantity of Reviews by Date")

Looks like most of the reviews in the dataset were between 2014 and 2016. 
# In[21]:


#scatter plot 
var = 'REF'
data = pd.concat([cocoa['Rating'], cocoa[var]], axis=1)
data.plot.scatter(x=var, y='Rating');

We'll now compare the Maximum Cocoa Percentage and the Mean Cocoa Percentage
# In[22]:


cocoa['Cocoa\nPercent'].value_counts()


# In[23]:


cocoa['Cocoa\nPercent'].value_counts().head(20).plot.bar()
plt.xlabel('Cocoa %')
plt.ylabel('Count of Chocolate Bars')
print("Chocolate with the Highest Cocoa %")

We see above that most of the chocolates have 70% cocoa. Let's see a little more information...
# In[24]:


cocoa[cocoa['Cocoa\nPercent' ] == 70.0]


# In[25]:


cocoa_seventy=cocoa[cocoa['Cocoa\nPercent' ] == 70.0]
cocoa_seventy.count()


# In[26]:


sns.countplot(x='Rating', data=cocoa_seventy, color='purple')
print("Ratings of Chocolate Bars with 70% Cocoa")


# In[27]:


cocoa[cocoa['Cocoa\nPercent' ] == 100.0]


# In[28]:


cocoa_hundred=cocoa[cocoa['Cocoa\nPercent' ] == 100.0]
cocoa_hundred.count()


# In[29]:


sns.countplot(x='Rating', data=cocoa_hundred, color='green')
print("Ratings of Chocolate Bars with 100% Cocoa")

Let's look at the percent of cocoa with the highest and most consumer ratings
# In[30]:


sns.countplot(x='Rating', data=cocoa)
plt.xlabel('Rating')
plt.ylabel('Count of Users')
plt.title('Number of Users that Rated Chocolate Bars')
print('Count of Chocolate Bar Ratings')

In this analysis, there are 1795 chocolate bars rated from 63 countries. The most number of ratings that were given was between 3.0 to 3.5, with the highest being 3.5 with a number of around 380 ratings. This shows us that most individuals are giving chocolate bars a rating of a little bit more than satisfactory.

We can see that very few chocolate bars were given the highest rating of 5%, let's see which ones:
# In[31]:


cocoa[cocoa['Rating'] == 5.0]

Both highest rated chocolate comes from Italy and both have 70% cocoa. 

We can also see that few were given very low ratings, let's take a look:
# In[32]:


cocoa[cocoa['Rating'] == 1.0]

Three out of four of the lowest rated chocolates are from Belgium, and all have either 70% or close to 70% cocoa percent. 