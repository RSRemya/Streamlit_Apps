#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pickle
import warnings
warnings.filterwarnings("ignore")


# In[5]:


# Set the title of the Streamlit app
st.title('Predict the Species')


# In[6]:


# Load the best trained model
model = pickle.load(open('iris_classification_model.p', 'rb'))


# In[7]:


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





# In[ ]:




