#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class METRIC_TYPE(Enum):
    """
    The type of a metric, for determining
    which metrics can be plotted against one another.
    """

    OTHER = "OTHER"
    PER_TIME = "PER_TIME"
    PER_AGENT = "PER_AGENT"
