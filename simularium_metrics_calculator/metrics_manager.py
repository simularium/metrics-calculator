#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from typing import Union, List

from simulariumio import (
    InputFileData,
    FileConverter,
    HistogramPlotData,
    ScatterPlotData,
)
from simulariumio.constants import CURRENT_VERSION

from .calculators.calculator import Calculator


class MetricsManager:
    def __init__(self, input_data: InputFileData, calculators: List[Calculator]):
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
        for calculator in calculators:
            plot_data = calculator.calculate(self.converter._data)
            self.converter.add_plot(plot_data, self._plot_type(plot_data))

    @staticmethod
    def _plot_type(plot_data: Union[ScatterPlotData, HistogramPlotData]) -> str:
        """
        """
        return "scatter" if isinstance(plot_data, ScatterPlotData) else "histogram"

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
