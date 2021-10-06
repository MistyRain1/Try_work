#please read README.md before using

from math import*


class SecantMethod:
    ls = ["exp", "pow", "sqrt"]  #表达式中支持使用的函数的函数名

    def __init__(self, v, ex, x0, x1, ac):
        self.variable = v
        self.expression = ex
        self.value0 = x0
        self.value1 = x1
        self.accuracy = ac
        self.unchanged_variable = v  #不会被修改的变量名
        self.flag = 1  #判断表达式是否合法的标志

    def change_variable_name(self):  #变量名统一改为x
        for n in self.ls:
            if self.variable in n:  #防止变量名与math库中的函数相关时，使得下面的变量名统一出现问题
                self.variable = self.variable + 'other'
                self.expression = self.expression.replace(variable, variable+'other')

        self.expression = self.expression.replace(self.variable, 'x')  #变量名统一

    def calculation(self, val, s):  #计算函数值
        x = val
        try:
            value = eval(s)
        except:
            self.flag = 0  #表达式非法
            return -1
        else:
            return value

    def func(self):
        acc = round(log(self.accuracy, 10))  #精度，保留小数点后acc位
        t1, t2 = self.value0, self.value1
        i = 1
        #精度达到要求或迭代次数超过100时跳出循环，防止死循环
        while not(t1-t2 <= self.accuracy and t2-t1 <= self.accuracy) or i > 100:
            tmp = t2
            t2 = t2 - (t2-t1)*self.calculation(t2, self.expression) / \
                (self.calculation(t2, self.expression)-self.calculation(t1, self.expression))
            t1 = tmp

            if self.flag == 1:  #判断表达式是否合法
                i = i+1
                print(self.unchanged_variable + "{} = {}".format(i, t2))
            else:
                print("Invalid input")
                break

            if i == 101:  #迭代次数达到100后跳出
                print("Fail to get the result.")
                flag = 0
                break

        if self.flag == 1:
            print("x = {}".format(round(t2, -acc)))  #输出结果，即根的近似值


if __name__ == "__main__":
    variable = input("please input the variable name:")  #输入/指定变量名
    expression = input("please input the expression:")  #输入函数表达式
    value0, value1 = map(float, input("please input the initial value, separating with space:").split())  #输入初始值
    accuracy = eval(input("please input expected accuracy:"))  #输入期望精度

    f = SecantMethod(variable, expression, value0, value1, accuracy)
    f.change_variable_name()
    f.func()
