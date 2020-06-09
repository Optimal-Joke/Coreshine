class Region:
    def __init__(self, shape, center_RA, center_Dec, rotation=None):
        self.shape = shape
        self.center_RA = center_RA
        self.center_Dec = center_Dec
        self.rotation = rotation

    def coord_filter(self):
        pass


class Box(Region):
    def __init__(self, center_RA, center_Dec, rotation, size_RA, size_Dec):
        super().__init__(center_RA, center_Dec, rotation)
        self.size_RA = size_RA
        self.size_Dec = size_Dec

    def filter_coords(self):
        pass


class Circle(Region):
    def __init__(self, shape, center_RA, center_Dec, rotation, radius):
        super().__init__(shape, center_RA, center_Dec, rotation)
        self.radius = radius


class Ellipse(Region):
    def __init__(self, shape, center_RA, center_Dec, rotation, radius_RA, radius_Dec):
        super().__init__(shape, center_RA, center_Dec, rotation)
        self.radius_RA = radius_RA
        self.radius_Dec = radius_Dec
