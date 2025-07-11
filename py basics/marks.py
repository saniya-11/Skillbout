def grade(avg):
    if avg>=90:
        return "A+"
    elif avg>=80:
        return "A"
    elif avg>=70:
        return "B"
    elif avg>=60:
        return "C"
    elif avg>=55:
        return "D"
    else:
        return "F"


def validate(marks):
    for mark in marks:
        if mark < 0 or mark > 100:
            return False
    return True






