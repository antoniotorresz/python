def calculate_investment():
    yield_rate = 12.5 # 12.5% annual return
    current_investment = 8137 # initial investment
    weeks = 28 # 0.5 year
    subscription = 2500 # weekly subscription
    for week in range(1, weeks):
        week_yield = current_investment * (yield_rate / 100) / 52
        current_investment = current_investment + subscription + week_yield
        if week % 2 == 0:
            print(f'Week {week}, with yield of: ${week_yield:.2f} will save ${current_investment:.2f}')

calculate_investment()