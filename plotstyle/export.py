from __future__ import annotations

import datetime
import os
import re

import matplotlib.pyplot as plt

_VALID_EXTENSIONS = ("pdf", "png", "jpg", "jpeg", "svg", "eps")


def save_timestamped_figure(
    name: str,
    save_dir: str | None = None,
    fig: plt.Figure | None = None,
    file_types: str | list[str] = ["pdf", "png"],
    date_format: str = "v%Y-%m-%d-%H:%M",
    **savefig_kwargs,
):
    """Save a figure with a time stamp in the file name."""
    if isinstance(file_types, str):
        file_types = [file_types]

    # check that all file types are valid
    for file_type in file_types:
        if file_type not in _VALID_EXTENSIONS:
            raise ValueError(
                f"Unrecognized file type {file_type}. Valid file types are {_VALID_EXTENSIONS}."
            )

    # if save_dir is given, check that the name is not an absolute path
    if save_dir:
        if os.path.isabs(name):
            raise ValueError("If `save_dir` is given, name must be a relative path.")
        # Turn the name into an absolute path
        name = os.path.join(save_dir, name)

    # remove any file extensions from the name
    name = re.sub(f'\.({"|".join(_VALID_EXTENSIONS)})$', "", name)

    # get the current time stamp
    timestamp = datetime.datetime.now().strftime(date_format)

    # save the figure(s)
    for file_type in file_types:
        if fig is None:
            plt.savefig(
                f"{name}_{timestamp}.{file_type}",
                **savefig_kwargs,
            )
        else:
            fig.savefig(
                f"{name}_{timestamp}.{file_type}",
                **savefig_kwargs,
            )
