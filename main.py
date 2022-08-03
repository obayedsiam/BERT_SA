import tensorflow as tf
import pandas as pd
import numpy as np
import ktrain
from ktrain import text
import tensorflow as tf

data = pd.read_csv('/test.xlsx', dtype=str)[['reviews', 'rating']]
data = data.rename(columns={'reviews': 'Reviews', 'rating': 'Sentiment'})
data.head()
