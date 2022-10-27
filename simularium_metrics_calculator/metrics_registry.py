#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .calculators import (
    AgentsCalculator,
    NearestNeighborCalculator,
    NumberOfAgentsCalculator,
    TimesCalculator,
)
from .constants import METRIC_TYPE
from .exceptions import MetricNotFoundError
from .metric_info import MetricInfo

metrics_registry = {
    0: MetricInfo(
        uid=0,
        display_name="Time",
        metric_type=METRIC_TYPE.PER_TIME,
        calculator=TimesCalculator,
    ),
    1: MetricInfo(
        uid=1,
        display_name="Agent IDs",
        metric_type=METRIC_TYPE.PER_AGENT,
        calculator=AgentsCalculator,
    ),
    2: MetricInfo(
        uid=2,
        display_name="Number of agents",
        metric_type=METRIC_TYPE.PER_TIME,
        calculator=NumberOfAgentsCalculator,
    ),
    3: MetricInfo(
        uid=3,
        display_name="Nearest neighbor distance",
        metric_type=METRIC_TYPE.PER_AGENT,
        calculator=NearestNeighborCalculator,
    ),
}


def metric_info_for_id(metric_id: int) -> MetricInfo:
    """
    Get a MetricInfo for a given metric's unique id.
    Raise an error if the metric_id is not found in the registry.
    """
    if metric_id not in metrics_registry:
        raise MetricNotFoundError(metric_id)
    return metrics_registry[metric_id]
