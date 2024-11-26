import timeit
import json

# Scenario 1: Check if a number is even
def scenario_1_branch(arr):
    result = []
    for x in arr:
        if x % 2 == 0:
            result.append(1)
        else:
            result.append(0)
    return result

def scenario_1_branchless(arr):
    return [(x % 2 == 0) for x in arr]

# Scenario 2: Check if a number is positive
def scenario_2_branch(arr):
    result = []
    for x in arr:
        if x > 0:
            result.append(1)
        else:
            result.append(0)
    return result

def scenario_2_branchless(arr):
    return [(x > 0) for x in arr]

# Scenario 3: Check if a number is divisible by 3
def scenario_3_branch(arr):
    result = []
    for x in arr:
        if x % 3 == 0:
            result.append(1)
        else:
            result.append(0)
    return result

def scenario_3_branchless(arr):
    return [(x % 3 == 0) for x in arr]

# Scenario 4: Check if a number is a multiple of 5
def scenario_4_branch(arr):
    result = []
    for x in arr:
        if x % 5 == 0:
            result.append(1)
        else:
            result.append(0)
    return result

def scenario_4_branchless(arr):
    return [(x % 5 == 0) for x in arr]

# Scenario 5: Check if a number is within a certain range (e.g., between 100 and 200)
def scenario_5_branch(arr):
    result = []
    for x in arr:
        if 100 <= x <= 200:
            result.append(1)
        else:
            result.append(0)
    return result

def scenario_5_branchless(arr):
    return [(100 <= x <= 200) for x in arr]

# Scenario 6: Double the number if it's greater than 5000
def scenario_6_branch(arr):
    result = []
    for x in arr:
        if x > 5000:
            result.append(x * 2)
        else:
            result.append(x)
    return result

def scenario_6_branchless(arr):
    return [(x * 2 if x > 5000 else x) for x in arr]

# Scenario 7: Check if a number is a power of 2
def scenario_7_branch(arr):
    result = []
    for x in arr:
        if x > 0 and (x & (x - 1)) == 0:
            result.append(1)
        else:
            result.append(0)
    return result

def scenario_7_branchless(arr):
    return [(x > 0 and (x & (x - 1)) == 0) for x in arr]

# Scenario 8: Check if a number is prime (simplified)
def scenario_8_branch(arr):
    def is_prime(n):
        if n < 2:
            return 0
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return 0
        return 1
    return [is_prime(x) for x in arr]

def scenario_8_branchless(arr):
    return [(lambda n: 0 if n < 2 else all(n % i != 0 for i in range(2, int(n**0.5) + 1)))(x) for x in arr]

# Scenario 9: Check if a number is less than 1000
def scenario_9_branch(arr):
    result = []
    for x in arr:
        if x < 1000:
            result.append(1)
        else:
            result.append(0)
    return result

def scenario_9_branchless(arr):
    return [(x < 1000) for x in arr]

# Scenario 10: Apply bitwise AND operation and check result
def scenario_10_branch(arr):
    result = []
    for x in arr:
        if (x & 1) == 1:
            result.append(1)
        else:
            result.append(0)
    return result

def scenario_10_branchless(arr):
    return [((x & 1) == 1) for x in arr]

# Scenario 11: Check multiple conditions (x > 100 and x < 500)
def scenario_11_branch(arr):
    result = []
    for x in arr:
        if x > 100 and x < 500:
            result.append(1)
        else:
            result.append(0)
    return result

def scenario_11_branchless(arr):
    return [(x > 100 and x < 500) for x in arr]

# Scenario 12: Nested conditions
def scenario_12_branch(arr):
    result = []
    for x in arr:
        if x % 2 == 0:
            if x > 2500:
                result.append(1)
            else:
                result.append(0)
        else:
            result.append(0)
    return result

def scenario_12_branchless(arr):
    return [(1 if (x % 2 == 0 and x > 2500) else 0) for x in arr]

# Scenario 13: Slice array based on a condition
def scenario_13_branch(arr):
    result = [x for x in arr if x < 1000]
    return result

def scenario_13_branchless(arr):
    return list(filter(lambda x: x < 1000, arr))

# Scenario 14: Count numbers greater than 5000
def scenario_14_branch(arr):
    count = 0
    for x in arr:
        if x > 5000:
            count += 1
    return count

def scenario_14_branchless(arr):
    return sum([1 for x in arr if x > 5000])

# Scenario 15: Check if divisible by 7
def scenario_15_branch(arr):
    result = []
    for x in arr:
        if x % 7 == 0:
            result.append(1)
        else:
            result.append(0)
    return result

def scenario_15_branchless(arr):
    return [(x % 7 == 0) for x in arr]

# Scenario 16: Check if a number is odd
def scenario_16_branch(arr):
    result = []
    for x in arr:
        if x % 2 != 0:
            result.append(1)
        else:
            result.append(0)
    return result

def scenario_16_branchless(arr):
    return [(x % 2 != 0) for x in arr]

# Scenario 17: Check if `x` is close to 5000 using abs
def scenario_17_branch(arr):
    result = []
    for x in arr:
        if abs(x - 5000) < 10:
            result.append(1)
        else:
            result.append(0)
    return result

def scenario_17_branchless(arr):
    return [(abs(x - 5000) < 10) for x in arr]

# Scenario 18: Apply a ternary operation
def scenario_18_branch(arr):
    result = []
    for x in arr:
        result.append(1 if x > 2500 else 0)
    return result

def scenario_18_branchless(arr):
    return [(1 if x > 2500 else 0) for x in arr]

# Scenario 19: Check if the square of `x` is greater than 5000000
def scenario_19_branch(arr):
    result = []
    for x in arr:
        if x * x > 5000000:
            result.append(1)
        else:
            result.append(0)
    return result

def scenario_19_branchless(arr):
    return [(x * x > 5000000) for x in arr]

# Scenario 20: Check if `x` is part of a pre-defined set
predefined_set = set(range(4500, 4600))
def scenario_20_branch(arr):
    result = []
    for x in arr:
        if x in predefined_set:
            result.append(1)
        else:
            result.append(0)
    return result

def scenario_20_branchless(arr):
    return [(x in predefined_set) for x in arr]

# Function to test and save results
def run_and_save_scenario(scenario_num, branch_func, branchless_func, arr, repeat=1000, number=100):
    branch_times = timeit.repeat(lambda: branch_func(arr), repeat=repeat, number=number)
    branchless_times = timeit.repeat(lambda: branchless_func(arr), repeat=repeat, number=number)

    # Create JSON output
    results = {
        "branch": branch_times,
        "branchless": branchless_times
    }

    # Save to JSON file
    with open(f'scenario_{scenario_num}_results.json', 'w') as f:
        json.dump(results, f, indent=4)

    print(f"Scenario {scenario_num} results saved.")

# Run all 20 scenarios
arr = range(0, 10000)
for i in range(1, 21):
    run_and_save_scenario(i, globals()[f"scenario_{i}_branch"], globals()[f"scenario_{i}_branchless"], arr)
