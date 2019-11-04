import Devices
import Vicon

class ForcePlate(Devices.Devices):

    def __init__(self, name, forces, moments):
        self.force = Vicon.Point(forces["Fx"]["data"], forces["Fy"]["data"], forces["Fz"]["data"])
        self.moment = Vicon.Point(moments["Mx"]["data"], moments["My"]["data"], moments["Mz"]["data"])
        sensor = Vicon.Newton(None, self.force, self.moment, None)
        super(ForcePlate, self).__init__(name, sensor, "IMU")

    def get_forces(self):
        return self._sensor.force

    def get_moments(self):
        return self._sensor.moment
