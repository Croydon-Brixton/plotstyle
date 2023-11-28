from __future__ import annotations

from distutils.spawn import find_executable

import matplotlib.pyplot as plt


def latex_is_available() -> bool:
    """Returns True if latex is available on the system."""
    return find_executable("latex") is not None


def use_tex(preamble: str | None = None) -> None:
    """Updates matplotlib.rcParams to use latex backend."""
    if not latex_is_available():
        raise RuntimeError("Latex executable not found.")

    if preamble is None:
        if "pgf.preamble" in plt.rcParams:
            preamble = plt.rcParams["pgf.preamble"]
    plt.rcParams.update(
        {
            "pgf.texsystem": "pdflatex",
            "text.usetex": True,
            "pgf.preamble": preamble,
        }
    )
