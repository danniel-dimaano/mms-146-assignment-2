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


"""
Situation:
Josanine wanted to contribute into building the dream boarding place with her friends.
She pitched to give a refrigirator but was confused with the options she was presented with during
her shopping at the mall.
"""

#We will now define the attributes and methods for the refrigerator object
class Refrigerator:
    def __init__(self,n,c,ty,cap,st,temp):
        self.name = n
        self.color = c
        self.type = ty
        self.capacity = cap
        self.state = st
        self.temperature = temp
        
    #The actions for the object define / intend to function as their names implies
    def change_name(self,n):
        self.name = n
        
    def pick_color(self,c):
        self.color = c
    
    def define_type(self,ty):
        self.type = ty
        
    def set_capacity(self,cap):
        self.capacity = cap
        
    def change_state(self,st):
        self.state = st
        
    def set_temperature(self,temp):
        self.temperature = temp
        
#And this is the Main Program

#This weird lines are there to act as a decoration.
#The lines below will add two succeeding lines withouot any contents.
print("")
print("")

refA = Refrigerator("LG","Shiny Silver","Side-by-Side","350 Liters","ON","24 degrees Celcius")

print ("Brand Name: ",refA.name)
print ("Color: ", refA.color)
print ("Type: ", refA.type)
print ("Total Capacity: ",refA.capacity)
print ("State:", refA.state)
print ("Current Temp.: ", refA.temperature)


print("")
print("")

#But then, Josanine wished to look for a different color of the same type and brand of refrigerator

print ("Brand Name: ",refA.name)
#This line can change the refrigerator into any color Josanine wishes
refA.pick_color("Midnight Black")

print ("Color: ", refA.color)
print ("Type: ", refA.type)
print ("Total Capacity: ",refA.capacity)
print ("State:", refA.state)
print ("Current Temp.: ", refA.temperature)


#And so, Josanine was delighted with her newly bought refrigerator in "Midnight Black!"



#This class is for a new object
#The object is a household Iron

"""
Situation:
Josanine headed to the "Washing Section" of the appliance store she visited yesterday.
She was greeted with vast variety of irons to pick, so she decided to narrow down her choices
into three brands offering similar functionalities (her trusted brand "Xiaomi", and two unfamiliar
brands she saw while browsing the catalouge online).
She wanted an iron that will help her save space in her room.
"""

#We will now define the attributes and methods of the iron object
class Iron:
    def __init__(self,n,c,ty,watt,st):
        self.name = n
        self.color = c
        self.type = ty
        self.wattage = watt
        self.state = st
        
    #The actions of the object intends to do what their names suggests :>
    def change_name(self,n):
        self.name = n
        
    def pick_color(self,c):
        self.color = c
    
    def define_type(self,ty):
        self.type = ty
        
    def set_wattage(self,watt):
        self.wattage = watt
        
    def change_state(self,st):
        self.state = st
        
        
        
#And this is the Main Program

print("")
print("")

iron1 = Iron("Black+Decker","Black","Steam Iron","1,200 watts","OFF")
iron2 = Iron("Xiaomi","White","Travel Steam Iron","1,200 watts","OFF")
iron3 = Iron("Rowenta Focus","Red","Steam Iron","1,725 watts","OFF")

print ("Brand Name: ",iron1.name)
print ("Color: ", iron1.color)
print ("Type: ", iron1.type)
print ("Wattage: ",iron1.wattage)
print ("State:", iron1.state)

print("")
print("")

print ("Brand Name: ",iron2.name)
print ("Color: ", iron2.color)
print ("Type: ", iron2.type)
print ("Wattage: ",iron2.wattage)
print ("State:", iron2.state)

print("")
print("")

print ("Brand Name: ",iron3.name)
print ("Color: ", iron3.color)
print ("Type: ", iron3.type)
print ("Wattage: ",iron3.wattage)
print ("State:", iron3.state)

#Josanine was happy for her purchase!
#Josanine picked the Xiaomi Travel Steam Iron as it was compact and has a small form-factor.

"""
Josanine suddenly decided to pick a new slippers to use for inside and for outside of the house.
She was presented with various options by the sales lady inside the "Clothing Section" of the mall
she went in.
So she narrowed down her options by looking at specific brands and specific designs.
"""


#We will now define the attributes and methods of the slippers object    
class Slippers:
    def __init__(self,n,c,sz,use,mat):
        self.name = n
        self.color = c
        self.size = sz
        self.usage = use
        self.material = mat
        
    #The following strings are written to help the encoders to manipulate the methids
    def change_name(self,n):
        self.name = n
        
    def pick_color(self,c):
        self.color = c
    
    def set_size(self,sz):
        self.size = sz
        
    def define_usage(self,use):
        self.usage = use
        
    def define_material(self,mat):
        self.material = mat
        
    
#And this is the Main Program


print("")
print("")

slip1 = Slippers("Marquina - The Bonnie Penny Loafers","Oxblood Burgundy","7","Office Shoes","Leather  ")
slip2 = Slippers("Nike - Jordan Sophia","Off-White","7","INDOORS","Rubber and Foam")
slip3 = Slippers("Vionic - Mule Slippers","Tan","8","INDOORS","Polyester Terry Cloth")


print ("Brand Name: ",slip1.name)
print ("Color: ", slip1.color)
print ("Size: ", slip1.size)
print ("Usage: ",slip1.usage)
print ("Material Used:", slip1.material)

print("")
print("")

print ("Brand Name: ",slip2.name)
print ("Color: ", slip2.color)
print ("Size: ", slip2.size)
print ("Usage: ",slip2.usage)
print ("Material Used:", slip2.material)


print("")
print("")

print ("Brand Name: ",slip3.name)
print ("Color: ", slip3.color)

#There are many colors to choose from!
slip3.pick_color("Black, Light Pink, and Dark Blue")
print ("Other Available Colors: ", slip3.color)
print ("Size: ", slip3.size)
print ("Usage: ",slip3.usage)
print ("Material Used:", slip3.material)


"""
Josanine was feeling tired from trying out various shoe types and sizes.
She only looked for one outdoor shoe and two for indoor shoes.
Josanine then decided to purchase one outdoor and one indoor shoe.
And she decided to go for her only option for outdoor shoes and her most loved mule indoors shoes
from Vionic.
"""



