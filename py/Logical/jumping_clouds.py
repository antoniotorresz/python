#from https://www.hackerrank.com/challenges/jumping-on-the-clouds/
def jumpingOnClouds(c):
    jumps = 1
    i = 0
    while i < len(c) - 3:
        if c[i + 2] == 0: 
            jumps += 1
            i += 2
        elif c[i + 1] == 0:
            jumps += 1
            i += 1
    return jumps
print(jumpingOnClouds([0, 0, 1, 0, 0, 0, 0, 1, 0, 0]))
