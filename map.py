# map.py

import constants


'''
    Map Coordinates:
        Origin is top left. Increasing x along the rows.
                            Increasing y down the columns
'''

class RandomMap:

    def __init__(self, width, height, density):
        self.width = width
        self.height = height
        self.density = density

    def reset(self):
        self.data = constants.map.space * (self.width * self.height)

