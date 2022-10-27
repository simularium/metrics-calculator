#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .constants import SCATTER_PLOT_MODE
from .exceptions import IncompatibleMetricsError
from .metrics_registry import metric_info_for_id


class PlotInfo:
    metric_id_x: int
    metric_id_y: int
    scatter_plot_mode: SCATTER_PLOT_MODE

    def __init__(
        self,
        metric_id_x: int,
        metric_id_y: int = -1,
        scatter_plot_mode: SCATTER_PLOT_MODE = SCATTER_PLOT_MODE.MARKERS,
    ):
        """
        This object takes Simularium trajectory data
        and calculates metrics that can be plotted
        in the Simularium Viewer.

        Parameters
        ----------
        metric_id_x : int
            ID for the metric to plot on the x-axis.
        metric_id_y : int (Optional)
            ID for the metric to plot on the y-axis.
            If not provided, the plot will be a histogram.
        scatter_plot_mode : SCATTER_PLOT_MODE (Optional)
            If the plot is a scatterplot, how to draw the points.
            Default: SCATTER_PLOT_MODE.MARKERS (draw as dots)
        """
        self.metric_id_x = metric_id_x
        self.metric_id_y = metric_id_y
        self.scatter_plot_mode = scatter_plot_mode

    def check_metrics_are_compatible(self) -> None:
        """
        Check that the X and Y metrics are of the same type,
        if this is not a histogram.
        """
        if self.is_histogram():
            return
        x_metric_type = metric_info_for_id(self.metric_id_x).metric_type
        y_metric_type = metric_info_for_id(self.metric_id_y).metric_type
        if x_metric_type != y_metric_type:
            x_metric_name = metric_info_for_id(self.metric_id_x).display_name
            y_metric_name = metric_info_for_id(self.metric_id_y).display_name
            raise IncompatibleMetricsError(x_metric_name, y_metric_name)

    def is_histogram(self) -> bool:
        """
        Is this plot a histogram? True if there is no Y metric.

        Returns
        -------
        bool
            True if this plot is a histogram
        """
        return self.metric_id_y < 0

    def __str__(self) -> str:
        """
        Get the name and type of this plot.

        Returns
        -------
        str
            "[X metric] vs [Y metric] [type of plot]"
        """
        x_metric_name = metric_info_for_id(self.metric_id_x).display_name
        if not self.is_histogram():
            y_metric_name = metric_info_for_id(self.metric_id_y).display_name
            return f"{y_metric_name} vs {x_metric_name.lower()} scatter plot"
        return f"{x_metric_name} histogram"
