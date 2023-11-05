child1 = {
    "name" : "Vera",
    "age" : 22
}
child2 = {
    "name" : "Mike",
    "age" : 21
}

child3 = (
    "Jacob",
    23
)

myfamily = [
     child1,
    child2,
    child3
]
name = myfamily[2]
t_change = list(name)
t_change[0] = "Daniel"
name = tuple(t_change)
myfamily[2] = name
print(myfamily)
