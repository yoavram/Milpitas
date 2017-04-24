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

# References {-}