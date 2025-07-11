from marks import grade,validate
name=input("Enter your name:")
marks=list(map(int,input("Enter marks:").split()))
tot=sum(marks)
avg=tot/len(marks)
print("Student:",name)
print("Marks",marks)
print("Average:",avg)
print(grade(avg))