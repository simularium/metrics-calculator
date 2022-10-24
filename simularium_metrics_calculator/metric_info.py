#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Type

from .calculators.calculator import Calculator
from .constants import METRIC_TYPE


class MetricInfo:
    uid: int
    display_name: str
    metric_type: METRIC_TYPE
    calculator: Type[Calculator]
    
    def __init__(
        self, 
        uid: int, 
        display_name: str, 
        metric_type: METRIC_TYPE,
        calculator: Type[Calculator]
    ):
        """
        Data about a metric that can be calculated.
        
        Parameters
        ----------
        uid: int
            The unique ID for this calculator, 
            for communication with clients choosing metrics.
        display_name: str
            The name for this metric to display on a plot axis.
        metric_type: METRIC_TYPE
            The type of metric, for determining which metrics 
            can be plotted against one another.
        calculator: Type[Calculator]
            The calculator class for this metric.
        """
        self.uid = uid
        self.display_name = display_name
        self.metric_type = metric_type
        self.calculator = calculator
