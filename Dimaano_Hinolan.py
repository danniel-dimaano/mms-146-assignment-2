# This is Fan (electric) class 

class Fan: 
    
#attributes
    def __init__(self, n, t, c, dj, m, p):
        self.name = n
        self.type = t
        self.color = c
        self.state = dj
        self.mode = m
        self.speed = p

#methods
    def give_name(self,n):
        self.name = n 
	      
    def change_shape(self,t):
        self.type = t
	      
    def change_color(self,c):
        self.color = c 
	      
    def change_state(self,dj):
        self.state = dj

    def change_mode(self,m):
        self.mode = m
	      
    def change_speed(self,p):
        self.speed = p

fan1 = Fan("Asahi", "ceiling", "green", "ON", "swing", "high")
fan2 = Fan("Xiaomi", "tower", "pink", "ON", "still", "medium")

print ("Fan brand is",fan1.name)
print ("Fan type is",fan1.type)
print ("Fan color is",fan1.color)
print ("Fan state is",fan1.state)
print ("Fan mode is",fan1.mode)
print("Fan speed is",fan1.speed)

print("")
print("")

print ("Changed brand to",fan2.name)
print ("Preferred: ",fan2.type,"fan type")
print ("Changed color to",fan2.color)
print ("Fan state is",fan2.state)
print ("Fan mode is",fan2.mode)
print("Fan speed is",fan2.speed)


"""
This is the Lamp class.
It encompasses the attributes and methods of the object which the enocoders wishes to include.
Some of the lines are copied over or modified from the original code to ease the encoder's life.
"""

class Lamp:
    def __init__(self,n,sh,bc,st,lc):
        self.name = n
        self.shape = sh
        self.body_color = bc 
        self.state = st
        self.light_color = lc
        
    def change_name(self,n):
        self.name = n    
        
    def change_shape(self,sh):
        self.shape = sh
        
    def change_body_color(self,bc):
        self.body_color = bc

    def change_state(self,st):
        self.state = st
        
# This is the Main Program

lamp1 = Lamp("Sylphat","Bar","Green","ON","White")
lamp2 = Lamp("Garimond","Circular","Grey","OFF","Warm")

# This line prints the brand name, the shape, the light color, and the state of lamp no. 1
print ("Brand Name: ",lamp1.name)
print ("Shape: ", lamp1.shape)
print ("Previous lamp state: ", lamp1.state)
print ("Light color: ",lamp1.light_color)
lamp1.change_state("OFF")
print ("Current state: ", lamp1.state)

#This code will print two empty lines just to format the appearance of the console
print ("")
print ("")

# This line prints the brand name, the shape, and the state of lamp no. 2
print ("Brand Name: ",lamp2.name)
print ("Shape: ", lamp2.shape)
print ("Lamp state: ", lamp2.state)


