import json
import numpy as np
import pyqtgraph as pg
from typing import Any
from Sim.Physics.ball import Ball

class RealTimeGraph:

    def __init__(self, duration: int, step: int) -> None:
        TOTAL_STEPS: int = round(duration / step)
        self.x_axis: np.ndarray = np.linspace(0, duration, TOTAL_STEPS, endpoint=False)
        self.y_axis: np.ndarray = np.full(TOTAL_STEPS, np.nan)
        self.plot_widget: pg.PlotWidget = pg.plot(self.x_axis, self.y_axis)
        self.curve: pg.PlotDataItem = self.plot_widget.plot(pen="r")
        self.index: int = 0
        self.app = pg.mkQApp()

        self.plot_widget.setLimits(
            xMin=0, 
            xMax=duration, 
            yMin=-Ball.LATERAL_OFFSET_LIMIT_MM, 
            yMax=Ball.LATERAL_OFFSET_LIMIT_MM,
            maxXRange=duration,
            maxYRange=Ball.LATERAL_OFFSET_LIMIT_MM * 2
            )

        self.plot_widget.setXRange(0, duration)
        self.plot_widget.setYRange(-Ball.LATERAL_OFFSET_LIMIT_MM, Ball.LATERAL_OFFSET_LIMIT_MM)

    def add_point(self, value: float) -> None:
        self.y_axis[self.index] = value
        self.index += 1
        self.curve.setData(self.x_axis[:self.index], self.y_axis[:self.index]) # Schedules a repaint of the graph with update values
        self.app.processEvents()