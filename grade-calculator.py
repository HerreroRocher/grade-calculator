desired_overall_score = float(input("Enter the % desired overall score you wish to achieve in this course unit: "))

coursework_weight = float(input("Enter the % weight of your coursework over the course unit: "))

print("")

calculate_course_score = input("Do you want me to calculate your total coursework % if you have had numerous courseworks? (y/n)")

if calculate_course_score.upper() == "Y" or calculate_course_score.upper() == "YES":
    coursework_number = int(input("How many courseworks did you do in this course unit? "))
    coursework_score_achieved = 0
    total_coursework_covered = 0  
    for i in range(coursework_number):
        print("")
        
        if i == coursework_number - 1:
            current_coursework_weight = 100 - total_coursework_covered
            current_course_score = float(input("Enter the % score you achieved in your last coursework: "))
            
        else:
            current_coursework_weight = float(input(f"Enter the % weight coursework {i+1} has over your total coursework: "))
            total_coursework_covered +=  current_coursework_weight
            current_course_score = float(input("Enter the % score you achieved in this specific coursework: "))
        coursework_score_achieved += current_course_score * current_coursework_weight / 100
        
        
else:
    coursework_score_achieved = float(input("Enter the % score you achieved in your coursework: "))

print("")
print("-------------------------------------------------------------------")




exam_weight = 100-coursework_weight

total_score_achieved = coursework_score_achieved * coursework_weight / 100
score_left_to_achieve = desired_overall_score - total_score_achieved
exam_score_required = (100/exam_weight) * score_left_to_achieve

print(f'You need to achieve {int(exam_score_required)}% in your exam to get {int(desired_overall_score)}% overall')

print("-------------------------------------------------------------------")
print("")
