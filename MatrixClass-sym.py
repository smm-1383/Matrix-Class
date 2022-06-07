from fractions import Fraction as F
import sympy as sp


class Matrix:
    def __init__(self, *rows):
        self.rows = [[F(j) for j in i] for i in rows]

    def __str__(self):
        return '\n'.join(' '.join(str(j) for j in i) for i in self.rows)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Matrix(*[[self.rows[i][j] + other.rows[i][j] for j in range(len(self.rows[i]))] for i in range(len(self.rows))])

    def __mul__(self, other):
        return Matrix(*[[self.rows[i][j] * other.rows[i][j] for j in range(len(self.rows[i]))] for i in range(len(self.rows))])

    def __sub__(self, other):
        return Matrix(*[[self.rows[i][j] - other.rows[i][j] for j in range(len(self.rows[i]))] for i in range(len(self.rows))])

    def rref(self):
        return Matrix.from_sympy(sp.Matrix(self.rows).rref()[0])

    def invert(self):
        return Matrix.from_sympy(sp.Matrix(self.rows).inv())

    def det(self):
        return sp.Matrix(self.rows).det()

    def get_row(self, row):
        return Matrix(self.rows[row])

    def get_col(self, col):
        return Matrix(*[[i[col]] for i in self.rows])

    def get_block(self, i1, i2):
        (x, y), (xx, yy) = i1, i2
        res = []
        for i in range(x, xx+1):
            r = []
            for j in range(y, yy+1):
                r.append(self.rows[i][j])
            res.append(r)
        return Matrix(*res)

    @classmethod
    def identity(cls, s):
        m = cls(*[[0]*s for _ in range(s)])
        for i in range(s):
            m.rows[i][i] = F(1)
        return m

    @classmethod
    def from_sympy(cls, mat):
        r, c = mat.shape
        res = []
        for i in range(r * c):
            frac = F(1, 1)
            d = mat[i].factors()
            for k in d:
                frac = frac * k ** d[k] if d[k] > 0 else frac / k ** abs(d[k])
            res.append(frac)
        return cls(*[*zip(*[res[i::c] for i in range(c)])])

    @classmethod
    def from_input(cls):
        r, c = [int(i) for i in input().split()]
        mat = []
        for i in range(r):
            mat.append([int(i) for i in input().split()])
        return cls(*mat)
