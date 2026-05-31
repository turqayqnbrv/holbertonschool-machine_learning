#!/usr/bin/env python3
"""
Module containing the analyze function for pandas DataFrame
"""


def analyze(df):
    """
    Computes summary descriptive statistics excluding the Timestamp column.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: Summary statistics matrix.
    """
    filtered_df = df.drop(columns=['Timestamp'], errors='ignore')
    return filtered_df.describe()
