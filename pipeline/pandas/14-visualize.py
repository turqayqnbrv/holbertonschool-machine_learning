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
    df = df.drop(columns=['Weighted_Price'], errors='ignore')

    df = df.rename(columns={'Timestamp': 'Date'})
    df['Date'] = pd.to_datetime(df['Date'], unit='s')

    df = df.set_index('Date')

    df['Close'] = df['Close'].ffill()

    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])
    df['Open'] = df['Open'].fillna(df['Close'])

    df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
    df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

    df_2017 = df.loc['2017':]

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
