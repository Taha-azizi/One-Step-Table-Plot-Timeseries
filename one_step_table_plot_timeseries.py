# How to summarize data broken down by time with no extra step dataframe manipulation 
# Here is how I summarize and plot time series data in one step using only the timestamp column
# creating table in one step in pandas dataframe
import pandas as pd
import numpy as np
df.groupby(pd.PeriodIndex(df['Your_TimeStamp_Column'], freq="D/M/Y (one of them)"))['Your_Numeric_Column'].agg(mean='mean',median='median' (or whateverelse)).round(2)

# creating plots using similar method (no dataframe manupulation)
df.groupby(pd.PeriodIndex(df['Your_TimeStamp_Column'], freq="D/M/Y (one of them)"))['Your_Numeric_Column'].agg(mean='mean',median='median' (or whateverelse)).plot(kind='bar',title='your numeric column mean and median etc by Day/Month/Year')
