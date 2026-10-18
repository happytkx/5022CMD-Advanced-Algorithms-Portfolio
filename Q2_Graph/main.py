from course import Course
from graph import Graph

programming_fundamentals = Course(
    "CS101",
    "Programming Fundamentals",
    3,
    "Core"
)

computer_architecture = Course(
    "CS102",
    "Computer Architecture",
    3,
    "Core"
)

data_structures = Course(
    "CS201",
    "Data Structures",
    3,
    "Core"
)

data_mining = Course(
    "CS202",
    "Data Mining",
    3,
    "Elective"
)

advanced_algorithms = Course(
    "CS301",
    "Advanced Algorithms",
    3,
    "Core"
)

artificial_intelligence = Course(
    "CS302",
    "Artificial Intelligence",
    3,
    "Elective"
)

courses = [
    programming_fundamentals,
    computer_architecture,
    data_structures,
    data_mining,
    advanced_algorithms,
    artificial_intelligence
]

# Search course by course code and get full info
def find_course(courses, course_code):
    for course in courses:
        # Search for course from course code
        if course.course_code == course_code:
            return course

    return None

course_graph = Graph()

for course in courses:
    course_graph.addVertex(course)

course_graph.addEdge(programming_fundamentals, data_structures)
course_graph.addEdge(programming_fundamentals, data_mining)

course_graph.addEdge(computer_architecture, advanced_algorithms)
course_graph.addEdge(data_structures, advanced_algorithms)

course_graph.addEdge(advanced_algorithms, artificial_intelligence)

choice = ""

# Continue displaying the menu until the user selects "5"
while choice != "5":
    print("\n~~~~~~~~ Course Prerequisite System ~~~~~~~~")
    print("1. Display All Courses")
    print("2. View Course Details")
    print("3. View Course Prerequisites")
    print("4. View Courses Unlocked")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    # 1. Display All Courses
    if choice == "1":
        print("\n============== All Courses ==============")

        for course in courses:
            print(course.course_code, "-", course.course_name)

    elif choice == "2":

        course_code = input("Enter Course Code: ").strip().upper()

        print("\n============= Course Details =============")

        selected_course = find_course(courses, course_code)

        if selected_course is not None:
            print("Course Code:", selected_course.course_code)
            print("Course Name:", selected_course.course_name)
            print("Credit Hours:", selected_course.credit_hours)
            print("Level:", selected_course.level)

        else:
            print("Course not found.")

    elif choice == "3":
        course_code = input("Enter Course Code: ").strip().upper()

        print("\n=========== Course Prerequisites ===========")

        selected_course = find_course(courses, course_code)

        if selected_course is not None:
            prerequisites = course_graph.listIncomingAdjacentVertex(selected_course)

            if len(prerequisites) > 0:
                print("Prerequisites for", selected_course.course_name + ":")

                for course in prerequisites:
                    print(course.course_code, "-", course.course_name)

            else:
                print("\n", selected_course.course_name, "has no prerequisites.")

        else:
            print("Course not found.")

    elif choice == "4":

        course_code = input("Enter Course Code: ").strip().upper()

        print("\n=========== Courses Unlocked ===========")

        selected_course = find_course(courses, course_code)

        if selected_course is not None:
            unlocked_courses = course_graph.listOutgoingAdjacentVertex(selected_course)

            if len(unlocked_courses) > 0:
                print("Courses unlocked by", selected_course.course_name + ":")

                for course in unlocked_courses:
                    print(course.course_code, "-", course.course_name)

            else:
                print("\n" + selected_course.course_name + " does not unlock any courses.")

        else:
            print("Course not found.")

    elif choice == "5":
        print("\nExiting Course Prerequisite System...")

    else:
        print("\nInvalid choice. Try again.")