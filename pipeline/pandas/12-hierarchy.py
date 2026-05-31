#!/usr/bin/env python3
"""
Module containing the hierarchy function for pandas DataFrame
"""


def hierarchy(df1, df2):
    """
    Concatenates tables within a timestamp window and swaps index levels.

    Parameters:
        df1 (pd.DataFrame): The coinbase DataFrame.
        df2 (pd.DataFrame): The bitstamp DataFrame.

    Returns:
        pd.DataFrame: The sorted MultiIndex DataFrame.
    """
    index_func = __import__('10-index').index
    idx_df1 = index_func(df1)
    idx_df2 = index_func(df2)

    start, end = 1417417980, 1417411980  # Chronological filter
    sub_df1 = idx_df1.loc[end:start]
    sub_df2 = idx_df2.loc[end:start]

    combined = __import__('pandas').concat(
        [sub_df2, sub_df1],
        keys=['bitstamp', 'coinbase']
    )
    combined = combined.swaplevel(0, 1)
    return combined.sort_index()
