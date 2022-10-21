#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from typing import List, Optional

import numpy as np
from simulariumio import (
    InputFileData,
    FileConverter,
    HistogramPlotData,
    ScatterPlotData,
)
from simulariumio.constants import CURRENT_VERSION

from .calculators.calculator import Calculator
from .calculators import (
    TimesCalculator,
    AgentsCalculator,
    NumberOfAgentsCalculator,
    NearestNeighborCalculator,
)
from .constants import METRIC_TYPE


AVAILABLE_CALCULATORS = [
    TimesCalculator,
    AgentsCalculator,
    NumberOfAgentsCalculator,
    NearestNeighborCalculator,
]


class MetricsManager:
    def __init__(self, input_data: InputFileData, plot_metrics: List[List[str]]):
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
        plot_metrics: List[List[str]]
            A list of plots, for each plot a list 
            of metric titles as strings.
            If list is length 1, plot as histogram,
            otherwise plot a scatter plot 
            of the first 2 metrics in the list in order of X, Y.
        """
        self.converter = FileConverter(input_data)
        for metrics in plot_metrics:
            # histogram
            if len(metrics) < 2:
                self.add_histogram(metrics[0])
            # scatter plot
            else:
                self.add_scatter_plot(metrics[0], metrics[1])

    @staticmethod
    def available_metrics(metric_type: METRIC_TYPE) -> List[str]:
        """
        """
        result = []
        for calculator in AVAILABLE_CALCULATORS:
            if calculator.METRIC_TYPE == metric_type:
                result.append(calculator.AXIS_TITLE)
        return result

    @staticmethod
    def _calculator_for_metric(metric_title: str) -> Optional[Calculator]:
        """
        """
        for calculator in AVAILABLE_CALCULATORS:
            if metric_title == calculator.AXIS_TITLE:
                return calculator
        return None
        
    def add_scatter_plot(self, x_metric_title: str, y_metric_title: str):
        """
        Add a scatter plot with the given metrics.

        Parameters
        ----------
        x_metric_title: str
            Title of the metric to plot on the x-axis
        y_metric_title: str
            Title of the metric to plot on the y-axis
        """
        x_calculator = self._calculator_for_metric(x_metric_title)()
        x_traces = x_calculator.calculate(self.converter._data)
        x_trace = x_traces[list(x_traces.keys())[0]]
        x_units = x_calculator.units(self.converter._data)
        if x_units:
            x_units = f" ({x_units})"
        y_calculator = self._calculator_for_metric(y_metric_title)()
        y_traces = y_calculator.calculate(self.converter._data)
        y_units = y_calculator.units(self.converter._data)
        if y_units:
            y_units = f" ({y_units})"
        plot_data = ScatterPlotData(
            title=f"{y_metric_title} vs {x_metric_title.lower()}",
            xaxis_title=f"{x_metric_title}{x_units}",
            yaxis_title=f"{y_metric_title}{y_units}",
            xtrace=x_trace,
            ytraces=y_traces,
            render_mode="lines",
        )
        self.converter.add_plot(plot_data, "scatter")
        
    def add_histogram(self, metric_title: str):
        """
        Add a histogram plot with the given metric.

        Parameters
        ----------
        metric_title: str
            Title of the metric to plot
        """
        calculator = self._calculator_for_metric(metric_title)()
        traces = calculator.calculate(self.converter._data)
        units = calculator.units(self.converter._data)
        if units:
            units = f" ({units})"
        plot_data = HistogramPlotData(
            title=metric_title,
            xaxis_title=f"{metric_title}{units}",
            traces=traces,
        )
        self.converter.add_plot(plot_data, "histogram")

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
