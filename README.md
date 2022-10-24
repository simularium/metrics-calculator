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
from simularium_metrics_calculator import MetricsManager
from simulariumio import InputFileData

# check the metrics that are available to plot
time_metrics = MetricsManager.available_metrics(METRIC_TYPE.PER_TIME)
agent_metrics = MetricsManager.available_metrics(METRIC_TYPE.PER_AGENT)

# choose some example metrics
plot1 = list(time_metrics.keys())[:2]  # Number of agents vs time scatterplot
plot2 = [list(agent_metrics.keys())[1]]  # Nearest neighbor distance histogram

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
result = metrics.plot_data()
```

## Documentation

For full package documentation please visit [simularium.github.io/metrics-calculator](https://simularium.github.io/metrics-calculator).

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

**Apache Software License 2.0**
