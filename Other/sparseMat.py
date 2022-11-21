'''
https://stackoverflow.com/questions/65154662/defining-matrix-class-in-python
https://medium.com/data-structures-and-algorithms-with-python/sparse-matrix-implementation-with-python-11d1314fa987
'''

# from __future__ import annotations
from typing import List, Dict
import copy


class sparceMat:
    '''2d matrix'''
    def __init__(self, nrow, ncol, matDic: Dict):
        self.nrow = nrow
        self.ncol = ncol
        self.mat = matDic
        # self.defVal = 0  # if matDic is empty, it's a mxn default val

    def __str__(self):
        strings = []
        for (row, col), val, in self.mat.items():
            strings.append(f'row {row}, col {col}, val {val}')
        return '\n'.join(strings)
    
    def __len__(self):
        return int(self.nrow * self.ncol)

    def __getitem__(self, point):
        row, col = point
        if (row, col) in self.mat:
            return self.mat[(row, col)]
        else:
            return 0

    def __setitem__(self, point, val):
        row, col = point
        self.mat[(row, col)] = val

    @classmethod
    def from_dense(cls, rawMat: [List[List[int]] or List[List[str]]]):
        '''covert raw Mat to dic
        '''
        nrow, ncol = len(rawMat), len(rawMat[0])
        mat = dict()
        for rowID, row in enumerate(rawMat):
            for colID, val in enumerate(row):
                if val:  # not 0 or None
                    mat[(rowID, colID)] = val
        return cls(nrow, ncol, mat)

    @classmethod
    def from_sparce(cls, nrow, ncol, matDic):
        return cls(nrow, ncol, matDic)

    def set_val(self, row, col, val):
        assert 0 <= row < self.nrow and 0 <= col < self.ncol, "rol and col must in range"
        self.mat[(row, col)] = val
    
    def get_val(self, row, col):
        assert 0 <= row < self.nrow and 0 <= col < self.ncol, "rol and col must in range"
        return self.mat[(row, col)]

    def reset(self):
        self.mat = dict()

    def to_dense(self):
        '''uncompress'''
        rawMat = [[0] * self.ncol for _ in range(self.nrow)]
        for (row, col), val in self.mat.items():
            rawMat[row][col] = val
        return rawMat

    def __matmul__(self, M: 'sparceMat'):
        assert self.ncol == M.nrow, "shape mismatch"
        # mat1: mxn, mat2: nxp -> output: mxp
        # out[i][j] = mat1[i][k] * mat2[k][j]  (k in range(N))
        mat1 = self.mat
        mat2 = M.mat
        outDict = dict()
        # get mat1's row1, k
        # get mat2's k, col2
        for (row1, k), val1, in mat1.items():
            for col2 in range(M.ncol):
                if (k, col2) in mat2:
                    val2 = mat2[(k, col2)]
                    outDict[(row1, col2)] = outDict.get((row1, col2), 0) + val1 * val2
        
        return self.from_sparce(self.nrow, M.ncol, outDict)

    def __add__(self, M: 'sparceMat'):
        assert self.ncol == M.ncol, "col shape mismatch"
        assert self.nrow == M.nrow, "row shape mismatch"
        mat1 = self.mat
        mat2 = M.mat
        outDict = copy.deepcopy(mat1)

        for (row2, col2), val2, in mat2.items():
            outDict[(row2, col2)] = outDict.get((row2, col2), 0) + val2
        
        return self.from_sparce(self.nrow, M.ncol, outDict)


# Mul
A = [[1,0,0],[-1,0,4]]
B = [[7,0,0],[0,0,0],[0,0,1]]

A = sparceMat.from_dense(A)
B = sparceMat.from_dense(B)
ANS1 = A @ B
print(ANS1.to_dense())


# Add
C = [[7,0,0],[0,0,0],[0,0,1]]
D = [[0,1,0],[0,1,0],[0,-1,0]]
C = sparceMat.from_dense(C)
D = sparceMat.from_dense(D)
ANS2 = C + D
print(ANS2.to_dense())

# set val
C.set_val(0, 0, 9)
ANS3 = C + D
print(ANS3.to_dense())

# check inner functions
print(C[0, 0])
print(C)
len(C)
