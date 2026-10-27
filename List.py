states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])
states_of_america[0] = "New York"
print(states_of_america[0])
states_of_america.append("New York")
print(states_of_america)


----------------------------------


import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#1 option
random_name = friends[random.randint(0,4)]
print(random_name)
#2 options
print(random.choice(friends))
