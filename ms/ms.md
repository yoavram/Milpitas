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
$$ {#eq:recurrence}

Where $\omega_A$ and $\omega_B$ are the fitness of phenotypes _A_ and _B_ in the current generation (depending on $\epsilon_t$).

When we write a similar recurrence for the probability that an individual is _B_ ($(1-x)' = F(1-x)$) and sum the two equations, we find that $\bar{\omega} = x \omega_A + (1-x) \omega_B$ is the mean fitness.

This recurrence equation can be reorganized to:

$$
x' = x \frac{x (1-\eta) (\omega_A - \omega_B) + \eta \omega_A + (1-\eta)\omega_B}{x (\omega_A - \omega_B) + \omega_B}
$$ {#eq:recurrence0}

# Results {-}

## Constant environment

We start with a constant environment $\epsilon_t=A \; \forall t$, such that $\omega_A = W > w = \omega_B$. 

### Proposition for $\eta=0$

If $\eta = 0$ then any $x \in [0,1]$ solves $x'=x$.

### Proof

Set $x'=x, \eta=0$ in @Eq:recurrence0:
$$
x = x \frac{x (\omega_A - \omega_B) + \omega_B}{x (\omega_A - \omega_B) + \omega_B}
$$

First, $x=0$ solves this equality. Otherwise, for $x>0$:
$$
\Leftrightarrow x (\omega_A - \omega_B) + \omega_B = x (\omega_A - \omega_B) + \omega_B
$$
which is an identity $\blacksquare$.

### Proposition for $W=w$

If $W = w$ then any $x \in [0,1]$ solves $x'=x$.

### Proof

Set $W = w > 0, x' = x \ne 0$ in @Eq:recurrence0:

\begin{multline*}
x =  x {\eta W + (1-\eta)W}{W} \Leftrightarrow \\
1 =  1 {\eta + (1-\eta)}{1} \Leftrightarrow \\
1 =  1 \\
\blacksquare
\end{multline*}

### Proposition for general case

If $\eta > 0$ and $\omega_A > \omega_B$, then $x^* = 1$ is the only solution for $x'=x$.

### Proof

First, we check that $x^*=1$ solves $x'=x$. Set $x=1$ in @Eq:recurrence0:

\begin{multline*}
x' = 
\frac{1-\eta)(\omega_A-\omega_B)+\eta \omega_A+(1-\eta)\omega_B}{\omega_A} = \\
\frac{\omega_A}{\omega_A} = 1
\end{multline*}

Next, we check that $x=0$ doesn't solve $x'=x$ by setting $x=0$ in @Eq:recurrence0:
$$
x' = \frac{\eta \omega_A + (1-\eta) \omega_B}{\omega_B} > 0
$$
since both the denominator and the numerator are positive.

Next, we check that any $0 < x < 1$ doesn't solve $x'=x$. Set $x'=x$ in @Eq:recurrence and substituting $\bar{\omega} = x \omega_A + (1-x) \omega_B$:

\begin{multline*}
x = x \cdot \frac{\omega_A}{\bar{\omega}} \cdot ((1-\eta)x+\eta) + (1-x) \cdot \frac{\omega_B}{\bar{\omega}} \cdot (1-\eta)x \Leftrightarrow \\
\bar{\omega} = \omega_A \cdot ((1-\eta)x+\eta) + (1-x) \cdot \omega_B \cdot (1-\eta) \Leftrightarrow \\
x \omega_A + (1-x) \omega_B = (1-\eta) x \omega_A + \eta \omega_A +  (1-\eta) (1-x) \omega_B \Leftrightarrow \\
\eta (x \omega_A + (1-x) \omega_B) = \eta \omega_A \Leftrightarrow \\
x \omega_A + (1-x) \omega_B =  \omega_A \Leftrightarrow \\
(1-x) \omega_A = (1-x) \omega_B \Leftrightarrow \\
x = 1 \\
\blacksquare
\end{multline*}

## Periodic environment

We concentrate on periodic environments in which both environments occur exactly the same number of generations in each "period". A simple example is _A1B1=ABABABAB..._, in which the environment switches every generation every generation from _A_ to _B_ and vice versa, or _A2B1=AABAABAAB..._ in which the every two _A_s are followed by a single _B_. In general, _AkBl_ denotes an environmental regime in which the period is of length _k+l_ and composed of exactly _k_ _A_s and _l_ _B_s.

We simulated evolution in such environments, and @Fig:env_period_overview shows the evolution of the distribution of $\pi$ in a population evolving in three such environmental regimes.

![Distribution of $\pi$ in populations evolving in periodic environments. **(A)** A1B1, **(B)** A2B1, **(C)** A40B40. Parameters: _N_=100,000, $\eta$=0.01, $W$=1, $w$=0.1.](figures/env_period_overview.pdf){#fig:env_period_overview}

### _A1B1_ regime

When the environment changes every generation, we can write the following recursion, which sets $\omega_A=W, \omega_B=w$ in [@Eq:recurrence0] to determine $x'$ and and then sets $\omega_A=w, \omega_B=W$ to determine $x''$:

$$\begin{aligned}
x' = x \frac{x (1-\eta) (W - w) + \eta W + (1-\eta)w}{x (W-w) + w} \\
x'' = x' \frac{x (1-\eta) (w - W) + \eta w + (1-\eta)W}{x' (w-W) + W}
\end{aligned}$$ {#eq:recurrenceA1B1} 

We are looking for solutions for $x''=x$, which evaluates to a quartic polynomial. Two solutions are $x=0,1$ (assign to [@Eq:recurrenceA1B1] to check), but there are two more potential solutions such that

$$\begin{aligned}
x''-x = x(1-x)G(x) = 0 \\
G(x) = Ax^2 + Bx + C
\end{aligned}$$

Using [SymPy](http://sympy.org/), a Python library for symbolic mathematics, a free alternative to Wolfram Mathematica™ [@SymPyDevelopmentTeam2014], we find all four solution of $x''-x=0$:

$$
G(x) = x^2 - \frac{W (1-\eta) - w (3-\eta)}{(2-\eta)(W - w)} x - \frac{w}{(2-\eta)(W - w)}
$$ {#eq:recurrenceA1B1_solution}

To find the roots of $G(x)$, recall that $W > w \ge 0, 1 \ge \eta \ge 0$, so
$$
G(0) = \frac{-w}{(2-\eta)(W-w)} < 0
$$
and
$$\begin{aligned}
G(1) = 1 - \frac{W (1-\eta) - w (3-\eta)}{(2-\eta)(W-w)} - \frac{w}{(2-\eta)(W-w)} = \\
\frac{W}{(2-\eta)(W-w)} > 0
\end{aligned}$$
and $lim_{x-> \pm \infty}{G(x)} = +\infty$.

Therefore, one root of $G(x)$ is negative and one, $\tilde{x}$, is positive and below 1. Let $\delta=\frac{-B-\sqrt{B^2-4AC}}{2A}-\frac{-B+\sqrt{B^2-4AC}}{2A}$ (where _A_, _B_, _C_ are the coefficients of $G(x)$, defined in [@Eq:recurrenceA1B1_solution]). Then, $\delta=\frac{\sqrt{(W+w)^2-\eta(2-\eta)(W-w)^2}}{(2-\eta)(W-w)}$. Because $\eta(2-\eta)$ is maximized at 1, 
$$
(W+w)^2-\eta(2-\eta)(W-w)^2 > (
W+w)^2-(W-w)^2=4Ww  > 0
$$
so $\delta > 0$. Therefore, the positive root is:

$$
\tilde{x}=\frac{-B-\sqrt{B^2-4AC}}{2A}
$$ {#eq:recurrenceA1B1_solution_tildex}

@Fig:env_A1B1 shows $\tilde{x}$ (dashed green) compared with $x$ from iteration of [@Eq:recurrenceA1B1] (blue) and with the population mean $\pi$ ($\bar{\pi}$) in Wright-Fisher simulations (orange) for several combinations of $\eta, W, w$. All iterations started with $\bar{\pi}=0.5$; in the WF simulations, population size _N_ is 100,000, the initial population is drawn from $N(0.5, 0.05)$, and the results are based on 50 simulations per parameter set. Note that the x-axis shows every other generation* (end of each period). The analytic approximation is good when selection is extreme ($w=0$), but overestimates $\bar{\pi}$ when selection in not extreme ($w=0.1$). In both cases the initial population distribution did not affect the results (as long as it wasn't trivial, _i.e._ $\pi=0$, see @Fig:env_A1B1_π0).

![Population mean $\pi$ in environment regime _A1B1_. _N_=100,000.](figures/env_A1B1.pdf){#fig:env_A1B1}

### _A2B1_ regime

In the _A2B1_ regime (every two generations in the _A_ environment are followed by a generation in environment _B_), an analytic approximation is not possible, as solving $x'''-x=0$ requires solving a polynomial of degree 6. However, iterating the relevant recurrence equation:
$$\begin{aligned}
x' = x \frac{x (1-\eta) (W-w) + \eta W + (1-\eta)w}{x (W-w) + w} \\
x'' = x' \frac{x' (1-\eta) (W-w) + \eta W + (1-\eta)w}{x' (W-w) + w} \\
x''' = x'' \frac{x'' (1-\eta) (w-W) + \eta w + (1-\eta)W}{x'' (w-W) + W}
\end{aligned}$$ {#eq:recurrenceA1B1}
provides similar results: the equilibrium value is in good fit with Wright-Fisher simulations for extreme selection ($w=0$) but over estimates the equilibrium otherwise (@Fig:env_A2B1). 

![Population mean $\pi$ in environment regime _A2B1_. _N_=100,000.](figures/env_A2B1.pdf){#fig:env_A2B1}

### Protected polymorphisms in _AkBl_ regime

What can we say about the more general case of _k_ generations in environment _A_ and _l_ generations in _B_? We examine the existence of a _protected polymorphism_ [@Prout1968], which means that none of the phenotypes become extinct even when initially rare. Environments _A_ and _B_ select for $\pi=1$ and $\pi=0$, respectively, and these are absorbing states: if all individuals are, for example, $\pi=0$, then they are all of phenotype $B$ and all offspring will be $\pi=0$, too. Mathematically, we examine the stability of $x=0$ and $x=1$; if both are unstable, then a protected polymorphism occurs. Intuitively, this will happen if neither environment occurs enough to fix it's preferred state. 

We rewrite @Eq:recurrence0 as $x'=x \cdot f_A(x)$ in environment _A_ and $x'=x \cdot f_B(x)$ in environment _B_, where:
$$\begin{aligned}
f_A(x) = \frac{x (1-\eta)(W - w) + \eta W + (1-\eta)w}{x (W - w) + w} \\
f_B(x) = \frac{x (1-\eta)(w - W) + \eta w + (1-\eta)W}{x (w - W) + W}
\end{aligned}$$

We concentrate on $l \ge k$ and check if $x=0$ is stable, because (i) if $x=0$ is not stable when $l \ge k$ then $x=1$ cannot be stable either, as selection is stronger, on the whole, towards 0; and (ii) checking the other case (stability of $x=1$ when $k \ge l$) is symmetric, and can be done in the same way by writing a recurrence equation for the frequency _y_ of phenotype _B_ rather than _A_ and studying the case of $y=0$. 

To check if $x = 0$ is stable, we start with a value very close to 0 and check if after a period of _k+l_ generations the population is closer or farther from 0 compared to where it started.

For $x_0 = x(t=0) \sim 0$, we can use a linear approximation of the form $f_A(x_0) = f_A(0) + o(x_0)$ and $f_B(x_0) = f_B(0) + o(x_0)$, where:
$$\begin{aligned}
f_A(0) =  1+\eta(\frac{W-w}{w}) \\
f_B(0) =  1+\eta(\frac{w-W}{W})
\end{aligned}$$

For _k_ generations in environment _A_, and _l_ generations with environment _B_, in any given order, we can write:
$$\begin{aligned}
x_{k+l} = x(t=k+l) \approx
x_0 f_A^k(0) f_B^l(0) \Rightarrow \\
\frac{x_{k+l}}{x_0} \approx f_A^k(0) f_B^l(0)
\end{aligned}$$
so that if we start very close to zero ($x_0 \sim 0$), the multiplicative change over the _k+l_ generations can be approximated by $f_A^k(0) f_B^l(0)$.

If $f_A^k(0) f_B^l(0) > 1$, then $x=0$ is not stable; since $x=1$ is not stable either (due to $l \ge k$), then we have a *protected polymorphism* somewhere ($0 < x(t) < 1$ for any generation _t_). In contrast, if $f_A^k(0) f_B^l(0) < 1$, then $x=0$ is stable and the *protected polymorphism* disappears.

Following we examine the protected polymorphism in several special and general cases.

#### $W = w$

In this case, fitness in both environments is equivalent, there is no selection, and therefore evolution is neutral.
Indeed, we find that $f_A(x) = f_B(x) \equiv 1$, without an approximation.

#### $\eta = 0$

In this case, there is no feedback between phenotype and inheritance, and only drift generates genetic variance, and evolution is neutral.
Indeed, we get $f_A(x) = f_B(x) = \equiv 1$.

#### $\eta = 1$

In this case, development is not stochastic, and after one generation the model becomes a standard two-type genetic model. Only genetic drift generates genetic variance, but natural selection does play a role.
Indeed, we get $f_A^k(0) f_B^l(0) = \Big(\frac{W}{w}\Big)^{k-l}$. Since $W > w$, we find that $\frac{x_{k+l}}{x_0}$ is

$$
\begin{cases}
< 1 &, k < l \\
= 1 &, k = l \\
> 1 &, k > l
\end{cases}
$$

#### Proposition for $k=l$
If $k=l, W > w > 0, 1 > \eta > 0$, then $f_A^k(0) f_B^l(0) > 1$.

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

#### Proposition for $l>k=1$
If $l > 1 + (1-\eta)\frac{W-w}{w}$ then $f_A(0)f_B^l(0) < 1$.

#### Proof

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

##### Proposition for general case: $l > k \ge 1$

If $l > k \Big( 1 + (1 - \eta) \frac{W - w}{w} \Big)$, then $f_A^k(0)f_B^l(0) < 1$.

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

##### Proposition

If $l < k \Big( 1 + \frac{(1-\eta) \frac{W-w}{w}}{1 + \eta (1-\eta) \frac{(W-w)^2}{W w}} \Big)$ then $f_A^k(0) f_B^l(0) > 1$.

##### Proof

Similar to previous proposition, but using a different Bernoulli inequality:

$$\begin{aligned}
(1+x)^n \ge 1+nx, \;\;\; \forall x > -1, \forall n \in \mathbb{R} \smallsetminus (0,1). \\
\blacksquare
\end{aligned}$$

### Random environments

TODO: 
- local stochastic stability
- see Levikson & Karlin, 1970's; Liberman & Karlin, 1970's

# Supporting figures {label="S"}

- @Fig:env_A1B1_π0

![Population mean $\pi$ in environment regime _A1B1_. Initial population distribution: (A) $\pi_i$=0.01; (B) $\pi_i$=0.5; (C) $\pi_i$=0.99; (D) $\pi_i \sim Uniform(0,1)$. _N_=100,000.](figures/env_A1B1_π0.pdf){#fig:env_A1B1_π0}

# References {-}