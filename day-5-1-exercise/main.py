# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#print(student_heights)

heightSum=0
avgHeight=0
studentCount=0

for S1 in student_heights:
  heightSum += S1
  avgHeight = round(heightSum/ (studentCount+1))
  studentCount+=1
print(avgHeight)




