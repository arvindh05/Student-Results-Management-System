# Arvindh Bharadwaj Venkatesan



# Documentation and reference is placed at the bottom of the file

#Importing library sys
import sys

# Creating Coruse class with coruseID,courseType, courseName, creditPoints, offeredSemesters  and formed required methods
class Course:
    def __init__(self, courseId, courseType, courseName, creditPoints, offeredSemesters):
        self.courseId = courseId
        self.courseType = courseType
        self.courseName = courseName
        self.creditPoints = creditPoints
        self.offeredSemesters = offeredSemesters

    # Function To get the courseID
    def getCourseId(self):
        return self.courseId
    
    # Function To get the courseType
    def getCourseType(self):
        return self.courseType

    # Function To get the courseName
    def getCourseName(self):
        return self.courseName

    # Function To get the CreditPoints
    def getCreditPoints(self):
        return self.creditPoints

    # Function to find out on which semester the course is offered
    def getOfferedSemesters(self):
        return self.offeredSemesters


# Creating Student class with attributes studentID, name, student_type, mode and required methods to work on it
class Student:
    def __init__(self, studentId,  name, student_type, mode):
        self.studentId = studentId
        self.name = name
        self.student_type = student_type
        self.mode = mode
        self.enrolled_courses = []

    # A function to get studentId
    def getStudentId(self):
        return self.studentId
    
    # A function to fetch student name
    def get_name(self):
        return self.name
    
    # Function to get type of the student 
    def get_student_type(self):
        return self.student_type

    # Function to get the mode
    def get_mode(self):
        return self.mode
    
    # Function to get student enrolled courses
    def get_enrolled_courses(self):
        return self.enrolled_courses

    # A function to add enrolled courses for that particular student
    def add_enrolled_course(self, course):
        self.enrolled_courses.append(course)
    
    # Function to find statistics such as average score, n_finish, n_ongoing and gpa
    def compute_statistics(self, results):
        finished_scores = []
        ongoing_count = 0
        results.enroll_students_in_courses()
        for course in results.courses:
            score = results.scores.get((self.studentId, course.courseId))
           
            if score is not None:
                if score == -1:
                    ongoing_count += 1
                elif score != '--' and score != '' :
                    finished_scores.append(float(score))


        average = sum(finished_scores) / len(finished_scores) if finished_scores else 0
        n_finish = len(finished_scores)
        n_ongoing = ongoing_count
        gpa4 = 0

        # checking the scores in this loop and assigning a gpa for that
        for i in finished_scores:
            if(i >= 79.5):
                gpa4 += 4
            elif(i >= 69.5 and i < 79.5):
                gpa4 += 3
            elif(i >= 59.5 and i < 69.5):
                gpa4 += 2
            elif(i >= 49.5 and i < 59.5):
                gpa4 += 1
            else:
                pass
        gpa4 = gpa4 / len(finished_scores) if finished_scores else 0

        return average, n_finish, n_ongoing, gpa4

