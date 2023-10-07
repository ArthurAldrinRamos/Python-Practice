# Sets
# No DUPLICATES allowed
# You cannot refer to an element in the SET with the SPECIFIC INDEX or KEY

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
nums3 = {1, 4, 4, 3}

print(nums)
print(nums2)
print(nums3)  # Sets don't recognize duplicates..

# Add a new Element to a Set
nums.add(5)
print(nums)

moreNums = set((6, 7, 8, 9, 10))
nums.update(moreNums)  # You can also use this in LISTS, TUPLES, and DICTIONARIES
print(nums)

one = set((1, 2, 3))
two = set((4, 5, 6))
mergedSets = one.union(two)  # Merged 2 SETS to create a NEW SET
print(mergedSets)

# To REMOVE DUPLICATES BETWEEN SETS
one = set((1, 3, 4))
two = set((3, 4, 6))
one.intersection_update(two)
print(one)  # Will only output the elements that have been duplicated

# To REMOVE DUPLICATES BETWEEN SETS
one = set((1, 3, 4))
two = set((3, 4, 6))
one.symmetric_difference_update(two)
print(one)
