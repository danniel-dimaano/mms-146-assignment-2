# This is Fan (electric) class 

""" 
Situation:

Danniel plans to purchase an electric fan for his new bedroom; however, he first wants to look at options before deciding. So, to narrow his choices, 
he settled with two brands: Asahi and Xiaomi. Then, he considered the following: the electric fan's type, color, state, mode, and speed. 

He mainly wanted a ceiling or tower fan as those are space-savers for his bedroom. Then he found the colors green or pink complementary to his room's theme. 
So, he asked for an Asahi Ceiling fan in the color green and a Xiaomi Tower fan in pink. Then, he turned them on and checked if the Asahi ceiling fan could
rotate smoothly in 360 degrees when on swing mode enough to cover his bedroom even when on medium speed only. And he turned on the Xiaomi tower fan and placed 
it at high speed to see if it could cover a vast space even on still mode.

Then, he turned the Asahi and  Xiaomi fans off and observed whether the green ceiling fan or the pink tower fan fit his bedroom the best. 
"""

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
	      
    def change_type(self,t):
        self.type = t
	      
    def change_color(self,c):
        self.color = c 
	      
    def change_state(self,dj):
        self.state = dj

    def change_mode(self,m):
        self.mode = m
	      
    def change_speed(self,p):
        self.speed = p

fan1 = Fan("Asahi", "Ceiling", "Green", "On", "Swing", "Medium")
fan2 = Fan("Xiaomi", "Tower", "Pink", "On", "Still", "High")
fan3 = Fan("Asahi", "Ceiling", "Green", "Off", "None", "None")
fan4 = Fan("Xiaomi", "Tower", "Pink", "Off", "None", "None")

print ("Brand:",fan1.name)
print ("Type:",fan1.type)
print ("Color:",fan1.color)
print ("State:",fan1.state)
print ("Mode:",fan1.mode)
print ("Speed:",fan1.speed)

print("")

print ("Brand:",fan2.name)
print ("Type:",fan2.type)
print ("Color:",fan2.color)
print ("State:",fan2.state)
print ("Mode:",fan2.mode)
print ("Speed:",fan2.speed)

print("")
print("")

print ("Brand:",fan3.name)
print ("Type:",fan3.type)
print ("Color:",fan3.color)
print ("State:",fan3.state)
print ("Mode:",fan3.mode)
print ("Speed:",fan3.speed)

print("")

print ("Brand:",fan4.name)
print ("Type:",fan4.type)
print ("Color:",fan4.color)
print ("State:",fan4.state)
print ("Mode:",fan4.mode)
print ("Speed:",fan4.speed)



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

#This code will print two empty lines just to format the appearance of the console
print ("")
print ("")

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


