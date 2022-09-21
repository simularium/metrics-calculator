#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simularium_metrics_calculator import NumberOfAgentsCalculator
from simulariumio import InputFileData

calculator = NumberOfAgentsCalculator(
    InputFileData(
        file_path="../data/aster_pull3D_couples_actin_solid_3_frames_small.json"
    )
)

print(calculator.plot_data())