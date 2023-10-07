users = ["Bunso", "Alianna", "Strok", "Tonky"]
emptyList = []
print(users)

# print("Bunso" in users)
# print(users.index("Bunso"))

users.append("Ponky")
print(users)

users.extend(["Tjoeki", "Oreo"])
print(users)

users.insert(0, "Duryan")  # You can specify which index to put the element
print(users)

users.remove("Duryan")
print(users)

users.pop()  # Removes the last element in the list
print(users)

del users[0]  # Deletes the element in the specified index of the list
print(users)

users.insert(0, "Bunso")
print(users)

print(emptyList)
# del emptyList  # Deletes the list totally
# print(emptyList)
emptyList.append("Kekw")
print(emptyList)
emptyList.extend(["Lmao", "Fr"])
print(emptyList)

emptyList.clear()
print(emptyList)

users.sort()  # Sorts the elements alphabetically (If Strings...)
print(users)

test_kekw = "Kekw,Lmao,fr"
print(test_kekw.split(",")[-1].capitalize())

nums = [1, 4, 2, 3]
print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)

usersCopy = list(users)  # Creates a copy of users
usersCopy.reverse()
print(users)
print(usersCopy)
