python = 3
math = 4
english = 4
physical = 2
military_theory = 2
philosophy = 2
####################Begin##################################
# 此处去掉注释符号“#”并补充你的代码
tuition = int(input())
credits = python + math + english + physical + military_theory + philosophy
tuitions = tuition * credits
print(f'你本学期选修了{credits}个学分。')
print(f'你应缴纳的学费为{tuitions}元。')




####################End##################################