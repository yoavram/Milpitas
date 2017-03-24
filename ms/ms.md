---
title: Evolution with Positive Feedback between Phenotype and Inheritance
author:
- Yoav Ram^[Department of Biology, Stanford University, Stanford, CA 94305-5020, yoav@yoavram.com]
- Uri Liberman^[School of Mathematical Sciences, Tel Aviv University, Tel Aviv, Israel 69978, uril@tauex.tau.ac.il]
- Marcus W. Feldman^[Department of Biology, Stanford University, Stanford, CA 94305-5020, mfeldman@stanford.edu; Corresponding author]
date: March 15, 2017 | v.0
year: 2017
abstract: |
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce non ex metus. Etiam tempor nisl at lorem facilisis, vel malesuada est mollis. Pellentesque nunc lacus, porttitor in mollis quis, pellentesque quis sem. Nunc consequat, elit vel tincidunt tincidunt, urna arcu efficitur turpis, ac mollis turpis velit vitae libero. Aenean mauris lacus, blandit a nulla a, scelerisque lobortis dolor. Etiam viverra, nibh vehicula vehicula congue, nisl dui mattis risus, quis convallis massa nisi quis elit. Maecenas gravida nunc nec dignissim consequat. Fusce scelerisque magna ut odio ullamcorper dapibus. Vivamus et dignissim nunc.
...

