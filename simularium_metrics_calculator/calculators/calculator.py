#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Union

from simulariumio import TrajectoryData, ScatterPlotData, HistogramPlotData


class Calculator(ABC):
    @abstractmethod
    def calculate(self, traj_data: TrajectoryData) -> Union[ScatterPlotData, HistogramPlotData]:
        pass
