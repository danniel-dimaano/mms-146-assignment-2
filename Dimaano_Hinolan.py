#INTRODUCTION

"""
Danniel and Josanine are an incoming third-year BA in Multimedia Studies students
from the University of the Philippines - Open University. And since they are online
distance learning students, they and their group of friends from class decided to
rent a boarding place where they could each have separate bedrooms, which also
serve as their personal study spaces. Being in college, they wanted to have a sense
of independence and figure out things in their life as they grew and matured. 

So, since Danniel and Josanine were the first to move into their new boarding
place, they decided to go ahead and organize their respective bedrooms. They each
made a list of what they needed to buy to settle comfortably in their new place. 

With that on Danniel's list, he needed the following for his bedroom: an electric
fan, bathroom tiles, and a bed. On the other hand, here is the list that Josanine
made: an LED lamp, an electric iron, and a pair of slippers. In addition, they both
decided to add something on their list as a welcome gift or contribution to their
group of friends as they settled into their new place. So, Danniel wanted to give
each of his friends a custom-made bar of soap, while Josanine decided to contribute
a refrigerator for them to share. 

Now, Danniel and Josanine are off to a shopping time at various online and physical
stores to complete what they need for their new place and bedrooms. The challenge
of this errand is how good will they be in making their choices to pick the right
items that will best fit their needs and expectations. 

So, keep scrolling to see how these two did on their shopping errand!
"""


# This is Fan (electric) class 

""" 
Situation: 

Danniel plans to purchase an electric fan for his new bedroom; however, he first wants to look at options before deciding. So, to narrow his choices, he settled 
with two brands: Asahi and Xiaomi. Then, he considered the following: the electric fan's type, color, state, mode, and speed. 

He mainly wanted a ceiling or tower fan as those are space-savers for his bedroom. Then he found the colors green or pink complementary to his room's theme. So, 
he asked for an Asahi Ceiling fan in the color green and a Xiaomi Tower fan in pink. Then, he turned them on and checked if the Asahi ceiling fan could 
rotate smoothly at 360 degrees when on swing mode enough to cover his bedroom from medium to high speed. And he turned on the Xiaomi tower fan and placed it from 
medium to high speed to see if it could cover a vast space even on still mode.

Then, he turned the Asahi and  Xiaomi fans off and observed whether the green ceiling fan or the pink tower fan fit his bedroom the best. 

At last, he picked the Xiaomi Tower fan in pink and decided to buy it already for his new bedroom. As he found its speed from medium to high stronger and more 
refreshing, the tower fan type is also a space saver and could cover a vast area of his room, and the color pink complements the theme of his room very well. 
"""

class Fan: 
    
#This contains the set of codes representing the attributes
    def __init__(self, n, ty, co, st, mo, sp):
        self.name = n
        self.type = ty
        self.color = co
        self.state = st
        self.mode = mo
        self.speed = sp

#This contains the set of codes representing the methods
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


#This is the main program

#These are the two options we made for the Fan (electric) object 
fan1 = Fan("Asahi", "Ceiling", "Green", "On", "Swing", "Medium")
fan2 = Fan("Xiaomi", "Tower", "Pink", "On", "Still", "Medium")

#This code will print the brand name of the Fan No. 1
print ("Brand:",fan1.name)

#This code will print one empty line to seperate the brand name from the rest
print("")

#This will print the type, color, state, mode, and speed of Fan No. 1
print ("Type:",fan1.type)
print ("Color:",fan1.color)

#This code will print the previous state of the Asahi Brand Ceiling Fan
print ("Previous State:",fan1.state)

print ("Mode:",fan1.mode)

#This code will print the initial speed of the Asahi Brand Ceiling Fan
print ("Initial Speed:",fan1.speed)

#This code will print the new speed of the Asahi Brand Ceiling Fan
fan1.set_speed("High")
print ("Change speed to:",fan1.speed)

#This code will print the current state of the Asahi Brand Ceiling Fan
fan1.change_state("Off")
print ("Current state:",fan1.state)

#This code will print two empty lines to seperate the Asahi and Xiaomi brands
print("")
print("")

#This code will print the brand name of the Fan No. 2
print ("Brand:",fan2.name)

#This code will print one empty line to seperate the brand name from the rest
print("")

#This will print the type, color, state, mode, and speed of Fan No. 2
print ("Type:",fan2.type)
print ("Color:",fan2.color)

#This code will print the previous state of the Xiaomi Brand Tower Fan
print ("Previous State:",fan2.state)

print ("Mode:",fan2.mode)

#This code will print the initial speed of the Xiaomi Brand Tower Fan
print ("Initial Speed:",fan2.speed)

#This code will print the new speed of the Xiaomi Brand Tower Fan
fan2.set_speed("High")
print ("Change speed to:",fan2.speed)

