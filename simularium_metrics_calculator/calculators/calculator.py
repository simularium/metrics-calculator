#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Dict

import numpy as np
from simulariumio import TrajectoryData

from..constants import METRIC_TYPE


class Calculator(ABC):
    @abstractmethod
    def calculate(self, traj_data: TrajectoryData) -> Dict[str, np.ndarray]:
        pass
        
    @abstractmethod
    def units(self, traj_data: TrajectoryData) -> str:
        pass
