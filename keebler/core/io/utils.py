import pandas as pd


def trsfrm_to_camel(string: str) -> str:
    """convert snake case to camel case string

    Examples:
    >>> df_asset.columns = map(trsfrm_to_camel, df_asset.columns)
    """
    return "".join(word.capitalize() for word in string.split("_"))
