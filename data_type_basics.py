##Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values.
##Tuples can contain mixed data types.
dog = ('Bruce','cocker spaniel',19,False)
print(dog[0])
##INVALID in tuple!
#dog[2] = 22

##Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

##Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values. When you're ready, you can find more built-in dictionary methods here.
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}

print(type(53.2))

total = 35
val = "36"
print(str(total)+val)
