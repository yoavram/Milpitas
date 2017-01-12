% Evolution of Learning
% Yoav Ram, Uri Liberman, and Marcus W. Feldman
% Jan 12, 2017, v.2

# Models

## Wright-Fisher model

Here we explicitly formulate the model of -@Xue2016. This will follow how we understand their simulations (final paragraph of _Materials & Methods_) and how I implemented our simulations using a Wright-Fisher model.

### Definitions

- N: constant population size.
- $\phi_i$: phenotype of individual _i_, $1 \le i \le N, \phi_i \in \{A,B\}$.
- $\epsilon_t$: the environment in generation _t_, $\epsilon_t \in \{A, B\}$. This is a sequence of Bernoulli random variables.
- $\omega^+$: individual fitness when phenotype and environment match $\phi_i = \epsilon_t$.
- $\omega^-$: individual fitness when phenotype and environment do not match $\phi_i \ne \epsilon_t$.
- $\omega_i$: fitness of individual _i_ at time _t_, $\omega_i=\omega^{+}$ if $\phi_i = \epsilon_t$ and $\omega_i=\omega^-$ otherwise.
- $\bar{\omega}$: population mean fitness.
- $\pi_i$: phenotype choice, the probability that individual $i$ becomes phenotype _A_, $1 \le i \le N$.
- $\eta$:  learning rate or non-genetic inheritance parameter, $0 \le \eta \le 1$. 


### Reproduction 

For each offspring in the population of generation _t+1_ we choose a parent from the population of generation _t_ and this choice depends on the parent relative fitness: the probability that individual _i_ is the parent is relative to its fitness, $\omega_i$. Therefore, reproduction is modeled by a multinomial distribution.

### Inheritance

The inheritance of the phenotype choice follows this "learning" rule for parent _k_ and offspring _i_:
$$
\pi_i = \pi_k \cdot (1-\eta) + \eta \cdot 1_{\phi_k=A}
$$
The offspring inherits the phetnoype choice of the parent with a modification: if the parent became _A_, then the offspring is even more likely to be _A_; if the parent was _B_, then the offspring is less likely to be _A_.

Note that the notation here is different from Eq. 1 in @Xue2016, as _i_ denotes individual, rather than phenotype. But the process is the same. 

### Iteration

At each generation _t_ the **set of phenotype choices** in the population, $\Pi_t = \{ \pi_i \}_{1 \le i \le N}$, is updated accoring to the following steps. Initial values can be determined (_i.e._, $\forall i \; \pi_i=0.5$), or values can be drawn from an initial distribution (_i.e._, $\pi_i \sim TN(0.5, 0.05)$, _TN_ is the truncated normal distribution). In addition, the sequence $\epsilon_t$ is given and is independent of the iteration.

At each time _t_:

1. **Development**: the phenotypes of all individuals are drawn from corresponding Bernoulli distributions: $P(\phi_i=A)=\pi_i$.
2. **Fitness**: the fitness of all individuals is set: $\omega_i = \omega^+ \cdot 1_{\phi_i=\epsilon_t}+ \omega^- \cdot 1_{\phi_i \ne \epsilon_t}$.
3. **Reproduction**: the number of offspring of each individual, $b_i$, is drawn from a multinomial distribution $MN(N, \{\omega_i/\bar{\omega}\}_{1 \le i \le N})$, such that $P(b_1 =x_1, …, b_N=x_N)=\frac{N!}{x_1! \cdot … \cdot x_N!}\cdot (\frac{\omega_1}{\sum_i{\omega_i}})^{x_1} \cdot … \cdot (\frac{\omega_N}{\sum_i{\omega_i}})^{x_N}$.
   1. **Inheritance**: the set of phenotype choices of the offspring generation, $\Pi_{t+1}$, is updated using Eq. 2 such that for each $i$, $\Pi_{t+1}$ includes exactly $b_i$ copies of $(\pi_i \cdot (1-\eta) + \eta \cdot 1_{\phi_i=A})$.

