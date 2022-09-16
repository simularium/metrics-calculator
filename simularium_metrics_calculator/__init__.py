# -*- coding: utf-8 -*-

"""Top-level package for simularium_metrics_calculator."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("simularium_metrics_calculator")
except PackageNotFoundError:
    __version__ = "uninstalled"

__author__ = "Blair Lyons"
__email__ = "blair208@gmail.com"


from .calculators import *