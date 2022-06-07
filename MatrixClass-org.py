from fractions import Fraction as F


class Matrix:
    def __init__(self, *rows):
        self.rows = [[F(j) for j in i] for i in rows]
        self.pivots = []
        for i in self.rows:
            for cc, j in enumerate(i):
                if j != 0:
                    break
            else:
                self.pivots.append(cc + 1)
                continue
            self.pivots.append(cc)

    def __str__(self):
        return '\n'.join(' '.join(str(j) for j in i) for i in self.rows)

    def __repr__(self):
        return self.__str__()

    def __mul__(self, other):
        mat = []
        for j in self.rows:
            for c in zip(*other.rows):
                s = 0
                for jj, cc in zip(j, c):
                    s += jj * cc
                mat.append(s)
        c = len(self.rows)
        return Matrix(*[*zip(*[mat[i::c] for i in range(c)])])

    def __add__(self, other):
        return Matrix(*[[self.rows[i][j] + other.rows[i][j] for j in range(len(self.rows[i]))] for i in range(len(self.rows))])

    def __sub__(self, other):
        return Matrix(*[[self.rows[i][j] - other.rows[i][j] for j in range(len(self.rows[i]))] for i in range(len(self.rows))])

    def ref(self):
        d = {c: i for c, i in enumerate(self.pivots)}
        dd = sorted(d, key=lambda i: d[i])
        mat = [self.rows[i] for i in dd]
        return Matrix(*mat)

    def rref(self):
        nmat = self.ref()
        mat = nmat.rows
        p = nmat.pivots
        for con in range(len(mat)):
            row = mat[con]
            for c in range(len(mat)):
                i = mat[c]
                if c == con:
                    continue
                rem = i[p[con]] / row[p[con]] * -1
                for cc in range(len(i)):
                    mat[c][cc] += rem * row[cc]
            nmat = Matrix(*mat)
            mat = nmat.rows
            p = nmat.pivots

        for c in range(len(mat)):
            rem = F(1) / mat[c][p[c]]
            for j in range(len(mat[c])):
                mat[c][j] *= rem

        return Matrix(*mat)

    def invert(self):
        ln = len(self.rows)
        imat = Matrix.identity(ln).rows
        nmat = [i + j for i, j in zip(self.rows, imat)]
        invmat = Matrix(*nmat).rref().rows
        inv = Matrix(*[i[ln:] for i in invmat])
        if (inv * self).rows != Matrix.identity(ln).rows:
            return False
        return inv

    def det(self):
        mat = self.rows
        if len(mat) == 2:
            return mat[1][1] * mat[0][0] - mat[0][1] * mat[1][0]
        row = mat.pop(0)
        s = 0
        for c, i in enumerate(row):
            nmat = mat.copy()
            nmat = [*zip(*nmat)]
            del nmat[c]
            s += Matrix(*[*zip(*nmat)]).det() * i * (-1) ** c
        return s


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
