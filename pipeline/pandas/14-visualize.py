#!/usr/bin/env python3
"""
Data preprocessing script for Bitcoin historical data charting
"""
import pandas as pd


def preprocess_and_resample(df):
    """
    Cleans, transforms, and resamples the tracking DataFrame daily.

    Parameters:
        df (pd.DataFrame): The raw input DataFrame.

    Returns:
        pd.DataFrame: Aggregated historical daily dataset for plotting.
    """
    # 1. Remove Weighted_Price
    df = df.drop(columns=['Weighted_Price'], errors='ignore')

    # 2 & 3. Rename Timestamp to Date & convert values
    df = df.rename(columns={'Timestamp': 'Date'})
    df['Date'] = pd.to_datetime(df['Date'], unit='s')

    # 4. Index on Date
    df = df.set_index('Date')

    # 5. Missing values in Close filled with previous row values
    df['Close'] = df['Close'].ffill()

    # 6. Missing Open, High, Low filled with matching row's Close
    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])
    df['Open'] = df['Open'].fillna(df['Close'])

    # 7. Volume dimensions set to 0 where NaN
    df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
    df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

    # 8. Filter data from 2017 and beyond
    df_2017 = df.loc['2017':]

    # 9. Daily interval grouping with specified aggregations
    agg_rules = {
        'High': 'max',
        'Low': 'min',
        'Open': 'mean',
        'Close': 'mean',
        'Volume_(BTC)': 'sum',
        'Volume_(Currency)': 'sum'
    }
    transformed_df = df_2017.resample('D').agg(agg_rules)

    return transformed_df
