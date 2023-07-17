# Databricks notebook source
# MAGIC %pip install shapely==1.8.5
# MAGIC %pip install geojson
# MAGIC %pip install pypopulation
# MAGIC %pip install pycountry
# MAGIC %pip install streamlit
# MAGIC %pip install httpx

# COMMAND ----------

import os
import pickle
import streamlit as st
import pandas as pd
import pycountry
import pypopulation
import plotly.express as px
import datetime
import client, errors, datatypes


# COMMAND ----------

import sys

sys.path.append(os.path.abspath('/Repos/huruiz@unicef.org/bazze-client/bazze_api_client'))
print("\n".join(sys.path))

# COMMAND ----------

from models import query_execution
from models import query_execution

# COMMAND ----------

sys.path.insert(0, '.')

# COMMAND ----------

import client
import api
import api.statistics
from .api.statistics import stats_counts_by_countries_get
#from api import statistics
#from api.statistics import record_counts_get
 
#from datatypes import Response


# COMMAND ----------

import Workspace.Repos.huruiz\@unicef.org.bazze-client.api.statistics.stats_counts_by_countries_get.py

# COMMAND ----------

stats_counts_by_countries_get.sync(
        client=client,
        from_date=datetime.date.today() - datetime.timedelta(days=366),
        to_date=datetime.date.today() - datetime.timedelta(days=2),
        wait=True,
    )
