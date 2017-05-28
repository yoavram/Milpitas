---
title: Evolution in fluctuating environments with parental and group effects
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

\newpage

# Model {-}

Consider a population of _N_ individuals exhibiting one of two phenotypes $\phi=A,B$ evolving in a fluctuating environment. The preferred phenotype in the current environment is $E \in \{A, B\}$. In environment $E=A$ the fitness of phenotypes _A_ and _B_ are _W_ and _w_, respectively; in environment $E=B$ the fitness of phenotypes _A_ and _B_ are reversed:
$$
\omega_{\phi} = \begin{cases}
W, & \phi = E \\
w, & \phi \ne E
\end{cases},
$$ {#eq:fitness_rule}

and the population mean fitness is $\bar{\omega} = x \omega_A + (1-x) \omega_B$, where _x_ is the frequency of phenotype _A_.

An offspring inherits its phenotype from its parent with probability $\rho$, and from a random individual in the parental population with probability $1-\rho$. In other words, phenotypes are transmitted from parent to offspring, but the offspring has a probability of $1-\rho$ of copying a random phenotype from the parental population.
Thus, given the parent phenotype is $\phi$ (assuming uni-parental inheritance) and the frequency of phenotype _A_ in the parental population is _x_, the probability that the phenotype $\phi'$ of an offspring is _A_ is:
$$
P(\phi' = A) = \begin{cases}
(1-\rho) x + \rho, & \phi = A \\
(1-\rho) x, & \phi = B
\end{cases},
$$ {#eq:inheritance_rule}

where $\rho$ and $1-\rho$ are the parental and group effect rates.
The formulation in @eq:inheritance_rule is analogous to a
combination of _vertical_ and _oblique transmission_ as defined by @Cavalli-Sforza1981. 


## Deterministic model

The following recursion describes $x'$, the expected frequency of phenotype _A_ in the next generation, given that the frequency of phenotype _A_ in the current generation is _x_ (@Fig:recurrence_example):

$$
x' = x \cdot \frac{\omega_A}{\bar{\omega}} \cdot ((1-\rho)x + \rho) + (1-x) \cdot \frac{\omega_B}{\bar{\omega}} \cdot (1-\rho)x.
$$ {#eq:recurrence}

@Eq:recurrence can be reorganized:
$$
x' = x \frac{x (1-\rho) (\omega_A - \omega_B) + \rho \omega_A + (1-\rho)\omega_B}{x (\omega_A - \omega_B) + \omega_B}.
$$ {#eq:recurrence0}

\pagebreak

| Parameter | Description |
|----------|----------------------------------------|
| N | constant population size |
| $\phi$ | phenotype,  $\phi_i \in \{A,B\}$ |
| $E$ | the  phenotype favored in the current environment, $E \in \{A, B\}$|
| $W$ | individual fitness when phenotype and environment match, $\phi = E$ |
| $w$ | individual fitness when phenotype and environment do not match, $\phi \ne E$ |
| $\omega_{\phi}$ | fitness of phenotype $\phi$ in the current environment, $\omega_{\phi}=W \cdot 1_{\phi = E} + w \cdot 1_{\phi \ne E}$ |
| $\bar{\omega}$ | population mean fitness |
| $x$| the frequency of phenotype _A_|
| $\rho$| parental effect rate, $0 \le \rho \le 1$, such that $1-\rho$ is the group conformity effect|

: Model parameters. {#tbl:model_parameters_table}

![Comparison of the transformation $x \to x'$ (@eq:recurrence) and the identity transformation $x \to x$ for $\rho$=0.1, _W_=1, _w_=0.1.](figures/recurrence_example.pdf){#fig:recurrence_example}

## Stochastic model

To include the effect of random drift, we carry out a binomial sampling after each generation, as in Wright-Fisher models [@Otto2007, ch. 13.4]. Therefore, given that the frequency of individuals with phenotype _A_ is _x_ in the parental generation, the probability that $k$ offspring are descendants of individuals with phenotype _A_ is

$$
{N \choose k}
\Big(x \frac{\omega_A}{\bar{\omega}}\Big)^k 
\Big((1-x) \frac{\omega_B}{\bar{\omega}}\Big)^{N-k}.
$$ {#eq:genetic_drift_rule}

Note that when $\rho=1$, this model simplifies to a standard Wright-Fisher two-allele model with selection and random genetic drift.

## Modifier model

Consider two modifier alleles _m_ and _M_ that produce parental effect rates $\rho$ and $P$,
and denote their frequencies by _p_ and _q_ ($p+q=1$). _x_ is the probability that a random individual with modifier allele _m_ is _A_,
and _y_ is that probability for a random individual with allele _M_.
Table 2 shows the pheno-haplotype [REF] frequencies assuming that the 
phenotypes \(A/B\) and parental effect rate control locus \(M/m\) are 
independent.

|      | mA  | mB     | MA  | MB     |
|------|-----|--------|-----|--------|
| frequency    | $p \cdot x$  | $p(1-x)$ | $q \cdot y$  | $q(1-y)$ |
| fitness    | $\omega_A$ | $\omega_B$    | $\omega_A$ | $\omega_B$    |
| parental effect rate | $\rho$   | $\rho$      | $P$   | $P$      |

: Modifier model. {#tbl:modifier_model_table}

The population recurrence is (based on @eq:recurrence0):

$$\begin{aligned}
x' = x \frac{x (1-\rho) (\omega_A - \omega_B) + \rho \omega_A + (1-\rho)\omega_B}{\bar{\omega}_{m}} \\
y' = y \frac{y (1-P) (\omega_A - \omega_B) + P \omega_A + (1-P)\omega_B}{\bar{\omega}_{M}} \\
p' = p \frac{x \omega_A + (1-x) \omega_B}{\bar{\omega}} \\
q' = q \frac{y \omega_A + (1-y) \omega_B}{\bar{\omega}} \\
\bar{\omega} = p \bar{\omega}_{m}  + q \bar{\omega}_{M} \\
\bar{\omega}_{m} = x \omega_A + (1-x) \omega_B \\
\bar{\omega}_{M} = y \omega_A + (1-y) \omega_B
\end{aligned}$$ {#eq:recurrence_modifiers}

# Results {-}

## Constant environment

First consider a constant environment favoring phenotype _A_, such that $\omega_A = W > w = \omega_B$. We seek $x^*$, the equilibrium frequency of phenotype _A_, such that $x'=x$ in (@eq:recurrence), and begin with some trivial cases.
First, in the neutral case ($W = w$), any $x \in [0,1]$ is an (unstable) equilibrium.
Second, if there is no parental effect $\rho=0$ and selection cannot affect the population because inheritance is independent of reproduction. In this case, again, any $x \in [0,1]$ is an (unstable) equilibrium.

**Result: constant environment.**
If $1 \ge \rho > 0$ and $\omega_A > \omega_B$, then $x^* = 1$ is the equilibrium and all the individuals will eventually have phenotype _A_ for any initial $x>0$.

**Proof.**
Rewrite @eq:recurrence0 as $x' = x \cdot \frac{f(x)}{g(x)}$ with $f(x) = (1-\rho)(\omega_A - \omega_B)x + \rho \omega_A + (1-\rho)\omega_B$ and $g(x) = (\omega_A - \omega_B)x + \omega_B$.

Clearly, $x'=x$ if and only if $f(x)=g(x)$ or $x=0$. 
However, _f_ and _g_ are both linear in _x_ and therefore can only intersect at one point.
Indeed, _f_ and _g_ intersect at $x=1$: $f(1)=g(1)=\omega_A$, which means that $x=1$ solves $x'=x$. 
Since $f(0) = \omega_B + \rho(\omega_A + \omega_B) > \omega_B = g(0)$, we can deduce that if $x<1$ then $f(x) > g(x)$ and hence $x' > x$.

Therefore, $x \to x'$ is a strictly monotone transformation for $x \in (0,1)$ (@Fig:recurrence_example), and the recursion converges to 1 for any initial value $0 < x< 1$. $\blacksquare$

## Periodic environmental regime

Consider periodic environmental regimes in which both environments occur  for exactly the same number of generations during each "period".
Simple examples are _A1B1=ABABABAB..._, in which the environment switches every generation from fitnesses _W_ and _w_ for phenotypes _A_ to _B_ to fitnesses _w_ and _W_, or _A2B1=AABAABAAB..._ where every two environments favoring phenotype _A_ are followed by a single environment favoring phenotype _B_.
In general, _AkBl_ denotes an environmental regime in which the period is of length _k+l_ and is composed of exactly _k_ generations of an environment favoring phenotype _A_, followed by _l_ generations in an environment favoring phenotype _B_. However, our general result applies for any permutation of these _k+l_ environments.

### _AkBl_ regime

What can be said about the more general case of _k_ generations in environment _A_ and _l_ generations in _B_?
We investigate conditions for the the existence of a _protected polymorphism_ [@Prout1968], in which neither phenotype can //become extinct//disappear//. 
Environments _A_ and _B_ select for $x=1$ and $x=0$, respectively, 
and these are absorbing states: if all individuals are _A_, for example, then all offspring will be _A_, too. 
Mathematically, we examine the stability of $x=0$ and $x=1$; 
if both are unstable, then there is a protected polymorphism occurs. 
Intuitively, this will happen if neither environment occurs frequently enough to fix the phenotype that if favored in that environment.

Rewrite @Eq:recurrence0 as $x'=x \cdot f_A(x)$ in environment _A_ and $x'=x \cdot f_B(x)$ in environment _B_, where:
$$\begin{aligned}
f_A(x) = \frac{x (1-\rho)(W - w) + \rho W + (1-\rho)w}{x (W - w) + w} \\
f_B(x) = \frac{x (1-\rho)(w - W) + \rho w + (1-\rho)W}{x (w - W) + W}
\end{aligned}$$

To be specific, assume $l \ge k$ and check whether $x=0$ is stable, because (i) if $x=0$ is not stable when $l \ge k$ then $x=1$ cannot be stable either, as selection is, on the whole, stronger towards 0; and (ii) checking the other case (stability of $x=1$ when $k \ge l$) is symmetric, and can be done in the same way by writing a recurrence equation for the frequency _y_ of phenotype _B_ and checking the stability of $y=0$. 

To check whether $x=0$ is stable, we start with a value very close to 0 and check whether after a period of _k+l_ generations the population is closer to or farther from 0 compared to where it started. This determines the local stability of $x=0$.

For $x_0 = x(t=0) \sim 0$, we use a linear approximation of the form $f_A(x_0) = f_A(0) + o(x_0)$ and $f_B(x_0) = f_B(0) + o(x_0)$, where:
$$\begin{aligned}
f_A(0) =  1+\rho(\frac{W-w}{w}) \\
f_B(0) =  1+\rho(\frac{w-W}{W})
\end{aligned}$$

For _k_ generations in environment _A_, and _l_ generations with environment _B_, in any given order, we can write:
$$\begin{aligned}
x_{k+l} = x(t=k+l) \approx
x_0 f_A^k(0) f_B^l(0) \Rightarrow \\
\frac{x_{k+l}}{x_0} \approx f_A^k(0) f_B^l(0).
\end{aligned}$$

Thus, starting close enough to zero ($x_0 \sim 0$), the multiplicative change over the _k+l_ generations can be approximated by $f_A^k(0) f_B^l(0)$.

If $f_A^k(0) f_B^l(0) > 1$, then $x=0$ is not stable; since $x=1$ is not stable either (since $l \ge k$), there is a protected polymorphism ($0 < x(t) < 1$ for any generation _t_). 
In contrast, if $f_A^k(0) f_B^l(0) < 1$, then $x=0$ is locally stable.

In the following, we examine the conditions for a protected polymorphism. In general, we find that:

1. A protected polymorphism exists if $\frac{l}{k} < 1 + \frac{(1-\rho){\frac{W-w}{w}}}{1+\rho(1-\rho)\frac{(W-w)^2}{Ww}}$.
1. $x=0$ is a stable equilibrium if $\frac{l}{k} = 1 + (1-\rho)\frac{W-w}{w}$.

We start with some trivial cases. 
First, in the neutral case ($W = w$), we find that $f_A(x) = f_B(x) \equiv 1$, without an approximation.

Second, with no parental effect ($\rho = 0$), the phenotype frequency does not change.
Indeed, we get $f_A(x) = f_B(x) \equiv 1$.

Third, with full parental effect ($\rho = 1$), the model becomes a standard two-allele model with $f_A^k(0) f_B^l(0) = \Big(\frac{W}{w}\Big)^{k-l}$. 
Since $W > w$, we find that $\frac{x_{k+l}}{x_0}$ is
$$
\begin{cases}
< 1 &, k < l \\
= 1 &, k = l \\
> 1 &, k > l
\end{cases}
$$

**Result.**
_If $k=l, W > w > 0, 1 > \rho > 0$, then $f_A^k(0) f_B^l(0) > 1$ and $x^*=0$ is locally unstable. In this case there is a protected polymorphism._

**Proof.**
First, $f_A^k(0) f_B^l(0) = (f_A(0)f_B(0))^k > 1$ iff $f_A(0)f_B(0)>1$.

To show the latter,

\begin{multline*}
f_A(0) f_B(0) = \\
(1 + \rho \frac{W-w}{w}) \cdot (1 + \rho \frac{w-W}{W}) = \\
(1 - \rho + \rho\frac{W}{w}) \cdot (1 - \rho + \rho\frac{w}{W}) = \\
(1-\rho)^2 +\rho^2 +\rho(1-\rho)(\frac{W}{w}+\frac{w}{W}) = \\
1 - 2\rho(1-\rho) +\rho(1-\rho)(\frac{W^2+w^2}{Ww}) = \\
1 + \rho (1-\rho)\frac{W^2 - 2 W w + w^2}{Ww} = \\
1 + \rho (1-\rho)\frac{(W - w)^2}{W w} > 1
\end{multline*}

if $1 > \rho > 0, W > w$.
$\blacksquare$

**Result.**
_If $k=1$, $W > w$, and $l > 1 + (1-\rho)\frac{W-w}{w}$ then $f_A(0)f_B^l(0) < 1$, and $x^*=0$ is locally stable._

**Proof.**
Set $n = l - 1$. Then,

\begin{multline}\label{eq:l_g_k_eq_1_A}
n > (1-\rho)\frac{W-w}{w} \Leftrightarrow \\
 n \rho \frac{W-w}{W}  > \rho (1-\rho)\frac{(W-w)^2}{Ww} \Leftrightarrow \\
1 + n \rho \frac{W-w}{W} > 1 + \rho (1-\rho)\frac{(W-w)^2}{Ww} \Leftrightarrow \\
1 >  \frac{1+\rho(1-\rho)\frac{(W-w)^2}{Ww}}{1 + n \rho \frac{W-w}{W}} \\
1 >  \frac{1+\rho(1-\rho)\frac{(W-w)^2}{Ww}}{1 - n \rho \frac{w-W}{W}} \\
\end{multline}

**TODO** dont' switch sign?

Now, if $w < W \$, then $0 \le \frac{W-w}{W} \le 1$, and together with $0 \le \rho \le 1$ we have $-1 \le \rho \frac{w-W}{W} \le 0$. 
These conditions allow us to use the following Bernoulli inequality (proof by induction):

$$
(1+x)^n \le \frac{1}{1 - nx}, \;\;\; \forall x \in [-1,0], \forall n \in \mathbb{N}.
$$ {#eq:bernoulli1}

From the Bernoulli inequality we have: 

$$
\Big(1+\rho \frac{w-W}{W}\Big)^n \le \frac{1}{1 - n \rho \frac{w-W}{W}}
$$ {#eq:l_g_k_eq_1_B}

Taken together, @Eq:l_g_k_eq_1_A and @Eq:l_g_k_eq_1_B imply that:

\begin{multline*}
f_A(0) f_B^{n+1}(0) = \\
\Big(1+\rho\frac{W-w}{w}\Big)\Big(1+\rho\frac{w-W}{W}\Big)\Big(1+\rho\frac{w-W}{W}\Big)^n = \\
\Big(1+\rho(1-\rho)\frac{(W-w)^2}{Ww}\Big)\Big(1+\rho\frac{w-W}{W}\Big)^n \le \\
\frac{1+\rho(1-\rho)\frac{(W-w)^2}{Ww}}{1 - n \rho \frac{w-W}{W}} < 1 \\\blacksquare
\end{multline*}

**Result.**
_If $k \ge 1$ and $l > k \Big( 1 + (1 - \rho) \frac{W - w}{w} \Big)$, then $f_A^k(0)f_B^l(0) < 1$, and $x^*=0$ is locally stable._

**Proof.**
First, assume $\frac{l-k}{k} \in \mathbb{N}$ and set $n = \frac{l-k}{k}$ so that $n > (1-\rho)\frac{W-w}{w}$.

Now, using the previous proposition,
$$
f_{A}^{k}(0) f_{B}^{l}(0) = \\
f_{A}^{k}(0) f_{B}^{(n+1)k}(0) = \\
(f_{A}(0) f_B^{n+1}(0))^{k} < 1
$$
because $\forall y>0, k>0 \; y < 1 \Rightarrow y^k < 1$.

Next, relax the assumption $\frac{l-k}{k} \in \mathbb{N}$; set $n = \lceil{\frac{l-k}{k}}\rceil > \frac{l-k}{k} > (1-\rho)\frac{W-w}{w}$, then
$$
f_A^k(0) f_B^l(0) < \\
f_A^k(0) f_B^{(n+1)k}(0) = \\
(f_A(0) f_B^{n+1}(0))^k < 1
$$
and again, the previous proposition provides the last inequality.
$\blacksquare$

**Result.**
_If $k \ge 1$ and $k < l < k \Big( 1 + \frac{(1-\rho) \frac{W-w}{w}}{1 + \rho (1-\rho) \frac{(W-w)^2}{W w}} \Big)$ then $f_A^k(0) f_B^l(0) > 1$ so that $x^*=0$ is locally unstable and there is a protected polymorphism._

**Proof.**
Similarly to the previous proposition, but using a different Bernoulli inequality:

$$\begin{aligned}
(1+x)^n \ge 1+nx, \;\;\; \text{for all} x > -1, \text{and} \in \mathbb{R} \smallsetminus (0,1). \\
\blacksquare
\end{aligned}$$

### _A1B1_ regime

When the environment changes every generation, we can write the following recurrence, which sets $\omega_A=W, \omega_B=w$ in [@Eq:recurrence0] to determine $x'$ and and then sets $\omega_A=w, \omega_B=W$ to determine $x''$:

$$\begin{aligned}
x' = x \frac{x (1-\rho) (W - w) + \rho W + (1-\rho)w}{x (W-w) + w} \\
x'' = x' \frac{x' (1-\rho) (w - W) + \rho w + (1-\rho)W}{x' (w-W) + W}
\end{aligned}$$ {#eq:recurrenceA1B1} 

We seek solutions to $x''=x$, which involves solving a quartic polynomial. 
Two solutions are $x=0,1$, but there nay be two other potential solutions, which are roots of a quadratic equation $G(x) = 0$ where $G(x) = Ax^2 + Bx + C$ with

$$
A = 1, \; B=- \frac{W (1-\rho) - w (3-\rho)}{(2-\rho)(W - w)}, \; C=- \frac{w}{(2-\rho)(W - w)}.
$$ {#eq:recurrenceA1B1_solution}

We found the roots of $G(x)$ using _SymPy_ [@SymPyDevelopmentTeam2014].

Since $W > w \ge 0, 1 \ge \rho \ge 0$,
$$
G(0) = C = \frac{-w}{(2-\rho)(W-w)} < 0
$$
and
$$\begin{aligned}
G(1) =
1 + B + C =
1 - \frac{W (1-\rho) - w (3-\rho) - w}{(2-\rho)(W-w)} = \\
\frac{W}{(2-\rho)(W-w)} > 0
\end{aligned}$$
and $lim_{x \to \pm \infty}{G(x)} = +\infty$.

Therefore, one root of $G(x)$ is negative and one, $x^*$, is positive and less than 1. $C<0$  and therefore $B < \sqrt{B^2-4C}$. Thus, $-B+\sqrt{B^2-4C}>0$ and $-B-\sqrt{B^2-4C}<0$, regardless of the sign of $B$, and:
$$\begin{aligned}
x^* = 
\frac{-B+\sqrt{B^2-4C}}{2} = & \\ &
\frac{W(1-\rho) - w(3-\rho) + \sqrt{(1-\rho)^2 (W-w)^2 + 4Ww}}{2 (2-\rho) (W-w)}
\end{aligned}$$ {#eq:recurrenceA1B1_solution_x_star}

Note that if $\rho=0$ then $x^* = 1/2$, and if $\rho=1$ then $x^* = \frac{-w + \sqrt{Ww}}{(W-w)}$. 

@Fig:env_A1B1 compares $x^*$ (dashed green; @eq:recurrenceA1B1_solution_x_star) with deterministic iterations of @Eq:recurrenceA1B1 (blue) and the average of stochastic Wright-Fisher simulations (orange) for several combinations of $\rho$, _W_, and _w_. 
Iterations and simulations started with $x=0.5$; in the WF simulations, the population size is _N=100,000_, and the results are based on 100 simulations per parameter set. 
Note that the x-axis shows every other generation (end of each period).

![Frequency of phenotype _A_ after every two generation in environmental regime _A1B1_. Comparison of Wright-Fisher simulations (orange line is the average of 100 simulations; shaded orange area is the 1% confidence interval), a deterministic iteration (blue; @eq:recurrenceA1B1), and equilibrium solution (dashed green; @eq:recurrenceA1B1_solution_x_star). Parameters: _W_=1, _N=1,000,000_, initial value $x=0.5$.](figures/env_A1B1.pdf){#fig:env_A1B1}

#### Evolutionary genetic stability of $\rho=0$

We now consider two modifier alleles in the _A1B1_ regime (@eq:recurrence_modifiers) as described in @tbl:modifier_model_table.
Let's assume that _m_ is fixed such that $p=1, q=0$ and that the population is at an equilibrium $x=x^*$ (@eq:recurrenceA1B1_solution_x_star).

If another modifier allele _M_ appears in low frequency $q \ll 1$ such that initially $y=x^*$, can _M_ invade the population and increase in frequency, or is the equilibrium $p=1, x=x^*$ stable?

To answer this question, we examine the relative change in frequency of _M_ after a full environmental cycle (two generations), $\lambda$, where in the first generation _A_ is the preferred phenotype with advantage _s_ ($\omega_A=1+s, \omega_B=1$) and in the second generation _B_ is the preferred phenotype with advantage _s_ ($\omega_A=1, \omega_B=1+s$). 
Because $p \approx 1$, the population mean fitness is dominated by _m_ ($\bar{\omega} = x \omega_A + (1-x) \omega_B)$, 
and we can write $\lambda$ as a function of the two rates $\rho$ and $P$ using @eq:recurrence_modifiers:
\begin{multline}\label{eq:modifiers_lambda}
\lambda(\rho, P) = \frac{q''}{q} = \frac{q''}{q'} \cdot \frac{q'}{q} = \\
\frac{y' + (1-y') (1+s)}{x' + (1-x') (1+s)} \cdot 
    \frac{y (1+s) + (1-y)}{x (1+s) + (1-x)} = \\
\frac{1 + s - s y'}{1 + s - s x'} \cdot \frac{1 + s y}{1 + s x} = \\
\frac{1 + s + s^2 (1-P) x^* (1-x^*)}{1 + s + s^2 (1-\rho) x^* (1-x^*)},
\end{multline}
where both the _m_ and the _M_ populations are initially at the equilibrium value for environmental regime A1B1 ($x=y=x^*$) as found in @Eq:recurrenceA1B1_solution_x_star,
and we use @eq:recurrence_modifiers to calculate $x', y'$.

For $1 > P > \rho = 0$, we have $x^* = x^{**} = \frac{1}{2}$, which leads to
$\lambda(0,P) = 1 - P(\frac{s}{2+s})^2 < 1$.

For $\rho = 1 > P > 0$, we have $x^* = \frac{\sqrt{1+s}-1}{s}, x^{**}=x^* \sqrt{1+s}$, which leads to $\lambda(1, P) = 1 + (1-P)\frac{(\sqrt{1+s}-1)^2}{\sqrt{1+s}} > 1$.

More generally,
$$
\frac{\partial }{\partial P} \lambda(\rho, P) = 
\frac{-s^2 x (1-x)}{1 + s + s^2 (1-\rho) x^*(1-x^*)} < 0,
$$
and because $\lambda(\rho, \rho)= 1$, we can deduce that if $P<\rho$ then $\lambda(\rho, P) > 1$ and _M_ can invade _m_; and vice verse, if $P>\rho$ then $\lambda(\rho, P) < 1$ and _m_ cannot be invaded by _M_ (@Fig:A1B1_EGS_eta_0 B). 
It follows that in the _A1B1_ regime, the only parental effect that can lead to evolutionary genetic stability [@Lessard1990] is $\rho=0$; that is, no parental effect and complete group conformity.

Note that the stable population mean fitness after each _AB_ cycle as a function of $\rho$ is (@Fig:A1B1_EGS_eta_0 A):
$$
\bar{\omega}^*(\rho)=1 + \frac{W(1-\rho)-w(3-\rho)+\sqrt{(1-\rho)^2s^2+4(1+s)}}{2(2-\rho)},
$$ {#eq:A1B1_mean_fitness}

With $\rho=0$ we have $\bar{\omega}^*(0)=1+\frac{s}{2}$,
whereas with $\rho=1$ we have $\bar{\omega}^*(1) = \sqrt{1+s} = \bar{\omega}^*(0) - \frac{s^2}{8} + o(s^2)$; 
in general, $\bar{\omega}^*(\rho)$ is a decreasing function of $\rho$, and is therefore maximized at $\rho=0$ (@Fig:A1B1_EGS_eta_0). 
Indeed, iterating the recurrence equations (@eq:recurrence_modifiers) while introducing modifiers with lower and lower inheritance rates shows that these invading modifiers sequentially reduce the parental effect towards zero, but only when successive modifier alleles are introduced near $x=0.5$ (@Fig:A1B1_modifier_invasions A).

![Evolutionary stability of $\rho=0$ in environmental regime _A1B1_. **(A)** Stable population mean fitness (@eq:A1B1_mean_fitness) as a function of the parental effect rate $\rho$ and the selection coefficient _s_ of the favorable phenotype. **(B)** The relative change in frequency of a modifier allele  $\lambda(0, P)$ (@eq:modifiers_lambda) with rate $P$ invading a population fixed at $\rho=0$ after a full environmental cycle.](figures/A1B1_EGS_eta_0.pdf){#fig:A1B1_EGS_eta_0}

![Consecutive fixation of modifiers that decrease the parental effect rate in environmental regime _A1B1_. The figure shows results of numerical simulations of evolution with two modifier alleles (@Eq:recurrence_modifiers). Every time a modifier allele fixes (frequency>99.9%), a new modifier allele is introduces with a rate one order of magnitude lower (vertical dashed lines). **(A)** The frequency of phenotype _A_ in the population over time. **(B)** The frequency of the invading modifier allele over time. **(C)** The population mean parental effect rate over time. Parental effect rate of initial resident modifier allele, $\rho_0 =0.1$; fitness values: _W=1, w=0.1_.](figures/A1B1_modifier_invasions.pdf){#fig:A1B1_modifier_invasions}

### _A2B1_ regime

In the _A2B1_ regime (every two generations which phenotype _A_ is favored are followed by a single generation in environment in which phenotype _B_ is favored), an analytic solution is not possible, as solving $x'''-x=0$ requires solving a polynomial of degree 6. However, iterating the relevant recurrence equation:
$$\begin{aligned}
x' = x \frac{x (1-\rho) (W-w) + \rho W + (1-\rho)w}{x (W-w) + w} \\
x'' = x' \frac{x' (1-\rho) (W-w) + \rho W + (1-\rho)w}{x' (W-w) + w} \\
x''' = x'' \frac{x'' (1-\rho) (w-W) + \rho w + (1-\rho)W}{x'' (w-W) + W}
\end{aligned}$$ {#eq:recurrenceA2B1}
provides similar results: the equilibrium value is close to the Wright-Fisher simulations for extreme selection ($w/W=0$) but over-estimates the equilibrium otherwise (@Fig:env_A2B1). **TODO**

![Frequency of phenotype _A_ after every three generation in environmental regime _A2B1_. Comparison of Wright-Fisher simulations (orange line is the average of 100 simulations; shaded orange area is the 99% confidence interval) and a deterministic iteration (blue; @eq:recurrenceA2B1). Parameters: _W_=1, _N=10,000_, initial population $x=0.5$.](figures/env_A2B1.pdf){#fig:env_A2B1}

#### Summary of results

TODO

## Stochastic environments

Consider a stochastic environment in which the fitness of phenotypes _A_ and _B_ at generation $t$ are $1+s_t$ and $1$, respectively, where the random variables $s_t \; (t=0, 1, 2, ...)$ are independent and identically distributed (i.i.d) and there are positive constants _C_ and _D_ such that $P(C \le s_t \le D) = 1$.

The recursion for this model can be rewritten as (based on @eq:recurrence0):
$$
x_{t+1} = x_t \frac{1 + \rho s_t + x_t (1-\rho) s_t}{1 + s_t x_t}.
$$ {#eq:recurrence_random_env}

Our analysis follows @Karlin1975 (see also @Carja2013).

**Definition: stochastic local stability.**
An equilibrium state $x^*$ is said to be _stochastically locally stable_ if for any $\epsilon>0$ there exists $\delta>0$ such that
$$
x_0 < \delta \Rightarrow P(\lim_{t \to \infty}{x_t} = x^*) \ge 1-\epsilon
$$ {#eq:SLS}

Thus, _stochastic local stability_ of $x^*$ means that if the frequency $x_t$ is sufficiently close to $x^*$, then it will eventually converge to $x^*$ with _high probability_. Note, however, that convergence is likely, but not certain.

**Result.**
_Suppose $\mathbb{E}[\log{(1+\rho s_t)}] > 0$, then $x^*=0$ is not _stochastically locally stable_, 
and in fact $P(\lim_{t \to \infty}{x_t}=0) = 0$._

**Proof.**
Rewrite the recursion (@eq:recurrence_random_env) as
$$
\frac{x_{t+1}}{x_{t}} = (1 + \rho s_t) \Big(1 - x_t \frac{\rho s_t (1+s_t)}{(1+\rho s_t)(1+x_t s_t)} \Big)
$$

Taking the log of both sides leads to:
$$
\log{x_{t+1}} - \log{x_{t}} = 
\log{(1+\rho s_t)} +
\log{\Big(1 - x_t \frac{\rho s_t (1+s_t)}{(1+\rho s_t)(1+x_t s_t)} \Big)}
$$

Summation yields:
$$
\frac{1}{t} (\log{x_{t}} - \log{x_{0}}) = 
\frac{1}{t} \sum_{n=0}^{t-1}{\log{(1+\rho s_n)}} + 
\frac{1}{t} \sum_{n=0}^{t-1}{\log{\Big(1 - x_n \frac{\rho s_n (1+s_n)}{(1+\rho s_n)(1+x_n s_n)} \Big)}}
$$

Let $\mu = \mathbb{E}[\log{(1+\rho s_t)}]$.
Because $\{s_t\}_{t \ge 0}$ are i.i.d. random variables, the strong law of large numbers (SLLN) applies and almost surely
$$
\lim_{t \to \infty}{\frac{1}{t} \sum_{n=0}^{t-1}{\log{(1+\rho s_n)}}} = \mu.
$$

Consider $\xi$ such that $\lim_{t \to \infty}{\frac{1}{t} \sum_{n=0}^{t-1}{\log{(1+\rho s_n(\xi))}}} = \mu, C \le s_t(\xi) \le D$ and assume that almost certainly $x^* = 0$, i.e.:
$$
\lim_{t \to \infty}{x_t(\xi)} = 0.
$$ {#eq:T1_assumption}

Because $0 \le \rho \le 1$, 
and $\{s_t(\xi)\}_{t \ge 0}$ are uniformly bounded away from zero and infinity,
we can deduce that
$$
\lim_{t \to \infty}{\frac{1}{t} \sum_{n=0}^{t-1}{\log{\Big(1 - x_n \frac{\rho s_n (1+s_n)}{(1+\rho s_n)(1+x_n s_n)} \Big)}}} = 0 ,
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

**Q: DOES THIS (=0) CONTRADICT ALMOST CERTAINLY AT (18)? MF**

Thus, for $x^*=0$ to be _stochastically locally stable_, it is necessary that $\mathbb{E}[\log{(1+\rho s_t)}] \le 0$. Furthermore, we can prove that the strict inequality is sufficient.

**Result.**
_Suppose $\mathbb{E}[\log{(1+\rho s_t)}] < 0$,
then $x^*=0$ is _stochastically locally stable_._

**Proof.**
Let $\mu = \mathbb{E}[\log{(1+\rho s_t)}] < 0$. 
Because $\{s_t\}_{t \ge 0}$ are i.i.d. random variables, the SLLN applies and almost surely
$$
\lim_{t \to \infty}{\frac{1}{t} \sum_{n=0}^{t-1}{\log{(1+\rho s_n)}}} = \mu.
$$

Appealing to the _Severini–Egoroff theorem_,
for any $\epsilon > 0$, there exists $T$ such that (remember that $\mu$ is negative):
$$
P\Big(\frac{1}{t} \sum_{n=0}^{t-1}{\log{(1 + \rho s_n)}} < \frac{\mu}{2} 
\; \text{for all} t \ge T \Big) \ge 1 - \epsilon.
$$

Because $0 \le \rho \le 1$ and $\{s_t(\xi)\}_{t \ge 0}$ are uniformly bounded away from zero and infinity, we can find $\delta'>0$ such that:
$$
x_t < \delta' \Rightarrow 
\Big| \log{\Big(1 - x_t\frac{\rho s_t (1+s_t)}{(1+\rho s_t)(1+x_t s_t)} \Big)} \Big| < -\frac{\mu}{4}.
$$

Also, 
$$
x_{t+1} = x_t \frac{x_t (1-\rho) s_t + \rho (1+s_t) + 1 - \rho}{1 + s_t x_t} < C \cdot x_t,
$$

where $C \in \mathbb{R}$ is independent of $t$; it follows that there exists $0 < \delta < \delta'$ such that:

$$
x_0 < \delta \Rightarrow x_t < \delta', \; t=0, 1, 2, ..., T-1.
$$

Let $\xi$ be a realization of the evolutionary process such that
$$
\frac{1}{t} \sum_{n=0}^{t-1}{\log{(1 + \rho s_n(\xi))}} < \frac{\mu}{2} \; \text{for all} t \ge T
$$ 
and assume $x_0 < \delta$.

Then:
\begin{multline*}
\frac{1}{T} \Big(\log{x_T(\xi)} - \log{x_0(\xi)}\Big) =
\frac{1}{T} \sum_{t=0}^{T-1}{\log{\Big(1 + \rho s_t(\xi)\Big)}} + \\
+ \frac{1}{T} \sum_{t=0}^{T-1} \log{\Big(1 - x_t(\xi)\frac{\rho s_t(\xi) (1+s_t(\xi))}{(1+\rho s_t(\xi))(1+x_t(\xi) s_t(\xi))} \Big)} < \\
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

- if $\mathbb{E}[\log{(1+\rho s_t)}] < 0$ then fixation of $x^*=0$ is _stochastically locally stable_.
- if $\mathbb{E}[\log{(1+\rho s_t)}] > 0$ then fixation of $x^*=0$ almost never occurs.
- if the fitness of phenotype _B_ is also a random variable, such that the fitness values of phenotypes _A_ and _B_ are $\tau_t, \sigma_t$, respectively, than we can normalize the fitness values by $\sigma_t$ and denote $s_t=\frac{\tau_t-\sigma_t}{\sigma_t}$. The above results then apply.
- the above results will stand for any sequence $\{s_t\}_{t \ge 0}$ for which the SLLN applies, even if they are not i.i.d.
- @Fig:stochastic_env_x_t shows $x_{t=10^6}$ with $\rho=0.01$ and initial value $x_0=10^{-3}$ for different selection coefficients _s_ and _p_ the probability of favoring phenotype _A_. The white lines represent _s_ and _p_ values for which $\mathbb{E}[\log{(1 + \rho s_t)}] = 0$; indeed, below this line $x_t$ tends to converge to 0.

![Stochastic local stability. The figure shows the frequency of phenotype _A_ after $10^6$ generations in a very large population evolving in a stochastic environment (@eq:recurrence_random_env). The fitness of phenotypes _A_ and _B_ are $1+s_t$ and $1$, where $s_t$ is _s_ with probability _p_ and _-s_ with probability _1-p_. The white line marks combinations of _p_ and _s_ for which $\mathbb{E}[\log{(1+\rho s_t)}]=0$; according to our analysis, we expect that  below this line $x^*=0$ will be stochastically locally stable. Parameters: $x_0=0.1$; $\rho=0.1$](figures/stochastic_env_x_t.pdf){#fig:stochastic_env_x_t}

# References {-}