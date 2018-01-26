import random

#return groups of 3-5 people, max 25, min 3
def makeGroups(names, currentGroups):
	#base case
	if (len(names) <= 2):
		if len(currentGroups) == 1:
			while len(names) > 0:
				currentGroups[0].append(names[0])
				names.remove(names[0])
			return currentGroups
		elif len(currentGroups) == 0:
			return [names]
		else:
			if len(names) == 1:
				currentGroups[0].append(names[0])
				names.remove(names[0])
			else: #2 leftover people
				currentGroups[0].append(names[0])
				currentGroups[1].append(names[1])
				names.remove(names[0])
				names.remove(names[0])
		return currentGroups

	elif (len(names) % 3 == 0):
		#split into groups and return 
		while len(names) > 0:
			group = [] 
			for i in range(3):
				name = random.choice(names)
				group.append(name)
				names.remove(name)
			currentGroups.append(group)
		return currentGroups

	else: #will have 1 or 2 leftovers
		while (len(names) != 2) and (len(names) != 1):
			#("lenth", len(names), names)
			group = [] 
			for i in range(3):
				#print(group, names)
				name = random.choice(names)
				group.append(name)
				names.remove(name)
			currentGroups.append(group)
		return makeGroups(names, currentGroups)

group1 = ["bob", "anna"] #group of 2
group2 = ["bob", "anna", "joe"] #group of 2
group3 = ["bob", "hannah", "joe", "anne"]  #4 people, should return 1 group of 4
group4 = ["bob", "hannah", "joe", "anne", "a", "b", "c", "d", "hello"] #9 people, should have 3 groups of 3
group5 = ["g", "y", "s", "d", "x", "v", "n", "m" ] #8 people, should have 2 groups of 4

print("groups: ", makeGroups(group1, []))
print("groups: ", makeGroups(group2, []))
print("groups: ", makeGroups(group3, []))
print("groups: ", makeGroups(group4, []))
print("groups: ", makeGroups(group5, []))

