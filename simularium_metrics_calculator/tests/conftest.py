#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict
import numpy as np

from simulariumio import TrajectoryData, MetaData, AgentData, UnitData, ScatterPlotData


def assert_scatter_plot_data_equal(
    plot_data: ScatterPlotData, 
    title: str,
    xaxis_title: str, 
    yaxis_title: str,
    xtrace: np.ndarray, 
    ytraces: Dict[str, np.ndarray]
):
    assert plot_data.title == title
    assert plot_data.xaxis_title == xaxis_title
    assert plot_data.yaxis_title == yaxis_title
    assert False not in np.isclose(plot_data.xtrace, xtrace)
    assert plot_data.ytraces.keys() == ytraces.keys()
    for type_name in ytraces:
        assert False not in np.isclose(plot_data.ytraces[type_name], ytraces[type_name])