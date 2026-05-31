#!/usr/bin/env python3
"""
Module containing the high function for pandas DataFrame
"""


def high(df):
    """
    Sorts a DataFrame by the High price column in descending order.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The sorted DataFrame.
    """
    return df.sort_values(by='High', ascending=False)