# Model
## Wright-Fisher model
We model evolution of a constant, finite size population with non-overlapping generations using a Wright-Fisher model  with natural selection, inheritance, and random genetic drift. This model is based on the simulation description in the final paragraph of the _Materials & Methods_ section of @Xue2016. Indeed, a simulation based on this model (<https://github.com/yoavram/Milpitas>) allowed us to reproduce Figure 2 of @Xue2016 ([@Fig:figure2_reproduction]).

![Reproduction of Figure 2 from @Xue2016. **A-C**: the average $\pi$ in the population over time and the distribution in blue; **D-F**: the effective population growth rate. **A,D**: the environment is randomly chosen at each generation such that P(A)=0.7 and P(B)=0.3; **B,E**: the environment flips between A and B, the duration of each is geometrically distributed with p=1/10 for A and p=1/5 for B; **C,F**: the environments flips every 40 generations. Parameters: _N_=100,000, # generations = 100, $\eta$=0.1, $W$=2, $w$=0.2.](figures/figure2_reproduction.pdf){#fig:figure2_reproduction}

### Definitions

- N: constant population size.
- $\phi_i$: phenotype of individual _i_, $1 \le i \le N, \phi_i \in \{A,B\}$.
- $\epsilon_t$: the environment at generation _t_, $\epsilon_t \in \{A, B\}$.
- $W$: individual fitness when phenotype and environment match, $\phi_i = \epsilon_t$.
- $w$: individual fitness when phenotype and environment do not match, $\phi_i \ne \epsilon_t$.
- $\omega_i$: fitness of individual _i_ at time _t_, $\omega_i=W \cdot 1_{\phi_i = \epsilon_t} + w \cdot 1_{\phi_i \ne \epsilon_t}$.
- $\bar{\omega}$: population mean fitness.
- $\pi_i$: phenotype probability, the probability that individual $i$ becomes phenotype _A_, $1 \le i \le N$.
- $\Pi$: set of phenotype probabilities in the population, $\Pi = \{ \pi_i \}_{1 \le i \le N}$
- $\eta$:  phenotypic inheritance rate, $0 \le \eta \le 1$.

### Reproduction 

For each offspring in the population of generation _t+1_ we choose a parent from the population of generation _t_ and this choice depends on the parent relative fitness: the probability that individual _i_ is the parent is relative to its fitness, $\omega_i$. Therefore, reproduction is modeled by a multinomial distribution. Therefore, reproduction includes the effects of natural selection and random genetic drift.

### Inheritance

The offspring inherits the phenotype probability of the parent with a modification -- if the parent became _A_, then the offspring is even more likely to be _A_; if the parent was _B_, then the offspring is less likely to be _A_. Specifically, for parent _k_ and offspring _i_:

$$
\pi_i = \pi_k \cdot (1-\eta) + \eta \cdot 1_{\phi_k=A}
$$ {#eq:learning_rule}

#### Note
The notation in [@Eq:learning_rule] is different from Eq. 1 in @Xue2016, as _i_ denotes individual, rather than phenotype. But the process is the same. 

#### Note
The expected difference between parent and offspring phenotype probability is $E[\pi_i - \pi_k | \pi_k] = 0$.

### Iteration

At each generation _t_, $\Pi$ is updated according to the following steps. Initial values can be determined (_i.e._, $\forall i, \; \pi_i=0.5$), or values can be drawn from an initial distribution (_i.e._, $\pi_i \sim TN(0.5, 0.05)$, _TN_ is the truncated normal distribution). In addition, the sequence $\epsilon_t$ is independent of the iteration on $Pi$.

At each generation _t_:

1. **Development**: the phenotypes of all individuals are drawn from corresponding Bernoulli distributions depending on their phenotype probabilities: $P(\phi_i=A)=\pi_i$.
1. **Fitness**: the fitness of all individuals is set: $\omega_i = W \cdot 1_{\phi_i=\epsilon_t}+ w \cdot 1_{\phi_i \ne \epsilon_t}$.
1. **Reproduction**: the number of offspring of each individual, $b_i$, is drawn from a multinomial distribution $MN(N, \{\frac{\omega_i}{\sum_i{\omega_i}}\}_{1 \le i \le N})$, such that 
$$
P(b_1 =x_1, \ldots, b_N=x_N)=\frac{N!}{x_1! \cdot \ldots \cdot x_N!}\cdot \Big(\frac{\omega_1}{\sum_i{\omega_i}}\Big)^{x_1} \cdot \ldots \cdot \Big(\frac{\omega_N}{\sum_i{\omega_i}}\Big)^{x_N}
$$.
1. **Inheritance**: the set of phenotype probabilities of the offspring generation is updated using [@Eq:learning_rule] such that for each $i$, $\Pi$ includes exactly $b_i$ copies of $(\pi_i \cdot (1-\eta) + \eta \cdot 1_{\phi_i=A})$.

#### Note
Only development and reproduction are stochastic; natural selection and drift occur at the reproduction step.

#### Note
If $\eta=0$, $\pi_i \in \{0,1\}$, and $\epsilon_t \equiv A$, then we have a standard single locus bi-allelic selection-drift Wright-Fisher model.

## Recurrence equation

We approximate the Wright-Fisher model using a recurrence equation. This approximation is most suitable when the population is composed of a single lineage -- for example, when selection is extreme and there is a common ancestor.

Define _x_ to be the probability that a random individual in the population is _A_. What is _x'_, the probability that a random offspring of that individual is _A_?

Assuming an "infinite" population undergoing exponential growth, this depends on (i) if the parent was _A_ or _B_, with probabilities _x_ and _1-x_, (ii) on the relative contribution of _A_ and _B_ phenotypes to the next generation in terms of fitness, and (iii) on the probability that offspring of _A_ or _B_ phenotypes eventually become _A_, according to the inheritance process ([@Eq:learning_rule]):

$$
x' = x \cdot \frac{\omega_A}{\bar{\omega}} \cdot ((1-\eta)x+\eta) + (1-x) \cdot \frac{\omega_B}{\bar{\omega}} \cdot (1-\eta)x
$$

Where $\omega_A$ and $\omega_B$ are the fitness of phenotypes _A_ and _B_ in the current generation (depending on $\epsilon_t$).

When we write a similar recurrence for the probability that an individual is _B_ ($(1-x)' = F(1-x)$) and sum the two equations, we find that $\bar{\omega} = x \omega_A + (1-x) \omega_B$ is the mean fitness.

This recurrence equation can be reorganized to:

$$
x' = x \frac{x (1-\eta) (\omega_A - \omega_B) + \eta \omega_A + (1-\eta)\omega_B}{x (\omega_A-\omega_B) + \omega_B}
$$ {#eq:recurrence0}

# Results

To be continued...

# References
