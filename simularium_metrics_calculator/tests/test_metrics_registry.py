#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simularium_metrics_calculator.metrics_registry import metrics_list


def test_metrics_registry() -> None:
    uids = set()
    for metric in metrics_list:
        uids.add(metric.uid)
    unique_ids = list(uids)
    assert len(unique_ids) == len(metrics_list), "Multiple metrics have the same ID, make sure new metrics have a unique ID."
