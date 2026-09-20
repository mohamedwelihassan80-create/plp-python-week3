### using for loop for grades
scores = [72, 45, 90, 61, 38]
for score in scores:
    if score >= 80:
        print("A:", score)
    elif score >= 70:
        print("B:", score)
    elif score >= 50:
        print("C:", score)
    else:
        print("F:", score)


scores = [72, 45, 90, 61, 38]

### Start Counters at 0
passed_count = 0
failed_count = 0

for score in scores:
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

print("Passed:", passed_count)
print("Failed:", failed_count)


### adding up scores and printing average
scores = [72, 45, 90, 61, 38]

average = sum(scores) / len(scores)
print("Average score:", round(average, 1))
