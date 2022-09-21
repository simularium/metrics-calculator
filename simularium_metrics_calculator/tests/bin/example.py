#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simulariumio import InputFileData

from simularium_metrics_calculator import NumberOfAgentsCalculator

calculator = NumberOfAgentsCalculator(
    InputFileData(
        file_path="../data/aster_pull3D_couples_actin_solid_3_frames_small.json"
    )
)

print(calculator.plot_data())
