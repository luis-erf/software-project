from rsoccer_gym.Entities import Robot
from utils.Point import Point

class BaseAgent:
    """Abstract Agent."""

    def __init__(self, id=0, yellow=False): #base stats of the robot
        self.id = id
        self.robot = Robot()
        self.pos = Point(0, 0)
        self.vel = Point(0, 0)
        self.body_angle = float(0)
        self.targets = []
        self.yellow = yellow
        self.opponents = dict()
        self.teammates = dict()

        self.next_vel = Point(0, 0)
        self.angle_vel = float(0)

    #it defines the next actions of the robot
    def step(self, self_robot : Robot, 
             opponents: dict[int, Robot] = dict(), 
             teammates: dict[int, Robot] = dict(), 
             targets: list[Point] = [], 
             keep_targets=False) -> Robot:

        self.reset() #resets the robots velocity so it can change its trajectory and goes to the next target
        self.pos = Point(self_robot.x, self_robot.y) #shows the roboy position with the value (x,y)
        self.vel = Point(self_robot.v_x, self_robot.v_y) #shows the robots velocity value in (x,y)
        self.body_angle = self_robot.theta #shows the robots angle

        if len(targets) > 0:
            self.targets = targets.copy()
        elif len(self.targets) == 0 or not keep_targets:
            self.targets = []
            
        self.robot = self_robot
        self.opponents = opponents.copy()
        self.teammates = teammates.copy()

        #sets the sequence of actions the robot will be taking during each of the steps analyzed
        self.decision()
        self.post_decision()

        #it returns the next atributes of the robot
        return Robot( id=self.id, yellow=self.yellow,
                      v_x=self.next_vel.x, v_y=self.next_vel.y, v_theta=self.angle_vel)

    def reset(self):
        self.next_vel = Point(0, 0)
        self.angle_vel = 0

    def decision(self):
        raise NotImplementedError()
    
    def post_decision(self):
        raise NotImplementedError()
    
    def set_vel(self, vel: Point):
        self.next_vel = vel
    
    def set_angle_vel(self, angle_vel: float):
        self.angle_vel = angle_vel
