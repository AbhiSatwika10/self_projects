import numpy as np
import random
import time

class CityNetwork:
    def __init__(self, grid_size=2):
        self.grid_size = grid_size
        self.intersections = [[Intersection(i, j) for j in range(grid_size)] for i in range(grid_size)]
        self.vehicles = []
        self.time_step = 0

    def add_vehicle(self):
        # Add random vehicle with start and end positions
        start = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))
        end = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))
        while start == end:
            end = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))
        self.vehicles.append(Vehicle(start, end))

    def step(self, use_ml=False, agent=None):
        # Simulate one time step
        for row in self.intersections:
            for inter in row:
                inter.update_lights(use_ml, agent, self.time_step)
        for vehicle in self.vehicles[:]:
            vehicle.move(self)
        self.vehicles = [v for v in self.vehicles if not v.arrived]
        self.time_step += 1

    def get_average_wait_time(self):
        if not self.vehicles:
            return 0
        return np.mean([v.wait_time for v in self.vehicles])

class Intersection:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.lights = {'NS': 'red', 'EW': 'green'}  # North-South, East-West
        self.queue_ns = 0  # Vehicles waiting NS
        self.queue_ew = 0  # Vehicles waiting EW
        self.green_duration = 10  # Fixed for baseline

    def update_lights(self, use_ml, agent, time_step):
        if use_ml and agent:
            state = self.get_state()
            action = agent.choose_action(state)
            if action == 0:
                self.lights = {'NS': 'green', 'EW': 'red'}
            else:
                self.lights = {'NS': 'red', 'EW': 'green'}
        else:
            # Fixed cycle
            if time_step % self.green_duration == 0:
                self.lights['NS'], self.lights['EW'] = self.lights['EW'], self.lights['NS']

    def get_state(self):
        return (self.queue_ns, self.queue_ew)  # Simplified state: queue lengths

class Vehicle:
    def __init__(self, start, end):
        self.pos = list(start)
        self.end = list(end)
        self.wait_time = 0
        self.arrived = False
        self.path = self.simple_path()  # Dummy path

    def simple_path(self):
        # Simple Manhattan path
        return [(self.pos[0], self.pos[1])]  # Placeholder; expand for real movement

    def move(self, city):
        if self.pos == self.end:
            self.arrived = True
            return
        # Simulate movement based on lights
        inter = city.intersections[self.pos[0]][self.pos[1]]
        direction = 'NS' if self.pos[0] != self.end[0] else 'EW'  # Simplified
        if inter.lights[direction] == 'green':
            # Move forward (simplified: increment position)
            if direction == 'NS':
                self.pos[0] = (self.pos[0] + 1) % city.grid_size
            else:
                self.pos[1] = (self.pos[1] + 1) % city.grid_size
        else:
            self.wait_time += 1
        # Update queues (simplified)
        inter.queue_ns += random.randint(0, 1)
        inter.queue_ew += random.randint(0, 1)