Note that only development and reproduction are stochastic, natural selection and drift occur at the reproduction step, and inheritance 

If $\eta=0$ and we only allow $\pi_i \in \{0,1\}$  and $\epsilon_t=A$, then we have a standard single locus bi-allelic selection-drift Wright-Fisher model.

## Thoughts

I think that the following notations can be useful for developing a tractable analysis of the Wright-Fisher model. 

The idea is that $X_t$ is the histogram of $\Pi_t$ and $Y_t$ counts the number of _A_ phenotypes.

- $X_t$: a sequence of random variables corresponding to the probability that a random individual at time _t_ will become  _A_; $ֿ\forall x \in [0,1], \; P(X_t= x)=\frac{|\{\pi_i\in\Pi_t | \pi_i = x\}|}{N}$.
- $Y_t$: the number of individuals with phenotype _A_ at time _t_, $\sum_i {1_{\phi_i=A}}$. This is a [Poisson binomial random variable](https://en.wikipedia.org/wiki/Poisson_binomial_distribution) , $Y_t \sim PB(\Pi_t)$, and we have $E[Y_t|X_t] =N\cdot E[X_t]$. 

I think that we would like to find a transformation $L$ such that $X_{t+1}=LX_t$ or else maybe $Y_{t+1} = LY_t$.

# Results

The following is a set of simulation results. The individual-based simulation follows the $\pi$ values of all individuals over time, and is true to the above model definition.

## Reproduction of previous results

We start by reproducing Fig. 2 from -@Xue2016:

![Original Figure 2 from -@Xue2016. Parameters: _N_=100,000, _n_=100, $\eta$=0.1, $\omega_0$=2, $\omega_1$=0.2.](figures/figure2_original.jpg){#fig:figure2_original}

The top row in [@Fig:figure2_original] shows the average $\pi$ in the population over time and the distribution in blue, the bottom row the effective population growth rate.

The different columns represent 3 environments, used throughout this document.

- Left panel - the environment is randomly chosen at each generation such that P(A)=0.7 and P(B)=0.3.
- Middle panel - the environment flips between A and B, the duration of each is geometrically distributed with p=1/10 for A and p=1/5 for B.
- Right panel - the environments flips every 40 generations.

The population is initialized such that $\Pi_0 \sim Normal(0.5, 0.05)$.

![Figure 2 reproduction](figures/figure2_reproduction.pdf){#fig:figure2_reproduction}

# Modifier competition

We now extend the model:

1. There are two learning modifiers $\eta_1, \eta_2$, that can have different values. Each individual has one and only one of these modifiers.
1. Mutations in the modifier loci, with probability $\kappa$, convert $\eta_i$ to $\eta_j$.

[@Fig:modifiers_eta0.1_eta0_kappa0] shows the dynamics from  with competition between modifiers.

![Learning rate modifiers competition with $\eta_1=0.1, \eta_2=0, \kappa=0$](figures/modifiers_eta0.1_eta0_kappa0.pdf){#fig:modifiers_eta0.1_eta0_kappa0}

The top row in [@Fig:modifiers_eta0.1_eta0_kappa0] shows the population mean $\pi$ over time in yellow and the distribution in blue. The bottom row shows the population mean $\eta$ over time. The three columns represent the environments (see below).

[@Fig:modifiers_eta0.1_eta0_kappa0.001] shows the dynamics from  with competition between modifiers with mutation between the modifier alleles.

![Learning rate modifiers competition with $\eta_1=0.1, \eta_2=0, \kappa=0.001$](figures/modifiers_eta0.1_eta0_kappa0.001.pdf){#fig:modifiers_eta0.1_eta0_kappa0.001}

### Multiple competitions

[@Fig:modifiers_eta0.1_eta0_kappa0;@Fig:modifiers_eta0.1_eta0_kappa0.001] show results of single simulations. Next, [@Fig:modifiers_eta1_0.1_eta2_0.2_kappa_0] shows the average result of multiple competitions between $\eta_1=0.1$ and $\eta_2=0.2$ with $\kappa=0$ in the three environments. 

![Multiple competitions between $\eta_1$=0.1 and $\eta_2$=0.2](figures/modifiers_eta1_0.1_eta2_0.2_kappa_0.pdf){#fig:modifiers_eta1_0.1_eta2_0.2_kappa_0}

The black solid lines the the average $\pi$ (top) and $\eta$ (bottom) in the population. The blue lines represent randomly chosen single simulations, to represent variance.

The figures shows that
- Left panel: there is selection against learning after the population reached the "optimal" strategy.
- Right panel: there is selection for learning, and the dynamics are very much deterministic. Note that as long as the low learning rate modifier exists, it is briefly selected for following every environmental change, because it is more likely to be associated with advantageous $\pi$ values - this follows from the fact it was disadvantageous before the environmental change.
- Middle panel: requires longer simulations. See below.

## Diversity

We now look a the diversity of the population, in terms of $\pi$ values, when evolving in slowly changing environments (left panels in the above figures).

For tractability, the population now starts fixed at $\pi_i=0.5 \; \forall i$ and then evolves.

![Population $\pi$ diversity in a highly stochastic environment](figures/diversity_envA.pdf){#fig:diversity_envA}

[@Fig:diversity_envA] shows the richness (# of different value; top), true diversity (exponent of Shannon index, _i.e._ $exp(-sum_{\pi}{\log{(f(\pi))} f(\pi)})$ where $f(\pi)$ is the frequency of $\pi$ in the population); center) and average (bottom) of $\pi$ in the population.

How does the distribution of $\pi$ in the population changes during a single adaptation event? [@Fig:pi_distribution_in_env_change] shows the histogram of $pi$ following an environmental change that changes the optimal phenotype from _A_ to _B_, and therefore the optimal $\pi$ from 0 to 1. This figure shows that between adaptation events the distribution of $\pi$ is very narrow, since both selection and learning drive it in the same direction. During the adaptive event, the distribution shifts to 1, and it has a pronounced "front", which includes the individuals who are most likely to reach $\pi$=1 first. These organisms probably have the highest reproductive value, although before the environmental change they had the lowest reproductive value - "When Everybody Zigs, You Zag".

![Distribution of $\pi$ in a population undergoing adaptation](figures/pi_distribution_in_env_change.pdf){#fig:pi_distribution_in_env_change}

## Periodic environment

We now explore the dynamics in an environment that -@Xue2016 did not explore, a period environment that deterministically switches from _A_ to _B_ every generation - denoted _ABAB_ - or every other generation for environment _A_ - denoted _AABAAB_.

![Population mean $\pi$ in a deterministic and stochastic rapidly changing environments](figures/periodic_environment.pdf){#fig:periodic_environment}

The top row in [@Fig:periodic_environment] shows the dynamics in such deterministic periodic environments. The initial population distribution was uniform ($\Pi_0 \sim U(0,1)$), but in the symmetric environment _ABAB_ ([@Fig:periodic_environment]A) the population mean $\pi$ fluctuates around 0.5. In contrast, if the _A_ environment is more frequent than _B_, as in the _AABAAB_ environment ([@Fig:periodic_environment]B), than the population mean $\pi$ goes to 1, and the diversity in the population (given by the blue shading) becomes narrower with time.

The dynamics in a similar stochastic environments, in which the environment is drawn every generation with 1:1 odds for _A_ and _B_ ([@Fig:periodic_environment]C, similar to left panel in [@Fig:figure2_original]) or 2:1 odds ([@Fig:periodic_environment]D), are very similar, except that there seems to be more variance in [@Fig:periodic_environment]C, where stochastic consecutive _A_s can drive the population mean $\pi$ to a value significantly higher than 0.5. Note, however, that the population mean $\pi$ is also influenced by other stochastic events even when the environment is deterministic ([@Fig:periodic_environment]A), specifically, random genetic drift and phenotype choice.

# References
