import random
from collections import defaultdict

# Task 1: Implementing the Dice Roll Function
def roll_dice(m, n):
    total_sum = 0
    for i in range(m):
        total_sum += random.randint(1, n)
    return total_sum


# Task 2: Simulating Multiple Rolls
import random

def roll_dice_multiple_times(m, n, k):
    results = []
    
    for i in range(k):
        total_sum = 0
        for i in range(m):
            total_sum += random.randint(1, n)
        results.append(total_sum)
    return results

# Task 3: Calculating Probability Distribution
def probability_distribution(m, n):
    if m == 0:
        return {}
    
    if m <= 0 or n <= 0:
        raise ValueError("Both m and n must be positive integers.")
    
    probabilities = defaultdict(float)
        
    if m == 1:
        for i in range(1, n + 1):
            probabilities[i] = 1 / n
        return probabilities
    
    sub_probs = probability_distribution(m - 1, n)

    for i in range(1, n + 1):
        for sum_val, prob in sub_probs.items():
            probabilities[sum_val + i] += prob / n

    return probabilities

# Task 4: User Interface
def main():

    n = int(input("Enter the number of sides on the dice (N): "))
    m = int(input("Enter the number of dice (M): "))
    k = int(input("Enter the number of rolls (K): "))

    probabilities = probability_distribution(m, n)

    # Display the results
    print("\nProbability Distribution:")
    for sum_value in sorted(probabilities.keys()):
        print(f"Sum: {sum_value}, Probability: {probabilities[sum_value]:.4f}")

if __name__ == "__main__":
    main()