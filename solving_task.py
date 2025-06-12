# def welcome_message():
#     name = input ("what is your name ?\n")
#     print(f"Welcome {name}")

# welcome_message()


stu_data = [
    "Ali,20,C++,HTML",
    "Sara,22,Java Script,Puthon,CSS",
    "Bilal,21,Java,C++,Python",
    "Ayesha,20,Python,HTML,CSS",
]
stu_tuple = []
for val in stu_data:
    parts = val.split(",")
    name = parts[0]
    age = int(parts[1])
    courses = parts[2:]
    stu_tuple.append((name,age,courses))

print("list of tuples:\n")
for student in stu_tuple:
    print(student)
   

stu_dict = {}
for name,age,courses in stu_tuple:
    stu_dict[name]= set(courses)

print("courses inrolled by students:")
for name,courses in stu_dict.items():
    print(f"{name} : {courses}")


uni_courses = set()
for courses in stu_dict.values():
    uni_courses.update(courses)

print(f"All unique courses:\n{uni_courses}")


