from oblique import *
from uuid import uuid4 as uuid
import sys
import json

if __name__ == '__main__':
    w = float(sys.argv[1])
    k = int(sys.argv[2])
    l = int(sys.argv[3])
    
    print("k={}, l={}, w={}".format(k, l, w))
    # find optimal ρ, this time using minimization of geom_wbar_target
    print("find optimal ρ")
    max_ρ = max_ρ_with_polymorphism(w, k, l)
    if round(max_ρ, 7) == 0:
        opt_ρ = np.nan
    else:
        res = scipy.optimize.minimize_scalar(
            geom_wbar_target, args=(w, k, l), bounds=[0, max_ρ], method='bounded')
        if not res.success: 
            print('Minimization failed for w={}, k={}, l={}'.format(w, k, l))
            opt_ρ  = np.nan
        else:
            opt_ρ = res.x
    print("optimal ρ: {:.2g}".format(opt_ρ))
    # find an evolutionary stable ρ, if k!=l
    if k != l:
        print("find stable ρ")
        stable_ρ = evol_stable(w=w, k=k, l=l, reps=1, PRINT=True)    
        print("stable ρ: {:.2g}".format(stable_ρ))
    else: # bring it from stable_xxx.json
        stable_ρ = np.nan

    fname = 'table_{}.json'.format(uuid().hex)
    with open(fname, 'wt') as f:
        json.dump(
            dict(w=w, k=k, l=l, opt_ρ=opt_ρ, stable_ρ=stable_ρ),
            f
        )
        