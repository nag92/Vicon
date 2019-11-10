import Devices


class ForcePlate(Devices.Devices):

    def __init__(self, name, forces, moments):
        self.force = Devices.Point(forces["Fx"]["data"], forces["Fy"]["data"], forces["Fz"]["data"])
        self.moment = Devices.Point(moments["Mx"]["data"], moments["My"]["data"], moments["Mz"]["data"])
        sensor = Devices.Newton(None, self.force, self.moment, None)
        super(ForcePlate, self).__init__(name, sensor, "ForcePlate")

    def get_forces(self):
        return self._sensor.force

    def get_moments(self):
        return self._sensor.moment
