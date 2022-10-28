#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from typing import Any, Dict, List

from simulariumio import (
    FileConverter,
    HistogramPlotData,
    InputFileData,
    ScatterPlotData,
)
from simulariumio.constants import CURRENT_VERSION
from simulariumio.plot_readers import HistogramPlotReader, ScatterPlotReader

from .constants import METRIC_TYPE, PLOT_TYPE
from .metrics_registry import metric_info_for_id, metrics_registry
from .plot_info import PlotInfo


class MetricsManager:
    def __init__(self, input_data: InputFileData):
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
        """
        self.traj_data = FileConverter(input_data)._data

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

    def plot_data(self, plots: List[PlotInfo]) -> str:
        """
        Add plots with the given configuration.

        Parameters
        ----------
        plots: List[PlotInfo]
            A list of PlotInfo configuration for each plot.

        Returns
        -------
        str
            A JSON string of the plot(s) in simularium format.
        """
        plot_dicts = self._plot_dicts(plots)
        return json.dumps(
            {
                "version": CURRENT_VERSION.PLOT_DATA,
                "data": plot_dicts,
            }
        )

    def _plot_dicts(self, plots: List[PlotInfo]) -> List[Dict[str, Any]]:
        """
        Calculate each plot and get a dict for each.
        """
        result = []
        for plot_info in plots:
            result.append(self._calculate_plot(plot_info))
        return result

    def _calculate_plot(self, plot_info: PlotInfo) -> Dict[str, Any]:
        """
        Calculate a plot with the given configuration.
        """
        plot_info.validate_plot_configuration()
        # X axis metric
        x_metric_info = metric_info_for_id(plot_info.metric_id_x)
        x_calculator = x_metric_info.calculator()
        x_traces, x_units = x_calculator.calculate(self.traj_data)
        x_metric_title = x_metric_info.display_name
        # create and add plots
        if plot_info.plot_type == PLOT_TYPE.HISTOGRAM:
            plot_data = HistogramPlotData(
                title=x_metric_title,
                xaxis_title=f"{x_metric_title}{x_units}",
                traces=x_traces,
            )
            return HistogramPlotReader().read(plot_data)
        else:  # SCATTER PLOT
            # only use the first trace for X axis since there can only be one
            x_trace = x_traces[list(x_traces.keys())[0]]
            # Y axis metric
            y_metric_info = metric_info_for_id(plot_info.metric_id_y)
            y_calculator = y_metric_info.calculator()
            y_traces, y_units = y_calculator.calculate(self.traj_data)
            y_metric_title = y_metric_info.display_name
            # create and add scatter plot
            plot_data = ScatterPlotData(
                title=f"{y_metric_title} vs {x_metric_title.lower()}",
                xaxis_title=f"{x_metric_title}{x_units}",
                yaxis_title=f"{y_metric_title}{y_units}",
                xtrace=x_trace,
                ytraces=y_traces,
                render_mode=plot_info.scatter_plot_mode.value,
            )
            return ScatterPlotReader().read(plot_data)
