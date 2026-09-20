count = 1
total = 0
### BUG 1: Forgot to include a colon after 5; Fixed by adding a colon after 5
### BUG 2: The condition '< 5' left out 5; fixed by changing condition from '< 5' to '<= 5'
while count <= 5:
    total = total + count
    count = count + 1
### BUG 3: cannot concatenate str and int with '+'; fixed by separating with a comma in the print statement
print("Sum of 1 to 5 is:", total)   