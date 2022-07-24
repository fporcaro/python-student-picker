import math

SEGMENT_TIME_KEY = 'segment_time'
ANGULAR_VELOCITY_KEY = 'angular_velocity'
ANGULAR_MOMENTUM_KEY = 'angular_momentum'


class PhysicalWheelModel:
    def __init__(self, number_of_segments=20, rotational_inertia=2.0, friction_torque=0.5):
        self.number_of_segments = number_of_segments
        # In radians (obviously)
        self.radians_per_segment = 2*math.pi/self.number_of_segments
        # In kg*m^2
        self.rotational_inertia = rotational_inertia
        # In rad/s
        self.current_angular_velocity = 0.0
        # in N*m
        self.current_torque = 0.0
        # in s
        self.remaining_time_of_torque = 0.0
        # in N*M*s?
        self.current_angular_momentum = 0.0
        # in N*m
        self.friction_torque = friction_torque
        self.segment_calcs = []

    def spin_wheel(self, spin_torque, duration) -> []:
        """
        Spins the wheel and generates a list of segment calcs at the end of the segment's rotation
        :param spin_torque:
        :param duration:
        :return: a list of relevant calculations for each segment of the wheel as it would spin, including
            the amount of time spent in each section and the angular velocity while that segment is the "active" segment
            of the wheel (where the pointer is pointing at it)
        """

    def calculate_eos_angular_velocity(self):
        return 0

    def calculate_time_in_current_segment(self):
        return 0
