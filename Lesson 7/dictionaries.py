# Dictionaries
# They are similar to JS' Objects
band = {"vocals": "Plant", "guitar": "Page"}
band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)

# You can access the Key-Value pair via:
print(band["guitar"])  # Output: Page
print(band.get("guitar"))  # Output: Page

# List all Keys
print(band.keys())

# List all Values
print(band.values())

# List the Key-Value pair as Tuples
print(band.items())

# Verify if a Key exists
print("guitar" in band)
print("kekw" in band)

# Change Values
band["guitar"] = "Slash"
print(band)

band.update({"bass": "Flea"})  # You can add another Key-Value pair in the Dict..
print(band)

# Remove Items
band.pop(
    "guitar"
)  # Removes the specific Key-Value pair in the Dict.. REMINDER: POP METHOD HERE IS DIFF. FROM LISTS..
print(band)

band["drums"] = "Wooky"
print(band)

band.popitem()  # This is SIMILAR to the POP METHOD in LISTS
print(band)

# Copy Dictionaries

# band = band2 # DO NOT DO THIS.. THIS CREATES A REFERENCE.. BAD COPY

print(band2)
band2 = band.copy()  # Correct way of COPYING DICTIONARIES
print(band2)

band3 = dict(band)  # ..Or use this..
print(band3)

print("")

# Nested Dictionaries
member1 = {"name": "Plant", "instrument": "vocals"}
member2 = {"name": "Page", "instrument": "guitar"}
member3 = dict(name="JPJ", instrument="bass")
member4 = dict(name="Bonham", instrument="drums")

band = {
    "member1": member1,
    "member2": member2,
    "member3": member3,
    "member4": member4,
}

print(band)
print(band.get("member1"))
print(band.get("member2"))
print(band.get("member3"))
print(band.get("member4"))
print(band.get("member1")["name"])
print(band.get("member2")["name"])
print(band.get("member3")["name"])
print(band.get("member4")["name"])
