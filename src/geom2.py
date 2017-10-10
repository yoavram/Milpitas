from uuid import uuid4 as uuid
import numpy as np
from oblique import max_ρ_with_polymorphism, geom_wbar_target, optimal_ρ
import scipy.optimize


if __name__ == '__main__':
	ks = np.arange(1, 51, 1, dtype=int)
	ws = np.array([0.1, 0.5, 0.9])

	ρs = np.empty((ws.size, ks.size))
	for i, w in enumerate(ws):
		for j, k in enumerate(ks):
			print("w={}, k={}, l={}".format(w, k, k))
			ρs[i, j] = optimal_ρ(w, k, k)
			print("ρ={}".format(ρs[i, j]))
	fname = 'optimal_ρ_{}.npz'.format(uuid().hex)
	np.savez_compressed(fname, ks=ks, ws=ws, ρs=ρs)
