import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Ініціалізація мінімальної купи
    heapq.heapify(cable_lengths)
    total_cost = 0

    # Поки в купі більше одного кабелю
    while len(cable_lengths) > 1:
        # Вибір і видалення двох кабелів з найменшою довжиною
        cost_to_connect = heapq.heappop(cable_lengths) + heapq.heappop(cable_lengths)

        # Додавання суми назад до купи
        heapq.heappush(cable_lengths, cost_to_connect)

        # Додавання вартості до загальних витрат
        total_cost += cost_to_connect

    return total_cost

# Приклад використання
cable_lengths = [5, 4, 2, 8]
print(min_cost_to_connect_cables(cable_lengths))