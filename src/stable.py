from oblique import *
from uuid import uuid4 as uuid
import json
import sys

if __name__ == '__main__':    
    w = float(sys.argv[1])
    k = int(sys.argv[2])
    l = k      
    ρ = 0.5#evol_stable(w=w, k=k, l=k, reps=1, PRINT=True)
    fname = 'stable_{}.json'.format(uuid().hex)
    with open(fname, 'wt') as f:
    	json.dump(
            dict(w=w, k=k, l=l, ρ=ρ),
            f
        )
