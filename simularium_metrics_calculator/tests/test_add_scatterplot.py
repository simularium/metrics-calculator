#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
import json

import numpy as np
import pytest
from simulariumio import InputFileData, ScatterPlotData

from simularium_metrics_calculator import MetricsManager
from simularium_metrics_calculator.tests import assert_plot_data_equal


@pytest.mark.parametrize(
    "spatial_data_path, plot_metrics, expected_plot_data",
    [
        (
            "simularium_metrics_calculator/tests/data/aster_pull3D_couples_actin_solid_3_frames_small.json",
            [
                [0, 2],
            ],
            {
                "layout": {
                    "title": "Number of agents vs time", 
                    "xaxis": {"title": "Time (s)"}, 
                    "yaxis": {"title": "Number of agents"}
                }, 
                "data": [
                    {
                        "name": "microtubule", 
                        "type": "scatter", 
                        "x": [0.0, 0.05, 0.1], 
                        "y": [1, 1, 1], 
                        "mode": "lines"
                    }, 
                    {
                        "name": "motor complex", 
                        "type": "scatter", 
                        "x": [0.0, 0.05, 0.1], 
                        "y": [1, 1, 1], 
                        "mode": "lines"
                    },
                ],
            },
        )
    ],
)
def test_num_agents(
    spatial_data_path: str, 
    plot_metrics: List[List[int]], 
    expected_plot_data: ScatterPlotData,
) -> None:
    test_plot_data = json.loads(
        MetricsManager(
            input_data=InputFileData(
                file_path=spatial_data_path,
            ),
            plot_metrics=plot_metrics,
        ).plot_data()
    )["data"][0]
    assert_plot_data_equal(test_plot_data, expected_plot_data)
