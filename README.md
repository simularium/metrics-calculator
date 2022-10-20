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
from simularium_metrics_calculator import MetricsManager, NumberOfAgentsCalculator, NearestNeighborCalculator
from simulariumio import InputFileData

metrics = MetricsManager(
    input_data=InputFileData(
        file_path="[path to .simularium file]",
    ),
    calculators=[
        NumberOfAgentsCalculator(
            exclude_types=["A"],
        ),
        NearestNeighborCalculator(
            time_indices=[0, 99],
        ),
    ],
)

result = metrics.plot_data()
```

## Documentation

For full package documentation please visit [simularium.github.io/metrics-calculator](https://simularium.github.io/metrics-calculator).

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

**Apache Software License 2.0**
