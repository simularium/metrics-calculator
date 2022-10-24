#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from typing import List

import pytest
from simulariumio import HistogramPlotData, InputFileData

from simularium_metrics_calculator import MetricsManager
from simularium_metrics_calculator.exceptions import MetricNotFoundError
from simularium_metrics_calculator.tests import assert_plot_data_equal


@pytest.mark.parametrize(
    "spatial_data_path, plot_metrics, expected_plot_data",
    [
        (
            (
                "simularium_metrics_calculator/tests/data/"
                "aster_pull3D_couples_actin_solid_3_frames_small.json"
            ),
            [
                [3],
            ],
            {
                "layout": {
                    "title": "Nearest neighbor distance",
                    "xaxis": {"title": "Nearest neighbor distance (\u00b5m)"},
                    "yaxis": {"title": "frequency"},
                },
                "data": [
                    {
                        "name": "t = 0.0 s",
                        "type": "histogram",
                        "x": [89.48637941050023, 89.48637941050023],
                    },
                    {
                        "name": "t = 0.1 s",
                        "type": "histogram",
                        "x": [87.40050629143975, 87.40050629143975],
                    },
                ],
            },
        ),
        # metric ID does not exist
        pytest.param(
            (
                "simularium_metrics_calculator/tests/data/"
                "aster_pull3D_couples_actin_solid_3_frames_small.json"
            ),
            [
                [-1],
            ],
            {},
            marks=pytest.mark.raises(exception=MetricNotFoundError),
        ),
    ],
)
def test_num_agents(
    spatial_data_path: str,
    plot_metrics: List[List[int]],
    expected_plot_data: HistogramPlotData,
) -> None:
    test_plot_data = json.loads(
        MetricsManager(
            input_data=InputFileData(
                file_path=spatial_data_path,
            ),
            plot_metrics=plot_metrics,
        ).plot_data()
    )["data"][0]
    assert_plot_data_equal(test_plot_data, expected_plot_data, is_histogram=True)
