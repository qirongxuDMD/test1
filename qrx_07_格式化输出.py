name = input("你的姓名是：")
age = input("你的年龄是：")
height = 1.712
# 输出的是字符串，所以要转换称整型
age1 = int(age)
print("我的姓名是：%s, 年龄是：%d,身高是：%.2f米" % (name, age1, height))  # 两位小数

# 学号是000077
stu_num = 77
print("学号是：%07d" % stu_num)  # %0nd,n表示整数有几位
# 及格率为90%
num = 90
# print('本次的考试及格率为%d%' % num),要输入百分号（%）要输入两次%%
print('本次的考试及格率为%d%%' % num)
print('本次的考试及格率为%d%%' % num)
print('本次的考试及格率为%d%%' % num)
print('本次的考试及格率为%d%%' % num)

