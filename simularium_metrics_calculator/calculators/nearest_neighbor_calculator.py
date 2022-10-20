#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

import numpy as np
from simulariumio import HistogramPlotData, TrajectoryData
import scipy

from .calculator import Calculator


class NearestNeighborCalculator(Calculator):
    def __init__(self, time_indices: List[int]):
        """
        Calculates the distance to the nearest neighbor for each agent
        at a given time index

        Parameters
        ----------
        time_index: int
            which time step to use
        """
        self.time_indices = time_indices
        
    @staticmethod
    def _nearest_neighbor_distances(positions):
        """
        Distance to nearest neighbor for each position
        """
        dist_grid = scipy.spatial.distance.cdist(positions, positions)
        masked_grid = np.ma.array(dist_grid, mask=np.eye(len(positions)))
        return np.min(masked_grid, axis=1).data
        
    def calculate(self, traj_data: TrajectoryData) -> HistogramPlotData:
        """
        Return a HistogramPlotData with 
        the distance to the nearest neighbor for each agent.

        Parameters
        ----------
        traj_data: TrajectoryData
            Trajectory data for which to calculate metrics.

        Returns
        -------
        HistogramPlotData
            Histogram plot data with nearest neighbor distance for each agent
        """
        time_units = str(traj_data.time_units)
        distance_units = str(traj_data.spatial_units)
        traces = {}
        for time_index in self.time_indices:
            time = traj_data.agent_data.times[time_index]
            trace_name = f"t = {time} {time_units}"
            traces[trace_name] = self._nearest_neighbor_distances(
                traj_data.agent_data.positions[time_index])
        return HistogramPlotData(
            title="Nearest Neighbor Distance",
            xaxis_title=f"Distance ({distance_units})",
            traces=traces,
        )
