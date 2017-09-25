from oblique import *

if __name__ == '__main__':
    import sys
    w = float(sys.argv[1])
    ks = np.arange(1, 51, 1)
    print("w={:.2g}".format(w))
    ρs = np.array([evol_stable(w=w, k=k, l=k, reps=50, PRINT=False) for k in ks])
    df = pd.DataFrame(dict(ρ=ρs, k=ks))
    df.to_csv('evol_stable_w{:.1f}.csv'.format(w))
