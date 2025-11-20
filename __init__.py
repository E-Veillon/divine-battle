#!/usr/bin/python
"""Global init of the game."""

import os
from collections.abc import Callable
import typing as tp


# Main paths inside file tree
ROOT = os.path.dirname(__file__)
"""Absolute path to the main directory."""

UTILSPATH = os.path.join(ROOT, "utils")
"""Absolute path to utils directory containing importable features."""

CONFIGPATH = os.path.join(ROOT, "config")
"""Absolute path to config directory containing all YAML config files."""

# Arguments parsing for all executable scripts inside the project
def _parse_input_args(
    cmd_line_func: Callable,
    process_args_func: Callable,
    standalone: bool = True,
    **kwargs
) -> dict[str, tp.Any]:
    """
    Gather and process input arguments, either from command-line or external script.
    
    Parameters:
        cmd_line_func (callable):       Function parsing command line arguments into attributes
                                        of a python object (e.g. argparse.Namespace object).

        process_args_func (callable):   Function asserting and processing input arguments.

        standalone (bool):              Whether parsed script is used directly through
                                        command-line (stand-alone script) or in an external
                                        pipeline script.

        kwargs:                         Input arguments values for external script calls.

    Returns:
        Dict of input arguments names and values.
    """
    if standalone: # Direct use of the script through command line
        print("Command line mode detected.")
        args = cmd_line_func()
        args = args.__dict__
    else: # Indirect use of the script as part of a pipeline script in another file
        print("Pipeline mode detected.")
        args = kwargs

    args: dict[str, tp.Any] = process_args_func(args)

    return args


def _clean_none_values(dct: dict[str, tp.Any]) -> dict[str, tp.Any]:
    """
    Remove all keys which associated value is None.

    Parameters
    ----------

    dct: dict[str, Any]
        Dictionary to clean unused keys from.

    Returns
    -------

    dict[str, Any]
        Same dict but purged of keys with value None.
    """
    return {k: v for k, v in dct.items() if dct.get(k) is not None}