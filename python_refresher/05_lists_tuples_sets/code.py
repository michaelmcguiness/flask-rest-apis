l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
# main difference: tuple is immutable
s = {"Bob", "Rolf", "Anne"}
# sets don't have duplicates (also don't keep order)

print(l[0])
print(t[2])

# can't do below on tuples or sets
l[0] = "Smith"
print(l[0])

# can't add or remove things from tuples
l.append("Smith")
l.remove("Smith")
print(l)

s.add("Smith")
s.add("Smith")
print(s)
