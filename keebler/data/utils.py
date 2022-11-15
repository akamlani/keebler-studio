from datetime import datetime

import pandas as pd


def trsfrm_dt(df: pd.DataFrame) -> pd.DataFrame:
    """transform the datetime attributes

    Args:
        df (pd.DataFrame): dataframe input with a timestamp field to be transformed

    Returns:
        pd.DataFrame: returns a DataFrame with index as date
    """
    df["date"] = df.timestamp.astype("datetime64[s]")
    df["time"] = df["date"].astype(str).apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")).dt.time
    df["date"] = df["date"].astype(str).apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")).dt.date
    df = df.set_index(df["date"])
    return df
