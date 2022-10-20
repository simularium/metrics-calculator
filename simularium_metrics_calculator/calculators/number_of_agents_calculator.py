#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

import numpy as np
from simulariumio import ScatterPlotData, TrajectoryData

from .calculator import Calculator


class NumberOfAgentsCalculator(Calculator):
    def __init__(self, exclude_types: List[str] = None, stride: int = 1):
        """
        Calculates the number of agents of each type over time.

        Parameters
        ----------
        exclude_types : List[str] (optional)
            Type names for agents to ignore
            Default: include all type names found in the trajectory
        stride: int (optional)
            include every nth timestep
            Default: 1
        """
        self.exclude_types = exclude_types
        self.stride = stride
        
    def calculate(self, traj_data: TrajectoryData) -> ScatterPlotData:
        """
        Return a ScatterPlotData with the number of agents
        of each type over time.

        Parameters
        ----------
        traj_data: TrajectoryData
            Trajectory data for which to calculate metrics.

        Returns
        -------
        ScatterPlotData
            Scatter plot data with number of each agent type vs time
        """
        type_names_array = np.array(traj_data.agent_data.types)
        time_units = str(traj_data.time_units)
        unique_types = np.unique(type_names_array)
        ytraces = {}
        for type_name in unique_types:
            if type_name in self.exclude_types:
                continue
            ytraces[type_name] = np.count_nonzero(type_names_array == type_name, axis=1)[::self.stride]
        return ScatterPlotData(
            title="Number of Agents over Time",
            xaxis_title=f"Time ({time_units})",
            yaxis_title="Agent count",
            xtrace=traj_data.agent_data.times[::self.stride],
            ytraces=ytraces,
            render_mode="lines",
        )
