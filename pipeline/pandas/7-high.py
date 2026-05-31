#!/usr/bin/env python3
"""
Module containing the prune function for pandas DataFrame
"""


def prune(df):
    """
    Removes any rows where the Close column contains NaN values.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with missing Close rows removed.
    """
    return df.dropna(subset=['Close'])
