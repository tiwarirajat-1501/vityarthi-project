import numpy as np 

def calculate_grades_std_dev(scores):

    mean = np.mean(scores) # Calculates mean i.e class avegrage
    std_dev = np.std(scores) # Calculates standard deviation
    
    print(f"Class Mean: {mean:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")
    print("-" * 30)

    results = {}
    for score in scores:
        # Calculate the Z-score: z = (x - mean) / standard_deviation
        if std_dev == 0:
            z_score = 0
        else:
            z_score = (score - mean) / std_dev
        
        grade = assign_grade(z_score)
        results[score] = {"Grade": grade}
        print(f"Score: {score}, Grade: {grade}")

    return results

def assign_grade(z_score):
    if z_score >= 2.0:
        return 'S'
    elif z_score >= 1.0:
        return 'A'
    elif z_score >= 0.5 and z_score < 1.0:
        return 'B'
    elif z_score >= -0.5 and z_score < 0.5:
        return 'C'
    elif z_score >= -1.3 and z_score < -0.5:
        return 'D'
    else:
        return 'F'

#Taking input from user for number of students and their scores
class_scores = []
n = int(input("Enter the number of students: "))
for i in range(n):
    score = float(input(f"Enter score for student {i + 1}: "))
    class_scores.append(score)

# Calculating and printing the grades
grade_results = calculate_grades_std_dev(class_scores)


