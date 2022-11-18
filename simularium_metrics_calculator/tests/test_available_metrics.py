#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Any, Dict, List

import pytest
from simulariumio import InputFileData

from simularium_metrics_calculator import MetricsManager


@pytest.mark.parametrize(
    "expected_metrics",
    [
        (
            [
                {
                    "display_name": "Time",
                    "metric_type": "PER_TIME",
                    "exclude_axes": ["y"],
                },
                {
                    "display_name": "Agent IDs",
                    "metric_type": "PER_AGENT",
                    "exclude_axes": ["y"],
                },
                {
                    "display_name": "Number of agents",
                    "metric_type": "PER_TIME",
                    "exclude_axes": [],
                },
                {
                    "display_name": "Nearest neighbor distance",
                    "metric_type": "PER_AGENT",
                    "exclude_axes": [],
                },
            ]
        ),
    ],
)
def test_available_metrics(
    expected_metrics: List[Dict[str, Any]],
) -> None:
    manager = MetricsManager(
        input_data=InputFileData(
            file_path=(
                "simularium_metrics_calculator/tests/data/"
                "aster_pull3D_couples_actin_solid_3_frames_small.json"
            ),
        )
    )
    test_metrics = manager.available_metrics()
    assert len(test_metrics) >= len(expected_metrics)
    for expected_metric_info in expected_metrics:
        found = False
        for test_metric_info in test_metrics:
            if test_metric_info["display_name"] == expected_metric_info["display_name"]:
                assert isinstance(test_metric_info["uid"], int)
                assert (
                    test_metric_info["metric_type"]
                    == expected_metric_info["metric_type"]
                )
                assert (
                    test_metric_info["exclude_axes"]
                    == expected_metric_info["exclude_axes"]
                )
                found = True
                break
        assert found
