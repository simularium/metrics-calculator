#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pytest
from simulariumio import TrajectoryData

from simularium_metrics_calculator.calculators import NumberOfAgentsCalculator
from simularium_metrics_calculator.tests import (
    assert_scatter_plot_data_equal,
    simple_test_traj_data,
)


@pytest.mark.parametrize(
    "traj_data, expected_xaxis_title, expected_ytraces",
    [
        (
            simple_test_traj_data,
            "Time (ns)",
            {
                "C": np.array([2.0, 0.0, 0.0]),
                "U": np.array([1.0, 1.0, 0.0]),
                "L": np.array([0.0, 1.0, 0.0]),
                "S": np.array([0.0, 1.0, 0.0]),
                "O": np.array([0.0, 0.0, 1.0]),
                "Y": np.array([0.0, 0.0, 1.0]),
                "W": np.array([0.0, 0.0, 1.0]),
            },
        )
    ],
)
def test_num_agents(
    traj_data: TrajectoryData, expected_xaxis_title: str, expected_ytraces: np.ndarray
) -> None:
    plot_data = NumberOfAgentsCalculator._calculate(traj_data)
    assert_scatter_plot_data_equal(
        plot_data,
        "Number of Agents over Time",
        expected_xaxis_title,
        "Agent count",
        traj_data.agent_data.times,
        expected_ytraces,
    )
