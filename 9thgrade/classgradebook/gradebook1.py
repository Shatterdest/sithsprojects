from statistics import mean

def findAverage(gradeList):
    return mean(gradeList)

student = {
    "name" : "Bob",
    "class" : "9",
    "grades" : [99,78,90,56],
    "average" : ""
}

student["average"] = findAverage(student["grades"])
print(student)
