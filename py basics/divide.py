def divide(a,b):

    try:
        result=a/b
    except ZeroDivisionError:
        print("you can't divide by Zero")
    else:
        print("Result:", result)

a = int(input())
b = int(input())
divide(a,b)