# Creating Results class with courses and students list to store the data from the file and a scores dictionary to store the scores data
class Results:
    def __init__(self):
        self.courses = []
        self.students = []
        self.scores = {}
        self.student_finished = set()


    # Read courses function will open and read the courses.txt file and store the information in the courses list
    def read_courses(self, course_file_name):
        with open(course_file_name, 'r') as file:
            for line in file:
                course_data = line.strip().split(',')
                courseId = course_data[0].strip().strip(',')
                courseType = course_data[1].strip().strip(',')
                courseName = course_data[2].strip().strip(',')
                creditPoints = int(course_data[3].strip())
                if(len(course_data)>4):
                    offeredSemesters = course_data[4].strip().strip(',')
                else:
                    offeredSemesters = 'All'
                course = Course(courseId,courseType, courseName, creditPoints, offeredSemesters)
                self.courses.append(course)


    # Read students function will open and read the students.txt file and store the information in the students list
    def read_students(self, student_file_name):
        with open(student_file_name, 'r') as file:
            for line in file:
                student_info = line.strip().strip(',').split(',')
                student_id = student_info[0].strip()
                name = student_info[1].strip()
                student_type = student_info[2].strip()
                if( len(student_info)>3 ):
                    mode = student_info[3].strip()
                else:
                    mode = 'FT'
                student = Student(student_id, name, student_type, mode)
                self.students.append(student)

    # Read results function will open and read the results.txt file and store the information in the score dictionary
    def read_results(self, result_file_name):
        with open(result_file_name, 'r') as file:
            for line in file:
                result_data = line.strip().split(", ")
                student_id = result_data[0]
                course_id = result_data[1].strip(',')
                score = float(result_data[2]) if len(result_data) > 2 and result_data[2] else -1

                self.scores[(student_id, course_id)] = score

    # Function to enroll students in the courses
    def enroll_students_in_courses(self):
        for student in self.students:
            for course in self.courses:
                if student.get_student_type() == 'UG' and len(student.get_enrolled_courses()) >= 4:
                    break
                elif student.get_student_type() == 'PG' and student.get_mode() == 'FT' and len(student.get_enrolled_courses()) >= 4:
                    break
                elif student.get_student_type() == 'PG' and student.get_mode() == 'PT' and len(student.get_enrolled_courses()) >= 2:
                    break
                student.add_enrolled_course(course)

    # This display results function will display each students marks in their respective subjects and will calculate the average pass rate percentage
    def display_results(self):
        # Checks if either the self.courses or self.students is empty or contains no data.
        if not self.courses or not self.students:
            print("No courses or students data available.")

        print()
        print("RESULTS")

        # Header row
        header = ["Student IDs"] + [course.courseId for course in self.courses]
        print("-" * (12 + 8 * len(header)))
        print('{:<12}'.format(header[0]), end='')
        # For loop to print the results table 
        for col in header[1:]:
            print('{:>8}'.format(col), end='')
        print()
        print("-" * (12 + 8 * len(header)))
        for student in self.students:
            print('{:<12}'.format(student.studentId), end='')
            for course in self.courses:
                if (student.studentId, course.courseId) in self.scores:
                    score = self.scores[(student.studentId, course.courseId)]
                    if score is not None and score >= 0:
                        print('{:>8.1f}'.format(score), end='')
                    else:
                        print('{:>8}'.format("--"), end='')
                else:
                    print('{:>8}'.format(' '), end='')
            print()

        print()
        total_students = len(self.students)
        total_courses = len(self.courses)
        total_scores = len([score for score in self.scores.values() if score is not None and score >= 0])
        pass_scores = sum(score >= 49.5 for score in self.scores.values() if score is not None)
        pass_rate = (pass_scores / total_scores) * 100 if total_scores > 0 else 0

        print("RESULTS SUMMARY")
        print("There are {} students and {} courses.".format(total_students, total_courses))
        print("The average pass rate is {:.2f}%.".format(pass_rate))
        print()

    # This function will display course information on the screen like courseID, name, type, credit, semester, Average, Nfinish and Nongoing
    # and will store these results in the reports.txt file
    def display_course_information(self):
        # Checking core courses ans storing it in the list
        core_courses = [course for course in self.courses if course.getCourseType() == "C"]
        # Checking elective courses and storing it in the list
        elective_courses = [course for course in self.courses if course.getCourseType() == "E"]

        # Writing the data in reports.txt file
        with open('reports.txt', 'w') as file:
            file.write("COURSE INFORMATION\n")
            file.write("-" * 106)
            file.write("\n{:<15}{:<15}{:<20}{:<12}{:<12}{:<12}{:<12}{:<12}".format("CourseID", "Name", "Type", "Credit", "Semester", "Average","Nfinish","Nongoing\n"))
            file.write("-" * 106)

            print("COURSE INFORMATION")
            print("-" * 106)
            print("{:<15}{:<15}{:<20}{:<12}{:<12}{:<12}{:<12}{:<12}".format("CourseID", "Name", "Type", "Credit", "Semester", "Average","Nfinish","Nongoing"))
            print("-" * 106)

            # Display core courses
            min_average_elective = 100
            min_average_core = 100
            most_dif_core_subject = ''
            most_dif_elective_subject = ''

            # Finding n_finish, n_ongoing, average score of the student along with finding the most difficult core and elective courses.
            for course in core_courses:

                # Finding n_finish
                n_finish = sum(1 for (student_id, course_id) in self.scores.keys() if self.scores[(student_id, course_id)] is not None and 
                            self.scores[(student_id, course_id)] >= 0 and  course_id == course.getCourseId())

                i = 0
                for student_id, course_id in self.scores.keys():
                    if course_id.strip(',') == course.getCourseId():
                        i += 1
                # Finding n_ongoing
                n_ongoing = i - n_finish

                # Finding average score
                avg_score = sum(self.scores[(student_id, course_id)] for (student_id, course_id) in self.scores.keys() if self.scores[(student_id, course_id)] is not None and 
                            self.scores[(student_id, course_id)] >= 0 and  course_id == course.getCourseId())
                avg_score_2 = avg_score / n_finish if n_finish > 0 else 0.0

                if min_average_core > avg_score_2:
                    min_average_core = avg_score_2
                    most_dif_core_subject = course.getCourseId()

                file.write("\n{:<15}{:<15}{:<20}{:<12}{:<12}{:<12.2f}{:<12}{:<12}".format(course.getCourseId(), course.getCourseName(),
                                                                        "C", course.getCreditPoints(), "All",
                                                                        avg_score_2,n_finish, n_ongoing))

                print("{:<15}{:<15}{:<20}{:<12}{:<12}{:<12.2f}{:<12}{:<12}".format(course.getCourseId(), course.getCourseName(),
                                                                        "C", course.getCreditPoints(), "All",
                                                                        avg_score_2,n_finish, n_ongoing))


            # Display elective courses
            file.write('\n')
            file.write("-" * 106)
            file.write("\n{:<15}{:<15}{:<20}{:<12}{:<12}{:<12}{:<12}{:<12}".format("CourseID", "Name", "Type", "Credit", "Semester", "Average","Nfinish","Nongoing\n"))
            file.write("-" * 106)
            file.write('\n')
            
            print()
            print("-" * 106)
            print("{:<15}{:<15}{:<20}{:<12}{:<12}{:<12}{:<12}{:<12}".format("CourseID", "Name", "Type", "Credit", "Semester", "Average","Nfinish","Nongoing"))
            print("-" * 106)
            # Finding n_finish,n_ongoing and average sore for the elective courses 
            for course in elective_courses:
                
                n_finish = sum(1 for (student_id, course_id) in self.scores.keys() if self.scores[(student_id, course_id)] is not None and 
                            self.scores[(student_id, course_id)] >= 0 and  course_id == course.getCourseId())

                i = 0
                for student_id, course_id in self.scores.keys():
                    if course_id.strip(',') == course.getCourseId():
                        i += 1
                n_ongoing = i - n_finish

                avg_score = sum(self.scores[(student_id, course_id)] for (student_id, course_id) in self.scores.keys() if self.scores[(student_id, course_id)] is not None and 
                            self.scores[(student_id, course_id)] >= 0 and  course_id == course.getCourseId())
                avg_score_2 = avg_score / n_finish if n_finish > 0 else 0.0


                if min_average_elective > avg_score_2:
                    min_average_elective = avg_score_2
                    most_dif_elective_subject = course.getCourseId()

                file.write("{:<15}{:<15}{:<20}{:<12}{:<12}{:<12.2f}{:<12}{:<12}\n".format(course.getCourseId(), course.getCourseName(),
                                                                        "E", course.getCreditPoints(),
                                                                        course.getOfferedSemesters(), avg_score_2, n_finish, n_ongoing))

                print("{:<15}{:<15}{:<20}{:<12}{:<12}{:<12.2f}{:<12}{:<12}".format(course.getCourseId(), course.getCourseName(),
                                                                        "E", course.getCreditPoints(),
                                                                        course.getOfferedSemesters(), avg_score_2, n_finish, n_ongoing))

            
            file.write('\n')
            file.write('\nCOURSE SUMMARY\n')
            file.write(f'The most difficult core course is {most_dif_core_subject} with an average score of {min_average_core:.2f}.\n')
            file.write(f'The most difficult elective course is {most_dif_elective_subject} with an average score of {min_average_elective:.2f}.\n')
            

            print()
            print('COURSE SUMMARY')
            print(f'The most difficult core course is {most_dif_core_subject} with an average score of {min_average_core:.2f}.')
            print(f'The most difficult elective course is {most_dif_elective_subject} with an average score of {min_average_elective:.2f}.')

    
    # Function to display student information like type (PG,UG) and whats their GPA score and how many courses they finished(Nfinish) and Nongoing
    def display_student_information(self, results):
            self.results = results
            self.enroll_students_in_courses()

            # Storing the student information  in the reports.txt file
            with open('reports.txt', 'a') as file:
                file.write("\nSTUDENT INFORMATION \n")
                file.write("POSTGRADUATE STUDENTS\n")
                file.write("-" * 110 + '\n')
                file.write(f"{'Student ID':<15} {'Name':<15} {'Type':>10} {'Mode':>10} {'GPA(100)':>15} {'GPA(4)':>10} {'Nfinish':>10} {'Nongoing':>10}\n")
                file.write("-" * 110 )

                print("\nSTUDENT INFORMATION")
                print("POSTGRADUATE STUDENTS")
                print("-" * 110 )
                print(f"{'Student ID':<15} {'Name':<15} {'Type':>10} {'Mode':>10} {'GPA(100)':>15} {'GPA(4)':>10} {'Nfinish':>10} {'Nongoing':>10}")
                print("-" * 110 )

                # finding the information for that particular student like type, mode, GPA, Nfinish and Nongoing and displaying the results
                for student in self.students:
                    enrolled_courses = student.get_enrolled_courses()
                    if student.get_student_type() == 'PG':
                        num_courses = len(enrolled_courses)
                        if student.get_mode() == 'FT' and student.compute_statistics(self.results)[1] + student.compute_statistics(self.results)[2] < 4:
                            student_name = f"{student.get_name()} (!)"
                            print(f"{student.getStudentId():<15} {student_name:<15} {student.get_student_type():>10} {student.get_mode():>10} {student.compute_statistics(self.results)[0]:>15.2f} {student.compute_statistics(self.results)[3]:>10.2f} {student.compute_statistics(self.results)[1]:>10} {student.compute_statistics(self.results)[2]:>10}")
                            file.write(f"\n{student.getStudentId():<15} {student_name:<15} {student.get_student_type():>10} {student.get_mode():>10} {student.compute_statistics(self.results)[0]:>15.2f} {student.compute_statistics(self.results)[3]:>10.2f} {student.compute_statistics(self.results)[1]:>10} {student.compute_statistics(self.results)[2]:>10}")
                        elif student.get_mode() == 'PT' and student.compute_statistics(self.results)[1] + student.compute_statistics(self.results)[2] < 2:
                            student_name = f"{student.get_name()} (!)"
                            print(f"{student.getStudentId():<15} {student_name:<15} {student.get_student_type():>10} {student.get_mode():>10} {student.compute_statistics(self.results)[0]:>15.2f} {student.compute_statistics(self.results)[3]:>10.2f} {student.compute_statistics(self.results)[1]:>10} {student.compute_statistics(self.results)[2]:>10}")

                            file.write(f"\n{student.getStudentId():<15} {student_name:<15} {student.get_student_type():>10} {student.get_mode():>10} {student.compute_statistics(self.results)[0]:>15.2f} {student.compute_statistics(self.results)[3]:>10.2f} {student.compute_statistics(self.results)[1]:>10} {student.compute_statistics(self.results)[2]:>10}")
                        else:
                            print(f"{student.getStudentId():<15} {student.get_name():<15} {student.get_student_type():>10} {student.get_mode():>10} {student.compute_statistics(self.results)[0]:>15.2f} {student.compute_statistics(self.results)[3]:>10.2f} {student.compute_statistics(self.results)[1]:>10} {student.compute_statistics(self.results)[2]:>10}")
                            file.write(f"\n{student.getStudentId():<15} {student.get_name():<15} {student.get_student_type():>10} {student.get_mode():>10} {student.compute_statistics(self.results)[0]:>15.2f} {student.compute_statistics(self.results)[3]:>10.2f} {student.compute_statistics(self.results)[1]:>10} {student.compute_statistics(self.results)[2]:>10}")

                    
                # Storing the undergraduate students information in the file
                file.write('\n')
                file.write("\nUNDERGRADUATE STUDENTS\n")    
                file.write("-" * 110 + "\n")
                file.write(f"{'Student ID':<15} {'Name':<15} {'Type':>10} {'Mode':>10} {'GPA(100)':>15} {'GPA(4)':>10} {'Nfinish':>10} {'Nongoing':>10}\n")
                file.write("-" * 110 )

            

            

                print("\nUNDERGRADUATE STUDENTS")
                print("-" * 110 )
                print(f"{'Student ID':<15} {'Name':<15} {'Type':>10} {'Mode':>10} {'GPA(100)':>15} {'GPA(4)':>10} {'Nfinish':>10} {'Nongoing':>10}")
                print("-" * 110 )
                for student in self.students:
                    enrolled_courses = student.get_enrolled_courses()
                    if student.get_student_type() == 'UG':
                        if (student.compute_statistics(self.results)[1] + student.compute_statistics(self.results)[2] < 4):
                            student_name = f"{student.get_name()} (!)"
                            print(f"{student.getStudentId():<15} {student_name:<15} {student.get_student_type():>10} {student.get_mode():>10} {student.compute_statistics(self.results)[0]:>15.2f} {student.compute_statistics(self.results)[3]:>10.2f} {student.compute_statistics(self.results)[1]:>10} {student.compute_statistics(self.results)[2]:>10}")
                            file.write(f"\n{student.getStudentId():<15} {student_name:<15} {student.get_student_type():>10} {student.get_mode():>10} {student.compute_statistics(self.results)[0]:>15.2f} {student.compute_statistics(self.results)[3]:>10.2f} {student.compute_statistics(self.results)[1]:>10} {student.compute_statistics(self.results)[2]:>10}")

                        else:
                            print(f"{student.getStudentId():<15} {student.get_name():<15} {student.get_student_type():>10} {student.get_mode():>10} {student.compute_statistics(self.results)[0]:>15.2f} {student.compute_statistics(self.results)[3]:>10.2f} {student.compute_statistics(self.results)[1]:>10} {student.compute_statistics(self.results)[2]:>10}")
                            file.write(f"\n{student.getStudentId():<15} {student.get_name():<15} {student.get_student_type():>10} {student.get_mode():>10} {student.compute_statistics(self.results)[0]:>15.2f} {student.compute_statistics(self.results)[3]:>10.2f} {student.compute_statistics(self.results)[1]:>10} {student.compute_statistics(self.results)[2]:>10}")



    # Function to find the best students in UG and PG and display their results and storing this in the reports.txt file
    def display_best_student(self):
        max_PG_score = 0
        max_UG_score = 0
        max_PG_student =''
        max_UG_student = ''
        with open('reports.txt', 'a') as file:           
           
           # For loop to find the hightest score of the PG student and storing it in max_PG_score varible
            for student in self.students:
                # Checking if the student is a PG or UG student
                if(student.get_student_type() == 'PG'):
                    gpa = student.compute_statistics(self.results)[3]
                    if(max_PG_score < gpa):
                        max_PG_score = gpa
                        max_PG_student = student.getStudentId()
                   
                else:
                    gpa_ug = student.compute_statistics(self.results)[3]
                    if(max_UG_score < gpa_ug):
                        max_UG_score = gpa_ug
                        max_UG_student = student.getStudentId()
                   
            # Pring the best UG and PG student ID and their score       
            print("\nSTUDENT SUMMARY")
            print(f"The best PG student is {max_PG_student} with a score of {max_PG_score:.2f}.")
            print(f"The best UG student is {max_UG_student} with a score of {max_UG_score:.2f}.")      

            file.write('\n')
            file.write("\nSTUDENT SUMMARY\n")
            file.write(f"The best PG student is {max_PG_student} with a score of {max_PG_score:.2f}.\n")
            file.write(f"The best UG student is {max_UG_student} with a score of {max_UG_score:.2f}.\n")

