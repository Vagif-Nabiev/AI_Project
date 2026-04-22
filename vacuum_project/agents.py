import random

class SimpleReflexAgent:
    def __init__(self):
        self.name = "Simple Reflex Agent"
        # the agent doesn't know the grid size, it just reacts

    def act(self, percept):
        location, is_dirty = percept
        
        if is_dirty:
            return 'Suck'
        else:
            # if it's clean, just wander around randomly
            return random.choice(['Up', 'Down', 'Left', 'Right'])


class ModelBasedAgent:
    def __init__(self, width=4, height=4):
        self.name = "Model-Based Agent"
        self.width = width
        self.height = height
        # keep track of squares we haven't visited yet
        self.unvisited = set((x, y) for x in range(width) for y in range(height))

    def act(self, percept):
        location, is_dirty = percept
        x, y = location
        
        # mark current location as visited
        if location in self.unvisited:
            self.unvisited.remove(location)

        if is_dirty:
            return 'Suck'
        
        # if we visited everywhere, we're probably done
        if not self.unvisited:
            return 'NoOp'

        # find the closest unvisited square
        closest_target = min(self.unvisited, key=lambda t: abs(t[0] - x) + abs(t[1] - y))
        target_x, target_y = closest_target

        # figure out which way to go
        if target_x > x:
            return 'Right'
        elif target_x < x:
            return 'Left'
        elif target_y > y:
            return 'Down'
        elif target_y < y:
            return 'Up'
            
        return 'NoOp'