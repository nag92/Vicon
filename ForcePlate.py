
import Devices
from lib.GaitCore.Core.Point import Point
from lib.GaitCore.Core.Newton import Newton

class ForcePlate(Devices.Devices):

    def __init__(self, name, forces, moments):
        self.force = Point(forces["Fx"]["data"], forces["Fy"]["data"], forces["Fz"]["data"])
        self.moment = Point(moments["Mx"]["data"], moments["My"]["data"], moments["Mz"]["data"])
        sensor = Newton(None, self.force, self.moment, None)
        super(ForcePlate, self).__init__(name, sensor, "IMU")

    def get_forces(self):
        """

        :return: the force from the force plate
        :rtype: Point
        """
        return self._sensor.force

    def get_moments(self):
        """

        :return: the Moment from the force plate
        :rtype: Point
        """
        return self._sensor.moment