#This code will print the current state of the Xiaomi Brand Tower Fan
fan2.change_state("Off")
print ("Current state:", fan2.state)



#This is Tile class

"""
For Danniel's bathroom, he wanted to be specific with its tiles to ensure that it
is pleasing, durable, and safe. So, he went to an online tile store and found 
two brand options by Wilcon and Eurotiles. Then, he specified his tile preferences
to the store's virtual assistant; he wanted something that was not slippery
but will look shiny. And he wanted tile shapes that were not too ordinary. 

With that, he was presented with two options for a bathroom-friendly tile: 

First is the Wilcon brand with a porcelain material in the shape of a hexagon with
a sandblasted texture, a coastal luster, and 8mm thickness. But he also wanted
the same tile features in a slate material, so he was presented with a slate tile
material with the same tile design. 

On the other hand, Eurotiles offers a slate material in the shape of a chevron with
an etched texture but with oyster luster and a thickness of 6mm. So, Danniel
also asked for the Eurotiles' tile design but in the porcelain material. 

Danniel liked the two options he was presented with. But before he decides, he
wants to make sure that he gets to see thoroughly on which brand offers the best
quality and design, in particular, with the tile material. That is why he also
switched the tile materials from Wilcon's porcelain to their slate and Eurotiles'
slate to their porcelain to see which one has the better deal. So, he ordered tile
samples from each brand with his specific preferences to see which one fits best
with his bathroom for this new bedroom. From there, once he's sure about a
particular choice for his bathroom tiles is when he will order a bunch to start
construction.
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



#This is Bed class

"""
Another thing that Danniel wants for his bedroom is to meticulously pick a bed
that fits him and his standard of comfort. So, he went online shopping again, but
this time for a bed. And he had the following things to consider: it must be a
single bed for an adult person with a rectangular shape, either metal or wood
frame, and in a brand new condition with a comfortable mattress to sleep on. 

The online store offers a wide range of brands to choose from. But he picked the
Sleepwell and Wakefit brands for his options since he is already familiar with
those two. 

First, the Sleepwell brand offers a brand new adult single bed with a size of
90cm x 190cm in a rectangular shape. However, they only have the bed in a metal bed
frame material. So, he checked the two options available: the iron metal and the
steel metal frame. And they have a traditional foam mattress that comes with it. 

And second, the Wakefit brand has the same features as the Sleepwell brand. But
they only have it in a wooden bed frame material which he can choose between
mahogany or oak wood frames. But it comes with a gel memory foam mattress. 

Since Danniel finds it crucial to find the most durable and comfortable bed
possible, he took his time to decide. He researched his options until he chose the
Sleepwell brand with the steel metal bed frame because he discovered that metal
steel bed frames are durable yet more affordable, and the Sleepwell brand has a gel
memory foam mattress that comes with it. And that is a good quality mattress and
bed he has wanted for a while now.
"""

class Bed: 
    
#attributes
    def __init__(self, n, sz, mt, fr, us, co, sh):
        self.name = n
        self.size = sz
        self.mattress_material = mt
        self.frame_material = fr
        self.user = us
        self.condition = co
        self.shape = sh

#methods
    def give_name(self,n):
        self.name = n 

    def set_size(self,sz):
        self.size = sz

    def pick_mattress_material(self,mt):
        self.mattress_material = mt
	      
    def pick_frame_material(self,fr):
        self.frame_material = fr
	      
    def set_user(self,us):
        self.user = us
	      
    def set_condition(self,co):
        self.condition = co

    def define_shape(self,sh):
        self.shape = sh
        
bed1 = Bed("Sleepwell", "Single (90cm x 190cm)", "Traditional Foam", "Metal", "Adult Person", "Brand New", "Rectangular")

bed2 = Bed("Wakefit", "Single (90cm x 190cm)", "Gel Memory Foam", "Wood", "Adult Person", "Brand New", "Rectangular")

print("Brand:",bed1.name)

print("")

print("Size:",bed1.size)
print("Mattress Material:",bed1.mattress_material)
print("Bed Frame Material:",bed1.frame_material)
bed1.pick_frame_material("Iron Metal")
print ("Change to Metal Option 1:", bed1.frame_material)
bed1.pick_frame_material("Steel Metal")
print ("Change to Metal Option 2:", bed1.frame_material)
print("User:",bed1.user)
print("Condition:",bed1.condition)
print("Shape:",bed1.shape)

print("")
print("")

print("Brand:",bed2.name)

print("")

print("Size:",bed2.size)
print("Mattress Material:",bed2.mattress_material)
print("Bed Frame Material:",bed2.frame_material)
bed1.pick_frame_material("Mahogany Wood")
print ("Change to Wood Option 1:", bed1.frame_material)
bed1.pick_frame_material("Oak Wood")
print ("Change to Wood Option 2:", bed1.frame_material)
print("User:",bed2.user)
print("Condition:",bed2.condition)
print("Shape:",bed2.shape)



#This is Soap class

"""
To complete his bathroom essentials, Danniel went to the Lush online store to order
a customized body soap and gift it to his friends at the boarding place. So he
considered the following: the soap's shape, color, fragrance, usage, and lather
intensity. 

