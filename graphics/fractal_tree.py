from turtle import *
import random 
left(90)
speed(0)
bgcolor('white')
color('black')
len_variation = 0.0
title('Fractal Tree')
def tree(i):
    if i < 30:
        pass
    else:
        len_variation = random.uniform(0.5, 0.9)
        forward(i)
        left(30)
        tree(8.5 * (i/10))
        right(60)
        tree(8.5 * (i/10))
        left(30)
        backward(i)

tree(100)
done()
