#!/usr/bin/env python
# coding: utf-8

# Install snowflake connector

# In[ ]:


pip install snowflake-connector-python


# Import relevant libraries

# In[2]:


import os, argparse
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas


# Input snowflake account credentials

# In[ ]:


user = 'my username'
password = 'my password'
account = 'https://****'
warehouse = 'my warehouse'
database = 'my database'
schema = 'my schema'


# Connect to snowflake

# In[ ]:


import snowflake.connector

def establish_snowflake_connection():
    user = 'my username'
    password = 'my password'
    account = 'https://***'
    warehouse = 'my warehouse'
    database = 'my database'
    schema = 'my schema'

    try:
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema,
            client_session_keep_alive=False,
            network_timeout=120,
            login_timeout=60,
            ocsp_fail_open=False
        )
        return conn
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

conn = establish_snowflake_connection()


# In[ ]:


def database_config(conn, database, schema, table, file):
 


# Create a cursor

# In[ ]:


cs = conn.cursor()


# Use the cursor to execute SQL statements

# In[ ]:


cs.execute("USE DATABASE " + mich)
cs.execute("USE SCHEMA " + public)


# Load data

# In[ ]:


df = pd.read_csv('data_dump.csv')
    


# Converting columns names to upper case

# In[ ]:


df.columns = df.columns.str.upper()


# In[ ]:




