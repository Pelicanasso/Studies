'''
    NumPy is a library that can be add to python, create to scientific computing in python:

    - A powerful object of array n-dimensional
    - Sofisticated Function
    - Ferramentas para intergras código c/c++ e Fortran
    - Recursos úteis de álgebra linear, transformação de Fourier e números aleatórios

'''

import numpy

matriz_1_1 = numpy.array([1, 2, 3]) #creating a array with 1 row and 1 collum
matriz_2_2 = numpy.array([[1, 2], [3, 4]]) #create a array with 2 rows and 2 collums
matriz_3_3 = numpy.array([[1, 2, 3], [4, 5, 6]])#create a array with 2 rows and 3 collums
matriz_2_4 = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]])#creata a array with 2 rows ans 4 collums
matriz_4_2 = numpy.array([[1, 2], [3, 4], [5, 6], [7, 8]])#create a array with 4 rows and 2 collums

print(f"Tipo da Matriz = {type(matriz_1_1)}")
print("\n", matriz_1_1)
print('\n', matriz_2_2)
print('\n', matriz_3_3)
print('\n', matriz_2_4)
print('\n', matriz_4_2)

print("\n======================================================================\n")

m1 = numpy.zeros((3, 3)) #crete a array 3x3 only with zeros
m2 = numpy.ones((4, 4)) #creatre a array 4x4 only with ones
m3 = numpy.eye(4) #create array 4x4 identity
m4 = numpy.random.randint(low=0, high=100, size=10).reshape(2, 5) #create a array 2x5 with random int numbers

print(f"numpy.zeros((3, 3)) =\n {m1}\n")
print(f"numpy.ones((4, 4)) =\n {m2}\n")
print(f"numpy.eye(4) = \n{m3}\n")
print(f"numpy.random.randint =\n {m4}\n")

print(f"\nA soma dos valores em m4 = {m4.sum()}")
print(f"Valor mínimo em m4 = {m4.min()}")
print(f"Valor máximo em m4 = {m4.max()}")
print(f"Média dos valores em m4 = {m4.mean()}")

