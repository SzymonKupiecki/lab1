import math
import numpy as np
def cylinder_area(r:float,h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r < 0 or h < 0:
        return None
    return 2*math.pi*r*r + 2*math.pi*r*h

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    if n <= 0:
        return None
    if n == 1:
        return np.array([0])
    if n == 2:
        return np.array([0,1])
    fibo = [0,1]
    for x in range(n):
        if x == 0 or x == 1:
            continue
        else:
            fibo.append((fibo[x-1]+fibo[x-2]))
    return np.array(fibo)

def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    m = np.array([[a,1,-a],[0,1,1],[-a,a,1]])
    mt = np.matrix.transpose(m)
    mdet = np.linalg.det(m)
    if mdet == 0:
        minv = None
    else:
        minv = np.linalg.inv(m)
    return (minv,mt,mdet)

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if m <= 0 or n <=0:
        return None
    matrix = np.zeros((m,n))
    for x in range(m):
        for y in range(n):
            if x > y:
                matrix[x,y] = x
            else:
                matrix[x,y] = y
    return matrix