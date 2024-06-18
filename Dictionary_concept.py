# Dictionary and sets

# Dictionary is also a mutable

# here we are calling object as a dictory 
player = {
    "name":"Waseem",
    "sport":"Cricket",
}

# print(player['name'],player['sport'])

# Methods in dictionary

# print(player.keys())  #to get all the keys 

#output : dict_keys(['name', 'sport'])

# print(player.values())  #to get all the values 

# output : dict_values(['waseem', 'Cricket'])

# print(player.items())

# output : dict_items([('name', 'waseem'), ('sport', 'Cricket')])

# Lets try to mutate the dictionary
# player["name"] = "wassu"

# print(player)

# how to add new key-value pair to the dictionary with "update" method

newFeature = {
    "hundreds":67
}

player.update(newFeature)
# print(player)

# we have two ways of accessing the dictionary or object
#mehtod-1
# print(player['hundreds1'])

#method-2 
print(player.get('hundreds1'))

''' The major difference between meetho-1 and 2 is if key 
doesnt match in method-1 it throws an error
but method-2 will return None '''





