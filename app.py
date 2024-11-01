
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
    probabilities = defaultdict(float)
    for roll in range(m, m * n + 1):
        probabilities[roll] = 0
    
    if m == 1:
        for i in range(1, n + 1):
            probabilities[i] = 1 / n
        return probabilities
    
    for i in range(1, n + 1):
        sub_probs = probability_distribution(m - 1, n)
        for sum, prob in sub_probs.items():
            probabilities[sum + i] += prob / n

    return probabilities

# Task 4: User Interface
def main():
    # Get user input for N, M, and K
    n = int(input("Enter the number of sides on the dice (N): "))
    m = int(input("Enter the number of dice (M): "))
    k = int(input("Enter the number of rolls (K): "))

    # Calculate the probability distribution
    probabilities = probability_distribution(m, n)

    # Display the results
    print("\nProbability Distribution:")
    for sum_value in sorted(probabilities.keys()):
        print(f"Sum: {sum_value}, Probability: {probabilities[sum_value]:.4f}")

# Run the main function
if __name__ == "__main__":
    main()