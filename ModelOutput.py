import lib.GaitCore.Core as core
from lib.GaitCore.Bio.Leg import Leg
from lib.GaitCore.Bio.Side import Side

class ModelOutput(object):

    def __init__(self, data, joint_name):

        self.joint_names = joint_name
        left_joints = {}
        right_joints = {}

        for side, joint in zip(("R", "L"), (left_joints, right_joints)):
            for output in self.joint_names:
                angle = core.Point.Point(data[side + output + "Angles"]["X"]["data"],
                                   data[side + output + "Angles"]["Y"]["data"],
                                   data[side + output + "Angles"]["Z"]["data"])
                force = core.Point.Point(data[side + output + "Force"]["X"]["data"],
                                   data[side + output + "Force"]["Y"]["data"],
                                   data[side + output + "Force"]["Z"]["data"])
                moment = core.Point.Point(data[side + output + "Moment"]["X"]["data"],
                                    data[side + output + "Moment"]["Y"]["data"],
                                    data[side + output + "Moment"]["Z"]["data"])
                power = core.Point.Point(data[side + output + "Power"]["X"]["data"],
                                   data[side + output + "Power"]["Y"]["data"],
                                   data[side + output + "Power"]["Z"]["data"])

                joint[output] = core.Newton.Newton(angle, force, moment, power)

        left_leg = Leg(left_joints["Hip"], left_joints["Knee"], left_joints["Ankle"])
        right_leg = Leg(right_joints["Hip"], right_joints["Knee"], right_joints["Ankle"])
        self._legs = Side(left_leg, right_leg)

    def get_legs(self):
        """

        :return:
        """
        return self._legs

    def get_right_leg(self):
        """

        :return:
        """
        return self._legs.right

    def get_left_leg(self):
        """

        :return:
        """
        return self._legs.left


