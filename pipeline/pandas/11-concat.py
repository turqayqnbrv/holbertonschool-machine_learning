#!/usr/bin/env python3
"""
Module containing the concat function for pandas DataFrame
"""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """
    Indexes and filters df2, then prepends it onto df1 with MultiIndex keys.

    Parameters:
        df1 (pd.DataFrame): The coinbase DataFrame.
        df2 (pd.DataFrame): The bitstamp DataFrame.

    Returns:
        pd.DataFrame: The concatenated multi-indexed DataFrame.
    """
    idx_df1 = index(df1)
    idx_df2 = index(df2)

    filtered_df2 = idx_df2.loc[:1417411920]

    return pd.concat([filtered_df2, idx_df1], keys=['bitstamp', 'coinbase'])
