# This is a test command line
class Lamp(object):
    """docstring for ."""

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg

# This is Fan (electric) class 

class Fan: 
    
    def __init__(self, n, s, c, d, j, p):
        self.name = n
        self.shape = s
        self.color = c
        self.on = d
        self.off = j
        self.speed = p
    
    def increase_speed(self):
		self.speed = self.speed + 1


        
