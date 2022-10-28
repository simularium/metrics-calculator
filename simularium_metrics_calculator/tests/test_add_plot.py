#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

import pytest
from simulariumio import HistogramPlotData, InputFileData

from simularium_metrics_calculator import (
    PLOT_TYPE,
    SCATTER_PLOT_MODE,
    MetricsManager,
    PlotInfo,
)
from simularium_metrics_calculator.exceptions import (
    IncompatibleMetricsError,
    InconsistentPlotTypeError,
    MetricNotFoundError,
)
from simularium_metrics_calculator.tests import assert_plot_data_equal


@pytest.mark.parametrize(
    "spatial_data_path, plot_metrics, expected_plot_data",
    [
        # histogram
        (
            (
                "simularium_metrics_calculator/tests/data/"
                "aster_pull3D_couples_actin_solid_3_frames_small.json"
            ),
            [
                PlotInfo(
                    plot_type=PLOT_TYPE.HISTOGRAM,
                    metric_id_x=3,
                ),
            ],
            {
                "layout": {
                    "title": "Nearest neighbor distance",
                    "xaxis": {"title": "Nearest neighbor distance (\u00b5m)"},
                    "yaxis": {"title": "frequency"},
                },
                "data": [
                    {
                        "name": "t = 0.0 s",
                        "type": "histogram",
                        "x": [89.48637941050023, 89.48637941050023],
                    },
                    {
                        "name": "t = 0.1 s",
                        "type": "histogram",
                        "x": [87.40050629143975, 87.40050629143975],
                    },
                ],
            },
        ),
        # scatterplot
        (
            (
                "simularium_metrics_calculator/tests/data/"
                "aster_pull3D_couples_actin_solid_3_frames_small.json"
            ),
            [
                PlotInfo(
                    plot_type=PLOT_TYPE.SCATTER,
                    metric_id_x=0,
                    metric_id_y=2,
                    scatter_plot_mode=SCATTER_PLOT_MODE.LINES,
                ),
            ],
            {
                "layout": {
                    "title": "Number of agents vs time",
                    "xaxis": {"title": "Time (s)"},
                    "yaxis": {"title": "Number of agents"},
                },
                "data": [
                    {
                        "name": "microtubule",
                        "type": "scatter",
                        "x": [0.0, 0.05, 0.1],
                        "y": [1, 1, 1],
                        "mode": "lines",
                    },
                    {
                        "name": "motor complex",
                        "type": "scatter",
                        "x": [0.0, 0.05, 0.1],
                        "y": [1, 1, 1],
                        "mode": "lines",
                    },
                ],
            },
        ),
        # metric ID does not exist
        pytest.param(
            (
                "simularium_metrics_calculator/tests/data/"
                "aster_pull3D_couples_actin_solid_3_frames_small.json"
            ),
            [
                PlotInfo(
                    plot_type=PLOT_TYPE.HISTOGRAM,
                    metric_id_x=-1,
                ),
            ],
            {},
            marks=pytest.mark.raises(exception=MetricNotFoundError),
        ),
        # plot type and metrics are inconsistent
        pytest.param(
            (
                "simularium_metrics_calculator/tests/data/"
                "aster_pull3D_couples_actin_solid_3_frames_small.json"
            ),
            [
                PlotInfo(
                    plot_type=PLOT_TYPE.SCATTER,
                    metric_id_x=0,
                ),
            ],
            {},
            marks=pytest.mark.raises(exception=InconsistentPlotTypeError),
        ),
        # metrics have incompatible type
        pytest.param(
            (
                "simularium_metrics_calculator/tests/data/"
                "aster_pull3D_couples_actin_solid_3_frames_small.json"
            ),
            [
                PlotInfo(
                    plot_type=PLOT_TYPE.SCATTER,
                    metric_id_x=0,
                    metric_id_y=1,
                ),
            ],
            {},
            marks=pytest.mark.raises(exception=IncompatibleMetricsError),
        ),
    ],
)
def test_add_plot(
    spatial_data_path: str,
    plot_metrics: List[PlotInfo],
    expected_plot_data: HistogramPlotData,
) -> None:
    metrics = MetricsManager(
        input_data=InputFileData(
            file_path=spatial_data_path,
        )
    )
    test_plot_data = metrics._plot_dicts(plot_metrics)
    assert len(test_plot_data) == 1
    assert_plot_data_equal(
        test_plot_data[0], expected_plot_data, plot_type=plot_metrics[0].plot_type
    )
