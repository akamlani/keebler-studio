import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns

pd.options.plotting.backend = "plotly"


class Plotter:
    """Conguration and Utilities for plotting diagrams"""

    def __init__(self):
        """Constructor for Plotter"""
        sns.set_theme(context="notebook")

    def set_axis_opts(self, axi, **kwargs):
        """axis configuration for visualization plotting

        Args:
            axi (Any): axis input

        Returns:
            None: not return
        """
        params = {"fontweight": "regular", "fontstyle": "italic", "fontsize": kwargs.get("fontsize", 14)}
        fn_dict = lambda axi: {
            "title": axi.set_title,
            "xaxis-label": axi.set_xlabel,
            "yaxis-label": axi.set_ylabel,
            "legend-title": axi.legend,
        }
        kw_dict = {k: v for k, v in kwargs.items() if k not in params}
        for k, v in kw_dict.items():
            fn_dict(axi)[k](v, **params)

        return axi
