from oblique import *

if __name__ == '__main__':
    import sys
    w = float(sys.argv[1])    
    print("w={:.2g}".format(w))
    ks_ls = [
        (1, 1),
        (1, 2),
        (2, 2),
        (3, 10),
        (5, 30),
        (12, 12),
        (20, 20),
        (30, 30),
        (50, 50)
    ]     

    results = []
    for k, l in ks_ls:
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
        # find an evolutionary stable ρ
        print("find stable ρ")
        try:
            stable_ρ = evol_stable(w=w, k=k, l=l, reps=20, PRINT=False)
        except TypeError as e:            
            print(e)
            continue
        print("stable ρ: {:.2g}".format(stable_ρ))
        results.append(
            dict(w=w, k=k, l=l, opt_ρ=opt_ρ, stable_ρ=stable_ρ)
        )

    table = pd.DataFrame(results)
    table.to_csv('table_w{:.1f}.csv'.format(w))
