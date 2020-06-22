# stuff = {'name':'Zed', 'age': 39, 'height': 74, 'city': 'SF'}

# print(stuff['name'])

# print(stuff['age'])

# print(stuff['height'])

# print(stuff['city'])



# Create a mapping of state to abbrevation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#Create a baisc set of states and some cities in them 
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-'*10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-' *10)
print("Michigan's abbrevation is: ", states['Michigan'])
print("Florida's abbrevation is: ",states['Florida'])

# do it by using the state then cities dic
print('-' *10)
print("Michigan has: ",cities[states['Michigan']])
print("FLorida has: ",cities[states['Florida']])

#print every states abbrevation
print('-' *10)
for state,abbrev in list(states.items()):
    print(f"{state} is abbrevated {abbrev}")

# print every city in state
print('-' *10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' *10)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbrevated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' *10)
# safely get a abbrevation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas")


# get a city with a default values
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")