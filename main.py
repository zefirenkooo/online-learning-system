def show_courses():
    return ["English", "Spanish", "Japanese"]

if __name__ == "__main__":
    print("Online Language Learning System")
    courses = show_courses()
    print("Available Language Courses:")
    for course in courses:
        print(f"- {course}")