

-->Problem Statement
The Core Issue: Limitations of Absolute Grading
In traditional academic assessment systems, students are typically evaluated based on Absolute Grading, where grades are assigned according to fixed score thresholds (e.g., >90% is an 'A', <40% is a 'Fail').
While simple, this approach has significant flaws:
Ignores Exam Difficulty: If an exam is exceptionally difficult, the class average may drop significantly. Under absolute grading, hardworking students might fail or receive poor grades simply because the paper was tough, not because they lacked knowledge.
Grade Inflation: Conversely, if an exam is too easy, a large portion of the class may score >90%, leading to grade inflation where distinction loses its value.
Lack of Peer Comparison: A raw score of 75/100 lacks context. It does not indicate whether it is the highest score in the class or below average. Absolute grading fails to answer this.
The Solution: Relative Grading
To address these disparities, there is a need for a Relative Grading System (grading on the curve) that evaluates a student's performance relative to their peers rather than against a static number.
This programm solves this by implementing a statistical approach:
It calculates the Class Mean ($\mu$) to establish a baseline performance level.
It computes the Standard Deviation ($\sigma$) to measure the spread or variance of the scores.
It normalizes every score into a Z-Score, ensuring that grades reflect a student's standing on the Normal Distribution Curve.

The primary objective of this project is to develop a computational tool that automates the relative grading process. This ensures fairness, eliminates subjective bias, and provides a mathematically defensible assessment of student performance regardless of the exam's difficulty level.



-->Objective
The primary objective of this project is to develop a computational tool that automates the relative grading process. This ensures fairness, eliminates subjective bias, and provides a mathematically defensible assessment of student performance regardless of the exam's difficulty level.

-->Scope of the Project
Statistical Computation: The system is capable of accurately calculating population statistics, specifically the Mean ($\mu$) and Standard Deviation ($\sigma$), for datasets of varying sizes.
Algorithmic Grading: It implements a Gaussian-based grading logic to assign letter grades (S, A, B, C, D, F) based on calculated Z-scores.
Edge Case Management: The tool includes robust error handling for mathematical anomalies, such as "Zero Variance" scenarios where all candidates score identical marks.
Performance Analysis: It provides immediate feedback on class performance, identifying outliers (high achievers and at-risk students) through statistical deviation.
Platform: The current implementation is a console-based application compatible with any system running Python 3.x.
Out-of-Scope (Future Expansion)
Database Integration: Persistent storage of student records in a SQL/NoSQL database is not currently implemented.
Complex Weightage: The system currently treats all input scores equally and does not account for weighted averages (e.g., assignments vs. exams).
Graphical User Interface (GUI): A visual interface (web or desktop) is planned for future releases but is not part of the initial core logic.


