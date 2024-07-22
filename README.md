# Student-Results-Management-System
The Student Results Management System is a Python-based project designed to manage and analyze student results, course offerings, and student enrollments. Leveraging Python’s object-oriented programming (OOP) concepts, the system organizes and processes data through classes and methods, ensuring efficient data handling and clear, structured reports. It reads data from text files, processes this data using OOP principles, and displays detailed reports about students' performances and course statistics.


## Overview of the Student Results Management System
The Student Results Management System is designed to efficiently manage and analyze student performance data. The system begins by executing the **main()** function, which loads three essential data files: courses, students, and results. These files are read and processed by the **read_courses**, **read_students**, and **read_results** methods within the Results class, respectively. This class is central to the system, handling data management and performing operations on courses, students, and scores. Once the data is loaded, the **display_results()** method is called to compute and display statistics for each student, showing their marks across various subjects. The **display_course_information()** method then provides detailed statistics on each course, including course ID, name, type, credit, and semester, and calculates averages and completion rates. It also identifies and displays the most challenging core and elective courses based on average scores. Following this, the **display_student_information()** method calculates and displays GPA and other relevant statistics for **both undergraduate (UG) and postgraduate (PG) students**. Finally, the **display_best_student()** method highlights the top-performing PG and UG students, showcasing their course IDs and GPAs. The system ensures that all relevant information is displayed on the screen and stored in a **reports.txt** file for record-keeping.


## Features
* **Course Management:** Read and store course details.
* **Student Management:** Read and store student details.
* **Result Management:** Read and store students' results.
* **Statistics Computation:** Calculate average scores, GPA, and other statistics for students and courses.
* **Reports Generation:** Generate detailed reports for courses and students.

## Usage
* **Add Course Data:** Courses are stored in courses.txt.
* **Add Student Data:** Students are stored in students.txt.
* **Add Results Data:** Results are stored in results.txt.
* **Run the Program:** Execute the script to process the data and generate reports.


## Dependencies
Python 3.x

## Files
* **main.py:** Main script containing the implementation.
* **courses.txt:** File containing course details.
* **students.txt:** File containing student details.
* **results.txt:** File containing results details.
* **reports.txt:** Generated report file.