# Main function this will run first and get the 3 files from command line and call all the required methods for processing and displaying the results
def main():
    # Checking if the user gave 3 file inputs, otherwise tell them its a wrong input
    if len(sys.argv) != 4:
         print("Incorrect number of data files. Usage: python program.py result_file course_file student_file")
         return

    result_file = sys.argv[1]
    course_file = sys.argv[2]
    student_file = sys.argv[3]

    # Creating an object for the results class
    results = Results()

    # Calling read_courses method in results class and passing the courses.txt file as input
    results.read_courses(course_file)
    # Calling read_students method in results class and passing the students.txt file as input
    results.read_students(student_file)
    # Calling read_results method in results class and passing the results.txt file as input
    results.read_results(result_file)

    # Calling display_results method in results class to display the results table
    results.display_results()
    # Calling display_course_information method in results class to display course information details
    results.display_course_information()
    # Calling display_student_information method in results class and passing results object as input to print student information details
    results.display_student_information(results)
    # calling display_best_student method in results class to print best students from UG and PG class
    results.display_best_student()


# Once this program runs it will check if the main file is running and will call main() function and start the implementation
if __name__ == '__main__':
    main()

# Documentation:
# # Design of the code:

# First the code will run and implement main function() and load the three data files from the terminal
    # Next read_courses function will be called from Results class to load the course file and store the data from it to the courses list
    # Next the read_students function will be called from Results class to load the students data and store the data from it to the students list
    # Next the read_results function will be called from Results class to load the results data and store the data from it to the scores list
    # The Results class is responsible for managing the data and performing operations on courses, students, and scores.

