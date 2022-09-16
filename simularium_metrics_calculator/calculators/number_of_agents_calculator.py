#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Tuple

from simulariumio import TrajectoryData, ScatterPlotData

from ..calculator import Calculator


class NumberOfAgentsCalculator(Calculator):

    def calculate(traj_data: TrajectoryData) -> Tuple[ScatterPlotData, str]:
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
            A scatter plot of number of each agent type vs time.
        """
        # TODO
