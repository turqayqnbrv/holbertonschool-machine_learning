#!/usr/bin/env python3
"""
Module containing the flip_switch function for pandas DataFrame
"""


def flip_switch(df):
    """
    Sorts a DataFrame in reverse chronological order and transposes it.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The reversed and transposed DataFrame.
    """
    reversed_df = df.iloc[::-1]
    return reversed_df.T
