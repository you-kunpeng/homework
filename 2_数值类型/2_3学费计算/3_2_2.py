python = 3
math = 4
english = 4
physical_education = 2
military_theory = 2
philosophy = 2

####################Begin##################################
# 此处去掉注释符号“#”并补充你的代码
tuition_per_credit = float(input("请输入每学分学费金额：")) #每学分缴费金额
living_expenses = float(input("请输入你每个月生活费："))  #生活费金额
total_credits = python + math + english + physical_education + military_theory + philosophy #总学分
total_tuition = total_credits * tuition_per_credit #总学分费
total_cost = living_expenses * 5 + total_tuition   #学费和生活费总额
student_loan =  float(total_cost) * 0.6
print(f'本学期你能够贷款{student_loan:.2f}元')





####################End##################################