# Next we will call the display_results() function from Results class and implement the results table
    # It will compute statistics for every student enrolled in different courses and display their marks in each subject

# Next display_course_information() method is called in Results class to implement the stastistics
    # We will have data related to the course such as courseID, name ,type, credit, semester
    # And we will calculate the Average, Nfinish, Nongoing based on the data in the courses file to compute results.
    # This function will display the course information in the screen and store the results in the reports.txt file
    # This function will also compute which is the most difficult core and elective course and display their courseID along with the average score

# Next display_student_information() method is called in Results class to implement the statstistics for PG and UG students
    # We will have data related to students such as StudentId, name, Type(UG/PG), mode (FT/PT) and marks
    # And we will calculate the GPA for each students based on percentage and GPA(4) and will display Nfinish and Nongoing
    # This function will display the students information in the screen and store the results in the reports.txt file

# Next we will call display_best_student() method from the Results class and display the output
    # We will display best PG student along with CourseID and their GPA
    # We will display best UG student along with CourseID and their GPA

# References

# W3schools.com. (2019). Python Classes. [online] Available at: https://www.w3schools.com/python/python_classes.asp.
# Python, R. (n.d.). Reading and Writing Files in Python (Guide) – Real Python. [online] realpython.com. Available at: https://realpython.com/read-write-files-python/.
# GeeksforGeeks. (2018). Python | Output Formatting. [online] Available at: https://www.geeksforgeeks.org/python-output-formatting/.
# GeeksforGeeks. (2019). Python Classes and Objects. [online] Available at: https://www.geeksforgeeks.org/python-classes-and-objects/.



