#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simulariumio import InputFileData
from simularium_metrics_calculator import MetricsManager

from simularium_metrics_calculator.constants import METRIC_TYPE


def main():
    # get the metrics that are available to plot
    time_metrics = MetricsManager.available_metrics(METRIC_TYPE.PER_TIME)
    agent_metrics = MetricsManager.available_metrics(METRIC_TYPE.PER_AGENT)
    # choose some example metrics
    plot1 = time_metrics[:2]  # Number of agents vs Time scatterplot
    plot2 = [agent_metrics[1]]  # Nearest neighbor distance histogram
    print(f"\nPlotting {plot1} and {plot2}\n")
    # calculate the plot data
    metrics = MetricsManager(
        input_data=InputFileData(
            file_path=(
                "simularium_metrics_calculator/tests/data/"
                "aster_pull3D_couples_actin_solid_3_frames_small.json"
            )
        ),
        plot_metrics=[
            plot1,
            plot2,
        ],
    )
    print(f"\nRESULT = \n{metrics.plot_data()}\n")

if __name__ == "__main__":
    main()