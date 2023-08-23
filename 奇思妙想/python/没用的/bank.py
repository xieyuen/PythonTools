means = [0, 0, 0]
loan = 0
rate = 0
pay = 0
investment = 0
annual_rate = 0


# 计算定投预期收益
# 定投收益的计算公式为：M=a(1+x)[-1+(1+x)^n]/x;
# 其中 M 代表预期收益，a 代表每期定投金额，x 代表收益率，而 n 代表定投期数。
# 假设用户每月定投金额为 300 元，一年也就是 3600 元，年收益率为 15%，
# 定投期限为 35 年，则可以计算出收益为 3600(1+15%)[-1+(1+15%)^35]/15=3648044 元。
def fixed_investment(inv, a_rate, y):
    global means
    inv = 12 * inv
    a_rate = a_rate / 100
    if a_rate == 0:
        expected = 0
    else:
        expected = inv * (1 + a_rate) * (pow((1 + a_rate), y) - 1) / a_rate
    print("定投的预期收入为: %.2f" % expected)
    means[1] = expected
    return expected


def balance():
    total = 0
    for i in means:
        total += i
    print("你的资产总额为：%.2f" % total)
    print("你的资产明细为：\n")
    print("存款：%.2f" % means[0])
    print("理财：%.2f" % means[1])
    print("负债：%.2f" % means[2])


def saving(amount):
    global means
    if amount < 0:
        print("存款金额不可小于 0！")
    else:
        means[0] += amount
        print("已存款：%.2f 元" % amount)
        print("当前余额：%.2f 元" % means[0])


def draw_money(drawing):
    global means
    if drawing < 0:
        print("取款金额不可小于 0！")
    elif drawing > means[0]:
        print("取款金额不可超过余额！")
    else:
        means[0] -= drawing
        print("已取款： %.2f 元" % drawing)
        print("当前余额： %.2f 元" % means[0])


def loans(loan, rate, pay, years):
    global means
    if pay < (loan - pay) * rate:
        print("你是还不完的！！！")
    else:
        if years == 0:
            count = 0
            while loan > 0:
                loan -= pay
                loan *= (1 + rate)
                count += 1
            print("将在 %d 年后还完贷款。" % count)
        else:
            for _ in range(years):
                loan -= pay
                if loan == 0:
                    break
                else:
                    loan *= (1 + rate)
                    print("你现在的负债是: %.2f" % loan)
            # means[2] = loan
            return loan


# 未来财务状况
def future(years):
    income = fixed_investment(investment, annual_rate, years)
    debt = loans(loan, rate, pay, years)
    captial = means[0] + income - debt
    print("你第%i年的总资产有: %.3f" % (years, captial))


def init():
    print()
    print('''以下为可办理的业务：
        1. 查询资产
        2. 存款
        3. 取款
        4. 计算复利
        5. 计算贷款
        6. 计算未来资产
        q. 退出''')


def main():
    init()
    while True:
        choice = input("请输入您要办理的业务代码: ")
        #  查询余额
        if choice == "1":
            balance()
        # 存款
        elif choice == "2":
            inc = float(input("请输入存款金额: "))
            saving(inc)
        # 取款
        elif choice == "3":
            dec = float(input("请输入取款金额: "))
            draw_money(dec)
        # 计算定投
        elif choice == "4":
            investment = float(input("请输入每月定投金额: "))
            annual_rate = float(input("请输入年收益率: "))
            years = int(input("请输入定投期限(年): "))
            if investment <= 0 or annual_rate <= 0 or years <= 0:
                print("输入的数据有误")
            else:
                money = fixed_investment(investment, annual_rate, years)
            print("最终收获: %.2f 元" % money)
        # 计算贷款
        elif choice == "5":
            loan = float(input("请输入当前贷款: "))
            rate = float(input("请输入年利率: "))
            pay = float(input("请输入每年还款: "))
            if loan <= 0 or rate <= 0 or pay <= 0:
                print("输入的数据有误")
            else:
                loans(loan, rate, pay, 0)
        elif choice == "6":
            years = int(input("希望查询多少年后的财务状况? "))
            future(years)
        # 退出
        elif choice == "q":
            print("欢迎下次光临！再见！")
            break
        else:
            print("你输入的指令有误，请重新输入\n")


if __name__ == '__main__':
    main()