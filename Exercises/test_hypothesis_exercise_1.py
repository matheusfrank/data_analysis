"""
Test Hipothesis Exercises
21/01/2025

Exercise 1: Testing the Average Monthly Salary
You are given a dataset representing the monthly salaries (in $) of 20 employees at a company.
The company claims the average monthly salary of their employees is $3,500. You want to test whether the actual average salary differs from this claim using a significance level (
𝛼
α) of 0.05.
""" 
import math
from IPython.display import display, Math
from scipy.stats import t
 
#Given data:
hypothesis_mean = 3500
salaries = [3400, 3600, 3200, 4000, 3100, 3900, 3700, 3500, 3300, 4200, 
            3000, 3800, 3100, 3400, 3900, 4000, 3500, 3600, 3300, 3700]

#Calculate the sum of the salaries:
sum_salaries = 0
n = 0
for salary in salaries:
    sum_salaries += salary
    n += 1
    
#Compute the mean:
mean = sum_salaries / n

#Calculating the Standard deviation:
def sigma_sum(x,n,mean):
    sum = 0
    for x_i in x:
        sum += (x_i - mean)**2
    return sum
sigma = math.sqrt((1/n)*(sigma_sum(salaries,n,mean)))

#Utilizing the T-test formula:
T = (mean - hypothesis_mean) /  (sigma/math.sqrt(n))

# Inputs
alpha = 0.05  # Significance level
df = n - 1  # Degrees of freedom

# Find the critical t-value
critical_t = t.ppf(1 - alpha/2, df)

# Output results:
print(f"Sample mean: {mean}")
print(f"Population standard deviation: {sigma}")
print(f"Test statistic (T): {T}")
print(f"Critical t-value (two-tailed): {critical_t}")

# Decision:
if abs(T) > critical_t:
    print("H_alpha: The alternative hypothesis is correct. The salary is not $3500")
else:
    print("H_0: The null hypothesis is correct. The salary is indeed $3500")
    
"""
ChatGPT code for comparison:

import math
from scipy.stats import t

# Given data:
hypothesis_mean = 3500
salaries = [3400, 3600, 3200, 4000, 3100, 3900, 3700, 3500, 3300, 4200, 
            3000, 3800, 3100, 3400, 3900, 4000, 3500, 3600, 3300, 3700]

# Calculate the mean:
n = len(salaries)
mean = sum(salaries) / n

# Calculating the Standard Deviation:
def calculate_sigma(data, mean, n):
    return math.sqrt(sum((x - mean) ** 2 for x in data) / n)

sigma = calculate_sigma(salaries, mean, n)

# T-Test formula:
T = (mean - hypothesis_mean) / (sigma / math.sqrt(n))

# Critical t-value:
alpha = 0.05  # Significance level
df = n - 1  # Degrees of freedom
critical_t = t.ppf(1 - alpha / 2, df)

# Output results:
print(f"Sample mean: {mean}")
print(f"Population standard deviation: {sigma}")
print(f"Test statistic (T): {T}")
print(f"Critical t-value (two-tailed): {critical_t}")

# Decision:
if abs(T) > critical_t:
    print("H_alpha: The alternative hypothesis is correct. The salary is not $3,500.")
else:
    print("H_0: The null hypothesis is correct. The salary is indeed $3,500.")
  
    """