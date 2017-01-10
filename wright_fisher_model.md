# Explicit Wright-Fisher model 

## Jan 9, 2017



I will explicitly formulate the model of Xue & Leibler 2016. This will follow how I understand their simulations (final paragraph of _Materials & Methods_) and how I implented my version of their simulations using a Wright-Fisher model.

#### Definitions

- N: constant population size.
- $\phi_i$: phenotype of individual _i_, $1 \le i \le N, \phi_i \in \{A,B\}$.
- $\epsilon_t$: the environment in generation _t_, $\epsilon_t \in \{A, B\}$. This is a sequence of Bernoulli random variables.
- $\omega^+$: individual fitness when phenotype and environment match $\phi_i = \epsilon_t$.
- $\omega^-$: individual fitness when phenotype and environment do not match $\phi_i \ne \epsilon_t$.
- $\omega_i$: fitness of individual _i_; at time _t_, $\omega_i=\omega^+ $ if $\phi_i = \epsilon_t$ and $\omega_i=\omega^-$ otherwise.
- $\bar{\omega}$: population mean fitness.
- $\pi_i$: phenotype choice, the probability that individual $i$ becomes phenotype _A_, $1 \le i \le N$.
- $\eta$:  learning rate or nongenetic inheritance parameter, $0 \le \eta \le 1$. 


#### Reproduction 

For each offspring in the population of generation _t+1_ we choose a parent from the population of generation _t_ and this choice depends on the parent relative fitness: the probability that individual _i_ is the parent is relative to its fitness, $\omega_i$. Therefore, reproduction is modeled by a multinomial distribution.

#### Inheritance

The inheritance of the phenotype choice follows this "learning" rule for parent _k_ and offspring _i_:
$$
\pi_i = \pi_k \cdot (1-\eta) + \eta \cdot 1_{\phi_k=A}
$$
The offspring inherits the phetnoype choice of the parent with a modification: if the parent became _A_, then the offspring is even more likely to be _A_; if the parent was _B_, then the offspring is less likely to be _A_.

Note that the notation here is different from Eq. 1 in Xue2016, as _i_ denotes individual, rather than phenotype. But the process is the same. 

#### Iteration

At each generation _t_ the **set of phenotype choices** in the population, $\Pi_t = \{ \pi_i \}_{1 \le i \le N}$, is updated accoring to the following steps. Initial values can be determined (_i.e._, $\forall i \; \pi_i=0.5$), or values can be drawn from an initial distribution (_i.e._, $\pi_i \sim TN(0.5, 0.05)$, _TN_ is the truncated normal distribution). In addition, the sequence $\epsilon_t$ is given and is independent of the iteration.

At each time _t_:

1. **Development**: the phenotypes of all individuals are drawn from corresponding Bernoulli distributions: $P(\phi_i=A)=\pi_i$.
2. **Fitness**: the fitness of all individuals is set: $\omega_i = \omega^+ \cdot 1_{\phi_i=\epsilon_t}+ \omega^- \cdot 1_{\phi_i \ne \epsilon_t}$.
3. **Reproduction**: the number of offspring of each individual, $b_i$, is drawn from a multinomial distribution $MN(N, \{\omega_i/\bar{\omega}\}_{1 \le i \le N})$, such that $P(b_1 =x_1, …, b_N=x_N)=\frac{N!}{x_1! \cdot … \cdot x_N!}\cdot (\frac{\omega_1}{\sum_i{\omega_i}})^{x_1} \cdot … \cdot (\frac{\omega_N}{\sum_i{\omega_i}})^{x_N}$.
   1. **Inheritance**: the set of phenotype choices of the offspring generation, $\Pi_{t+1}$, is updated using Eq. 2 such that for each $i$, $\Pi_{t+1}$ includes exactly $b_i$ copies of $(\pi_i \cdot (1-\eta) + \eta \cdot 1_{\phi_i=A})$.

Note that only development and reproduction are stochastic, natural selection and drift occur at the reproduction step, and inheritance 

If $\eta=0$ and we only allow $\pi_i \in \{0,1\}$  and $\epsilon_t=A$, then we have a standard single locus bi-allelic selection-drift Wright-Fisher model.

#### Thoughts

I think that the following notations can be useful for developing a tractable analysis of the above stochastic model. 

The idea is that $X_t$ is the histogram of $\Pi_t$ and $Y_t$ counts the number of _A_ phenotypes.

- $X_t$: a sequence of random variables corresponding to the probability that a random individual at time _t_ will become  _A_; $ֿ\forall x \in [0,1], \; P(X_t= x)=\frac{|\{\pi_i\in\Pi_t | \pi_i = x\}|}{N}$.
- $Y_t$: the number of individuals with phenotype _A_ at time _t_, $\sum_i {1_{\phi_i=A}}$. This is a [Poisson binomial random variable](https://en.wikipedia.org/wiki/Poisson_binomial_distribution) , $Y_t \sim PB(\Pi_t)$, and we have $E[Y_t|X_t] =N\cdot E[X_t]$. 

I think that we would like to find a transformation $L$ such that $X_{t+1}=LX_t$ or else maybe $Y_{t+1} = LY_t$ .


