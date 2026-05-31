#!/usr/bin/env python3
"""
Module containing the index function for pandas DataFrame
"""


def index(df):
    """
    Sets the Timestamp column as the DataFrame index.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The indexed DataFrame.
    """
    return df.set_index('Timestamp')
