from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

__all__ = [
    "cambridge_special",
    "cambridge_light",
    "cambridge_core",
    "cambridge_dark",
]


class Colors:
    def __init__(self, colors: list[str] | dict[str, str] | str) -> None:
        if isinstance(colors, dict):
            self.colors = colors
        elif isinstance(colors, list):
            self.colors = {str(i): color for i, color in enumerate(colors)}
        else:
            raise ValueError(f"Unrecognized type {type(colors)} for colors.")

    @classmethod
    def from_json(cls, json_file: str) -> Colors:
        import json

        with open(json_file, "r") as f:
            colors: dict[str, str] = json.load(f)
        return cls(colors)

    @classmethod
    def from_yaml(cls, yaml_file: str) -> Colors:
        import yaml

        with open(yaml_file, "r") as f:
            colors: dict[str, str] = yaml.load(f, Loader=yaml.FullLoader)
        return cls(colors)

    def __len__(self) -> int:
        return len(self.colors)

    @property
    def names(self) -> list[str]:
        return list(self.colors.keys())

    def _idx_to_color_key(self, idx: int) -> str:
        if idx >= len(self.colors):
            raise IndexError(f"Index {idx} is out of bounds. The color palette has {len(self.colors)} colors.")
        elif idx < (-1 * len(self.colors)):
            raise IndexError(f"Index {idx} is out of bounds. The color palette has {len(self.colors)} colors.")
        key = self.names[idx]
        return key

    def __getitem__(self, key: str | int) -> str:
        if isinstance(key, int):
            key = self._idx_to_color_key(key)
        return self.colors[key]

    def __setitem__(self, key: str | int, value: str):
        if isinstance(key, int):
            if key > len(self.colors):
                raise IndexError(f"Index {key} is out of bounds. The color palette has {len(self.colors)} colors.")
            elif key == len(self.colors):
                # Add a new color
                key = str(key)
            else:
                # Update an existing color
                key = self._idx_to_color_key(key)
        self.colors[key] = value

    def __add__(self, other: Colors) -> Colors:
        return Colors(self.colors | other.colors)

    def to_cycler(self, **kwargs) -> plt.cycler:
        return plt.cycler(color=self.colors.values(), **kwargs)

    def to_palette(self, **kwargs) -> sns.Palette:
        return sns.color_palette(list(self.colors.values()), **kwargs)

    def to_rgb_list(self) -> list[tuple[float, float, float]]:
        return [mpl.colors.colorConverter.to_rgb(rgb) for rgb in self.colors.values()]

    def to_rgba_list(self) -> list[tuple[float, float, float, float]]:
        return [mpl.colors.colorConverter.to_rgba(rgba) for rgba in self.colors.values()]

    def to_hex_list(self) -> list[str]:
        return [mpl.colors.rgb2hex(rgb) for rgb in self.to_rgb_list()]

    def to_hsv_list(self) -> list[tuple[float, float, float]]:
        return [mpl.colors.rgb_to_hsv(rgb) for rgb in self.to_rgb_list()]

    def _repr_html_(self) -> str:
        """Rich display of the color palette in an HTML frontend."""
        return self.to_palette()._repr_html_()


cambridge_special = Colors(
    # Cambridge colour palettes from: https://www.cam.ac.uk/system/files/guidelines_v8_december_2019.pdf#page=17
    colors={"cambridge_blue": "#a3c1ad", "logo_red": "#ef3340", "logo_yellow": "#ffd100"}
)

cambridge_light = Colors(
    # Cambridge colour palettes from: https://www.cam.ac.uk/system/files/guidelines_v8_december_2019.pdf#page=17
    colors={
        "Pantone_197": "#E89CAE",
        "Pantone_284": "#6CACE4",
        "Pantone_142": "#F1BE48",
        "Pantone_583": "#B7BF10",
        "Pantone_5215": "#AF95A6",
        "Pantone_557": "#85B09A",
    }
)

cambridge_core = Colors(
    # Cambridge colour palettes from: https://www.cam.ac.uk/system/files/guidelines_v8_december_2019.pdf#page=17
    colors={
        "Pantone_199": "#D50032",
        "Pantone_285": "#0072CE",
        "Pantone_158": "#E87722",
        "Pantone_369": "#64A70B",
        "Pantone_513": "#93328E",
        "Pantone_7466": "#00B0B9",
    }
)

cambridge_dark = Colors(
    # Cambridge colour palettes from: https://www.cam.ac.uk/system/files/guidelines_v8_december_2019.pdf#page=17
    colors={
        "Pantone_1955": "#A81538",
        "Pantone_541": "#003C71",
        "Pantone_718": "#BE4D00",
        "Pantone_574": "#4E5B31",
        "Pantone_669": "#3F2A56",
        "Pantone_5473": "#115E67",
    }
)
