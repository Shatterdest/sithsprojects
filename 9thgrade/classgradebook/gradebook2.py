from statistics import mean
import sys
import time

try:
    classAverage = []
    newLine = '\n'

    def findAverage(gradeList):
        return mean(gradeList)

    def newStudent():
        nameInput = input('What is the name of the student? ')
        classInput = input('What class is the student in? ')
        student = {
            "name" : nameInput,
            "class" : classInput,
            "grades" : [],
            "average" : ""
    }   
        def getGrade():
            finished = False
            while finished == False:
                gradeInput = int(input("Enter a grade here: "))
                student["grades"] += [gradeInput]
                finishedInput = input('Are you finished entering grades? (yes/no, y/n) ')
                if finishedInput.lower() in ('yes', 'y'):
                    student["average"] = findAverage(student["grades"])
                    finished = True
                    print('Calculating Student Average... Please wait...')
                    time.sleep(1)
                    studentGrades = ', '.join(map(str, student["grades"]))
                    print(f'The student\'s name is {student["name"]}. The student\'s class is {student["class"]}. The student\'s grades are the following: {studentGrades}. {newLine}The student\'s average grade is {student["average"]}.')
                    classAverage.append(student["average"])
        getGrade()

    continueAddingStudents = True

    while continueAddingStudents == True:
        newStudent()
        done = input('Are you done adding students? (yes/no, y/n) ')
        if done.lower() in ('yes', 'y'):
            continueAddingStudents = False
            studentAverages = ', '.join(map(str, classAverage))
            print('Calculating class average... Please wait...')
            time.sleep(1.5)
            print(f'The list of student averages are {studentAverages}. The class average is {findAverage(classAverage)}. Thank you for using the Class Gradebook Program!')


except Exception:
    e = sys.exc_info()[1]
    print('Oops, an error occured! Please run the code again! Error: ' + e.args[0])
