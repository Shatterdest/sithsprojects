from statistics import mean
import sys
import time

try:
    class_average = []
    new_line = '\n'

    def newstudent():
        name_input = input('What is the name of the student? ')
        class_input = input('What class is the student in? ')
        student = {
            "name" : name_input,
            "class" : class_input,
            "grades" : [],
            "average" : ""
    }   

        def findaverage():
            return mean(student['grades'])


        def getgrade():
            finished = False
            while finished == False:
                gradeinput = int(input("Enter a grade here: "))
                student["grades"] += [gradeinput]
                finishedinput = input('Are you finished entering grades? (yes/no, y/n) ')
                if finishedinput.lower() in ('yes', 'y'):
                    student["average"] = findaverage()
                    finished = True
                    print('Calculating Student Average... Please wait...')
                    time.sleep(1)
                    print(f'The student\'s name is {student["name"]}. The student\'s class is {student["class"]}. The student\'s grades are the following: {student["grades"]}. {new_line}The student\'s average grade is {student["average"]}.')
                    class_average.append(student["average"])
        getgrade()


    def find_class_average():
        return mean(class_average)

    continue_adding_students = True

    while continue_adding_students == True:
        newstudent()
        done = input('Are you done adding students? (yes/no, y/n) ')
        if done.lower() in ('yes', 'y'):
            continue_adding_students = False
            find_class_average()
            print('Calculating class average... Please wait...')
            time.sleep(1.5)
            print(f'The class average is {find_class_average()}. Thank you for using the Class Gradebook Program!')


except Exception:
    e = sys.exc_info()[1]
    print('Oops, an error occured! Please run the code again! Error: ' + e.args[0])
