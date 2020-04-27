import numpy as np
import pandas as pd

def drop_na_cols(df):
    """Return cols with more than half missing value"""
    na_cols = [df.columns[i] for i in range(len(df.columns) if df.count()[i] < (df.shape[0] / 2))]
    df = df.drop(na_cols, axis = 1)
    return df
