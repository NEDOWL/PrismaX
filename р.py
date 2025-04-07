from itertools import combinations, product

symbols = ['🍒', '🍋', '🍉', '⭐', '🔔', '7️⃣', '🍇', '🍓', '🍍', '💎', '💰']
total_combinations = len(symbols) ** 6

def calculate_probability(unique_count):
    count = 0
    for combo in combinations(symbols, unique_count):
        for arrangement in product(combo, repeat=6):
            if len(set(arrangement)) == unique_count:
                count += 1
    return count / total_combinations

# Вероятности
jackpot_prob = calculate_probability(1)  # Все одинаковые
three_or_less_prob = sum(calculate_probability(k) for k in range(1, 4))
four_unique_prob = calculate_probability(4)
five_or_six_prob = 1 - (jackpot_prob + three_or_less_prob + four_unique_prob)

print(f"Джекпот: {jackpot_prob:.6f}")
print(f"Три или меньше уникальных: {three_or_less_prob:.6f}")
print(f"Четыре уникальных: {four_unique_prob:.6f}")
print(f"Пять или шесть уникальных: {five_or_six_prob:.6f}")