from __future__ import annotations

from dataclasses import dataclass

import matplotlib.pyplot as plt

__all__ = [
    "GOLDEN_RATIO",
    "WIDTH",
    "convert_unit",
    "get_dim",
    "set_dim",
]

GOLDEN_RATIO = (5**0.5 - 1) / 2

_UNIT_CONVERSIONS = {
    ("in", "cm"): 2.54,
    ("in", "pt"): 72.27,
    ("cm", "pt"): 72.27 / 2.54,
    ("mm", "pt"): 72.27 / 25.4,
    ("in", "mm"): 25.4,
    ("cm", "mm"): 10.0,
}


def convert_unit(from_unit: str, to_unit: str) -> float:
    """Convert from one unit to another."""
    if (from_unit, to_unit) in _UNIT_CONVERSIONS:
        return _UNIT_CONVERSIONS[(from_unit, to_unit)]
    elif (to_unit, from_unit) in _UNIT_CONVERSIONS:
        return 1.0 / _UNIT_CONVERSIONS[(to_unit, from_unit)]
    else:
        raise ValueError(f"Conversion {from_unit} to {to_unit} not implemented.")


@dataclass
class WIDTH:
    # Determined via: https://tex.stackexchange.com/a/39384
    #  all textwidths measured in pt
    _units: str = "pt"
    # Latex default
    latex_default_article: float = 345.0
    # Cambridge thesis guidelines
    mres_report: float = 398.3386
    phd_thesis: float = 455.24411
    # Machine learning conference guidelines
    neurips_article: float = 397.48499
    # https://www-nature-com.ezp.lib.cam.ac.uk/nature/for-authors/final-submission
    nature_column: float = 89.0 * convert_unit("mm", "pt")
    nature_2column: float = 183.0 * convert_unit("mm", "pt")
    nature_page: float = 247.0 * convert_unit("mm", "pt")
    # https://www.science.org/content/page/instructions-preparing-initial-manuscript
    science_column: 5.7 * convert_unit("cm", "pt")
    science_2column: float = 12.1 * convert_unit("cm", "pt")
    science_3column: float = 18.4 * convert_unit("cm", "pt")


def get_dim(
    width: float = WIDTH.latex_default_article,
    width_unit: str = "pt",
    fraction_of_line_width: float = 1.0,
    ratio: float = GOLDEN_RATIO,
) -> tuple[float, float]:
    """
    Return figure (width, height) in inches to avoid scaling when the figure is
    inserted into a latex document.

    Args:
        width (float): Textwidth of the document to make fontsizes match, in the
            units given in `width_unit`. Defaults to `WIDTH.latex_default_article`
            (345.0pt)
        width_unit (str, optional): Units of width. Defaults to "pt".
        fraction_of_line_width (float, optional): Fraction of the document width
            which you wish the figure to occupy.  Defaults to 1.
        ratio (float, optional): Fraction of figure width that the figure height
            should be. Defaults to the golden ratio (5 ** 0.5 - 1)/2.
    Returns:
        fig_dim (tuple):
            Dimensions of figure in inches - (width, height).
    """

    # Width of figure
    fig_width_pt = width * fraction_of_line_width

    # Figure width in inches
    fig_width_in = fig_width_pt * convert_unit(width_unit, "in")
    # Figure height in inches
    fig_height_in = fig_width_in * ratio

    return (fig_width_in, fig_height_in)


def set_dim(
    fig: plt.Figure | None = None,
    **get_dim_kwargs,
) -> None:
    """Set aesthetic figure dimensions to avoid scaling in latex.
    Args:
        fig (plt.Figure | None): The figure to set the dimensions of. If None,
            the current figure is used. Defaults to None.
        width (float): Textwidth of the document to make fontsizes match, in the
            units given in `width_unit`.
        width_unit (str, optional): Units of width. Defaults to "pt".
        fraction_of_line_width (float, optional): Fraction of the document width
            which you wish the figure to occupy.  Defaults to 1.
        ratio (float, optional): Fraction of figure width that the figure height
            should be. Defaults to the golden ratio (5 ** 0.5 - 1)/2.
    Returns:
        void; alters current figure to have the desired dimensions
    """
    if fig is None:
        fig = plt.gcf()
    fig.set_size_inches(get_dim(**get_dim_kwargs))
