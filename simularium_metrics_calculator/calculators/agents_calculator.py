#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict

import numpy as np
from simulariumio import TrajectoryData

from .calculator import Calculator


class AgentsCalculator(Calculator):
    def __init__(self, time_index: int = 0):
        """
        Calculates the agent IDs at the given timestep.

        Parameters
        ----------
        time_index: int (optional)
            use every nth time step
            Default: 0
        """
        self.time_index = time_index

    def traces(self, traj_data: TrajectoryData) -> Dict[str, np.ndarray]:
        """
        Return the agent IDs at the given time step.

        Parameters
        ----------
        traj_data: TrajectoryData
            Trajectory data for which to calculate metrics.

        Returns
        -------
        Dict[str, np.ndarray]
            The name of each trace mapped
            to an array of the data for that trace
        """
        return {"Agent IDs": traj_data.agent_data.unique_ids[self.time_index]}

    def units(self, traj_data: TrajectoryData) -> str:
        """
        Return a string label for the units to use on the axis title

        Parameters
        ----------
        traj_data: TrajectoryData
            Trajectory data for which to calculate the metric

        Returns
        -------
        str
            A label for the units
        """
        return ""
