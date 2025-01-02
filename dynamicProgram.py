def add_item_to_backpack(backpack, item_name, item_price, item_size):
    backpack[item_name] = (item_price, item_size)
    return backpack


def knapsack(backpack, max_size):
    items = list(backpack.items())
    n = len(items)
    dp = [[0] * (max_size + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        item_name, (item_price, item_size) = items[i - 1]
        for j in range(max_size + 1):
            if item_size <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_size] + item_price)
            else:
                dp[i][j] = dp[i - 1][j]

    max_value = dp[n][max_size]
    selected_items = []
    j = max_size
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name, (item_price, item_size) = items[i - 1]
            selected_items.append(item_name)
            j -= item_size

    return max_value, selected_items


def main():
    backpack = {}
    max_size = int(input("Введите максимальный размер рюкзака: ").strip())

    while True:
        command = input("Введите команду (Device, Solve, Exit): ").strip().lower()
        if command == "device":
            item_name = input("Введите название предмета: ").strip()
            item_price = int(input("Введите стоимость предмета: ").strip())
            item_size = int(input("Введите размер предмета: ").strip())
            add_item_to_backpack(backpack, item_name, item_price, item_size)
            print(f"Обновлённый рюкзак: {backpack}")

        elif command == "solve":
            max_value, selected_items = knapsack(backpack, max_size)
            print(f"Максимальная стоимость: {max_value}")
            print(f"Выбранные предметы: {selected_items}")

        elif command == "exit":
            print("Завершение программы.")
            break

        else:
            print("Неверная команда. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
