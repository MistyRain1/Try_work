# please read README.md before using
import numpy as np


class Method:
    def __init__(self, size, A_arr, b_arr):
        self.size = size
        self.A = np.array(A_arr)
        self.A = self.A.reshape((size, size))  # 系数矩阵
        self.b = np.array(b_arr)  # 矩阵b
        self.A_b = np.zeros((size, size+1), dtype=float)  # 增广矩阵
        self.x = np.zeros(size, dtype=float)  # 解向量
        for i in range(size):
            self.A_b[i, 0:-1] = self.A[i, :]
            self.A_b[i, -1] = self.b[i]

    def dsolve(self, flags='n'):  # 列主元素高斯消去法 核心算法
        # 获得阶梯行矩阵
        A_b = self.A_b
        for i in range(self.size-1):
            max_row = i  # 记录当前列中绝对值最大的数所在行
            for j in range(i+1, self.size):  # 找到当前列中绝对值绝对值最大的数所在行
                if abs(A_b[j][i]) > abs(A_b[max_row][i]):
                    max_row = j
            if max_row != i:  # 交换行
                A_b[(i, max_row), :] = A_b[(max_row, i), :]
            for k in range(i+1, self.size):  # 得到阶梯形矩阵
                A_b[k, :] -= (A_b[k, i] / A_b[i, i]) * A_b[i, :]

        # 回代求解
        for j in range(self.size):  # 得到反序的解向量(只是为了写起来方便点)  i+j = self.size-1
            self.x[j] = A_b[-(j+1), -1]  # 取得对应行的b值
            for k in range(j):  # a(i,i)*x(i) = b(i) - Σa(i,k)*x(k)
                self.x[j] -= A_b[-(j+1), -(k+2)]*self.x[k]
            self.x[j] = self.x[j] / A_b[-(j+1), -(j+2)]  # 除以系数得到x(i)
        self.x = self.x[::-1]  # 颠倒顺序，得到解向量

        if flags == 'y':  # 用户选择是否输出阶梯形矩阵
            print(self.A_b)
        print("x =", self.x)  # 输出解向量


if __name__ == "__main__":
    size = int(input("please input the size of the coefficient matrix:"))
    A_arr = list(map(float, input("please input the coefficient matrix:").split()))
    b_arr = list(map(float, input("please input the vector b:").split()))
    flag = input("whether output the simplified matrix:[Y/N]").lower()
    m = Method(size, A_arr, b_arr)
    m.dsolve(flag)
