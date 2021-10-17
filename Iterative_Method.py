# please read README.md before using
import numpy as np
# import cv2 as cv


class Method:
    def __init__(self, size, A_arr, b_arr, initial):
        self.size = size
        self.A = np.array(A_arr)
        self.A = self.A.reshape((size, size))
        self.b = np.array(b_arr)
        self.x0 = np.array(x0)
        self.iter_matrix = np.zeros((size, size+1), dtype=float)  #迭代矩阵
        for i in range(size):
            beta = self.A[i, i]
            self.iter_matrix[i, 0:-1] = self.A[i, :] / (-beta)
            self.iter_matrix[i, i] = 0
            self.iter_matrix[i, -1] = self.b[i] / beta

    def dsolve(self, flag='J'):
        if flag == 'J':  # 雅可比迭代法
            self.J_iter()
        elif flag == 'B-S':  # 高斯-塞德尔迭代法
            self.B_S_iter()
        else:
            print("illegal sign")

    def J_iter(self):  # 雅可比迭代法
        print("Jacobi Iterative Method:")
        iter_m = self.iter_matrix
        iter_v = np.ones(size+1)
        iter_v[0: -1] = self.x0
        temp = iter_v.copy() + 1
        i = 1
        # dur = 0.0  # 记录计算时间(不包括输出消耗的时间)
        # start = cv.getTickCount()
        # x(k+1)-x(k)的无穷范数小于10**(-4)时结束迭代
        while np.linalg.norm((iter_v - temp)[0: -1], ord=np.inf) >= 10e-5 and i <= 1000:
            temp = iter_v.copy()
            iter_v[0: -1] = np.matmul(iter_m, iter_v)

            # end = cv.getTickCount()
            # dur = dur + (end - start) / cv.getTickFrequency()
            print("x{} = [".format(i), end='')
            print(iter_v[0: -1], end=']')
            if i % 3 == 0:
                print()
            else:
                print(' ', end='')
            i = i+1
            # start = cv.getTickCount()
        if (i-1) % 3 != 0:
            print()
        print("x* = ", end='')
        print(iter_v[0: -1])
        # print('J\'s consumption is {:.20f}s'.format(dur))

    def B_S_iter(self):
        print("Gauss-Seidel Iterative Method:")
        iter_m = self.iter_matrix
        iter_v = np.ones(size + 1)
        iter_v[0: -1] = self.x0
        temp = iter_v.copy() + 1
        i = 1
        # dur = 0.0  # 记录计算时间(不包括输出消耗的时间)
        # start = cv.getTickCount()
        # x(k+1)-x(k)的无穷范数小于10**(-4)时结束迭代
        while np.linalg.norm((iter_v - temp)[0: -1], ord=np.inf) >= 10e-5 and i <= 1000:
            temp = iter_v.copy()
            for j in range(self.size):
                iter_v[j] = np.matmul(iter_m[j, :], iter_v)

            # end = cv.getTickCount()
            # dur = dur + (end - start) / cv.getTickFrequency()
            print("x{} = [".format(i), end='')
            print(iter_v[0: -1], end=']')
            if i % 3 == 0:
                print()
            else:
                print(' ', end='')
            i = i+1
            # start = cv.getTickCount()
        if (i-1) % 3 != 0:
            print()
        print("x* = ", end='')
        print(iter_v[0: -1])
        # print('B-S\'s consumption is {:.20f}s'.format(dur))


if __name__ == "__main__":
    size = int(input("please input the size of the coefficient matrix:"))
    A_arr = list(map(float, input("please input the coefficient matrix:").split()))
    b_arr = list(map(float, input("please input the vector b:").split()))
    x0 = list(map(float, input("please input x0:").split()))
    d = Method(size, A_arr, b_arr, x0)
    d.dsolve('J')
    d.dsolve('B-S')

