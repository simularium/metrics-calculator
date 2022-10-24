#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MetricNotFoundError(Exception):
    def __init__(self, metric_uid: int, **kwargs: int):
        """
        This exception is intended to communicate that the requested metric ID
        does not exist in the metrics registry.
        """
        super().__init__(**kwargs)
        self.metric_uid = metric_uid

    def __str__(self) -> str:
        return f"Cannot add plot: Metric ID = {self.metric_uid} not found in registry."
