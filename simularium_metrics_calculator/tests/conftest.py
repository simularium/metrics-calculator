#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict

import numpy as np
from simulariumio import AgentData, MetaData, ScatterPlotData, TrajectoryData, UnitData

simple_test_traj_data = TrajectoryData(
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
)


def assert_scatter_plot_data_equal(
    plot_data: ScatterPlotData,
    title: str,
    xaxis_title: str,
    yaxis_title: str,
    xtrace: np.ndarray,
    ytraces: Dict[str, np.ndarray],
) -> None:
    assert plot_data.title == title
    assert plot_data.xaxis_title == xaxis_title
    assert plot_data.yaxis_title == yaxis_title
    assert False not in np.isclose(plot_data.xtrace, xtrace)
    assert plot_data.ytraces.keys() == ytraces.keys()
    for type_name in ytraces:
        assert False not in np.isclose(plot_data.ytraces[type_name], ytraces[type_name])
