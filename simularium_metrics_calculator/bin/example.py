#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simulariumio import InputFileData

from simularium_metrics_calculator import (
    METRIC_TYPE,
    PLOT_TYPE,
    SCATTER_PLOT_MODE,
    MetricsManager,
    PlotInfo,
)


def main() -> None:
    # get the metrics that are available to plot
    time_metrics = MetricsManager.available_metrics(METRIC_TYPE.PER_TIME)
    print(f"\nAvailable per time metrics:\n{time_metrics}")
    agent_metrics = MetricsManager.available_metrics(METRIC_TYPE.PER_AGENT)
    print(f"\nAvailable per agent metrics:\n{agent_metrics}")

    # configure some plots
    plot1 = PlotInfo(  # Number of agents vs time scatterplot
        plot_type=PLOT_TYPE.SCATTER,
        metric_id_x=0,
        metric_id_y=2,
        scatter_plot_mode=SCATTER_PLOT_MODE.LINES,
    )
    plot2 = PlotInfo(  # Nearest neighbor distance histogram
        plot_type=PLOT_TYPE.HISTOGRAM,
        metric_id_x=3,
    )
    print(f"\nTo plot:\n- {plot1}\n- {plot2}\n")

    # calculate plot data
    metrics = MetricsManager(
        input_data=InputFileData(
            file_path=(
                "simularium_metrics_calculator/tests/data/"
                "aster_pull3D_couples_actin_solid_3_frames_small.json"
            )
        ),
    )
    result = metrics.plot_data(
        plots=[
            plot1,
            plot2,
        ],
    )
    print(f"\nRESULT = \n{result}\n")


if __name__ == "__main__":
    main()
