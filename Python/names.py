# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# for index, user in enumerate(students):
# 	print("{} {} - ".format(user['first_name'],user['last_name']))
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
 # students = [
 #     {'first_name':  'Michael', 'last_name' : 'Jordan'},
 #     {'first_name' : 'John', 'last_name' : 'Rosales'},
 #     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
 #     {'first_name' : 'KB', 'last_name' : 'Tonel'}
 #  ]

studentsf = ['Michael','john','mark','kb']
studentsl = ['Jordan','rosales','Guillen','Tonel']
Instructorsf['Michael', 'Martin']
Instructorsl['Choi','Puryear']
students_zip = zip(studentsf,studentsl)
Instructor_zip = zip(Instructorsf,Instructorsl)

for index, user in enumerate(users):
	print(index, user)
	if index(user) is 0:
		for  key, value  in user.items():
			print("{} {} {}".format(index,user[zip(studentsf)],user[zip(studentsl)]))