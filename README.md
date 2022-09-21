# Simularium Metrics Calculator

[![Build Status](https://github.com/simularium/metrics-calculator/workflows/CI/badge.svg)](https://github.com/simularium/metrics-calculator/actions)
[![Documentation](https://github.com/simularium/metrics-calculator/workflows/Documentation/badge.svg)](https://simularium.github.io/metrics-calculator)

Calculate plot metrics from spatial agent data

---

## Installation

[Coming soon!] **Stable Release:** `pip install simularium_metrics_calculator`<br>
**Development Head:** `pip install git+https://github.com/simularium/metrics-calculator.git`

## Quickstart

```python
from simularium_metrics_calculator import NumberOfAgentsCalculator
from simulariumio import InputFileData

calculator = NumberOfAgentsCalculator(
    InputFileData(
        file_path=(
            "simularium_metrics_calculator/tests/data/"
            "aster_pull3D_couples_actin_solid_3_frames_small.json"
        )
    )
)

print(calculator.plot_data())
```

## Documentation

For full package documentation please visit [simularium.github.io/metrics-calculator](https://simularium.github.io/metrics-calculator).

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

**Apache Software License 2.0**
