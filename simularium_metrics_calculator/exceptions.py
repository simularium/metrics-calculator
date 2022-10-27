#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MetricNotFoundError(Exception):
    def __init__(self, metric_id: int, **kwargs: int):
        """
        This exception is intended to communicate that the requested metric ID
        does not exist in the metrics registry.
        """
        super().__init__(**kwargs)
        self.metric_id = metric_id

    def __str__(self) -> str:
        return f"Cannot add plot: Metric ID = {self.metric_id} not found in registry."


class IncompatibleMetricsError(Exception):
    def __init__(self, x_metric_name: str, y_metric_name: str, **kwargs: int):
        """
        This exception is intended to communicate that the requested metrics
        have incompatible metric types and can't be plotted against each other.
        """
        super().__init__(**kwargs)
        self.x_metric_name = x_metric_name
        self.y_metric_name = y_metric_name

    def __str__(self) -> str:
        return (
            f"Cannot add plot: {self.y_metric_name} and "
            f"{self.x_metric_name} are incompatible."
        )
