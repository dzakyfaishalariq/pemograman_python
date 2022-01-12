import numpy as np
a, b, c, d = 10, 0o12, 0xA, 0b1010
print('konversi : ')
print('{}-desimal\n{}-oktal\n{}-heksadesimal\n{}-biner'.format(a, b, c, d))
o = np.array([1, 2, 3])
i = np.array([5, 4, 7])
print(o-i)
h1 = {'a', 'b'}
h2 = {'c', 'd'}
print(type(h1))
k = set([1, 2, 3, 4])
print(k)
mat1 = [[1, 2, 3],
        [2, 3, 4]]
print(np.array(mat1))
