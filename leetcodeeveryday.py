seats = [2,2,6,6]
students = [1,3,2,6]
srt_seats = sorted(seats)
srt_students = sorted(students)
count = 0
for i in range(len(seats)):
    count += abs(srt_seats[i]-srt_students[i])
print(count)