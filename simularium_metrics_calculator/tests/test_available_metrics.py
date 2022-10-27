#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict

import pytest

from simularium_metrics_calculator import METRIC_TYPE, MetricsManager


@pytest.mark.parametrize(
    "metric_type, expected_metrics",
    [
        (
            METRIC_TYPE.PER_TIME,
            {
                0: "Time",
                2: "Number of agents",
            },
        ),
        (
            METRIC_TYPE.PER_AGENT,
            {
                1: "Agent IDs",
                3: "Nearest neighbor distance",
            },
        ),
    ],
)
def test_available_metrics(
    metric_type: METRIC_TYPE,
    expected_metrics: Dict[int, str],
) -> None:
    test_metrics = MetricsManager.available_metrics(metric_type)
    for metric_id in expected_metrics:
        assert metric_id in test_metrics
        assert test_metrics[metric_id] == expected_metrics[metric_id]
