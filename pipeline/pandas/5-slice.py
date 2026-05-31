#!/usr/bin/env python3
"""
Module containing the slice function for pandas DataFrame
"""


def slice(df):
    """
    Extracts specific columns and selects every 60th row.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The sliced DataFrame.
    """
    columns = ['High', 'Low', 'Close', 'Volume_(BTC)']
    sliced_df = df[columns].iloc[::60]
    return sliced_df
