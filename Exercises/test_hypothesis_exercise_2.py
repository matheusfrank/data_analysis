"""
Exercise 2: Testing the Proportion of Defective Products
You are working for a company that manufactures electronic devices. The company claims that only 5% of the products in a large batch are defective. 
You decide to test this claim by randomly selecting a sample of 200 products. In your sample, you find that 15 products are defective. 
You want to test whether the proportion of defective products in the batch is significantly different from the company's claim using a significance level (𝛼) of 0.05.

Hypotheses
Null Hypothesis (𝐻_0): The proportion of defective products is 5% (𝑝=0.05).
Alternative Hypothesis (𝐻𝑎): The proportion of defective products is different from 5% (𝑝≠0.05).
"""

import math
from scipy.stats import norm

#Given data:
sample = 200
defective_sample = 15
p_0 = 0.05
p_hat = defective_sample/sample

#Using the Z-test formula:
Z = (p_hat - p_0)/math.sqrt(p_0*(1-p_0)/sample)

#Inputs
alpha = 0.05  # Significance level
z_critical = norm.ppf(1 - alpha/2)  # Critical Z-value for a two-tailed test

#Laying out the results:
print(f"Null Hypothesis, H_0: {p_0}%")
print(f"Alternative Hyphotesis, H_a: {p_hat}")
print(f"alpha: {alpha}")
print(f"Z-test: {Z}")
print(f"z-critical value: {z_critical}")

# Decision based on Z-test:
if abs(Z) > z_critical:
    print("Reject H_0: The proportion of defective products is significantly different from 5%.")
else:
    print("Fail to reject H_0: The proportion of defective products is not significantly different from 5%.")