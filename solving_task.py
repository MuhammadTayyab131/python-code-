# # def welcome_message():
# #     name = input ("what is your name ?\n")
# #     print(f"Welcome {name} in our code:")

# # welcome_message()


stu_data = [
    "Ali,20,C++,HTML",
    "Sara,22,Java Script,Python,CSS",
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

print("Students enrolled python:")
for name , courses in stu_dict.items():
    if "Python" in courses:
        print(f"{name}")


search_course = input("Enter a course to see enrolled students: ").strip()
enrol_stu = []
for name, courses in stu_dict.items():
    if search_course in courses:
        enrol_stu.append(name)
        
if enrol_stu:
    print(f"\nStudents enrolled in {search_course}:")
    for student in enrol_stu:
        print(student)
else:
    print(f"\nNo students found for course: {search_course}")


# Kashif Bhai's tsak


people = [
    {"name": "Shafaqat", "city": "Lahore"},
    {"name": "Abrar", "city": "Rawalpindi"},
    {"name": "Tayyab", "city": "Multan"},
    {"name": "Kaleem", "city": "Faisalabad"},
    {"name": "Numan", "city": "Sindh"},
    {"name": "Uzman", "city": "Lahore"},
    {"name": "Usman", "city": "Multan"},
    {"name": "Ali", "city": "Islamabad"},
    {"name": "Hassan", "city": "Faisalabad"},
    {"name": "Basit", "city": "Sindh"},
    {"name": "Ab. Haseeb", "city": "Multan"},
    {"name": "Ab. Tawab", "city": "Rawalpindi"},
    {"name": "Irfan", "city": "Islamabad"},
    {"name": "Farooq", "city": "Faisalabad"},
    {"name": "Rauf", "city": "K.P.K"},
    {"name": "Adeel", "city": "Lahore"},
    {"name": "Adil", "city": "Rawalpindi"},
    {"name": "Azeem", "city": "Islamabad"},
    {"name": "Atif", "city": "K.P.K"},
    {"name": "Umar", "city": "Sindh"}
]


city = input("Enter City Name: ")

count = 0

for person in people:
    if person["city"].lower() == city.lower():
        count+=1

if count:
    print(f"The number of people live in {city} are: {count}")

else:
    print(f"No people live in {city}")

names=[]

for person in people:
    if person["city"].lower() == city.lower():
        names.append(person["name"])

if names:
    print(f"peoples of {city} are:\n{", ".join(names)}")
else:
    print(f"No person in {city}")

