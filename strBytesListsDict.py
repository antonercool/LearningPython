# str - Data type for string
# Supports both "" , ''  --> "he said 'yes' " or 'he said "yes"'
# Supports \n \t
# raw string like @ from C#  --> r"This is a raw string / \ \t"
# s = "test"
# type(s[2]) is also of type str
# strings are Imutable meaning the cant be changed 
# c = "hello there", c.capitalize , print(c) --> "hello there"
# allways returns a new string

# bytes - Supports nearly the same as str 
# d = b"some bytes" , d[0] --> 115 instead of 's' if it was type str
# convert from bytes to str
# tekst = "hej med dig"
# tekstAsBytes = teskt.encode("uft8");
# backToTeskt = tekstAsBytes.decode("uft8")

# list - holds any obj and are mutable
# list can hold diffent types at the same time
# listOfStrAndInts = ["helloThere", 321, "test"], emptyList= []

#dict
# d = {'item1' :  12341234, 'item2' : 123}
# d['item2] --> 123
# d['item3': 12341]  --> creates new cause it does not exits
# e =  {} --> empty dict