And as he scrolled, he found a color yellow body soap in a rectangular shape with a
lather intensity of seven in a lemon citrus scent. However, he doesn't feel like it
is the right one for him and something his friends would enjoy having for a bath.
So, he customized the body soap through the Lush website's soap customization
featured page and changed the shape to an oval, the color to peach, and its
fragrance to an oat milk scent, but kept the lather intensity to seven. 

Once satisfied with his choice of soap, he ordered a couple of pieces for himself
and his friends. 
"""

class Soap: 
    
#attributes
    def __init__(self, n, sh, co, fg, ug, lh):
        self.name = n
        self.shape = sh
        self.color = co
        self.fragrance = fg
        self.usage = ug
        self.lather_intensity = lh
        
#methods
    def give_name(self,n):
        self.name = n 

    def set_shape(self,sh):
        self.shape = sh

    def set_color(self,co):
        self.color = co
    
    def set_fragrance(self,fg):
        self.fragrance = fg
    
    def define_usage(self,ug):
        self.usage = ug
    
    def set_lather_intensity(self,lh):
        self.lather_intensity = lh

soap = Soap("Lush", "Rectangle", "Yellow", "Lemon Citrus", "Body Soap", "7")

print("Brand:",soap.name)

print("")

print("Shape Option 1:",soap.shape)
soap.set_shape("Oval")
print ("Change to Shape Option 2:",soap.shape)

print("")

print("Color Option 1:",soap.color)
soap.set_color("Peach")
print ("Change to Color Option 2:",soap.color)

print("")

print("Fragrance Option 1:",soap.fragrance)
soap.set_fragrance("Oat Milk")
print ("Change to Fragrance Option 2:",soap.fragrance)

print("")

print("Usage:",soap.usage)
print("Lather Intensity:",soap.lather_intensity)



"""
Situation:
Everyone knows how much of a night owl Josanine has always been. She's a pro at
staying late at night for study or leisure time, so a good-quality and durable lamp
is essential for her bedroom. With that, she went to a lighting store that sells
various lamps. But, she prefers explicitly an LED lamp that has a setting to change
different light colors. 
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
	
"""
The store assistant brought her two brands of LED lamps in the name of Sylphat and
Garimond. First, the Sylphat brand is a bar-shaped LED lamp with a changing light
color setting. So, she turned the lamp on, checked the white light color, and then
turned it off to see if it fit her bedroom well. Meanwhile, the Garimond brand was
circular, but she kept it turned off. 
"""
        
# This is the Main Program

#This code will print two empty lines just to format the appearance of the code in the console
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

#This code will print two empty lines just to format the appearance of the code in the console
print ("")
print ("")

# This line prints the brand name, the shape, and the state of lamp no. 2
print ("Brand Name: ",lamp2.name)
print ("Shape: ", lamp2.shape)
print ("Lamp state: ", lamp2.state)

"""
In the end, she made a quick decision and bought the Sylphat LED lamp as
she found the style more pleasing and the light friendly to her vision.
"""


#We will now create a new class.
#We will make a Refrigerator object!

"""
Situation:
Josanine went to the mall's appliance section to contribute to their group to find
a refrigerator that best suited their needs at the boarding place. Specifically,
she wants a side-by-side type of fridge with a capacity of 350 liters and
preferably an LG brand. 
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

	
"""
Fortunately, the store has all the fridge features that she wants and the brand.
She noticed that the fridge was already cool enough, even at its current
temperature of 24 degrees Celcius. However, she wanted another color option besides
the Shiny Silver color. So, the store assistant offered her a refrigerator with the
same features but in the shade of Midnight Black.
"""
#And this is the Main Program

#This weird lines are here to act as a decoration.
#The code below will add two succeeding lines withouot any contents.
print("")
print("")

refA = Refrigerator("LG","Shiny Silver","Side-by-Side","350 Liters","ON","24 degrees Celcius")

print ("Brand Name: ",refA.name)
print ("Color: ", refA.color)
print ("Type: ", refA.type)
print ("Total Capacity: ",refA.capacity)
print ("State:", refA.state)
print ("Current Temp.: ", refA.temperature)

#This is also for decorations only
print("")
print("")

#But then, Josanine wished to look for a different color of the same type and brand of refrigerator
#Let us change the color!
print ("Brand Name: ",refA.name)
#This line can change the refrigerator into any color Josanine wishes
refA.pick_color("Midnight Black")

print ("Color: ", refA.color)
print ("Type: ", refA.type)
print ("Total Capacity: ",refA.capacity)
print ("State:", refA.state)
print ("Current Temp.: ", refA.temperature)


"""
At last, Josanine found the LG refrigerator in Midnight Black, the one for their
new boarding place. So she went ahead to order it and have it delivered to their
home.
"""



#This class is for a new object
#The object is a household Iron

"""
Situation:
Another day, another chance for Josanine to finish her shopping errand. So, she
returned to the mall's Appliance Section to find an electric iron for her clothes.
She was greeted with a wide variety of choices. So, she narrowed down her choices
by picking three brands offering similar functionalities: Xiaomi, her trusted
brand, and two other unfamiliar brands in the name of Black+Decker and Rowenta
Focus. In addition, she wants something that will save space in her room. 

