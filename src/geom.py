from oblique import *
 
if __name__ == '__main__':
    import sys
    w = float(sys.argv[1])    
    print("w={:.2g}".format(w))
    ρs = np.linspace(0.0, 1.0, 101, dtype=float)
    ρs[0] = 1e-10
    ks = np.arange(1, 51, 1, dtype=int)
    xAkBk = np.array([
        simulation(ρs, w, k_, k_, n=100000)
        for k_ in ks
    ])
    np.savez_compressed('xAkBk{:.1f}.npz'.format(w), xAkBk=xAkBk)
