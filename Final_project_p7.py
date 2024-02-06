import random
import pandas as pd
import matplotlib.pyplot as plt

table_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
    8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

def monte_carlo_simulation(num_trials):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums_count[total] += 1

    probabilities = {key: value / num_trials for key, value in sums_count.items()}
    return probabilities

def main():
    num_trials = 100000

    probabilities = monte_carlo_simulation(num_trials)

    data = {
        'Сума': list(probabilities.keys()),
        'Імовірність (Монте-Карло)': list(probabilities.values()),
        'Імовірність (Таблиця)': [table_probabilities[sum_value] for sum_value in probabilities.keys()]
    }
    data['Різниця'] = [p - table_probabilities[s] for p, s in zip(data['Імовірність (Монте-Карло)'], data['Сума'])]

    df = pd.DataFrame(data)

    df['Імовірність (Монте-Карло)'] = df['Імовірність (Монте-Карло)'].apply(lambda x: f"{x*100:.2f} ({x:.2%})")
    df['Імовірність (Таблиця)'] = df['Імовірність (Таблиця)'].apply(lambda x: f"{x*100:.2f} ({x:.2%})")

    print(df)

    plt.figure(figsize=(10, 6))
    plt.plot(list(probabilities.keys()), list(probabilities.values()), label="Монте-Карло", marker='o', color='blue')
    plt.plot(list(table_probabilities.keys()), list(table_probabilities.values()), label="Таблиця", linestyle='--', color='red')
    plt.xlabel('Сума')
    plt.ylabel('Імовірність')
    plt.title('Імовірність сум при киданні двох кубиків')
    plt.xticks(range(2, 13))
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
