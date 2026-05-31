#!/usr/bin/env python3
"""
Module containing the rename function for pandas DataFrame
"""
import pandas as pd

def rename(df):
    """
    Renames Timestamp column, converts to datetime, and filters columns.

    Parameters:
        df (pd.DataFrame): The input DataFrame containing a 'Timestamp' column.

    Returns:
        pd.DataFrame: The modified DataFrame with 'Datetime' and 'Close' columns.
    """
    df = df.rename(columns={'Timestamp': 'Datetime'})
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')
    df = df[['Datetime', 'Close']]
    return df
