def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def main():
    print("--------------------")
    student_name = input("Enter Student Name: ")
    roll_no = input("Enter Roll No.: ")
    maths_marks = int(input("Enter marks in Maths: "))
    physics_marks = int(input("Enter marks in Physics: "))
    chemistry_marks = int(input("Enter marks in Chemistry: "))
    print("---------------------")
    
    grade_maths = calculate_grade(maths_marks)
    grade_physics = calculate_grade(physics_marks)
    grade_chemistry = calculate_grade(chemistry_marks)
    
    overall_score = (maths_marks + physics_marks + chemistry_marks) / 3
    overall_grade = calculate_grade(overall_score)
    
    print("Here is the Grade Card:")
    print("--------------------")
    print(f"Student Name: {student_name}")
    print(f"Student Roll: {roll_no}")
    print(f"Grade in Maths: {grade_maths}")
    print(f"Grade in Physics: {grade_physics}")
    print(f"Grade in Chemistry: {grade_chemistry}")
    print(f"Overall Grade: {overall_grade}")
    print("--------------------")
    print("Thank you!")

if __name__ == "__main__":
    main()