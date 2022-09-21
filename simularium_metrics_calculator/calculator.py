#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC
import json

from simulariumio import (
    InputFileData, 
    FileConverter,
    TrajectoryData, 
    ScatterPlotData, 
    HistogramPlotData,
)
from simulariumio.constants import CURRENT_VERSION
        
    

class Calculator(ABC):

    def __init__(self, input_data: InputFileData):
        """
        This object takes simulation trajectory data
        and calculates metrics that can be plotted 
        in the Simularium Viewer.

        Parameters
        ----------
        input_data : InputFileData
            An object containing simularium data, 
            either a file path where the data can be loaded, 
            or the data already in memory. Data can be 
            in JSON or binary format.
        """
        self.converter = FileConverter(input_data)
        plot_data = self._calculate(self.converter._data)
        plot_type = "scatter"
        if isinstance(plot_data, HistogramPlotData):
            plot_type = "histogram"
        self.converter.add_plot(plot_data, plot_type)
    
    @staticmethod
    def _calculate(traj_data: TrajectoryData) -> ScatterPlotData or HistogramPlotData:
        pass
    
    def plot_data(self) -> str:
        """
        Get the calculated plot data as a JSON string.
        
        Returns
        -------
        str
            A JSON string of plot data in simularium format.
        """
        return json.dumps(
            {
                "version": CURRENT_VERSION.PLOT_DATA,
                "data": self.converter._data.plots,
            }
        )
