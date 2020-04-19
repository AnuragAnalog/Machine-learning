#!/usr/bin/python3

class Matrix():
    def __init__(self, row, col):
        self.col = col
        self.row = row
        self.matrix = []
        self.zeroes()

    def __str__(self):
        return "Rows:"+str(self.row)+" Columns:"+str(self.col)

    def __getitem__(self, indices):
        if isinstance(indices, list):
            indices = tuple(indices)
        elif isinstance(indices, int):
            return self.matrix[indices]
        elif not isinstance(indices, tuple):
            print("Datatype not understood")
            return

        if len(indices) == 2:
            row, col = indices[0], indices[1]
            tmp = self.matrix[row][col]
        else:
            print("Matrix is only two dimensional")

        return tmp

    def __setitem__(self, indices, value):
        if isinstance(indices, list):
            indices = tuple(indices)
        elif isinstance(indices, int):
            self.matrix[indices] = value
        elif not isinstance(indices, tuple):
            print("Datatype not understood")
            return

        if len(indices) == 2:
            row, col = indices[0], indices[1]
            self.matrix[row][col] = value
        else:
            print("Matrix is only two dimensional")

        return

    def __compute(self, value1, value2, oper):
        expr = str(value1) + oper + str(value2)

        return eval(expr)

    def __apply_operation_complete(self, mat, oper):
        new_mat = list()
        for i in range(self.row):
            tmp = list()
            for j in range(self.col):
                value = self.__compute(self.matrix[i][j], mat[i][j], oper)
                tmp.append(value)
            new_mat.append(tmp)

        return new_mat

    def __apply_operation_row_wise(self, mat, oper):
        pass

    def __apply_operation_column_wise(self, mat, oper):
        pass

    def __apply_operation_partially(self, mat, oper):
        pass

    def __return_error(self, oper, mat):
        error = "unsupported operand type(s) for "+oper+": 'Matrix' and "
        other_type = str(type(mat)).split()[1][1:-2]

        return error + other_type

    def __add__(self, mat):
        if isinstance(mat, Matrix):
            if (self.row, self.col) == mat.get_dimension():
                new_mat = self.__apply_operation_complete(mat, "+")
            elif self.row == mat.get_row() and self.col != 1:
                pass
            elif self.row != 1 and self.col == mat.get_col():
                pass
            elif self.row != mat.get_row() and self.col != mat.get_col():
                pass
            return new_mat
        else:
            return self.__return_error("+", mat)

    def __mul__(self, mat):
        if isinstance(mat, Matrix):
            if (self.row, self.col) == mat.get_dimension():
                new_mat = list()
                for i in range(self.row):
                    tmp = list()
                    for j in range(self.col):
                        tmp.append(self.matrix[i][j]*2)
                    new_mat.append(tmp)
            return new_mat
        else:
            return self.__return_error("*", mat)

    def transpose(self,  inplace=False):
        tmp_mat = Matrix(self.col, self.row)
        for i in range(self.row):
            for j in range(self.col):
                tmp_mat[j][i] = self.matrix[i][j]

        if inplace:
            # self.matrix = tmp_mat.copy()
            tmp_mat = None

        return tmp_mat

    def get_trace(self):
        if self.row == self.col:
            trace = 0
            for i in range(self.row):
                trace += self.matrix[i][i]
            return trace
        else:
            return "Trace is only defined for square matrices"

    def get_dimension(self):
        return (self.row, self.col)

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def zeroes(self):
        self.matrix = [[0 for i in range(self.row)] for j in range(self.col)]

    def ones(self):
        self.matrix = [[1 for i in range(self.row)] for j in range(self.col)]

    def random(self):
        pass

    def shuffle(self):
        pass

    def sum(self, axis=-1):
        matrix_sum = 0
        if axis == -1:
            for i in range(self.row):
                for j in range(self.col):
                    matrix_sum += self.matrix[i][j]
        elif axis == 0:
            pass
        elif axis == 1:
            pass

        return matrix_sum

    def reshape(self, indices):
        if isinstance(indices, tuple):
            if self.row * self.col == indices[0] * indices[1]:
                pass
            else:
                print("Matrix cannot be reshaped")
        else:
            print("Datatype not understood")

if __name__ == "__main__":
    mat = Matrix(3, 3)
    print(mat.matrix)

    mat1 = Matrix(2, 5)
    mat
    # print(mat1.transpose())
    