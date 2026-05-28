#!/usr/bin/env python3
"""
New code updates Pandas DataFrame script to:
- rename the column Timestamp to Datetime
- convert the timestamp values into datetime values
- display only the Datetime and Close columns
"""

import pandas as pd
def from_file(filename, delimiter):
    """
    Loads data from a file as a Pandas DataFrame

    parameters:
        filename [str]: file to load the data from
        delimiter [str]: the column separator

    returns:
        the newly created pd.DataFrame
    """
    df = pd.read_csv(filename, delimiter=delimiter)
    return df

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

df = df.rename(columns={'Timestamp': 'Datetime'})
df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')
df = df.loc[:, ['Datetime', 'Close']]

print(df.tail())
