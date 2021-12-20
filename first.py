
class Bicycle(Bicycle):
    def step(self, v, w):
        # ==================================
        #  Implement kinematic model here
        # ==================================
        self.xc_dot = v * cos(theta + beta)
        self.yc_dot = v * sin(theta + beta)
        self.theta_dot = v * cos(beta)* tan(delta)/L
        self.delta_dot = w
        self.beta = arctan(lr*tan(delta)/L)
        pass
