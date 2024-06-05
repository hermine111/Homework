#2) Change value of a key in a nested dictionary
#sample_dict = {
#'emp1': {'name': 'Jhon', 'salary': 7500},
#'emp2': {'name': 'Emma', 'salary': 8000},
#''emp3': {'name': 'Brad', 'salary': 500}
#}




diction = {
"emp1":{"name":  "John", "salary": 7500},
"emp2":{"name": "Jill", "salary": 800},
"emp3":{"name": "Jim", "salary": 500}
}

diction["emp1"]["salary"] = 200
print(diction)