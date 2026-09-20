### using for loop for grades 

scores = [72, 45, 90, 61, 38]

passed_count = 0
failed_count = 0
total_score = 0

for score in scores:
    # 1. Determine grade & update pass/fail tally at the same time
    if score >= 80:
        print("A:", score)
        passed_count += 1
    elif score >= 70:
        print("B:", score)
        passed_count += 1
    elif score >= 50:
        print("C:", score)
        passed_count += 1
    else:
        print("F:", score)
        failed_count += 1

    # 2. Add to total in the same loop
    total_score += score

# 3. Print the final summary once at the end
average = total_score / len(scores)

print("Passed:", passed_count)
print("Failed:", failed_count)
print("Average score:", round(average, 1))