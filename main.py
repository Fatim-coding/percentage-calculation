# take makes as input from user
print("Enter marks obtained in 4 subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
socialandenvironmentalstudies = int(input("social and environmental studies:"))

# let's calculate the precentage of marks
sum = math+english+science+socialandenvironmentalstudies
print("sum of math,english,science and socialanenvironmental studies")

perc = (sum/400)*100

print(end="percentage mark = ")
print(perc)
