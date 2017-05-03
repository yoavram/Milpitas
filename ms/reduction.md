---
title: Reduction principle for learning rate model
chapters: True
chaptersDepth: 1
chapDelim: ""
---

We start with the recurrence equation we developed for the model of @Xue2016 (I changed $x$ to $\pi$ to avoid confusion with the formulation of @Altenberg2017):

$$
\pi' = \pi \cdot \frac{\omega_A}{\bar{\omega}} \cdot ((1-\eta)\pi+\eta) + (1-\pi) \cdot \frac{\omega_B}{\bar{\omega}} \cdot (1-\eta)\pi
$$ {#eq:recurrence}

Assume two modifier loci $M$ and $m$ that induce learning rates $\eta^*$ and $\eta$. Denote $x=(\pi_M, 1-\pi_M)$ the frequency of phenotype _A_ with modifier _M_ and $y =(\pi_M, 1-\pi_m)$ the frequency of phenotype _A_ with modifier _m_. 

The boundary equilibrium $x^*=(\pi^*_M, 1-\pi^*_M)$ in which _M_ is fixed satisfies the equation (see Eq. 65 in @Altenberg2017):
$$
[\eta^* I + (1-\eta^*) S]Dx^* = x^*
$$ {#eq:eq65}
where **I** is the identity matrix, **S** is a positive column-stochastic matrix:
$$
S =  \begin{bmatrix}
\pi^*_M & \pi^*_M \\
1-\pi^*_M & 1-\pi^*_M
 \end{bmatrix},
$$ {#eq:S}
and **D** is the diagonal matrix:
$$
D = diag\Big(\frac{\omega_A}{\bar{\omega}^*}, \frac{\omega_B}{\bar{\omega}^*}\Big),
$$ {#eq:D}
where $\bar{\omega}^*$ is the equilibrium population mean fitness $\bar{\omega}^* = \pi^*_M \omega_A + \pi^*_M \omega_B$.

Since there is no recombination in the model ($r=0$), if we substitute $\sigma = 1-\eta$ then $L^*_{ex} = [(1-\sigma) I + \sigma S]D$ with **S** and **D** satisfying the conditions of _Karlin's theorem_.

This means that the spectral radius of $L^*_{ex}$ is strictly **increasing** when $\eta$ increases. $\eta$ controls how much of the phenotype is inherited from the genotype ($\pi$) and how much is inherited from the phenotype. With $\eta=1$, the phenotype is fully-inherited and there is essentially no plasticity, which makes sense in a constant environment. In a rapidly and randomly changing environment, however, we expect that once the optimal bet-hedging strategy $\pi^*=P(\epsilon_t=A)$ is reached the learning rate will be **reduced**, this doesn't make sense, but I guess that for that we need to define **D** (@Eq:D) differently.

@Xue2016 have shown numerically (in SI) that with extreme selection, in a rapidly changing environment, $\eta^* \to 0$, whereas if environmental changes are farther apart (>9), then $\eta^* > 0$. This was done by maximizing mean fitness, which has been shown (@Carja2014) to fit with simulation results in analyses of evolution of stable modification rates.

There has been a body of work on models in which the phenotype is genetically encoded by two alleles (_A_ and _a_) and the transition between these alleles is determined by a mutation modifier allele [see summary in @Liberman2011]. In these models, under fluctuating environment, the evolutionary stable mutation rate is ~1/n if the favored allele changes deterministicly every _n_ generations, but can be different if _n_ is random or if selection is not symmetric. In the model presented in @Xue2016, however, the phenotype switching rate is (epi)genetically encoded, and mutation is not needed for transitioning between the phenotypes. Moreover, the transition rate is modified by the phenotype (@Eq:learning_rule). If  we assume that the rate of this modification, $\eta$, is determined by a modifier locus, then the dynamics of alleles at this modifier locus are different from those of a mutation modifier locus.



# References {-}