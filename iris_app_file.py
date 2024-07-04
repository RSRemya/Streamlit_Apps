#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pickle
import pandas as pd

import numpy as np
from sklearn.datasets import load_iris

import warnings
warnings.filterwarnings("ignore")


# In[4]:


# Set the title of the Streamlit app
st.title('Predict the Species')


# In[5]:


# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Map numerical target values to species names
df['species'] = iris.target
species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['species'] = df['species'].map(species_map)


# In[6]:


# Display the dataset with species names
st.subheader('Iris Dataset')
st.dataframe(df)  # Display the dataframe as an interactive table


# In[7]:


# Alternatively, use st.table for a static table
st.subheader('Iris Dataset (Static Table)')
st.table(df)


# In[8]:


# Load the best trained model
model = pickle.load(open('iris_classification_model.p', 'rb'))


# In[9]:


# Collect user inputs
sepal_length = st.number_input('Sepal Length', min_value=0.01, max_value=10.00, value=0.01)
sepal_width = st.number_input('Sepal Width', min_value=0.01, max_value=10.00, value=0.01)
petal_length = st.number_input('Petal Length', min_value=0.01, max_value=10.00, value=0.01)
petal_width = st.number_input('Petal Width', min_value=0.01, max_value=10.00, value=0.01)

output = ""

if st.button("Predict"):
    # Prepare input data as a DataFrame
    input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                              columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])

    # Make prediction
    result = model.predict(input_data)
    st.success('The output of the above is {}'.format(result))


# In[ ]:




