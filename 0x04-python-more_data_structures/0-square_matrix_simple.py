#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        squares = []
        for row in matrix:
            squared_row = [element * element for element in row]
            squares.append(squared_row)
        return squares
