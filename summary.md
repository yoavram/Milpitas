% Evolution of Learning
% Yoav Ram, Uri Liberman, and Marcus W. Feldman
% Jan 18, 2017, v.2

# Models

## Wright-Fisher model

Here we explicitly formulate the model of @Xue2016. This will follow how we understand their simulations (final paragraph of _Materials & Methods_) and how I implemented our simulations using a Wright-Fisher model.

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
$$ {#eq:learning_rule}

The offspring inherits the phenotype choice of the parent with a modification: if the parent became _A_, then the offspring is even more likely to be _A_; if the parent was _B_, then the offspring is less likely to be _A_.

Note that the notation in [@eq:learning_rule] is different from Eq. 1 in @Xue2016, as _i_ denotes individual, rather than phenotype. But the process is the same. 

### Iteration

At each generation _t_ the **set of phenotype choices** in the population, $\Pi_t = \{ \pi_i \}_{1 \le i \le N}$, is updated according to the following steps. Initial values can be determined (_i.e._, $\forall i \; \pi_i=0.5$), or values can be drawn from an initial distribution (_i.e._, $\pi_i \sim TN(0.5, 0.05)$, _TN_ is the truncated normal distribution). In addition, the sequence $\epsilon_t$ is given and is independent of the iteration.

At each time _t_:

1. **Development**: the phenotypes of all individuals are drawn from corresponding Bernoulli distributions: $P(\phi_i=A)=\pi_i$.
1. **Fitness**: the fitness of all individuals is set: $\omega_i = \omega^+ \cdot 1_{\phi_i=\epsilon_t}+ \omega^- \cdot 1_{\phi_i \ne \epsilon_t}$.
1. **Reproduction**: the number of offspring of each individual, $b_i$, is drawn from a multinomial distribution $MN(N, \{\omega_i/\bar{\omega}\}_{1 \le i \le N})$, such that 
$$
P(b_1 =x_1, …, b_N=x_N)=\frac{N!}{x_1! \cdot … \cdot x_N!}\cdot (\frac{\omega_1}{\sum_i{\omega_i}})^{x_1} \cdot … \cdot (\frac{\omega_N}{\sum_i{\omega_i}})^{x_N}
$$.
1. **Inheritance**: the set of phenotype choices of the offspring generation, $\Pi_{t+1}$, is updated using [@Eq:learning_rule] such that for each $i$, $\Pi_{t+1}$ includes exactly $b_i$ copies of $(\pi_i \cdot (1-\eta) + \eta \cdot 1_{\phi_i=A})$.

Note that only development and reproduction are stochastic, natural selection and drift occur at the reproduction step, and inheritance 

If $\eta=0$ and we only allow $\pi_i \in \{0,1\}$  and $\epsilon_t=A$, then we have a standard single locus bi-allelic selection-drift Wright-Fisher model.

## Recurrence equation {#sec:recurrence-equation}

This is an approximation of the model using a recurrence equation.

Define _x_ as the probability that a random individual in the population is _A_. What is _x'_, the probability that a random offspring of that individual is _A_?

Assuming an "infinite" population undergoing exponential growth, this depends on  (i) if the parent was _A_ or _B_, with probabilities _x_ and _1-x_, (ii) on the relative contribution of _A_ and _B_ to the next generation in terms of fitness, and (iii) on the probability that offspring of _A_ or _B_ are _A_, according to the "learning" rule:

$$
x' = x \cdot \frac{\omega_A}{\bar{\omega}} \cdot ((1-\eta)x+\eta) + (1-x) \cdot \frac{\omega_B}{\bar{\omega}} \cdot (1-\eta)x
$$

Where $\omega_A$ and $\omega_B$ are the fitness of phenotypes _A_ and _B_ in the current generation (depending on $\epsilon_t$).

When we write a similar recurrence for the probability that an individual is _B_ ($(1-x)' = F(1-x)$) and sum the two equations, we find that $\bar{\omega} = x \omega_A + (1-x) \omega_B$ is the mean fitness.

This recurrence equation can be reorganized to:

$$
x' = x \frac{x (1-\eta) (\omega_A - \omega_B) + \eta \omega_A + (1-\eta)\omega_B}{x (\omega_A-\omega_B) + \omega_B}
$$

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

We now explore the dynamics in an environment that -@Xue2016 did not explore, a periodic environment that deterministically switches from _A_ to _B_ every generation - denoted _ABAB_ - or every other generation for environment _A_ - denoted _AABAAB_.

![Population mean $\pi$ in a deterministic and stochastic rapidly changing environments](figures/periodic_environment.pdf){#fig:periodic_environment}

The top row in [@Fig:periodic_environment] shows the dynamics in such deterministic periodic environments. The initial population distribution was uniform ($\Pi_0 \sim U(0,1)$), but in the symmetric environment _ABAB_ ([@Fig:periodic_environment]A) the population mean $\pi$ fluctuates around 0.5. In contrast, if the _A_ environment is more frequent than _B_, as in the _AABAAB_ environment ([@Fig:periodic_environment]B), than the population mean $\pi$ goes to 1, and the diversity in the population (given by the blue shading) becomes narrower with time.

The dynamics in a similar stochastic environments, in which the environment is drawn every generation with 1:1 odds for _A_ and _B_ ([@Fig:periodic_environment]C, similar to left panel in [@Fig:figure2_original]) or 2:1 odds ([@Fig:periodic_environment]D), are very similar, except that there seems to be more variance in [@Fig:periodic_environment]C, where stochastic consecutive _A_s can drive the population mean $\pi$ to a value significantly higher than 0.5. Note, however, that the population mean $\pi$ is also influenced by other stochastic events even when the environment is deterministic ([@Fig:periodic_environment]A), specifically, random genetic drift and phenotype choice.

### Analytic approximation

We use the recurrence equation [@Sec:recurrence-equation] to study deterministic 1-period environments(_ABABAB_) such that:

$$
x^{'} = x \frac{x (1-\eta) (\omega_A - \omega_B) + \eta \omega_A + (1-\eta)\omega_B}{x (\omega_A-\omega_B) + \omega_B}
$${#eq:recurrence1}

$$
x^{''}=x' \frac{x' (1-\eta) (\omega_B - \omega_A) + \eta \omega_B + (1-\eta)\omega_A}{x' (\omega_B-\omega_A) + \omega_A}
$${#eq:recurrence2}

Note that here $\omega_A$ and $\omega_B$ are the fitness of _A_ and _B_ in the initial generation, and the changes in fitness are baked in to the equations.

We are looking for a solution to $x''=x$, which evaluates to a quartic polynomial. Two solutions are 0 and 1 (assign to [@Eq:recurrence1]), but there are two more potential solutions solutions, such that 

$$
0=x''-x=x(1-x)G(x),
\;\;\;
G(x)=Ax^2+Bx+C
$$

Using [SymPy](http://sympy.org/), a Python library for symbolic mathematics, a free alternative to Wolfram Mathematica™[@SymPyDevelopmentTeam2014], we find all four solution of $x''-x=0$:

$$
0=x''- x = x(1-x)(x^2 - \frac{\omega_A (1-\eta) - \omega_B (3-\eta)}{(2-\eta)(\omega_A - \omega_B)} x - \frac{\omega_B}{(2-\eta)(\omega_A - \omega_B)})
$$

or 

$$
G(x) = x^2 - \frac{\omega_A (1-\eta) - \omega_B (3-\eta)}{(2-\eta)(\omega_A - \omega_B)} x - \frac{\omega_B}{(2-\eta)(\omega_A - \omega_B)}
$$

Assume $\omega_A , \omega_B >0, 0 \le \eta \le 1$. If $\omega_A>\omega_B$:

$$
G(0) = \frac{-\omega_B}{(2-\eta)(\omega_A - \omega_B)} < 0
$$

$$
G(1) = 
1 - \frac{\omega_A (1-\eta) - \omega_B (3-\eta)}{(2-\eta)(\omega_A - \omega_B)} - \frac{\omega_B}{(2-\eta)(\omega_A - \omega_B)} = \\
\frac{\omega_A}{(2-\eta)(\omega_A - \omega_B)} > 0
$$

and $lim_{x-> \pm \infty}{G(x)} = +\infty$.  If instead $\omega_B>\omega_A$, then $G(0)>0, G(1)<0$. 

Therefore, there are two roots to $G(x)$. If $\omega_A>\omega_B$, then one of them is negative and one of them, $\tilde{x}$, is positive and below 1. If $\omega_B>\omega_A$, then both are positive but only one of them, $\tilde{x}$,  is below 1.

Let $\delta=\frac{-B-\sqrt{B^2-4AC}}{2A}-\frac{-B+\sqrt{B^2-4AC}}{2A}$ (where _A_, _B_, _C_ are the coefficients of $G(x)$, defined in eq. 3). Then, $\delta=\frac{\sqrt{(\omega_A+\omega_B)^2-\eta(2-\eta)(\omega_A-\omega_B)^2}}{(2-\eta)(\omega_A-\omega_B)}$. Because $\eta(2-\eta)$ is maximized at 1, 

$$
(\omega_A+\omega_B)^2-\eta(2-\eta)(\omega_A-\omega_B)^2 > (\omega_A+\omega_B)^2-(\omega_A-\omega_B)^2=4\omega_A\omega_B  >0
$$

so $sign(\delta)=sign(\omega_A-\omega_B)$. Therefore, is $\omega_A>\omega_B$, then $\frac{-B-\sqrt{B^2-4AC}}{2A}$ is the positive root; if $\omega_B>\omega_A$, then $\frac{-B-\sqrt{B^2-4AC}}{2A}$ is the smaller root; either way, $\tilde{x}=\frac{-B-\sqrt{B^2-4AC}}{2A}$.


[@Fig:deterministic_periodic_environment] shows $\tilde{x}$ in dashed lines and the numerical iteration of [@Eq:recurrence1; @Eq:recurrence2] in solid lines for a several combinations of $\eta, \omega_A, \omega_B$. All iterations started with $x(0)=0.5$. Note that the figure shows _x_ in **every other generation**.

![Analytic approximation (dashed line) to the evolution of $\bar{\pi}$ (solid line) in a deterministic 1-period environment (_ABABAB_).](figures/deterministic_periodic_environment.pdf){#fig:deterministic_periodic_environment}

## Bet-hedging in stochastic rapidly changing environments

We next focus on stochastic environments that change every generation, such as in [@Fig:periodic_environment]C.

The authors [@Xue2016] argued that (notation slightly different from our notation, so $\pi_i$ is the probability to become phenotype _i_ and $p_i$ is the frequency of environment _i_):

> Now, suppose that the environment switches repeatedly during
> that timescale $\tau_{ad}$; _i.e._, the typical duration of an environment, $\tau_{env}$, is much shorter than $\tau_{ad}$. Then, through the learning mechanism, the phenotype probability distribution $\pi_i$ converges to a steady distribution $\pi_i^*$ and fluctuates around it... which yields $\pi_i^*=p_i$...

They presented analysis (eq. [3]) showing that when selection is extreme, $\bar{\pi}$ fluctuates around $p$, the empirical frequency of environment _A_. The analysis is presented in Materials and Methods (eq. [10]) and assumes both extreme selection (fitness in the unfavorable environment is 0) and $\eta \ll 1$ via eq. [13]. 
In addition, they analyze the case of non-extreme selection (see SI), and suggest that $\bar{\pi}$ fluctuates around $\pi^*$ which satisfies (see eq. S6 in SI):

$$
pi_i^* = \sum_{j}{p_j \frac{\omega_i^j \pi_i^*}{\sum_k{\omega_k^j \pi_k^*}}}
$$

where the outer sum is over the different environments/phenotypes, $p_j$ is the frequency of environment _j_, $\pi_j$ is the probability for becoming phenotype _j_, and $\omega_i^j$ is the fitness of phenotype _i_ in environment _j_ (note this notation is different from the one proposed here).

First, we solve the above equation for two environments, _A_ and _B_, to find that for $0 < p_A < 1, \omega_A \ne \omega_B$:

$$
\pi^* = \frac{p \omega_0 - (1 - p) \omega_1}{\omega_0 - \omega_1}
$$

where $p_A$ is the frequency of environment _A_, $\omega_0$ is the fitness of phenotype _i_ in environment _i_, and $\omega_1$ is the fitness of phenotype _i_ in environment _i_ ($i \ne j$).

Second, we focus on environments in which the environment is drawn at every generation from a coin flip with 70% for A and 30% for B. Population size N=100,000, initial $\pi_A$ values for each individual is drawn from $Norm(0.5, 0.05)$, and the fitness of individuals is $\omega_0=2.0$ in a favorable environment and $\omega_1 = 0.2$ or $0.0$ in an unfavorable environment. These values result in $\pi_A^*$ = 0.7 or 0.744, respectively.

We look at simulations with different learning rates $\eta$ and look at $\bar{\pi}_A$, the population mean value of $\pi_A$, over time.

![$\bar{\pi}_A$ over time for different $\eta$ values (columns) and extreme (bottom) or non-extreme (top) selection ($\omega_1 =0$ or $0.2$, respectively). The red lines represent $\pi_A^*$, the blue lines represent $p_A$, the empirical frequency of environment _A_.](bethedging_timeseries.png){#fig:bethedging_timeseries}

With extreme selection ([@Fig:bethedging_timeseries], bottom row) $\bar{\pi}_A$ does seem to fluctuate around $p_A=0.7$ (blue dashed lines), and fluctuations increase with $\eta$. This is in accordance with [@Xue2016].

With non-extreme selection ([@Fig:bethedging_timeseries], top row), $\bar{\pi}_A$ (black lines for multiple simulations) fluctuates around $\pi_A^*=0.744...$ (red lines) which is **higher** then $p_A=0.7$ (blue lines). 
These fluctuations increase with $\eta$ (from $\eta=0$ in the leftmost panel to $\eta=0.1$ in second panel from the right), except for $\eta=1$ for which almost all individuals are $\pi_A=1$ (rightmost panel). 

We also examine the histograms of $\bar{\pi}_A$ in the above simulations, but only for $t>250$, so that we ignore the time required for the population to adapt from $\bar{\pi}_A \approx 0.5$ to $\bar{\pi}_A \approx \pi_A^*$.

![Histograms of  $\bar{\pi}_A$ in multiple simulations](bethedging_histograms.png){#fig:bethedging_histograms}

The layout [@Fig:bethedging_histograms] is the same as [@Fig:bethedging_timeseries], but it shows histograms of $\bar{\pi}_A$ for _t>250_. The red line represent $\pi_A^*$, and the blue dashed lines represent $p_A$. Note that columns have different x-scale; we can get an impression of relative x-scales from the y-scales in [@Fig:bethedging_timeseries].

With extreme selection ([@Fig:bethedging_histograms], bottom), indeed $\bar{\pi}_A$ fluctuates around $p_A=0.7$ as the histograms are more or less centered around 0.7 (dashed blue line), as expected from [@Xue2016].

With non-extreme selection, the histograms are not centered around $p_A=0.7$ but rather around $\pi_A^*=0.744...$, which does not coincide with $p_A=0.7$ ([@Fig:bethedging_timeseries], bottom panel).

### Optimality 

@Xue2016 assert that this $\pi^*$ is an optimal bet-hedging strategy:

> ... the proposed learning mechanism enables the population to reach the **optimal phenotype distribution for bet hedging**. Eq. 3 also implies that the phenotype distribution $\pi_i$ converges to the optimal distribution exponentially, following the direction of fastest adaption.

"Optimality" is explained in _Materials and Methods_, where they show the optimal strategy maximizes the _asymptotic growth rate_ of a population (Eq. 11):

$$
\Lambda(\pi) = \sum_j p_j \Big(\log{\sum_i{\pi_i \omega_i^j} \Big)}
$$

This $\Lambda(\pi)$ term is the time averaged _Malthusian fitness_ [@Orr2009].

We checked this optimality criterion by competing _N_=100000 individuals with an initial uniform distribution of $\pi$ values (such that there are initially 100 individuals with each $\pi \in \{\frac{k}{999} | 0 \le k \le 999 \})$ and with $\eta=0$ so that any change in frequencies of $\pi$ values can only be attributed to natural selection and genetic drift.

[@Fig:bethedging_competitions] shows the $\bar{\pi}$ in yellow, dispersion in blue, $p$ (frequency of environment _A_) in black, and $\pi^*$ in red.
$\bar{pi}$ indeed converges to $\pi^*$, which means that individuals that were initially $\pi^*$ out-compete individuals with other $\pi$ values, and therefore $\pi^*$ represents an evolutionary optimal bet-hedging strategy.

![Competitions between different $\pi$ strategies in rapidly changing environments; $\eta=0, N=1,000,000$ means that change in frequencies mainly due to natural selection.](figures/bethedging_competitions.pdf){#fig:bethedging_competitions}

# References