So, since no store assistants were available to assist her, she could not turn the
items on. But she decided based on the features included in each brand she picked:

The Black+Decker was in color black, a steam iron, with 1,200 watts.
The Xiaomi travel steam iron in color white with 1,200 watts.
The Rowenta Focus, which is in the color red, is steam iron with 1,725 watts. 
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

#The codes below are here to serve as decorations
print("")
print("")

#Let us create 3 iron objects.
iron1 = Iron("Black+Decker","Black","Steam Iron","1,200 watts","OFF")
iron2 = Iron("Xiaomi","White","Travel Steam Iron","1,200 watts","OFF")
iron3 = Iron("Rowenta Focus","Red","Steam Iron","1,725 watts","OFF")

print ("Brand Name: ",iron1.name)
print ("Color: ", iron1.color)
print ("Type: ", iron1.type)
print ("Wattage: ",iron1.wattage)
print ("State:", iron1.state)

#The codes below are here to serve as decorations
print("")
print("")

print ("Brand Name: ",iron2.name)
print ("Color: ", iron2.color)
print ("Type: ", iron2.type)
print ("Wattage: ",iron2.wattage)
print ("State:", iron2.state)

#The codes below are here to serve as decorations
print("")
print("")

print ("Brand Name: ",iron3.name)
print ("Color: ", iron3.color)
print ("Type: ", iron3.type)
print ("Wattage: ",iron3.wattage)
print ("State:", iron3.state)

"""
In the end, Josanine purchased the  Xiaomi travel steam iron as it is an absolute
space saver and is already a familiar and trusted brand to her.
"""

#We will now create a new class.
#The class will be called "Slippers" as we want to create a slipper object.

"""
Situation:
One more thing from Josanine's list is a new pair of slippers for inside and
outside the house. So, she went to the mall's Footwear Section, overwhelmed with
how many choices she had to choose from. 

She found three brands to choose from: the Marquina - The Bonnie Penny Loafers
office leather shoes in an oxblood burgundy color size seven. Then, she found the
Nike - Jordan Sophia indoor rubber and foam slides in an off-white color available
in size seven. And the Vionic - Mule Slippers indoor slippers in a polyester terry
cloth material in the colors tan, black, light pink, and dark blue are available in
sizes eight.
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


#This weird lines are here to act as a decoration.
#The code below will add two succeeding lines withouot any contents.
print("")
print("")


#We will now create three objects out of the defined attributes and methods above
slip1 = Slippers("Marquina - The Bonnie Penny Loafers","Oxblood Burgundy","7","Office Shoes","Leather  ")
slip2 = Slippers("Nike - Jordan Sophia","Off-White","7","INDOORS","Rubber and Foam")
slip3 = Slippers("Vionic - Mule Slippers","Tan","8","INDOORS","Polyester Terry Cloth")


print ("Brand Name: ",slip1.name)
print ("Color: ", slip1.color)
print ("Size: ", slip1.size)
print ("Usage: ",slip1.usage)
print ("Material Used:", slip1.material)


#These codes are for decorations only
print("")
print("")

print ("Brand Name: ",slip2.name)
print ("Color: ", slip2.color)
print ("Size: ", slip2.size)
print ("Usage: ",slip2.usage)
print ("Material Used:", slip2.material)

#These codes are for decorations only
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
After a while, Josanine finally chose the Marquina brand office leather shoes for
her outdoor pair, as it was her only choice. And bought the Vionic brand for her
indoor pair of slippers.
"""


#TO END...
"""
Finally, Danniel and Josanine were able to complete the items on their list and
will be able to settle comfortably in their new boarding place and separate
bedrooms. Indeed, they will be well-prepared to start their new adventure of living
together under one roof as their new trimester begins in a few weeks.
"""

