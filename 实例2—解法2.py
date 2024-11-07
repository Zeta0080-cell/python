def calculate_bonus(profit):
    bonus = 0.0
    if profit <= 100000:
        bonus = profit * 0.10
    elif profit <= 200000:
        bonus = 100000 * 0.10 + (profit - 100000) * 0.075
    elif profit <= 400000:
        bonus = 100000 * 0.10 + 100000 * 0.075 + (profit - 200000) * 0.05
    elif profit <= 600000:
        bonus = 100000 * 0.10 + 100000 * 0.075 + 200000 * 0.05 + (profit - 400000) * 0.03
    elif profit <= 1000000:
        bonus = 100000 * 0.10 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (profit - 600000) * 0.015
    else:
        bonus = 100000 * 0.10 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (profit - 1000000) * 0.01

    return bonus
profit = float(input("请输入当月利润："))
bonus = calculate_bonus(profit)
print(f"应发放奖金总数为：{bonus:.2f}元")