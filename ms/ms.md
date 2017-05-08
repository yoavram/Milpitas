---
title: Evolution with Positive Feedback between Phenotype and Inheritance
author:
- Yoav Ram^[Department of Biology, Stanford University, Stanford, CA 94305-5020, yoav@yoavram.com]
- Uri Liberman^[School of Mathematical Sciences, Tel Aviv University, Tel Aviv, Israel 69978, uril@tauex.tau.ac.il]
- Marcus W. Feldman^[Department of Biology, Stanford University, Stanford, CA 94305-5020, mfeldman@stanford.edu; Corresponding author]
year: 2017
abstract: |
    TODO
chapters: True
chaptersDepth: 1
chapDelim: ""
---

# Model {-}
## Wright-Fisher model

We model evolution of a constant, finite size population with non-overlapping generations using a Wright-Fisher model [@Otto2007, ch. 13.4]  with natural selection, inheritance, and random genetic drift. This model is based on the simulation description in the final paragraph of the _Materials & Methods_ section of @Xue2016. Indeed, a simulation based on this model (<https://github.com/yoavram/Milpitas>) allowed us to reproduce Figure 2 of @Xue2016 ([@Fig:figure2_reproduction]).

![Reproduction of Figure 2 from @Xue2016. **A-C**: the average $\pi$ in the population over time and the distribution in blue; **D-F**: the effective population growth rate. **A,D**: the environment is randomly chosen at each generation such that P(A)=0.7 and P(B)=0.3; **B,E**: the environment flips between A and B, the duration of each is geometrically distributed with p=1/10 for A and p=1/5 for B; **C,F**: the environments flips every 40 generations. Parameters: _N_=100,000, # generations = 100, $\eta$=0.1, $W$=2, $w$=0.2.](figures/figure2_reproduction.pdf){#fig:figure2_reproduction}

### Definitions

- N: constant population size.
- $\phi_i$: phenotype of individual _i_, $1 \le i \le N, \phi_i \in \{A,B\}$.
- $\epsilon_t$: the environment at generation _t_, $\epsilon_t \in \{A, B\}$.
- $W$: individual fitness when phenotype and environment match, $\phi_i = \epsilon_t$.
- $w$: individual fitness when phenotype and environment do not match, $\phi_i \ne \epsilon_t$.
- $\omega_{\phi}$: fitness of phenotype $\phi$ at time _t_, $\omega_{\phi}=W \cdot 1_{\phi = \epsilon_t} + w \cdot 1_{\phi \ne \epsilon_t}$.
- $\bar{\omega}$: population mean fitness.
- $\pi_i$: phenotype probability, the probability that individual $i$ becomes phenotype _A_, $1 \le i \le N$.
- $\Pi$: set of phenotype probabilities in the population, $\Pi = \{ \pi_i \}_{1 \le i \le N}$
- $\eta$:  phenotypic inheritance rate, $0 \le \eta \le 1$.

### Reproduction 

For each offspring in the population of generation _t+1_ we choose a parent from the population of generation _t_ and this choice depends on the parent relative fitness: the probability that individual _i_ is the parent is relative to its fitness, $\omega_{\phi_i}$. Therefore, reproduction is modeled by a multinomial distribution. Therefore, reproduction includes the effects of natural selection and random genetic drift.

### Inheritance

The offspring inherits the phenotype probability of the parent with a modification -- if the parent became _A_, then the offspring is even more likely to be _A_; if the parent was _B_, then the offspring is less likely to be _A_. Specifically, for parent _k_ and offspring _i_:

$$
\pi_i = \pi_k \cdot (1-\eta) + \eta \cdot 1_{\phi_k=A}
$$ {#eq:learning_rule}

#### Notes
1. The notation in @Eq:learning_rule is different from Eq. 1 in @Xue2016, as _i_ denotes individual, rather than phenotype. But the process is the same. 
1. The expected difference between parent and offspring phenotype probability is $E[\pi_i - \pi_k | \pi_k] = 0$.

### Iteration

At each generation _t_, $\Pi$ is updated according to the following steps. Initial values can be determined (_i.e._, $\forall i, \; \pi_i=0.5$), or values can be drawn from an initial distribution (_i.e._, $\pi_i \sim TN(0.5, 0.05)$, _TN_ is the truncated normal distribution). In addition, the sequence $\epsilon_t$ is independent of the iteration on $\Pi$.

At each generation _t_:

1. **Development**: the phenotypes of all individuals are drawn from corresponding Bernoulli distributions depending on their phenotype probabilities: $P(\phi_i=A)=\pi_i$.
1. **Fitness**: the fitness of all individuals is set: $\omega_{\phi_i} = W \cdot 1_{\phi_i=\epsilon_t} + w \cdot 1_{\phi_i \ne \epsilon_t}$.
1. **Reproduction**: the number of offspring of each individual, $b_i$, is drawn from a multinomial distribution $MN(N, \{\frac{\omega_{\phi_i}}{\sum_i{\omega_{\phi_i}}}\}_{1 \le i \le N})$, such that 
$$
P(b_1 =x_1, \ldots, b_N=x_N)=\frac{N!}{x_1! \cdot \ldots \cdot x_N!}\cdot \Big(\frac{\omega_{\phi_1}}{\sum_i{\omega_{\phi_i}}}\Big)^{x_1} \cdot \ldots \cdot \Big(\frac{\omega_{\phi_N}}{\sum_i{\omega_{\phi_i}}}\Big)^{x_N}.
$$
1. **Inheritance**: the set of phenotype probabilities of the offspring generation is updated using @Eq:learning_rule such that for each $i$, $\Pi$ includes exactly $b_{i}$ copies of $(\pi_i \cdot (1-\eta) + \eta \cdot 1_{\phi_i=A})$.

#### Notes
1. Only development and reproduction are stochastic; natural selection and drift occur at the reproduction step.
1. If $\eta=0$, $\pi_i \in \{0,1\}$, and $\epsilon_t \equiv A$, then we have a standard single locus bi-allelic selection-drift Wright-Fisher model.

## Recurrence equation

We present a deterministic population analog of the individual above model. This recurrence equation model is equivalent to the Wright-Fisher model when the population is composed of a single lineage -- for example, when selection is extreme and there is a common ancestor.

Define _x_ to be the probability that a random individual in the population is _A_. What is _x'_, the probability that a random offspring is _A_?

Assuming an "infinite" population undergoing exponential growth, this depends on (i) if the parent was _A_ or _B_, with probabilities _x_ and _1-x_, (ii) on the relative contribution of _A_ and _B_ phenotypes to the next generation in terms of fitness, and (iii) on the probability that offspring of parental _A_ or _B_ phenotypes eventually become _A_, according to the inheritance process ([@Eq:learning_rule]):

$$
x' = x \cdot \frac{\omega_A}{\bar{\omega}} \cdot ((1-\eta)x+\eta) + (1-x) \cdot \frac{\omega_B}{\bar{\omega}} \cdot (1-\eta)x,
$$ {#eq:recurrence}
where $\omega_A$ and $\omega_B$ are the fitness values of phenotypes _A_ and _B_ in the parental generation, depending on $\epsilon_t$ (@Fig:recurrence_example).

A similar recurrence for the probability that an individual is _B_  can be written ($(1-x)' = F(1-x)$); summing the two equations produces an expression for the mean fitness: $\bar{\omega} = x \omega_A + (1-x) \omega_B$.

@Eq:recurrence can be reorganized to:
$$
x' = x \frac{x (1-\eta) (\omega_A - \omega_B) + \eta \omega_A + (1-\eta)\omega_B}{x (\omega_A - \omega_B) + \omega_B}
$$ {#eq:recurrence0}

## Recurrence with two modifier alleles

Consider two modifier alleles _m_ and _M_ that induce rates $\eta$ and _H_,
and denote their frequencies by _p_ and _q_ ($p+q=1$). _x_ is the probability that a random individual with modifier allele _m_ is _A_,
and _y_ is that probability for a random individual with allele _M_:

|      | mA  | mB     | MA  | MB     |
|------|-----|--------|-----|--------|
| freq.    | $p \cdot x$  | $p(1-x)$ | $q \cdot y$  | $q(1-y)$ |
| fitness    | $\omega_A$ | $\omega_B$    | $\omega_A$ | $\omega_B$    |
| rate | $\eta$   | $\eta$      | _H_   | _H_      |

and therefore the population recurrence is (based on @eq:recurrence0):

$$\begin{aligned}
x' = x \frac{x (1-\eta) (\omega_A - \omega_B) + \eta \omega_A + (1-\eta)\omega_B}{\bar{\omega}_{m}} \\
y' = y \frac{y (1-H) (\omega_A - \omega_B) + H \omega_A + (1-H)\omega_B}{\bar{\omega}_{M}} \\
p' = p \frac{x \omega_A + (1-x) \omega_B}{\bar{\omega}} \\
q' = q \frac{y \omega_A + (1-y) \omega_B}{\bar{\omega}} \\
\bar{\omega} = p \bar{\omega}_{m}  + q \bar{\omega}_{M} \\
\bar{\omega}_{m} = x \omega_A + (1-x) \omega_B \\
\bar{\omega}_{M} = y \omega_A + (1-y) \omega_B
\end{aligned}$$ {#eq:recurrence_modifiers}

# Results {-}

## Constant environment

We start with a constant environment $\epsilon_t=A \; \forall t$, such that $\omega_A = W > w = \omega_B$. 

### Special cases

- Neutral evolution: If $W = w$ then any $x \in [0,1]$ solves $x'=x$.
- No phenotype feedback on inheritance: If $\eta = 0$ then any $x \in [0,1]$ solves $x'=x$.

### General case

If $\eta > 0$ and $\omega_A > \omega_B$, then $x = 1$ is the only solution for $x'=x$ and the recurrence converges to $x = 1$ for any initial $x>0$.

#### Proof

Rewrite @eq:recurrence0 as $x' = x \cdot \frac{f(x)}{g(x)}$ with $f(x) = (1-\eta)(\omega_A - \omega_B)x + \eta \omega_A + (1-\eta)\omega_B$ and $g(x) = (\omega_A - \omega_B)x + \omega_B$.

Clearly, $x'=x$ if and only if $f(x)=g(x)$ or $x=0$. 
However, _f_ and _g_ are both linear in _x_ and therefore can only intersect at one point.
Indeed, _f_ and _g_ intersect at $x=1$: $f(1)=g(1)=\omega_A$, which means that $x=1$ solves $x'=x$. 
Since $f(0) = \omega_B + \eta(\omega_A + \omega_B) > \omega_B = g(0)$, we can deduce that $\forall x<1, \; f(x) > g(x) \Rightarrow x' > x$.

Therefore, $x \to x'$ is strictly monotone transformation in $x \in (0,1)$ (@Fig:recurrence_example), and the recurrence converges to 1 for any initial value $0 < x< 1$. $\blacksquare$

## Periodic environmental regime

Consider periodic environmental regimes in which both environments occur exactly the same number of generations in each "period". Simple examples are _A1B1=ABABABAB..._, in which the environment switches every generation every generation from _A_ to _B_ and vice versa, or _A2B1=AABAABAAB..._ in which the every two _A_s are followed by a single _B_. In general, _AkBl_ denotes an environmental regime in which the period is of length _k+l_ and composed of exactly _k_ generations of environment _A_ followed by _l_ generations on environment _B_ (however, our general result applies for any permutation of these _k+l_ environments).

@Fig:env_period_overview shows the evolution of the distribution of $\pi$ in a population evolving in three such environmental regimes.

![Distribution of $\pi$ in populations evolving in periodic environments. **(A)** A1B1, **(B)** A2B1, **(C)** A40B40. Parameters: _N_=100,000, $\eta$=0.01, $W$=1, $w$=0.1.](figures/env_period_overview.pdf){#fig:env_period_overview}

### _A1B1_ regime

When the environment changes every generation, we can write the following recurrence, which sets $\omega_A=W, \omega_B=w$ in [@Eq:recurrence0] to determine $x'$ and and then sets $\omega_A=w, \omega_B=W$ to determine $x''$:

$$\begin{aligned}
x' = x \frac{x (1-\eta) (W - w) + \eta W + (1-\eta)w}{x (W-w) + w} \\
x'' = x' \frac{x' (1-\eta) (w - W) + \eta w + (1-\eta)W}{x' (w-W) + W}
\end{aligned}$$ {#eq:recurrenceA1B1} 

We are looking for solutions for $x''=x$, which involves solving a quartic polynomial. Two solutions are $x=0,1$ (assign to [@Eq:recurrenceA1B1] to check), but there are two other potential solutions which are roots of a quadratic equation $G(x) = 0$ where $G(x) = Ax^2 + Bx + C$.

We found the roots of $G(x)$ using [SymPy](http://sympy.org/), a Python library for symbolic mathematics, a free alternative to Wolfram Mathematica™ [@SymPyDevelopmentTeam2014]. We can write:
$$
A = 1, \; B=- \frac{W (1-\eta) - w (3-\eta)}{(2-\eta)(W - w)}, \; C=- \frac{w}{(2-\eta)(W - w)}.
$$ {#eq:recurrenceA1B1_solution}

Since $W > w \ge 0, 1 \ge \eta \ge 0$,
$$
G(0) = C = \frac{-w}{(2-\eta)(W-w)} < 0
$$
and
$$\begin{aligned}
G(1) =
1 + B + C =
1 - \frac{W (1-\eta) - w (3-\eta) - w}{(2-\eta)(W-w)} = \\
\frac{W}{(2-\eta)(W-w)} > 0
\end{aligned}$$
and $lim_{x \to \pm \infty}{G(x)} = +\infty$.

Therefore, one root of $G(x)$ is negative and one, $x^*$, is positive and less than 1. $C<0$  and therefore $B < \sqrt{B^2-4C}$. Thus, $-B+\sqrt{B^2-4C}>0$ and $-B-\sqrt{B^2-4C}<0$, regardless of the sign of $B$, and:
$$\begin{aligned}
x^* = 
\frac{-B+\sqrt{B^2-4C}}{2} = & \\ &
\frac{W(1-\eta) - w(3-\eta) + \sqrt{(1-\eta)^2 (W-w)^2 + 4Ww}}{2 (2-\eta) (W-w)}
\end{aligned}$$ {#eq:recurrenceA1B1_solution_x_star}

Note that $\eta=0 \Rightarrow x^* = 1/2$ and $\eta=1 \Rightarrow x^* = \frac{-w + \sqrt{Ww}}{(W-w)}$. 

@Fig:env_A1B1 compares $x^*$ (dashed green; @eq:recurrenceA1B1_solution_x_star) with $x$ from iteration of @Eq:recurrenceA1B1 (blue) and with the population mean $\pi$ ($\bar{\pi}$) in Wright-Fisher simulations (orange) for several combinations of $\eta, W, w$. All iterations started with $\bar{\pi}=0.5$; in the WF simulations, population size _N_ is 100,000, the initial population is drawn from $N(0.5, 0.05)$, and the results are based on 50 simulations per parameter set. Note that the x-axis shows every other generation (end of each period). The analytic approximation is good when selection is extreme ($w/W=0$), but over-estimates $\bar{\pi}$ when selection in not extreme ($w/W=0.1$). In both cases the initial population distribution did not affect the results (as long as it wasn't trivial, _i.e._ $\pi=0$, see @Fig:env_A1B1_π0).

![Population mean $\pi$ in environment regime _A1B1_. Comparison of Wright-Fisher simulations (orange; average of >100 simulations), recurrence equation iteration (blue; @eq:recurrenceA1B1), and recurrence solution (dashed green; @eq:recurrenceA1B1_solution_x_star). Parameters: _W_=1, _N_=100,000, initial population $\pi_i \sim Uniform(0,1)$.](figures/env_A1B1.pdf){#fig:env_A1B1}

#### Evolutionary genetic stability of $\eta=0$

We now consider two modifier alleles in the _A1B1_ regime (@eq:recurrence_modifiers). 
Let's assume that _m_ is fixed such that $p=1, q=0$ and that the population is at an equilibrium $x=x^*$ (@eq:recurrenceA1B1_solution_x_star).

If another modifier allele _M_ appears in low frequency $q \ll 1$ such that initially $y=x^*$, can _M_ invade the population and increase in frequency, or is the equilibrium $p=1, x=x^*$ stable?

To answer this question, we will examine the relative change in frequency of _M_ after a full environmental cycle (two generations), $\lambda$, where in the first generation _A_ is the preferred phenotype with advantage _s_ ($\omega_A=1+s, \omega_B=1$) and in the second generation _B_ is the preferred phenotype with advantage _s_ ($\omega_A=1, \omega_B=1+s$). Because $p \approx 1$, the population mean fitness is dominated by _m_ ($\bar{\omega} = x \omega_A + (1-x) \omega_B)$, and we can write $\lambda$ as a function of the two rates $\eta$ and $H$ using @eq:recurrence_modifiers:
\begin{multline*}
\lambda(\eta, H) = \frac{q''}{q} = \frac{q''}{q'} \cdot \frac{q'}{q} = \\
\frac{y' + (1-y') (1+s)}{x' + (1-x') (1+s)} \cdot 
    \frac{y (1+s) + (1-y)}{x (1+s) + (1-x)} = \\
\frac{1 + s - s y'}{1 + s - s x'} \cdot \frac{1 + s y}{1 + s x} = \\
\frac{1 + s + s^2 (1-H) x^* (1-x^*)}{1 + s + s^2 (1-\eta) x^* (1-x^*)},
\end{multline*}
where both the _m_ and the _M_ populations are initially at the equilibrium value ($x=y=x^*$),
and we use @eq:recurrence_modifiers to calculate $x', y'$.

For $1 > H > \eta=0$, we have $x^* = x^{**} = \frac{1}{2}$, which leads to
$\lambda(0,H) = 1 - H(\frac{s}{2+s})^2 < 1$.

For $\eta = 1 > H > 0$, we have $x^* = \frac{\sqrt{1+s}-1}{s}, x^{**}=x^* \sqrt{1+s}$, which leads to $\lambda(1,H) = 1 + (1-H)\frac{(\sqrt{1+s}-1)^2}{\sqrt{1+s}} > 1$.

More generally,
$$
\frac{\partial }{\partial H} \lambda(\eta, H) = 
\frac{-s^2 x (1-x)}{1 + s + s^2 (1-\eta) x^*(1-x^*)} < 0,
$$
and because $\lambda(\eta, \eta)= 1$, we can deduce that if $H<\eta$ then $\lambda(\eta, H) > 1$ and _M_ can invade _m_; and vice verse, if $H>\eta$ then $\lambda(\eta, H) < 1$ and _m_ cannot be invaded by _M_ (@Fig:A1B1_EGS_eta_0 B). 
It follows that in the _A1B1_ regime, the only phenotypic inheritance rate that can lead to evolutionary genetic stability [@Lessard1990] is $\eta=0$.

Note that the stable population mean fitness after each _AB_ cycle as a function of $\eta$ is (@Fig:A1B1_EGS_eta_0 A):
$$
\bar{\omega}^*(\eta)=1 + \frac{W(1-\eta)-w(3-\eta)+\sqrt{(1-\eta)^2s^2+4(1+s)}}{2(2-\eta)},
$$ {#eq:A1B1_mean_fitness}

With $\eta=0$ we have $\bar{\omega}^*(0)=1+\frac{s}{2}$,
whereas with $\eta=1$ we have $\bar{\omega}^*(1) = \sqrt{1+s} = \bar{\omega}^*(0) - \frac{s^2}{8} + o(s^2)$; 
in general, $\bar{\omega}^*(\eta)$ is a decreasing function of $\eta$, and is therefore maximized at $\eta=0$ (@Fig:A1B1_EGS_eta_0). Indeed, iterating the recurrence equations (@eq:recurrence_modifiers) while introducing modifiers with lower and lower inheritance rates shows that these invading modifiers are successful in sequentially reducing the population phenotypic inheritance rate towards zero, but only after the populations phenotype distribution is established around 0.5 (@Fig:A1B1_modifier_invasions A).

![Evolutionary stability of $\eta=0$ in environmental regime _A1B1_. **(A)** Stable population mean fitness (@eq:A1B1_mean_fitness) as a function of the phenotypic inheritance rate $\eta$ and the selection coefficient _s_ of the favorable phenotype. **(B)** The relative change in frequency of a modifier allele  $\lambda(0, H)$ (equation ref) inducing rate $H$ and invading to a population fixed at $\eta=0$ after a full environmental cycle.](figures/A1B1_EGS_eta_0.pdf){#fig:A1B1_EGS_eta_0}

![Consecutive fixation of modifiers that decrease the phenotypic inheritance rate in environmental regime _A1B1_. The figure shows results of numerical simulations of evolution with two modifier alleles (@Eq:recurrence_modifiers). Every time a modifier allele fixes (frequency>99.9%), a new modifier allele is introduces with a rate one order of magnitude lower (vertical dashed lines). **(A)** The frequency of phenotype _A_ in the population over time. **(B)** The frequency of the invading modifier allele over time. **(C)** The population mean phenotypic inheritance rate over time. Parameters: Phenotypic rate of initial resident modifier allele, 0.1; Fitness values, _W=1, w=0.1_.](figures/A1B1_modifier_invasions.pdf){#fig:A1B1_modifier_invasions}

### _A2B1_ regime

In the _A2B1_ regime (every two generations in environment _A_ are followed by a single generation in environment _B_), an analytic approximation is not possible, as solving $x'''-x=0$ requires solving a polynomial of degree 6. However, iterating the relevant recurrence equation:
$$\begin{aligned}
x' = x \frac{x (1-\eta) (W-w) + \eta W + (1-\eta)w}{x (W-w) + w} \\
x'' = x' \frac{x' (1-\eta) (W-w) + \eta W + (1-\eta)w}{x' (W-w) + w} \\
x''' = x'' \frac{x'' (1-\eta) (w-W) + \eta w + (1-\eta)W}{x'' (w-W) + W}
\end{aligned}$$ {#eq:recurrenceA2B1}
provides similar results: the equilibrium value fits the Wright-Fisher simulations for extreme selection ($w/W=0$) but over-estimates the equilibrium otherwise (@Fig:env_A2B1). 

![Population mean $\pi$ in environment regime _A2B1_. Comparison of Wright-Fisher simulations (orange; average of >65 simulations) and recurrence equation iteration (blue; @eq:recurrenceA2B1). Parameters: _W_=1, _N_=100,000, initial population $\pi_i \sim Uniform(0,1)$.](figures/env_A2B1.pdf){#fig:env_A2B1}

### Protected polymorphisms in _AkBl_ regime

What can we say about the more general case of _k_ generations in environment _A_ and _l_ generations in _B_? We investigate conditions for the the existence of a _protected polymorphism_ [@Prout1968], in which neither phenotype can become extinct. Environments _A_ and _B_ select for $\pi=1$ and $\pi=0$, respectively, and these are absorbing states: if all individuals are, for example, $\pi=0$, then they are all of phenotype $B$ and all offspring will be $\pi=0$, too. Mathematically, we examine the stability of $x=0$ and $x=1$; if both are unstable, then a protected polymorphism occurs. Intuitively, this will happen if neither environment occurs frequently enough to fix it's preferred phenotype. 

We rewrite @Eq:recurrence0 as $x'=x \cdot f_A(x)$ in environment _A_ and $x'=x \cdot f_B(x)$ in environment _B_, where:
$$\begin{aligned}
f_A(x) = \frac{x (1-\eta)(W - w) + \eta W + (1-\eta)w}{x (W - w) + w} \\
f_B(x) = \frac{x (1-\eta)(w - W) + \eta w + (1-\eta)W}{x (w - W) + W}
\end{aligned}$$

We assume $l \ge k$ and check whether $x=0$ is stable, because (i) if $x=0$ is not stable when $l \ge k$ then $x=1$ cannot be stable either, as selection is stronger, on the whole, towards 0; and (ii) checking the other case (stability of $x=1$ when $k \ge l$) is symmetric, and can be done in the same way by writing a recurrence equation for the frequency _y_ of phenotype _B_ and examining the stability of $y=0$. 

To check whether $x=0$ is stable, we start with a value very close to 0 and check whether after a period of _k+l_ generations the population is closer to or farther from 0 compared to where it started. This determines the local stability of $x=0$.

For $x_0 = x(t=0) \sim 0$, we can use a linear approximation of the form $f_A(x_0) = f_A(0) + o(x_0)$ and $f_B(x_0) = f_B(0) + o(x_0)$, where:
$$\begin{aligned}
f_A(0) =  1+\eta(\frac{W-w}{w}) \\
f_B(0) =  1+\eta(\frac{w-W}{W})
\end{aligned}$$

For _k_ generations in environment _A_, and _l_ generations with environment _B_, in any given order, we can write:
$$\begin{aligned}
x_{k+l} = x(t=k+l) \approx
x_0 f_A^k(0) f_B^l(0) \Rightarrow \\
\frac{x_{k+l}}{x_0} \approx f_A^k(0) f_B^l(0).
\end{aligned}$$

This, starting very close to zero ($x_0 \sim 0$), the multiplicative change over the _k+l_ generations can be approximated by $f_A^k(0) f_B^l(0)$.

If $f_A^k(0) f_B^l(0) > 1$, then $x=0$ is not stable; since $x=1$ is not stable either (due to $l \ge k$), then we have a protected polymorphism somewhere ($0 < x(t) < 1$ for any generation _t_). In contrast, if $f_A^k(0) f_B^l(0) < 1$, then $x=0$ is stable and the protected polymorphism disappears.

In the following, we examine the conditions for a protected polymorphism. In general, we find that:
1. A protected polymorphism exists if $\frac{l}{k} < 1 + \frac{(1-\eta){frac{W-w}{w}}}{1+\eta(1-\eta)\frac{(W-w)^2}{Ww}}$.
1. $x=0$ is a steady equilibrium if $\frac{l}{k} = 1 + (1-\eta)\frac{W-w}{w}$.

#### Neutral evolution: $W = w$

In this case, fitness in both environments is equivalent, there is no selection, and therefore evolution is neutral.
Indeed, we find that $f_A(x) = f_B(x) \equiv 1$, without an approximation.

#### No phenotype feedback on inheritance: $\eta = 0$

In this case, there is no feedback between phenotype and inheritance, and only drift generates genetic variance, and evolution is neutral.
Indeed, we get $f_A(x) = f_B(x) = \equiv 1$.

#### Complete phenotype inheritance: $\eta = 1$

In this case, development is not stochastic, and after one generation the model becomes a standard two-type genetic model. Only genetic drift generates genetic variance, but natural selection does play a role.
Indeed, we get $f_A^k(0) f_B^l(0) = \Big(\frac{W}{w}\Big)^{k-l}$. Since $W > w$, we find that $\frac{x_{k+l}}{x_0}$ is
$$
\begin{cases}
< 1 &, k < l \\
= 1 &, k = l \\
> 1 &, k > l
> \end{cases}
$$

#### 

#### Result 1: $k=l$
_If $k=l, W > w > 0, 1 > \eta > 0$, then $f_A^k(0) f_B^l(0) > 1$._

#### Proof
First, $f_A^k(0) f_B^l(0) = (f_A(0)f_B(0))^k > 1$ iff $f_A(0)f_B(0)>1$.

To show the latter,

\begin{multline*}
f_A(0) f_B(0) = \\
(1 + \eta \frac{W-w}{w}) \cdot (1 + \eta \frac{w-W}{W}) = \\
(1 - \eta + \eta\frac{W}{w}) \cdot (1 - \eta + \eta\frac{w}{W}) = \\
(1-\eta)^2 +\eta^2 +\eta(1-\eta)(\frac{W}{w}+\frac{w}{W}) = \\
1 - 2\eta(1-\eta) +\eta(1-\eta)(\frac{W^2+w^2}{Ww}) = \\
1 + \eta (1-\eta)\frac{W^2 - 2 W w + w^2}{Ww} = \\
1 + \eta (1-\eta)\frac{(W - w)^2}{W w}
\end{multline*}

which, under the proposition conditions, is _> 1_.
$\blacksquare$

#### Result 2: $l>k=1$
_If $l > 1 + (1-\eta)\frac{W-w}{w}$ then $f_A(0)f_B^l(0) < 1$._

##### Proof

Set $n = l - 1$. Then,

\begin{multline}\label{eq:l_g_k_eq_1_A}
n > (1-\eta)\frac{W-w}{w} \Leftrightarrow \\
 n \eta \frac{W-w}{W}  > \eta (1-\eta)\frac{(W-w)^2}{Ww} \Leftrightarrow \\
1 - n \eta \frac{w-W}{W} > 1 + \eta (1-\eta)\frac{(W-w)^2}{Ww} \Leftrightarrow \\
1 >  \frac{1+\eta(1-\eta)\frac{(W-w)^2}{Ww}}{1 - n \eta \frac{w-W}{W}} \\
\end{multline}

Now, $W > w \Rightarrow 1 \ge \frac{W-w}{W} \ge 0$, and together with $1 \ge \eta \ge 0$ we get $0 \ge \eta \frac{w-W}{W} \ge -1$. These conditions allow us to use the following Bernoulli inequality (proof with induction):
$$
(1+x)^n \le \frac{1}{1 - nx}, \;\;\; \forall x \in [-1,0], \forall n \in \mathbb{N}.
$$ {#eq:bernoulli1}

From the Bernoulli inequality we have: 

$$
\Big(1+\eta \frac{w-W}{W}\Big)^n \le \frac{1}{1 - n \eta \frac{w-W}{W}}
$$ {#eq:l_g_k_eq_1_B}

Taken together, @Eq:l_g_k_eq_1_A and @Eq:l_g_k_eq_1_B imply that:

\begin{multline*}
f_A(0) f_B^{n+1}(0) = \\
\Big(1+\eta\frac{W-w}{w}\Big)\Big(1+\eta\frac{w-W}{W}\Big)\Big(1+\eta\frac{w-W}{W}\Big)^n = \\
\Big(1+\eta(1-\eta)\frac{(W-w)^2}{Ww}\Big)\Big(1+\eta\frac{w-W}{W}\Big)^n \le \\
\frac{1+\eta(1-\eta)\frac{(W-w)^2}{Ww}}{1 - n \eta \frac{w-W}{W}} < 1 \\\blacksquare
\end{multline*}

#### Result 3: $l > k \ge 1$

_If $l > k \Big( 1 + (1 - \eta) \frac{W - w}{w} \Big)$, then $f_A^k(0)f_B^l(0) < 1$._

##### Proof

First, assume $\frac{l-k}{k} \in \mathbb{N}$ and set $n = \frac{l-k}{k} \Rightarrow n > (1-\eta)\frac{W-w}{w}$.

Now, using the previous proposition,
$$
f_A^k(0) f_B^l(0) = \\
f_A^k(0) f_B^{(n+1)k}(0) = \\
(f_A(0) f_B^{n+1}(0))^k < 1
$$
because $\forall y>0, k>0 \; y < 1 \Rightarrow y^k < 1$.

Next, relax the assumption $\frac{l-k}{k} \in \mathbb{N}$; set $n = \lceil{\frac{l-k}{k}}\rceil > \frac{l-k}{k} > (1-\eta)\frac{W-w}{w}$, then
$$
f_A^k(0) f_B^l(0) < \\
f_A^k(0) f_B^{(n+1)k}(0) = \\
(f_A(0) f_B^{n+1}(0))^k < 1
$$

and again, the previous proposition provides the last inequality.
$\blacksquare$

#### Result 4: $l > k \ge 1$

If $l < k \Big( 1 + \frac{(1-\eta) \frac{W-w}{w}}{1 + \eta (1-\eta) \frac{(W-w)^2}{W w}} \Big)$ then $f_A^k(0) f_B^l(0) > 1$.

##### Proof

Similar to previous proposition, but using a different Bernoulli inequality:

$$\begin{aligned}
(1+x)^n \ge 1+nx, \;\;\; \forall x > -1, \forall n \in \mathbb{R} \smallsetminus (0,1). \\
\blacksquare
\end{aligned}$$

#### Summary of results

TODO

## Stochastic environments

Consider a stochastic environment in which the fitness of phenotypes _A_ and _B_ at generation $t$ are $1+s_t$ and $1$, respectively, where the random variables $s_t \; (t=0, 1, 2, ...)$ are independent and identically distributed (i.i.d) and there are positive constants _C_ and _D_ such that $P(C \le s_t \le D) = 1$.

The recurrence for this model can be rewritten as (based on @eq:recurrence0):
$$
x_{t+1} = x_t \frac{1 + \eta s_t + x_t (1-\eta) s_t}{1 + s_t x_t}.
$$ {#eq:recurrence_random_env}

The following analysis follows @Karlin1975 (see also @Carja2013).

### Stochastic local stability

#### Definition

An equilibrium state $x^*$ is said to be _stochastically locally stable_ if for any $\epsilon>0$ there exists $\delta>0$ such that
$$
x_0 < \delta \Rightarrow P(\lim_{t \to \infty}{x_t} = x^*) \ge 1-\epsilon
$$ {#eq:SLS}

Thus, _stochastic local stability_ of $x^*$ means that if the frequency $x_t$ is sufficiently close to $x^*$, then it will eventually converge to $x^*$ with _high probability_. Note, however, that convergence is likely, but not certain.

#### Theorem 1

_Suppose $\mathbb{E}[\log{(1+\eta s_t)}] > 0$, then $x^*=0$ is not _stochastically locally stable_, 
and in fact $P(\lim_{t \to \infty}{x_t}=0) = 0$._

##### Proof

Rewrite the recurrence (@eq:recurrence_random_env):
$$
\frac{x_{t+1}}{x_{t}} = (1 + \eta s_t) \Big(1 - x_t \frac{\eta s_t (1+s_t)}{(1+\eta s_t)(1+x_t s_t)} \Big)
$$

Taking the log of both sides leads to:
$$
\log{x_{t+1}} - \log{x_{t}} = 
\log{(1+\eta s_t)} +
\log{\Big(1 - x_t \frac{\eta s_t (1+s_t)}{(1+\eta s_t)(1+x_t s_t)} \Big)}
$$

Summation yields:
$$
\frac{1}{t} (\log{x_{t}} - \log{x_{0}}) = 
\frac{1}{t} \sum_{n=0}^{t-1}{\log{(1+\eta s_n)}} + 
\frac{1}{t} \sum_{n=0}^{t-1}{\log{\Big(1 - x_n \frac{\eta s_n (1+s_n)}{(1+\eta s_n)(1+x_n s_n)} \Big)}}
$$

Let $\mu = \mathbb{E}[\log{(1+\eta s_t)}]$.
Because $\{s_t\}_{t \ge 0}$ are i.i.d. random variables, the strong law of large numbers (SLLN) applies and almost surely
$$
\lim_{t \to \infty}{\frac{1}{t} \sum_{n=0}^{t-1}{\log{(1+\eta s_n)}}} = \mu.
$$

Consider $\xi$ such that $\lim_{t \to \infty}{\frac{1}{t} \sum_{n=0}^{t-1}{\log{(1+\eta s_n(\xi))}}} = \mu, C \le s_t(\xi) \le D$ and assume that almost certainly $x^* = 0$, i.e.:
$$
\lim_{t \to \infty}{x_t(\xi)} = 0.
$$ {#eq:T1_assumption}

Because $0 \le \eta \le 1$, 
and $\{s_t(\xi)\}_{t \ge 0}$ are uniformly bounded away from zero and infinity,
we can deduce that
$$
\lim_{t \to \infty}{\frac{1}{t} \sum_{n=0}^{t-1}{\log{\Big(1 - x_n \frac{\eta s_n (1+s_n)}{(1+\eta s_n)(1+x_n s_n)} \Big)}}} = 0 ,
$$
so that
$$
\lim_{t \to \infty}{\frac{1}{t} \Big(\log{x_{t}(\xi)} - 
\log{x_{0}(\xi)}\Big)} = \mu.
$$

However, the hypothesis states that $\mu  > 0$, implying that $\lim_{t \to \infty}{x_{t}(\xi)} = \infty$ which is incompatible with the assumption @eq:T1_assumption. Therefore we must have
$$
P(\lim_{t \to \infty}{x_{t}} = 0) = 0. \; \blacksquare
$$

Thus, for $x^*=0$ to be _stochastically locally stable_, it is necessary that $\mathbb{E}[\log{(1+\eta s_t)}] \le 0$. Furthermore, we can prove that the strict inequality is sufficient.

#### Theorem 2

_Suppose $\mathbb{E}[\log{(1+\eta s_t)}] < 0$,
then $x^*=0$ is _stochastically locally stable_._

##### Proof

Let $\mu = \mathbb{E}[\log{(1+\eta s_t)}]$, so that $\mu<0$. 
Because $\{s_t\}_{t \ge 0}$ are i.i.d. random variables, the SLLN applies and almost surely
$$
\lim_{t \to \infty}{\frac{1}{t} \sum_{n=0}^{t-1}{\log{(1+\eta s_n)}}} = \mu.
$$

Appealing to the _Severini–Egoroff theorem_,
for any $\epsilon > 0$, there exists $T$ such that (remember that $\mu$ is negative):
$$
P\Big(\frac{1}{t} \sum_{n=0}^{t-1}{\log{(1 + \eta s_n)}} < \frac{\mu}{2} 
\; \forall t \ge T \Big) \ge 1 - \epsilon.
$$

Because $0 \le \eta \le 1$ and $\{s_t(\xi)\}_{t \ge 0}$ are uniformly bounded away from zero and infinity, we can find $\delta'>0$ such that:
$$
x_t < \delta' \Rightarrow 
\Big| \log{\Big(1 - x_t\frac{\eta s_t (1+s_t)}{(1+\eta s_t)(1+x_t s_t)} \Big)} \Big| < -\frac{\mu}{4}.
$$

Also, 
$$
x_{t+1} = x_t \frac{x_t (1-\eta) s_t + \eta (1+s_t) + 1 - \eta}{1 + s_t x_t} < C \cdot x_t,
$$
where $C \in \mathbb{R}$ is independent of $t$; it follows that there exists $0 < \delta < \delta'$ such that:
$$
x_0 < \delta \Rightarrow x_t < \delta', \; \forall t=0, 1, 2, ..., T-1.
$$

Let $\xi$ be a realization of the evolutionary process such that
$$
\frac{1}{t} \sum_{n=0}^{t-1}{\log{(1 + \eta s_n(\xi))}} < \frac{\mu}{2} \; \forall t \ge T
$$ 
and assume $x_0 < \delta$.

Then:
\begin{multline*}
\frac{1}{T} \Big(\log{x_T(\xi)} - \log{x_0(\xi)}\Big) =
\frac{1}{T} \sum_{t=0}^{T-1}{\log{\Big(1 + \eta s_t(\xi)\Big)}} + \\
+ \frac{1}{T} \sum_{t=0}^{T-1} \log{\Big(1 - x_t(\xi)\frac{\eta s_t(\xi) (1+s_t(\xi))}{(1+\eta s_t(\xi))(1+x_t(\xi) s_t(\xi))} \Big)} < \\
\frac{\mu}{2}-\frac{\mu}{4} = 
\frac{\mu}{4} < 0,
\end{multline*}
and therefore $x_T(\xi) < x_0(\xi) < \delta'$. 

Invoking induction we get that for $t \ge T$, 
$$
\log{\frac{x_t(\xi)}{x_0}} \le \frac{\mu}{4} \cdot t \Rightarrow \\
x_t(\xi) \le x_0 \cdot \exp{\Big(\frac{\mu t}{4}\Big)}.
$$

As $\mu < 0$, this implies $\lim_{t \to \infty}{x_t(\xi)}=0$.

Therefore, we have shown that for any $\epsilon > 0$ there exists $\delta>0$
such that if $x_0 < \delta$, then $P(\lim_{t \to \infty}{x_t} = 0) \ge 1-\epsilon$,
which proves that $x^*=0$ is _stochastically locally stable_. $\blacksquare$

These theorems can be summarized as follows:

- if $\mathbb{E}[\log{(1+\eta s_t)}] < 0$ then fixation of $x^*=0$ is _stochastically locally stable_.
- if $\mathbb{E}[\log{(1+\eta s_t)}] > 0$ then fixation of $x^*=0$ almost never occurs.
- if the fitness of phenotype _B_ is also a random variable, such that the fitness values of phenotypes _A_ and _B_ are $\tau_t, \sigma_t$, respectively, than we can normalize the fitness values by $\sigma_t$ and denote $s_t=\frac{\tau_t-\sigma_t}{\sigma_t}$. The above results then apply.
- the above results will stand for any sequence $\{s_t\}_{t \ge 0}$ for which the SLLN applies, even if they are not i.i.d.
- @Fig:stochastic_env_x_t shows $x_{t=10^6}$ with $\eta=0.01$ and initial value $x_0=10^{-3}$ for different selection coefficients _s_ and _p_ the probability of favoring phenotype _A_. The white lines represent _s_ and _p_ values for which $\mathbb{E}[\log{(1 + \eta s_t)}] = 0$; indeed, below this line $x_t$ tends to converge to 0.

![Stochastic local stability. The figure shows $x_{t=10^6}$ the probability for phenotype _A_ after $10^6$ generations, calculated using the recurrence model (@eq:recurrence_random_env). The fitness of phenotypes _A_ and _B_ is $1+s_t$ and $1$, where $s_t$ is _s_ with probability _p_ and _-s_ with probability _1-p_. The white line marks combinations of _p_ and _s_ for which $\mathbb{E}[\log{(1+\eta s_t)}]=0$; according to Theorems 1 and 2 we expect that only below this line $x^*=0$ will be stochastically locally stable. Parameters: $x_0=0.1$; $\eta=0.1$](figures/stochastic_env_x_t.pdf){#fig:stochastic_env_x_t}

# Supporting figures {label="S"}

- @Fig:recurrence_example
- @Fig:env_A1B1_π0

![Comparison of the recurrence transformation $x \to x'$ (@eq:recurrence) and the identity transformation $x \to x$ for $\eta$=0.1, _W_=1, _w_=0.1.](figures/recurrence_example.pdf){#fig:recurrence_example}

![Population mean $\pi$ in environment regime _A1B1_. Comparison of Wright-Fisher simulations (orange; average of >100 simulations), recurrence equation iteration (blue; @eq:recurrenceA1B1), and recurrence solution (dashed green; @eq:recurrenceA1B1_solution_x_star).  Initial population distribution: (A) $\pi_i$=0.01; (B) $\pi_i$=0.5; (C) $\pi_i$=0.99; (D) $\pi_i \sim Uniform(0,1)$. Parameters: _W_=1, $\eta$=0.1, _N_=100,000.](figures/env_A1B1_π0.pdf){#fig:env_A1B1_π0}

# References {-}