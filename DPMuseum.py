def maximum(time_lim, attraction):
    n = len(attraction)
    dp = [[0] * (time_lim + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, time, value = attraction[i-1]
        for t in range(time_lim + 1):
            if time > t:
                dp[i][t] = dp[i-1][t]
            else:
                dp[i][t] = max(dp[i-1][t], dp[i-1][t-time] + value)

    t = time_lim
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][t] != dp[i - 1][t]:
            chosen.append(attraction[i - 1][0])
            t -= attraction[i - 1][1]

    return dp[n][time_lim], chosen

attractions = [
    ("Вестминстерское аббатство", 6, 7),
    ("Театр 'Глобус'", 6, 6),
    ("Национальная галерея", 12, 9),
    ("Британский музей", 24, 9),
    ("Собор св. Павла", 6, 8),
    ("Лондонский Тауэр", 8, 7),
    ("Букингемский дворец", 10, 10),
    ("Музей мадам Тюссо", 14, 8),
    ("Гайд-парк", 5, 6),
    ("Шекспировский мост", 4, 5)
]

time_limit = 48

max_value, chosen_attractions = maximum(time_limit, attractions)
print(f"Максимальная оценка: {max_value}")
print("Выбранные достопримечательности:", " -> ".join(chosen_attractions))