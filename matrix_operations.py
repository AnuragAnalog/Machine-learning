#!/usr/bin/python3

class Matrix():
    def __init__(self, row, col):
        self.col = col
        self.row = row
        self.matrix = [[i+j for i in range(self.col)] for j in range(self.row)]

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

        if len(indices) in range(1, 3):
            tmp = self.matrix.copy()
            for ind in indices:
                tmp = tmp[ind]

        return tmp

    def __add__(self, mat):
        if isinstance(mat, Matrix):
            if (self.row, self.col) == mat.get_dimension():
                new_mat = list()
                for i in range(self.row):
                    tmp = list()
                    for j in range(self.col):
                        tmp.append(self.matrix[i][j]+2)
                    new_mat.append(tmp)
            return new_mat
        else:
            error = "unsupported operand type(s) for +: 'Matrix' and "
            other_type = str(type(mat)).split()[1][1:-2]
            return error+other_type

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
            error = "unsupported operand type(s) for *: 'Matrix' and "
            other_type = str(type(mat)).split()[1][1:-2]
            return error+other_type

    def transpose(self):
        tmp_mat = self.matrix.copy()
        for i in range(self.col):
            for j in range(self.row):
                self.matrix[i][j] = tmp_mat[j][i]
        return self.matrix

    def get_dimension(self):
        return (self.row, self.col)

if __name__ == "__main__":
    mat = Matrix(3, 3)

    print(mat[2, 2])
    