# Sets and Frozen sets

# Sets are unordered
# Create a set

car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)

# Remove parts of a set
car_parts.discard("doors")
print(car_parts)

# Add parts to a set
car_parts.add("Windows")
print(car_parts)

# Frozen sets

x = frozenset([1, 2, 3, 4, "Five"])
print(x)