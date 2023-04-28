# person = {"location":"Nairobi", "Countries": ["Kenya","Turkey"]}
# person["age"] = 20
# print(person["Countries"][-1])
# print("Country" in person.keys())
# print(person.values())
# print(person.items())
# # print(person)

# thisdict = {"name" :"John", "age": 36, "country" :"Kenya"}
# thisdict["City"] = "Nairobi"
# print(thisdict)
# print("age" in thisdict.keys())
# print("Kenya" in thisdict.values())
# print(thisdict.values())
# print(thisdict.items())
# print(thisdict["country"])
# print(thisdict["age"])
# print(thisdict["name"])
# print(type(thisdict))
# print(len(thisdict))




#taskList = [23, “Jane”, [“Lesson 23”, 560, {“currency” : “KES”}], 987, (76,”John”)]

# taskList = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John"), "Jane"]

# 1. Determining class of taskList using an inbuilt function
# 2. Print KES
# 3. Print 560
# 4. Use a function to determine the length of taskList
# 5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
# For number 5 above we can research the solution online
# 6. Change the name “John” to “Jane” . 
# 7. In the dictionary with the key currency, add another key “amount” with value 90

# print(type(taskList)) .................ans: <class 'list'> quiz 1
# print(taskList[2][2]["currency"])    ...........ans: quiz 2
# print("KES" in taskList.values[2][3])
# print(taskList[2][1]) ..................ans: 560   quiz 3
# print(len(taskList)) ...............ans: 5 quiz 4
# taskList[3] = int(str(taskList[3])[::-1]) .............ans: quiz 5

# taskList[4] = list(taskList[4])
# taskList[4][1] = "Jane"
# taskList[4] = tuple(taskList[4])
# print(taskList[4]) .................ans: (76, 'Jane')   quiz 6

# taskList[2][2]["amount"] = 90 
# print(taskList)

ls1 = ["Mombasa", ["Kitale", ("Eldoret", "Fill"), ("Nakuru")]]
ls1[1][1] = list(ls1[1][1])
ls1[1][1][1] = "Machakos"
ls1[1][1] = tuple(ls1[1][1])

print(ls1)

 
