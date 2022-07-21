# This is Fan (electric) class 

""" 
Danniel plans to purchase an electric fan for his new bedroom; however, he first wants to look at options before deciding. So, to narrow his choices, he settled 
with two brands: Asahi and Xiaomi. Then, he considered the following: the electric fan's type, color, state, mode, and speed. 

He mainly wanted a ceiling or tower fan as those are space-savers for his bedroom. Then he found the colors green or pink complementary to his room's theme. So, 
he asked for an Asahi Ceiling fan in the color green and a Xiaomi Tower fan in pink. Then, he turned them on and checked if the Asahi ceiling fan could 
rotate smoothly at 360 degrees when on swing mode enough to cover his bedroom from medium to high speed. And he turned on the Xiaomi tower fan and placed it from 
medium to high speed to see if it could cover a vast space even on still mode.

Then, he turned the Asahi and  Xiaomi fans off and observed whether the green ceiling fan or the pink tower fan fit his bedroom the best. 
"""

class Fan: 
    
#attributes
    def __init__(self, n, ty, co, st, mo, sp):
        self.name = n
        self.type = ty
        self.color = co
        self.state = st
        self.mode = mo
        self.speed = sp

#methods
    def give_name(self,n):
        self.name = n
	      
    def change_type(self,ty):
        self.type = ty
	      
    def change_color(self,co):
        self.color = co
	      
    def change_state(self,st):
        self.state = st

    def change_mode(self,mo):
        self.mode = mo
	      
    def set_speed(self,sp):
        self.speed = sp

fan1 = Fan("Asahi", "Ceiling", "Green", "On", "Swing", "Medium")
fan2 = Fan("Xiaomi", "Tower", "Pink", "On", "Still", "Medium")

print ("Brand:",fan1.name)
print ("Type:",fan1.type)
print ("Color:",fan1.color)
print ("Previous State:",fan1.state)
print ("Mode:",fan1.mode)
print ("Initial Speed:",fan1.speed)
fan1.set_speed("High")
print ("Change speed to:",fan1.speed)
fan1.change_state("Off")
print ("Current state:",fan1.state)

print("")

print ("Brand:",fan2.name)
print ("Type:",fan2.type)
print ("Color:",fan2.color)
print ("Previous State:",fan2.state)
print ("Mode:",fan2.mode)
print ("Initial Speed:",fan2.speed)
fan2.set_speed("High")
print ("Change speed to:",fan2.speed)
fan2.change_state("Off")
print ("Current state:", fan2.state)



#This is Tile class

"""
Situation:

For Danniel's bathroom, he wanted to be specific with its tiles to ensure that it is pleasing, durable, and safe. So, he went to a tile store and found two 
brand options by Wilcon and Eurotiles. Then, he explained his tile preferences to the store assistant; he wanted something that was not slippery but will look shiny. 
And he wanted tile shapes that were not too ordinary. 

With that, he was presented with two options for a bathroom-friendly tile: 
First is the Wilcon brand with a porcelain material in the shape of a hexagon with a sandblasted texture, a coastal luster, and 8mm thickness. But he also wanted 
the same tile features in a slate material, so he was presented with a slate tile material with the same tile design. 

On the other hand, Eurotiles offers a slate material in the shape of a chevron with an etched texture but with oyster luster and a thickness of 6mm. So, Danniel 
also asked for the Eurotiles' tile design but in the porcelain material. 

Danniel liked the two options he was presented with. But before he decides, he wants to make sure that he gets to see thoroughly on which brand 
offers the best quality and design, in particular, with the tile material. That is why he also switched the tile materials from Wilcon's porcelain to their 
slate and Eurotiles' slate to their porcelain to see which one has the better deal. So, he took tile samples from each brand with his specific preferences to 
see which one fits best with his bathroom for this new bedroom. 
"""

class Tile: 
    
#attributes
    def __init__(self, n, ma, sh, tx, lu, th):
        self.name = n
        self.material = ma
        self.shape = sh
        self.texture = tx
        self.luster = lu
        self.thickness = th

#methods
    def give_name(self,n):
        self.name = n 

    def set_material(self,ma):
        self.material = ma 
	      
    def set_geometry(self,sh):
        self.geometry = sh
	      
    def set_texture(self,tx):
        self.texture = tx 
	      
    def make_luster(self,lu):
        self.luster = lu

    def set_thickness(self,th):
        self.thickness = th
        
tile1 = Tile("Wilcon", "Porcelain", "Hexagon", "Sandblasted", "Coastal", "8mm")
tile2 = Tile("Eurotiles", "Slate", "Chevron", "Etched", "Oyster", "6mm")

print("Brand:",tile1.name)

print("")

print("Initial Material:",tile1.material)
tile1.set_material("Slate")
print ("Change material to:", tile1.material)
print("Shape:",tile1.shape)
print("Texture:",tile1.texture)
print("Luster:",tile1.luster)
print("Thickness:",tile1.thickness)

print("")
print("")

print("Brand:",tile2.name)

print("")

print("Initial Material:",tile2.material)
tile2.set_material("Porcelain")
print ("Change material to:", tile2.material)
print("Shape:",tile2.shape)
print("Texture:",tile2.texture)
print("Luster:",tile2.luster)
print("Thickness:",tile2.thickness)



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


