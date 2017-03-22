from math import sin, cos, pi
from matrix import *

def circx(x, t, r):
    return r * cos(2 * pi * t) + x

def circy(y, t, r):
    return r * sin(2 * pi * t) + y

def add_circle(matrix, x, y, z, r):
    return draw_parametric(matrix, x, y, z, r, circx, circy, 0.01)

def cubicx(x, t, c):
    #xc is x coefficients
    xc = c[0]
    return (xc[0] * (t ** 3)) + (xc[1] * (t ** 2)) + (xc[2] * t) + xc[3] 

def cubicy(y, t, c):
    #yc is y coefficients
    yc = c[1]
    return (yc[0] * (t ** 3)) + (yc[1] * (t ** 2)) + (yc[2] * t) + yc[3]

def add_curve(matrix, type, vals):

    xdata = vals[::2]
    ydata = vals[1::2]
    
    xc = get_coefficients(type, xdata)
    yc = get_coefficients(type, ydata)

    coeffs = [xc, yc]

    return draw_parametric(matrix, vals[0], vals[1], 0, coeffs, cubicx, cubicy, 0.01) 

def draw_parametric(matrix, x, y, z, data, fx, fy, step = 0.01):
    t = 0.0
    #tx0, ty0, tx1, ty1 = 0.0
    stop = 1.001

    tx0 = fx(x, 0, data)
    ty0 = fy(y, 0, data)

    while t <= stop:
        tx1 = fx(x, t, data)
        ty1 = fy(y, t, data)
        
        matrix = add_edge(matrix, tx0, ty0, 0, tx1, ty1, 0)
        
        tx0 = tx1
        ty0 = ty1
        t += step
    return matrix

def get_coefficients(type, vals):
    #values will be p0, p1, m0, m1 for hermite and p0, p1, p2, p3 for bezier
    m = []
    m.append(vals)

    coefficients = []
    if type == "h":
        coefficients = mtrx_mult(m, hermite_mtrx())
    elif type == "b":
        coefficients = mtrx_mult(m, bezier_mtrx())

    return coefficients[0]
