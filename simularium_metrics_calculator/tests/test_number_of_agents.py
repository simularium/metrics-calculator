#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import numpy as np

from simulariumio import TrajectoryData, MetaData, AgentData, UnitData, ScatterPlotData

from simularium_metrics_calculator import NumberOfAgentsCalculator
from .conftest import assert_scatter_plot_data_equal


@pytest.mark.parametrize(
    "traj_data, expected_xaxis_title, expected_ytraces",
    [
        (
            TrajectoryData(
                meta_data=MetaData(),
                agent_data=AgentData(
                    times=0.5 * np.array(list(range(3))),
                    n_agents=np.array(3 * [3]),
                    viz_types=np.array(3 * [3 * [1000.0]]),
                    unique_ids=np.array([[0.0, 1.0, 2.0], [0.0, 1.0, 2.0], [0.0, 1.0, 2.0]]),
                    types=[["C", "U", "C"], ["U", "L", "S"], ["O", "Y", "W"]],
                    positions=np.zeros((3, 3, 3)),
                    radii=np.ones((3, 3)),
                ),
                time_units=UnitData("ns"),
            ),
            "Time (ns)",
            {
                "C" : np.array([2., 0., 0.]),
                "U" : np.array([1., 1., 0.]),
                "L" : np.array([0., 1., 0.]),
                "S" : np.array([0., 1., 0.]),
                "O" : np.array([0., 0., 1.]),
                "Y" : np.array([0., 0., 1.]),
                "W" : np.array([0., 0., 1.]),
            }
        )
    ],
)
def test_num_agents(
    traj_data: TrajectoryData, 
    expected_xaxis_title: str, 
    expected_ytraces: np.ndarray
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
