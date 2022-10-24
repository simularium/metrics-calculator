#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from typing import Dict, List

from simulariumio import (
    FileConverter,
    HistogramPlotData,
    InputFileData,
    ScatterPlotData,
)
from simulariumio.constants import CURRENT_VERSION

from .constants import METRIC_TYPE
from .exceptions import MetricNotFoundError
from .metrics_registry import metric_registry


class MetricsManager:
    def __init__(self, input_data: InputFileData, plot_metrics: List[List[int]]):
        """
        This object takes Simularium trajectory data
        and calculates metrics that can be plotted
        in the Simularium Viewer.

        Parameters
        ----------
        input_data : InputFileData
            An object containing simularium data,
            either a file path where the data can be loaded,
            or the data already in memory. Data can be
            in JSON or binary format.
        plot_metrics: List[List[int]]
            A list of plots, for each plot a list of metric uids.
            If list is length 1, plot as histogram,
            otherwise plot a scatter plot of the first 2 metrics
            in the list in order of X, Y.
        """
        self.converter = FileConverter(input_data)
        for plot in plot_metrics:
            # histogram
            if len(plot) < 2:
                self.add_histogram(plot[0])
            # scatter plot
            else:
                self.add_scatter_plot(plot[0], plot[1])

    @staticmethod
    def available_metrics(metric_type: METRIC_TYPE) -> Dict[int, str]:
        """ """
        result = {}
        for metric in metric_registry.values():
            if metric.metric_type == metric_type:
                result[metric.uid] = metric.display_name
        return result

    def add_histogram(self, metric_uid: int) -> None:
        """
        Add a histogram plot with the given metric.

        Parameters
        ----------
        metric_uid: int
            ID of the metric to plot in the histogram.
        """
        if metric_uid not in metric_registry:
            raise MetricNotFoundError(metric_uid)
        metric_info = metric_registry[metric_uid]
        calculator = metric_info.calculator()
        traces = calculator.calculate(self.converter._data)
        units = calculator.units(self.converter._data)
        metric_title = metric_info.display_name
        if units:
            units = f" ({units})"
        plot_data = HistogramPlotData(
            title=metric_title,
            xaxis_title=f"{metric_title}{units}",
            traces=traces,
        )
        self.converter.add_plot(plot_data, "histogram")

    def add_scatter_plot(self, x_metric_uid: int, y_metric_uid: int) -> None:
        """
        Add a scatter plot with the given metrics.

        Parameters
        ----------
        x_metric_uid: int
            ID of the metric to plot on the x-axis.
        y_metric_uid: int
            ID of the metric to plot on the y-axis.
        """
        if x_metric_uid not in metric_registry:
            raise MetricNotFoundError(x_metric_uid)
        if y_metric_uid not in metric_registry:
            raise MetricNotFoundError(y_metric_uid)
        # X axis metric
        x_metric_info = metric_registry[x_metric_uid]
        x_calculator = x_metric_info.calculator()
        x_traces = x_calculator.calculate(self.converter._data)
        # only use the first trace for X axis since there can only be one
        x_trace = x_traces[list(x_traces.keys())[0]]
        x_units = x_calculator.units(self.converter._data)
        if x_units:
            x_units = f" ({x_units})"
        x_metric_title = x_metric_info.display_name
        # Y axis metric
        y_metric_info = metric_registry[y_metric_uid]
        y_calculator = y_metric_info.calculator()
        y_traces = y_calculator.calculate(self.converter._data)
        y_units = y_calculator.units(self.converter._data)
        if y_units:
            y_units = f" ({y_units})"
        y_metric_title = y_metric_info.display_name
        # create and add plot
        plot_data = ScatterPlotData(
            title=f"{y_metric_title} vs {x_metric_title.lower()}",
            xaxis_title=f"{x_metric_title}{x_units}",
            yaxis_title=f"{y_metric_title}{y_units}",
            xtrace=x_trace,
            ytraces=y_traces,
            render_mode="lines",
        )
        self.converter.add_plot(plot_data, "scatter")

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
