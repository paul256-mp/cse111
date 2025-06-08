def check_student(student_dict,):
    """
    Check if the student object has the required attributes.
    """
    assert hasattr(student, 'name'), "Student object must have a 'name' attribute"
    assert hasattr(student, 'age'), "Student object must have an 'age' attribute"
    assert hasattr(student, 'grade'), "Student object must have a 'grade' attribute"