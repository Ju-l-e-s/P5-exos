def display_student_grades(students:dict):
    """
    Display the grades and average of a specified student from a dictionary of students.

    :param students: A dictionary containing student names as keys and their grades as values.
    :type students: dict
    :return: None
    :rtype: None
    """
    student_name = input("Entrez le nom de l’étudiant : ")

    if student_name in students:
        print(f"Notes de {student_name} :")
        notes = students[student_name]
        for subject, grade in notes.items():
            print(f"{subject} : {grade}")
        average = sum(notes.values()) / len(notes)
        print(f"Moyenne de {student_name} : {average}")
    else:
        print(f"L'étudiant {student_name} n'existe pas dans la liste.")


# Example usage
students = {
    'Alice': {
        'Mathematiques': 90,
        'Francais': 80,
        'Histoire': 95
    },
    'Bob': {
        'Mathematiques': 75,
        'Francais': 85,
        'Histoire': 70
    },
    'Charlie': {
        'Mathematiques': 88,
        'Francais': 92,
        'Histoire': 78
    }
}

display_student_grades(students)
