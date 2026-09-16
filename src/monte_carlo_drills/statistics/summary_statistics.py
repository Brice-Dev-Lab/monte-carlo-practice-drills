"""Helper functions for summary statistics"""

import pandas as pd


def summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates summary statistics"""
    summary = {
        "minimum": df["peak_flow"].min(),
        "maximum": df["peak_flow"].max(),
        "mean": df["peak_flow"].mean(),
        "median": df["peak_flow"].median()
    }

    return pd.DataFrame([summary])
