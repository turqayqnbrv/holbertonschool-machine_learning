#!/usr/bin/env python3
"""
Module containing the array function for pandas DataFrame
"""
import pandas as pd


def array(df):
    """
    Selects the last 10 rows of High and Close columns as a numpy array.

    Parameters:
        df (pd.DataFrame): The input DataFrame containing High and Close.

    Returns:
        numpy.ndarray: The last 10 rows converted to a numpy array.
    """
    selected_data = df[['High', 'Close']].tail(10)
    return selected_data.to_numpy()
