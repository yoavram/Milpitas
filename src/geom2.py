from uuid import uuid4 as uuid
import numpy as np
from oblique import max_ρ_with_polymorphism, geom_wbar_target
import scipy.optimize

def optimal_ρ(w, k, l):    
    max_ρ = max_ρ_with_polymorphism(w, k, l)
    if np.isclose(max_ρ, 0):
        return np.nan
    res = scipy.optimize.minimize_scalar(
        geom_wbar_target, args=(w, k, l), bounds=[0, max_ρ], method='bounded')
    if not res.success: 
        print('Minimization failed for w={}, k={}, l={}'.format(w, k, l))
        return np.nan
    return res.x

if __name__ == '__main__':
	ks = np.arange(1, 51, 1, dtype=int)
	ws = np.array([0.1, 0.5, 0.9])

	ρs = np.empty((ws.size, ks.size))
	for i, w in enumerate(ws):
		for j, k in enumerate(ks):
			print("w={}, k={}, l={}".format(w, k, k))
			ρs[i, j] = optimal_ρ(w, k, k)
			print("ρ={}".format(ρs[i, j]))
	fname = 'geom2_{}.npz'.format(uuid().hex)
	np.savez_compressed(fname, ks=ks, ws=ws, ρs=ρs)
