# -*- coding: utf-8 -*-

"""Top-level package for simularium_metrics_calculator."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("simularium_metrics_calculator")
except PackageNotFoundError:
    __version__ = "uninstalled"

__author__ = "Blair Lyons"
__email__ = "blair208@gmail.com"


from .calculators import AgentsCalculator  # noqa: F401
from .calculators import NearestNeighborCalculator  # noqa: F401
from .calculators import NumberOfAgentsCalculator  # noqa: F401
from .calculators import TimesCalculator  # noqa: F401
from .constants import METRIC_TYPE  # noqa: F401
from .metrics_manager import MetricsManager  # noqa: F401
