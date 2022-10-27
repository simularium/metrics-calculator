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
from .metrics_registry import metrics_registry, metric_info_for_id
from .plot_info import PlotInfo


class MetricsManager:
    def __init__(self, input_data: InputFileData, plot_metrics: List[PlotInfo]):
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
        plot_metrics: List[PlotInfo]
            A list of PlotInfo configuration for each plot.
        """
        self.converter = FileConverter(input_data)
        for plot_info in plot_metrics:
            self.add_plot(plot_info)

    @staticmethod
    def available_metrics(metric_type: METRIC_TYPE) -> Dict[int, str]:
        """
        Get the IDs and display names for the metrics
        that are compatible with the given type of data.

        Returns
        -------
        Dict[int, str]
            A dict mapping metric unique ID to its display name.
        """
        result = {}
        for metric in metrics_registry.values():
            if metric.metric_type == metric_type:
                result[metric.uid] = metric.display_name
        return result

    def add_plot(self, plot_info: PlotInfo) -> None:
        """
        Add a plot with the given configuration.

        Parameters
        ----------
        plot_info: PlotInfo
            Info to configure the plot.
        """
        # X axis metric
        x_metric_info = metric_info_for_id(plot_info.metric_x)
        x_calculator = x_metric_info.calculator()
        x_traces, x_units = x_calculator.calculate(self.converter._data)
        x_metric_title = x_metric_info.display_name
        if plot_info.is_histogram():
            # create and add histogram
            plot_data = HistogramPlotData(
                title=x_metric_title,
                xaxis_title=f"{x_metric_title}{x_units}",
                traces=x_traces,
            )
            self.converter.add_plot(plot_data, "histogram")
        else: # scatter plot
            # only use the first trace for X axis since there can only be one
            x_trace = x_traces[list(x_traces.keys())[0]]
            # Y axis metric
            y_metric_info = metric_info_for_id(plot_info.metric_y)
            y_calculator = y_metric_info.calculator()
            y_traces, y_units = y_calculator.calculate(self.converter._data)
            y_metric_title = y_metric_info.display_name
            # create and add scatter plot
            plot_data = ScatterPlotData(
                title=f"{y_metric_title} vs {x_metric_title.lower()}",
                xaxis_title=f"{x_metric_title}{x_units}",
                yaxis_title=f"{y_metric_title}{y_units}",
                xtrace=x_trace,
                ytraces=y_traces,
                render_mode=plot_info.scatter_plot_mode,
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
