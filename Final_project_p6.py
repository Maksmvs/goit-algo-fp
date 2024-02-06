import time

def greedy_algorithm(items, budget):
    start_time = time.time()
    sorted_items = sorted(items, key=lambda x: x['calories'] / x['cost'], reverse=True)

    chosen_items = []
    total_cost = 0
    total_calories = 0

    for item in sorted_items:
        if total_cost + item['cost'] <= budget:
            chosen_items.append(item['name'])
            total_cost += item['cost']
            total_calories += item['calories']

    end_time = time.time()
    execution_time = end_time - start_time

    return chosen_items, total_calories, total_cost, execution_time

def dynamic_programming(items, budget):
    start_time = time.time()
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if items[i - 1]['cost'] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1]['cost']] + items[i - 1]['calories'])

    total_calories = dp[n][budget]
    total_cost = budget
    chosen_items = []

    for i in range(n, 0, -1):
        if dp[i][total_cost] != dp[i - 1][total_cost]:
            chosen_items.append(items[i - 1]['name'])
            total_calories -= items[i - 1]['calories']
            total_cost -= items[i - 1]['cost']

    end_time = time.time()
    execution_time = end_time - start_time

    return chosen_items, dp[n][budget], execution_time

items = [
    {"name": "pizza", "cost": 50, "calories": 300},
    {"name": "hamburger", "cost": 40, "calories": 250},
    {"name": "hot-dog", "cost": 30, "calories": 200},
    {"name": "pepsi", "cost": 10, "calories": 100},
    {"name": "cola", "cost": 15, "calories": 220},
    {"name": "potato", "cost": 25, "calories": 350}
]

budget = 100

greedy_items, greedy_calories, greedy_cost, greedy_time = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Chosen Items:", greedy_items)
print("Total Calories:", greedy_calories)
print("Total Cost:", greedy_cost)
print("Execution Time:", greedy_time, "seconds")

dynamic_items, dynamic_calories, dynamic_time = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print("Chosen Items:", dynamic_items)
print("Total Calories:", dynamic_calories)
print("Execution Time:", dynamic_time, "seconds")
