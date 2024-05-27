from __future__ import annotations

import datetime
import os
import re
from typing import Optional

import matplotlib.pyplot as plt

__all__ = ["save_timestamped_figure"]

_VALID_EXTENSIONS = ("pdf", "png", "jpg", "jpeg", "svg", "eps")


def save_timestamped_figure(
    name: str,
    save_dir: str | None = None,
    fig: plt.Figure | None = None,
    file_types: str | list[str] = ["pdf", "png"],
    date_format: str = "v%Y-%m-%d-%H-%M",
    bbox_inches: Optional[str] = "tight",
    **savefig_kwargs,
) -> list[str]:
    """Save a figure with a time stamp in the file name.

    Args:
        name (str): The base name of the figure (without timestamp). If `save_dir` is given, this is a relative path
            from `save_dir`.
        save_dir (str, optional): The directory to save the figure in. Defaults to None, in which case the figure is
            saved in the current working directory if `name` is a relative path, or in the same direcotry specified by
            `name` if `name` is an absolute path.
        fig (plt.Figure, optional): The figure to save. Defaults to None, in which case the current figure is saved.
        file_types (str or list[str], optional): The file types to save the figure as. Defaults to ["pdf", "png"].
            Must be one of "pdf", "png", "jpg", "jpeg", "svg", "eps".
        date_format (str, optional): The format of the time stamp. Defaults to "v%Y-%m-%d-%H-%M".
        bbox_inches (str, optional): The bounding box to use. Defaults to "tight", which ensures that all elements of
            the figure are included in the saved image, even if they are outside the axes limits. If None, the figure
            is saved with the default bounding box.
        **savefig_kwargs: Additional keyword arguments to pass to `plt.savefig`. See
            https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html for details.

    Returns:
        saved_figure_paths (list[str]): A list of the paths to the saved figures.
    """
    if isinstance(file_types, str):
        file_types = [file_types]

    # check that all file types are valid
    for file_type in file_types:
        if file_type not in _VALID_EXTENSIONS:
            raise ValueError(f"Unrecognized file type {file_type}. Valid file types are {_VALID_EXTENSIONS}.")

    # if save_dir is given, check that the name is not an absolute path
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        if os.path.isabs(name):
            raise ValueError("If `save_dir` is given, name must be a relative path.")
        # Turn the name into an absolute path
        name = os.path.join(save_dir, name)

    # remove any file extensions from the name
    name = re.sub(f'\.({"|".join(_VALID_EXTENSIONS)})$', "", name)

    # get the current time stamp
    timestamp = datetime.datetime.now().strftime(date_format)

    # save the figure(s)
    saved_figure_paths = []
    for file_type in file_types:
        fname = f"{name}_{timestamp}.{file_type}"
        save_func = plt.savefig if fig is None else fig.savefig
        save_func(
            fname,
            bbox_inches=bbox_inches,
            **savefig_kwargs,
        )
        saved_figure_paths.append(fname)

    # return the file name
    return saved_figure_paths


if __name__ == "__main__":
    import os

    # Test saving a random figure
    random_fig = plt.figure()
    plt.plot([1, 2, 3], [1, 2, 3])

    saved_paths = save_timestamped_figure("test", save_dir=".", file_types=["pdf", "png"])
    print(saved_paths)

    # Delete saved paths again
    for path in saved_paths:
        os.remove(path)
