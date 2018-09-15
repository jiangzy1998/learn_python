from person import Person


class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)  # 出现了冗余
        # 推荐使用 Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)
    print(tom)  # __str__


# 输出:
# Doe
# 65000.0
# <Manager => Tom Doe>
