#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyspark


# In[2]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, month, count, avg, sum, when, countDistinct, date_format


# In[ ]:


spark = SparkSession.builder \
    .appName("MonthlyDataProcessing") \
    .enableHiveSupport() \
    .getOrCreate()

spark.sql("CREATE DATABASE IF NOT EXISTS car_accidents")

# Описание дня
spark.sql("""
CREATE TABLE IF NOT EXISTS car_accidents.conditions (
    Accident_Number STRING,
    Date_and_Time DATETIME,
    Weather_Description STRING,
    Illumination_Description STRING
)
PARTITIONED BY (Date_and_Time STRING)
STORED AS ORC
""")

# Описание угона
spark.sql("""
CREATE TABLE IF NOT EXISTS car_accidents.cases (
    Accident_Number STRING,
    Number_of_Motor_Vehicles INT,
    Number_of_Injuries INT,
    Number_of_Fatalities INT,
    Property_Damage INT,
    Hit_and_Run STRING,
    Collision_Type_Description STRING
)
PARTITIONED BY (Date_and_Time STRING)
STORED AS ORC
""")

