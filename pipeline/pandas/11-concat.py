#!/usr/bin/env python3
"""
Module containing the concat function for pandas DataFrame
"""


def concat(df1, df2):
    """
    Indexes and filters df2, then prepends it onto df1 with MultiIndex keys.

    Parameters:
        df1 (pd.DataFrame): The coinbase DataFrame.
        df2 (pd.DataFrame): The bitstamp DataFrame.

    Returns:
        pd.DataFrame: The concatenated multi-indexed DataFrame.
    """
    index_func = __import__('10-index').index
    idx_df1 = index_func(df1)
    idx_df2 = index_func(df2)

    filtered_df2 = idx_df2.loc[:1417411920]

    return __import__('pandas').concat(
        [filtered_df2, idx_df1],
        keys=['bitstamp', 'coinbase']
    )
