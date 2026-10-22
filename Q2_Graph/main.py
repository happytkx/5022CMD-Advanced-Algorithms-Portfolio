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

# Finds and returns Course object using its course code
def find_course(course_list, target_code):
    for current_course in course_list:
        # Search for course from course code
        if current_course.course_code == target_code:
            return current_course

    return None

course_graph = Graph()

# Add each Course object as a vertex in the graph
for course in courses:
    course_graph.addVertex(course)

# Edge direction: prerequisite -> course that it unlocks
course_graph.addEdge(programming_fundamentals, data_structures)
course_graph.addEdge(programming_fundamentals, data_mining)

course_graph.addEdge(computer_architecture, advanced_algorithms)
course_graph.addEdge(data_structures, advanced_algorithms)

course_graph.addEdge(advanced_algorithms, artificial_intelligence)

choice = ""

# Continue displaying the menu until the user selects "6"
while choice != "6":
    print("\n~~~~~~~~ Course Prerequisite System ~~~~~~~~")
    print("1. Display All Courses")
    print("2. View Course Details")
    print("3. View Course Prerequisites")
    print("4. View Courses Unlocked")
    print("5. Add Course Prerequisite")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    # 1. Display All Courses
    if choice == "1":
        print("\n============== All Courses ==============")

        for course in courses:
            print(course.course_code, "-", course.course_name)

    # 2. View Course Details
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

    # 3. View Course Prerequisites
    elif choice == "3":
        course_code = input("Enter Course Code: ").strip().upper()

        print("\n=========== Course Prerequisites ===========")

        selected_course = find_course(courses, course_code)

        if selected_course is not None:
            # Get all vertices that point to the selected course
            # Incoming vertices represent its prerequisites
            prerequisites = course_graph.listIncomingAdjacentVertex(selected_course)

            if len(prerequisites) > 0:
                print("Prerequisites for", selected_course.course_name + ":")

                for course in prerequisites:
                    print(course.course_code, "-", course.course_name)

            else:
                print("\n" + selected_course.course_name + " has no prerequisites.")

        else:
            print("Course not found.")

    # 4. View Courses Unlocked
    elif choice == "4":

        course_code = input("Enter Course Code: ").strip().upper()

        print("\n=========== Courses Unlocked ===========")

        selected_course = find_course(courses, course_code)

        if selected_course is not None:
            # Get all vertices that the selected course points to
            # Outgoing vertices represent courses it unlocks
            unlocked_courses = course_graph.listOutgoingAdjacentVertex(selected_course)

            if len(unlocked_courses) > 0:
                print("Courses unlocked by", selected_course.course_name + ":")

                for course in unlocked_courses:
                    print(course.course_code, "-", course.course_name)

            else:
                print("\n" + selected_course.course_name + " does not unlock any courses.")

        else:
            print("Course not found.")

    # 5. Add Course Prerequisite
    elif choice == "5":
        print("\n============== Add Prerequisite =============")

        prerequisite_code = input("Enter prerequisite course code: ").strip().upper()

        course_code = input("Enter course code that requires this prerequisite: ").strip().upper()

        # Convert the entered course codes into Course objects
        prerequisite_course = find_course(courses, prerequisite_code)
        selected_course = find_course(courses, course_code)

        # Continues only when both course codes exist
        if prerequisite_course is not None and selected_course is not None:

            # Get courses that already have an outgoing edge from the proposed prerequisite course
            existing_courses = course_graph.listOutgoingAdjacentVertex(prerequisite_course)

            # Prevent a course from being its own prerequisite
            if prerequisite_course == selected_course:
                print("A course cannot be its own prerequisite.")

            # Prevent the same directed edge from being added twice
            elif selected_course in existing_courses:
                print(prerequisite_course.course_name,
                      "is already a prerequisite for",
                      selected_course.course_name + ".")

            # Check the reverse direction before adding the new edge.
            elif course_graph.hasPath(selected_course, prerequisite_course):
                print("Cannot add this prerequisite because it would make",
                      prerequisite_course.course_name,
                      "and", selected_course.course_name, "depend on each other.")

            else:
                # Add prerequisite_course -> selected_course
                course_graph.addEdge(prerequisite_course, selected_course)

                print(prerequisite_course.course_name,
                      "has been added as a prerequisite for",
                      selected_course.course_name + ".")

        else:
            print("One or both course codes were not found.")

    # 6. Exit
    elif choice == "6":
        print("\nExiting Course Prerequisite System...")

    else:
        print("\nInvalid choice. Try again.")