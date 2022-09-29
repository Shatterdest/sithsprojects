from statistics import mean

def findaverage():
    return mean(student['grades'])

student = {
    "name" : "Bob",
    "class" : "9",
    "grades" : [99,78,90,56],
    "average" : ""
}

student["average"] = findaverage()
print(student)
