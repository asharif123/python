##function intermediate II
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

##Update Values in Dictionaries and Lists

##1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)
##2. Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)
##3. In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
##4. Change the value 20 in z to 30
z[0]['y'] = 30
print(z)



##Iterate Through a List of Dictionaries and print each key value
def iterateDictionary(students):
    for student in students:
        print(student.keys)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)


##Get values for a list of dictionaries
def listDictionary(key,list_of_dicts):
    for item in list_of_dicts:
        print(item[key])
        
students = [{'first_name':  'Michael', 'last_name' : 'Jordan'},{'first_name' : 'John', 'last_name' : 'Rosales'},{'first_name' : 'Mark', 'last_name' : 'Guillen'},{'first_name' : 'KB', 'last_name' : 'Tonel'}]
(listDictionary('first_name',students))
(listDictionary('last_name',students))

##Tterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key in some_dict:
        print(str(len(some_dict[key])) + ' ' + key.upper())
        for i in range(len(some_dict[key])):
            print(some_dict[key][i])
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)


