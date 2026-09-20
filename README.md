# plp-python-week3
# Week 3: Python Conditions and Loops Assignment

## File Descriptions
- `grade_reporter.py`: Processes a list of learner scores in a single pass to assign letter grades, count total passes and fails, and calculate the rounded average score.
- `bug_hunt.py`: Calculates the sum of numbers from 1 to 5 using a `while` loop, with three bugs identified and resolved using `# BUG:` comments.

## Reflection on Part B (Bug Hunt)
The hardest bug to find was the logic error in the loop condition (`while count < 5`). Because Python executed without throwing any red error messages, it looked correct at first glance. However, I knew something was wrong because the final output printed `10` instead of the expected `15`, showing that the loop stopped too early and excluded the number 5.