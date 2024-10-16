desired_overall_score = float(input("Enter the % desired overall score you wish to achieve in this course unit: "))
coursework_weight = float(input("Enter the % weight of your coursework to the course unit: "))
coursework_score_achieved = float(input("Enter the % score you achieved in your coursework: "))
exam_weight = 100-coursework_weight

# desired_overall_score = (coursework_score_achieved * coursework_weight / 100) + (exam_weight * exam_score_required/100)

# desired_overall_score - (coursework_score_achieved * coursework_weight / 100) = (exam_weight * exam_score_required/100)

# (exam_weight * exam_score_required/100) = desired_overall_score - (coursework_score_achieved * coursework_weight / 100) 

# exam_weight * exam_score_required = 100 * (desired_overall_score - (coursework_score_achieved * coursework_weight / 100)) 

total_score_achieved = coursework_score_achieved * coursework_weight / 100
score_left_to_achieve = desired_overall_score - total_score_achieved
exam_score_required = (100/exam_weight) * score_left_to_achieve

print(f'You need to achieve {int(exam_score_required)}% in your exam to get {int(desired_overall_score)}% overall')
