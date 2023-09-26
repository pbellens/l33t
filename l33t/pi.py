import random
import math
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

    def norm(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

def generate_point() -> Point: 
    return Point(x = random.random(), y = random.random())

def approximate(it: int) -> float:
    circled = 0
    squared = 0

    for _ in range(it): 
        p = generate_point()
        if p.norm() < 1.0:
            circled += 1
        else:
            squared += 1

    return 4 * circled / (squared + circled)



