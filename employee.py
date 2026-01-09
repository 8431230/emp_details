# Program to calculate employee performance appraisal

def calculate_average(p1, p2, p3):
    return (p1 + p2 + p3) / 3


def assign_appraisal_status(avg):
    if avg >= 90:
        return "Eligible for Promotion"
    elif avg >= 80:
        return "Exceeds Expectations"
    elif avg >= 65:
        return "Meets Expectations"
    elif avg >= 50:
        return "Needs Improvement"
    elif avg >= 40:
        return "Performance Warning"
    else:
        return "Subject to Training / Review"


if __name__ == "__main__":
    import sys
    print("=== Employee Performance Appraisal System ===")

    try:
        # If user gives input through command line
        if len(sys.argv) == 7:
            name = sys.argv[1]
            department = sys.argv[2]
            designation = sys.argv[3]
            p1 = float(sys.argv[4])
            p2 = float(sys.argv[5])
            p3 = float(sys.argv[6])
        else:
            # Take user input
            name = input("Enter Employee Name: ")
            department = input("Enter Department: ")
            designation = input("Enter Designation: ")
            p1 = float(input("Enter performance score 1: "))
            p2 = float(input("Enter performance score 2: "))
            p3 = float(input("Enter performance score 3: "))

        print("\n=== Program Parameters ===")
        print(f"Employee Name : {name}")
        print(f"Department    : {department}")
        print(f"Designation   : {designation}")
        print(f"Scores        : {p1}, {p2}, {p3}")

        average = calculate_average(p1, p2, p3)
        status = assign_appraisal_status(average)

        print(f"\nAverage Score     = {average:.2f}")
        print(f"Appraisal Status  = {status}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
