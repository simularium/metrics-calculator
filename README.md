# Simularium Metrics Calculator

[![Build Status](https://github.com/simularium/metrics-calculator/workflows/CI/badge.svg)](https://github.com/simularium/metrics-calculator/actions)
[![Documentation](https://github.com/simularium/metrics-calculator/workflows/Documentation/badge.svg)](https://simularium.github.io/metrics-calculator)

Calculate plot metrics from spatial agent data

---

## Installation

**Stable Release:** [Coming soon!] `pip install simularium_metrics_calculator`<br>
**Development Head:** `pip install git+https://github.com/simularium/metrics-calculator.git`

To install in editable mode with all dev dependencies: `just install`

## Quickstart

```python
from simulariumio import FileConverter, InputFileData
from simularium_metrics_calculator import (
    PLOT_TYPE,
    SCATTER_PLOT_MODE,
    MetricsService,
    PlotInfo,
)

# create main class
metrics_service = MetricsService()

# check the metrics that are available to plot
metrics = metrics_service.available_metrics()

# load simularium trajectory data using simulariumio
traj_data = FileConverter(
    input_file=InputFileData(
        file_path=(
            "simularium_metrics_calculator/tests/data/"
            "aster_pull3D_couples_actin_solid_3_frames_small.json"
        )
    )
)._data

# configure some plots
plot1 = PlotInfo(  # Number of agents vs time scatterplot
    plot_type=PLOT_TYPE.SCATTER,
    metric_info_x=metrics[0]["uid"],
    metric_info_y=metrics[2]["uid"],
    scatter_plot_mode=SCATTER_PLOT_MODE.LINES,
)
plot2 = PlotInfo(  # Nearest neighbor distance histogram
    plot_type=PLOT_TYPE.HISTOGRAM,
    metric_info_x=metrics[3]["uid"],
)

# calculate the plot data
result = manager.plot_data(
    traj_data,
    plots=[
        plot1,
        plot2,
    ],
)
```

## Documentation

For full package documentation please visit [simularium.github.io/metrics-calculator](https://simularium.github.io/metrics-calculator).

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

**Apache Software License 2.0**
