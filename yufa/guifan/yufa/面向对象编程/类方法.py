# coding=utf-8
# !/usr/bin/env python3

class Account:
    """定义银行账户类"""

    interest_rate = 0.0668

    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount

    # 类方法
    @classmethod
    def interest_by(cls, amt):

        return cls.interest_rate * amt


interest = Account.interest_by(12_000.0)
print('计算利息:{0:.4f}'.format(interest))
