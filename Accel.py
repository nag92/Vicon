import Devices
from lib.GaitCore.Core.Point import Point


class Accel(Devices.Devices):

    def __init__(self, name, sensor):
        self._accel = Point(self.sensor["ACCX"],
                                self.sensor["ACCZ"],
                                self.sensor["ACCY"])
        super(Accel, self).__init__(name, sensor, "Accel")

    def get(self):
        return self._accel
