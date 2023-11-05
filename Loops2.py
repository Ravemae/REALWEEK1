# i = 1
# while i < 6:
#     print(i)

#     i += 1

#     i = 1
# i =  1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# Fruits = ["Apple", "Banana", "Cherry"]

# for x in Fruits: 
#     print("I love "+x)

# for x in range(6):
#     print(x)

# for x in range(6 + 1):
#     print(x)

# for x in range(1 , 6):
#     print(x)

# adj = ["red", "big", "tasty"]
# Fruits = ["Apple", "Banana", "Cherry"]

# for x in adj:
#     for y in Fruits: 
#         print(x, y)

# students = {
#     "name": "Mike",
#     "age": 23,
#     "color": "black"
# }

# for x in students:
#     print(x , students[x])


student_scores ={
    "Harry": 81,
    "Ron":  78,
    "Hermonie": 99,
    "Draco": 74,
    "Neville": 62,
}

students_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        students_grades[student] = "Excellent"
    elif  score > 80:
        students_grades[student] = "Acceptable"
    elif score > 70:
        students_grades[student] = "Average"
    elif  score > 60:
        students_grades[student] = "failed"
    
print(students_grades)

    