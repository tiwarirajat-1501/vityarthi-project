# vityarthi-project
#Grade Calculator
A relative grade calculator that determines student grades and thresholds based on class average (Mean) and Standard Deviation


#Overview
A Relative Grading System (grading on the curve). Addressing the limitations of absolute grading, this project evaluates student performance based on the class average (Mean) and score distribution (Standard Deviation). By normalizing raw scores into Z-scores, the system ensures a fair assessment that adapts to the difficulty of the exam, automatically identifying outliers and eliminating subjective bias in the grading process.


#Features of Standard Deviation Calculator
•	Fair Assessment: Automatically adjusts grades based on class performance, ensuring students aren't penalized for exceptionally difficult exams.

•	Bias Elimination: Removes subjective human error by relying strictly on statistical metrics (Mean & Standard Deviation) for grading.

•	Outlier Detection: Instantly flags high achievers (Z > 2.0) for rewards and at-risk students (Z < -1.3) for remedial support.

•	Scalability: efficiently handles grading for large-scale standardized tests or entrance exams where relative ranking matters more than absolute scores.


#Tools Used
**Python:** The core programming language used for logic implementation.
* **NumPy:** A powerful library used for high-precision statistical calculations (Mean, Standard Deviation) and array handling.
* **VS Code:** The Integrated Development Environment (IDE) used for writing and debugging the code.
* **Version Control:** Git

## 🚀 Steps to Install & Run the Project
Follow these steps to set up the project locally on your machine.

1. Ensure Python is installed in your device
2. Download the project file from github to your computer
3. This project uses NumPy for statistical calculations. Install it using pip:# pip install numpy
4. Run the main Python script to start the calculator
5. Once the program is running, follow the prompts in the terminal:
    >Enter the total number of students.
    >Enter the score for each student one by one.
6. The final grade of each student will be calculated


## 🧪 Instructions for Testing

To ensure the **Vityarthi Grade Calculator** is functioning correctly, follow these testing procedures.

### General Testing Procedure
1.  Open your terminal or command prompt.
2.  Navigate to the project directory.
3.  Run the command: `python main.py`
4.  Enter the input values as described in the test cases below and compare the output with the expected results.

### ✅ Test Case 1: Standard Distribution (Normal Class)
This tests if the calculator correctly handles a typical range of scores.

* **Input:**
    * Number of students: `5`
    * Scores: `95`, `85`, `75`, `65`, `55`
* **Expected Output:**
    * **Class Mean:** `75.00`
    * **Standard Deviation:** `14.14`
    * **95.0** → Grade **A** (Z ≈ 1.41)
    * **75.0** → Grade **C** (Z = 0.00)
    * **55.0** → Grade **F** (Z ≈ -1.41)

### ⚠️ Test Case 2: Zero Variance (Edge Case)
This verifies that the program does not crash when all students score the same marks (which causes Standard Deviation to be 0).

* **Input:**
    * Number of students: `3`
    * Scores: `80`, `80`, `80`
* **Expected Output:**
    * **Class Mean:** `80.00`
    * **Standard Deviation:** `0.00`
    * **80.0** → Grade **C** (Default assignment for Z=0)

### 🔍 What to Verify
* Check that the **Mean** matches the average of the numbers entered.
* Ensure that no runtime errors (like `ZeroDivisionError`) occur during Test Case 2.
* Verify that higher scores receive 'S' or 'A' grades and lower scores receive 'D' or 'F'.



