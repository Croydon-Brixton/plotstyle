from __future__ import annotations

import matplotlib.pyplot as plt

from plotstyle.size import get_dim


def patch_plot(style: str, figsize: float | tuple[float, float]):
    """Applies a specified matplotlib style to an existing figure and adjusts its size.

    Args:
    - style (str): The name of the matplotlib style to apply to the figure.
    - figsize (float | tuple[float, float]): The size of the figure in inches. If a float is provided,
        the size assumed to be the width of the figure and the height is calculated using the golden ratio.

    Returns:
    - fig, ax (matplotlib.figure.Figure, matplotlib.axes.Axes): The created figure and axes objects.
    """
    with plt.style.context(style):
        fig, ax = plt.gcf(), plt.gca()

        # Set figure size
        if isinstance(figsize, tuple):
            fig.set_size_inches(figsize)
        else:
            fig.set_size_inches(get_dim(figsize))

        # Get the text artists in the figure and set the font size
        for text_artist in fig.findobj(match=plt.Text):
            text_artist.set_fontsize(plt.rcParams["font.size"])

        # X labels:
        # Get fixed number of xtick values (FixedLocator)
        # get x-label of current axis
        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels(ax.get_xticklabels(), fontsize=plt.rcParams["xtick.labelsize"])
        ax.set_xlabel(ax.get_xlabel(), fontsize=plt.rcParams["axes.labelsize"])

        # Y labels:
        # Get fixed number of ytick values (FixedLocator)
        # get y-label of current axis
        ax.set_yticks(ax.get_yticks())
        ax.set_yticklabels(ax.get_yticklabels(), fontsize=plt.rcParams["ytick.labelsize"])
        ax.set_ylabel(ax.get_ylabel(), fontsize=plt.rcParams["axes.labelsize"])

        # Set figure title
        ax.set_title(ax.get_title(), fontsize=plt.rcParams["axes.titlesize"])

        legend = ax.get_legend()
        if legend:
            for text in legend.get_texts():
                text.set_fontsize(plt.rcParams["legend.fontsize"])

        # Tight layout
        fig.tight_layout()

        return fig, ax
