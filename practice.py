import pandas as pd
import numpy as np

df = pd.read_csv('data/user-item-interactions.csv')
df_content = pd.read_csv('data/articles_community.csv')
df_content.head()

df_content.merge()