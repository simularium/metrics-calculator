#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .constants import SCATTER_PLOT_MODE


class PlotInfo:
    metric_x : int
    metric_y: int
    scatter_plot_mode : SCATTER_PLOT_MODE
    
    def __init__(
        self, 
        metric_x : int,
        metric_y: int = -1,
        scatter_plot_mode : SCATTER_PLOT_MODE = SCATTER_PLOT_MODE.MARKERS,
    ):
        """
        This object takes Simularium trajectory data
        and calculates metrics that can be plotted
        in the Simularium Viewer.

        Parameters
        ----------
        metric_x : int
            ID for the metric to plot on the x-axis.
        metric_y : int (Optional)
            ID for the metric to plot on the y-axis.
            If not provided, the plot will be a histogram.
        scatter_plot_mode : SCATTER_PLOT_MODE (Optional)
            If the plot is a scatterplot, how to draw the points.
            Default: SCATTER_PLOT_MODE.MARKERS (draw as dots)
        """
        self.metric_x = metric_x
        self.metric_y = metric_y
        self.scatter_plot_mode = scatter_plot_mode
    
    def is_histogram(self) -> bool:
        """
        Is this plot a histogram? True if there is no Y metric.

        Returns
        -------
        bool
            Is this plot a histogram?
        """
        return self.metric_y < 0
