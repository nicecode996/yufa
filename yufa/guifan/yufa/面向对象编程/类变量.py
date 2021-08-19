# !/usr/bin/env python3
# coding-utf-8

class Account:
    """定义银行账户类"""

    interest_rate = 0.0668       # 类变量利率

    def __init__(self,owner,amount):
        self.owner = owner    # 定义实例变量账户名
        self.amount = amount  # 定义实例变量账户金额

account = Account('Tony',1_800_000.0)

print('账户名:{0}'.format(account.owner))
print('账户金额:{0}'.format(account.amount))
print('利率:{0}'.format(Account.interest_rate))