#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simulariumio import InputFileData
from simularium_metrics_calculator import (
    MetricsManager, 
    NumberOfAgentsCalculator, 
    NearestNeighborCalculator,
)


def main():
    metrics = MetricsManager(
        input_data=InputFileData(
            file_path=(
                "simularium_metrics_calculator/tests/data/"
                "aster_pull3D_couples_actin_solid_3_frames_small.json"
            )
        ),
        calculators=[
            NumberOfAgentsCalculator(
                exclude_types=["motor complex"],
            ),
            NearestNeighborCalculator(
                time_indices=[0, 2],
            ),
        ],
    )
    print(f"\nRESULT = \n{metrics.plot_data()}\n")

if __name__ == "__main__":
    main()