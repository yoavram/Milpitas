---
title: Vertical and oblique transmission under fluctuating selection
author:
- Yoav Ram^[Department of Biology, Stanford University, Stanford, CA 94305-5020, yoav@yoavram.com]
- Uri Liberman^[School of Mathematical Sciences, Tel Aviv University, Tel Aviv, Israel 69978, uril@tauex.tau.ac.il]
- Marcus W. Feldman^[Corresponding author; Department of Biology, Stanford University, Stanford, CA 94305-5020, mfeldman@stanford.edu]
year: 2017
abstract: |
    TODO
chapters: True
chaptersDepth: 1
chapDelim: ""
link-citations: true
header-includes:
    - \usepackage{lineno}
    - \linenumbers
---

\newpage

# Introduction {-}

Since the emergence of the *modern synthesis* in the 1940s, evolutionary
biology has been structured around genetic inheritance as the transmission mode of traits between generations [@Laland2014].
Indeed, most evolutionary biology textbooks begin by describing evolution
through natural selection as a process in which *"genetic changes that
improve the fitness of individuals will tend to increase in frequency
over time"* [@Bergstrom2012, ch. 1.1].

However, it is apparent that in many animals, and especially in humans,
some traits are transmitted through imitation, teaching, learning,
and other forms of communication that comprise *cultural evolution*
[@Cavalli-Sforza1973; @Cavalli-Sforza1981; @Boyd1985; @Avital2000; @Whiten2017; @Laland2017].
Other non-genetic phenotype-modifying transmission vehicles have received increasing attention over the past two decades [@Jablonka2014], including
epigenetics [@Verhoeven2016], symbionts [@Zilber-Rosenberg2008], and even prions [@Wickner2016].
These transmission mechanisms vary in their persistence, speed, timing, and direction when compared to the kind of vertical transmission between parent and offspring that is restricted to genetic inheritance.

Of special interest is *oblique transmission* [@Cavalli-Sforza1981, pg.54; @Bergstrom2012, ch. 19.4], 
in which offspring inherit traits from adults that are not their parents.
One mechanism for oblique transmission is social learning, e.g., imitation and teaching [@Kline2013].
For example, in a small Amazon society, in which young individuals
frequently interact with older individuals, transmission of botanical
knowledge and skills from the parental cohort was more significant than
transmission from parents [@Reyes-Garcia2009].
In contrast, in tribal Iranian populations, transmission of weaving techniques from parents has a larger effect than oblique transmission [@Tehrani2009, more examples therein].
Social learning is also common in birds and mammals [@Creanza2016], and evidence suggests a role for oblique transmission in inheritance of foraging strategies in dolphins [@Mann2007; @Whitehead2014; @Creanza2016].

**TODO: niche construction as a form of oblique transmission?**

The microbiome provides another mechanism for oblique transmission.
Although it is usually vertically transmitted [@Rosenberg2016], both symbionts and pathogens can be transmitted between unrelated individuals, and can lead to phenotype change in the host.
Therefore, transmission of symbionts from the parental cohort may be regarded as oblique transmission [@Theis2016].

Oblique transmission also occurs through mechanisms involving DNA.
In bacteria, phenotypes might be determined by heritable mobile genetic
elements such as phages [@Zinder1952], plasmids [@Lederberg1946], integrons [@Mazel2006], and transposons [@Salyers2004](**TODO: CRISPR?**).
Similarly, some phenotypes are determined by genes that are commonly converted by uptake of foreign DNA, i.e. transformation [@Milkman1990].
In these cases, inheritance of a phenotype may combine vertical transmission from the parent cell and oblique transmission from other cells, even if the latter did not originally evolve for that purpose [@Redfield1993].

Here, we model the dynamics of a phenotype that is inherited by a
combination of vertical and oblique transmission.
We study properties of the steady state frequencies of phenotypic variants in constant and fluctuating selection, and find conditions under which oblique
transmission is likely to evolve.
Our model is loosely based on a recently published model of phenotype switching by @Xue2016.
However, in their study the phenotype distribution is a vertically transmitted trait, modified by parental effects, whereas in our study the phenotype is the transmitted trait, and the phenotype distribution is represented by the population.

# Model {-}

Consider a population of individuals with one of two phenotypes, $\phi=A$ or $B$.
The frequency of phenotypes _A_ and _B_ are _x_ and _1-x_,
the fitness of phenotypes _A_ and _B_ is $\omega_A$ and $\omega_B$,
and the population mean fitness is $\bar{\omega} = x \omega_A + (1-x) \omega_B$ (@Tbl:model_parameters_table).

An offspring inherits its phenotype vertically from its parent with probability $\rho$, and diagonally from a random individual in the parental population with probability $1-\rho$.
Therefore, given the parent phenotype is $\phi$ and assuming uni-parental inheritance [@Zefferman2016],
the probability that the phenotype $\phi'$ of an offspring is _A_ is:
$$
P(\phi' = A) = \begin{cases}
(1-\rho) x + \rho, & \phi = A \\
(1-\rho) x, & \phi = B
\end{cases},
$$ {#eq:inheritance_rule}

where $\rho$ and $1-\rho$ are the vertical and oblique transmission rates (@Tbl:model_parameters_table).

**Q: not sure what to do about the next paragraph**

Averaging @eq:inheritance_rule over the population, we get

$$
\mathbb{E}[P(\phi' = A)] = \\
x((1-\rho) x + \rho) + (1-x)(1-\rho)x = \\
x,
$$

which does not depend on $\rho$ and demonstrates that this inheritance mode is unbiased.
However, the population variance in @eq:inheritance_rule is

$$
\mathbb{V}[P(\phi' = A)] = \\
\mathbb{E}[P(\phi' = A)^2] - \mathbb{E}^2[P(\phi' = A)] = \\
\rho^2 x (1-x),
$$

so that the population variance increases with the rate of vertical transmission $\rho$, from zero variance for complete oblique transmission ($\rho=0$), to a Bernoulli distribution variance value of $x(1-x)$ for complete vertical transmission ($\rho=1$).

The following recursion describes $x'$, the expected frequency of phenotype _A_ in the next generation, given that the frequency of phenotype _A_ in the current generation is _x_ (@Fig:recurrence_example A):

$$
x' = x \cdot \frac{\omega_A}{\bar{\omega}} \cdot ((1-\rho)x + \rho) + (1-x) \cdot \frac{\omega_B}{\bar{\omega}} \cdot (1-\rho)x.
$$ {#eq:recurrence}

@Eq:recurrence can be reorganized to
$$
x' = x \frac{x (1-\rho) (\omega_A - \omega_B) + \rho \omega_A + (1-\rho)\omega_B}{x (\omega_A - \omega_B) + \omega_B}.
$$ {#eq:recurrence0}

| Parameter | Description |
|----------|----------------------------------------|
| N | constant population size |
| $\phi$ | phenotype,  $\phi \in \{A,B\}$ |
| $\Phi$ | phenotype favored in the current generation, $\Phi \in \{A, B\}$|
| $W$ | fitness of favored phenotype $\phi = \Phi$ |
| $w$ | fitness of unfavored phenotype $\phi \ne \Phi$ |
| $\omega_{\phi}$ | fitness of phenotype $\phi$ in the current generation, $\omega_{\phi}=W \cdot 1_{\phi = \Phi} + w \cdot 1_{\phi \ne \Phi}$ |
| $\bar{\omega}$ | population mean fitness |
| $x$| frequency of phenotype _A_|
| $\rho$| vertical transmission rate, $0 \le \rho \le 1$, such that $1-\rho$ is the oblique transmission rate|

: Model parameters. {#tbl:model_parameters_table}

![Dynamics of _x_ the frequency of phenotype _A_. **(A)** The change in frequency of _A_ between consecutive generations, $x \to x'$ (@eq:recurrence), for different vertical transmission rates ($\rho$). The shaded area marks $x' \le x$. **(B)** Evolution under constant selection with advantage to phenotype _A_ leads to fixation of phenotype _A_, and this fixation is faster for higher rates of vertical transmission $\rho$.  Parameters: _W_=1, _w_=0.9.](figures/recurrence_example.pdf){#fig:recurrence_example}

## Finite size population model

To include the effect of random drift, we carry out a binomial sampling after each generation, as in Wright-Fisher models [@Otto2007, ch. 13.4]. Therefore, given that the frequency of individuals with phenotype _A_ is _x_ in the parental generation, the probability that $k$ offspring are descendants of individuals with phenotype _A_ is

$$
{N \choose k}
\Big(x \frac{\omega_A}{\bar{\omega}}\Big)^k 
\Big((1-x) \frac{\omega_B}{\bar{\omega}}\Big)^{N-k}.
$$ {#eq:genetic_drift_rule}

With complete vertical transmission ($\rho=1$), this model simplifies to a standard Wright-Fisher two-allele model with selection and random genetic drift. Cavalli-Sforza and Feldman [-@Cavalli-Sforza1981, ch. 3.10] used a similar model to study drift in cultural evolution. 

## Modifier model

Consider two modifier alleles _m_ and _M_ that produce vertical transmission rates $\rho$ and $P$.
The frequencies of the four pheno-genotypes, _mA_, _mB_, _MA_, and _MB_ are $x_1$, $x_2$, $x_3$, and $x_4$, respectively, and their fitness values are determined by the phenotypes (_A_ and _B_) and the environment, same as above (@tbl:modifier_model_table).

| Pheno-genotype     | mA  | mB     | MA  | MB     |
|------|-----|--------|-----|--------|
| Frequency    | $x_1$  | $x_2$ | $x_3$  | $x_4$ |
| Fitness    | $\omega_A$ | $\omega_B$    | $\omega_A$ | $\omega_B$    |
| Vertical transmission rate | $\rho$   | $\rho$      | $P$   | $P$      |

: Modifier model. {#tbl:modifier_model_table}

The pheno-genotypes frequencies change according to (based on @eq:recurrence):

$$\begin{aligned}
\bar{\omega} x_1' = x_1 \omega_A ((1-\rho)(x_1 + x_3)+\rho) + x_2 \omega_B(1-\rho)(x_1 + x_3) \\
\bar{\omega} x_2' = x_1 \omega_A (1-\rho)(x_2 + x_4) + x_2 \omega_B ((1-\rho)(x_2 + x_4) + \rho) \\
\bar{\omega} x_3' = x_3 \omega_A ((1-P)(x_1 + x_3) + P) + x_4 \omega_B (1-P)(x_1 + x_3) \\
\bar{\omega} x_4' = x_3 \omega_A (1-P)(x_2 + x_4) + x_4 \omega_B ((1-P)(x_2 + x_4) + P) \\
\bar{\omega} = \omega_A (x_1 + x_3) + \omega_B (x_2 + x_4)
\end{aligned}$$ {#eq:recurrence_modifiers}

# Results {-}

## Constant selection

First consider constant selection favoring phenotype _A_, such that $\omega_A \ge \omega_B$ (@Fig:recurrence_example B). We seek $x^*$, the equilibrium frequency of phenotype _A_, which solves $x'=x$ in @Eq:recurrence.

The basic requirement for evolution via natural selection is a heritable phenotype that produces differential fitness. 
Therefore, if selection is neutral ($\omega_A = \omega_B$) or if there is no vertical transmission $\rho=0$, then any $0 \le x \le 1$ is an (unstable) equilibrium.

The following result agrees with previous models that include a combination of vertical and oblique transmission [@Cavalli-Sforza1981, pg. 251].

**Result: constant environment.**
_If $0 < \rho \le 1$ and $\omega_A > \omega_B$, then $x^* = 1$ is the equilibrium frequency of phenotype _A_  for any initial $x>0$, such that all the individuals will eventually have phenotype _A_._

**Proof.**
Rewrite @eq:recurrence0 as $x' = x \cdot \frac{f(x)}{g(x)}$ with $f(x) = (1-\rho)(\omega_A - \omega_B)x + \rho \omega_A + (1-\rho)\omega_B$ and $g(x) = (\omega_A - \omega_B)x + \omega_B$.

Clearly, $x'=x$ if and only if $f(x)=g(x)$ or $x=0$. 
However, _f_ and _g_ are both linear in _x_ and therefore can only intersect at one point.
Indeed, _f_ and _g_ intersect at $x=1$ ($f(1)=g(1)=\omega_A$), which means that $x=1$ solves $x'=x$. 
Since $f(0) = \omega_B + \rho(\omega_A + \omega_B) > \omega_B = g(0)$,
we can deduce that $f(x) > g(x)$ for any $x<1$ and hence $x' > x$ (see @Fig:recurrence_example A). $\blacksquare$

How does the convergence rate depend on $\rho$?
Note that $\frac{d (x' - x)}{d\rho} = \frac{(\omega_A-\omega_B) x (1-x) }{(\omega_A-\omega_B)x + \omega_B} > 0$, 
so the higher the vertical transmission rate, the faster the convergence to $x=1$ (@Fig:recurrence_example B).

### Extreme selection

A special case is that of extreme selection, in which individuals of the unfavored phenotype cannot reproduce - $\omega_A=1$ and $\omega_B=0$ - and
the recurrence equation (@eq:recurrence) simplifies to
$$
x' = (1-\rho)x + \rho.
$$
Note that precludes the case of $x=0$ which should lead to a population extinction within a single generation.

This recurrence has a closed form solution: $x_t$ the frequency of the favored phenotype _A_ after _t_ generations is (proof by induction, similar to [@Xue2016])
$$
x_t = 
1 - (1-\rho)^t (1-x_0)
$$
where $x_0$ is the initial frequency of phenotype _A_.

With perfect vertical transmission ($\rho=1$), fixation of the favored phenotype takes only a single generation, because only the favored phenotype reproduces and all offspring inherit their parent phenotype.
On the other hand, with perfect oblique transmission ($\rho=0$), phenotype frequencies do not change over time and the favored phenotype will never fix.
This is because oblique transmission decouples selection from inheritance: it allows the unfavored phenotype to be transmitted from the parental generation to the offspring generation despite the fact that all offspring are produced by parents with the favored phenotype.

With a mix of vertical and oblique transmission, we set $x_t=1-x_0$ to find the time $\tau$ required for the favored phenotype to become fixed ($x_t \approx 1$) when initialy rare ($x_0 \approx 0$):
$$
\tau = 
\frac{\log{(\frac{x_0}{1-x_0})}}{\log{(1-\rho)}} \approx 
\frac{\log{x_0}}{\log{(1-\rho)}}.
$$ {#eq:extreme_selection_fixation_time}

@Fig:extreme_selection_fixation_time A shows the fixation time $\tau$ for different values of $\rho$ and $x_0$, demonstrating that higher vertical transmission leads to significant decreases in fixation time.
Because of this reduced fixation time, modifier alleles that increase the vertical transmission rate can invade the population if the favored phenotype is initially rare, i.e. after a change in the selection regime (@Fig:extreme_selection_fixation_time B).

![Constant extreme selection. **(A)** Fixation time as a function of the  vertical transmission rate for different initial frequencies of phenotype _A_, based on @Eq:extreme_selection_fixation_time. **(B)** Competitions between two modifiers alleles (@eq:recurrence_modifiers). When the favored phenotype _A_ is intially rare, a modifier allele _m_ that increases the vertical transmission rate can invade the population. Parameters: vertical transmission rates: $\rho=0.1$ for _m_, $P=0.01$ for _M_; initial frequency of modifier allele _m_ and of phenotype _A_ are both independently 0.01.](figures/extreme_selection_fixation_time.pdf){#fig:extreme_selection_fixation_time}

## Periodically changing selection

Next, we consider selection regimes in which the favored phenotype changes after a fixed number of generations.
Simple examples are _A1B1=ABABABAB..._, in which the favored genotype $\Phi$  switches every generation,
or _A2B1=AABAABAAB..._ where every two generations in which selection favored phenotype _A_ are followed by a single generation in which selection favors phenotype _B_.

When the favored phenotype is _A_, the fitness of phenotypes _A_ and _B_ are _W_ and _w_, respectively; when the favored phenotype is _B_, the fitness of phenotypes _A_ and _B_ are reversed:
$$
\omega_{\phi} = \begin{cases}
W, & \phi = \Phi \\
w, & \phi \ne \Phi
\end{cases}.
$$

### _AkBl_ selection regime

In general, _AkBl_ denotes a selection regime in which the period is of length _k+l_ and is composed of exactly _k_ generations favoring phenotype _A_, followed by _l_ generations favoring phenotype _B_.
However, our general result applies for any permutation of these _k+l_ environments.

We investigate conditions for the the existence of a _protected polymorphism_ [@Prout1968], in which neither phenotype can //become extinct//disappear//. 
$x=1$ and $x=0$ are absorbing states:
if all individuals are _A_, for example, then all offspring will be _A_, too. 
Mathematically, we examine the stability of $x=0$ and $x=1$; 
if both are unstable, then there is a protected polymorphism. 
Intuitively, this will happen if neither phenotypes is favored frequently enough to fix.

Rewrite @Eq:recurrence0 as $x'=x \cdot f_A(x)$ when phenotype _A_ is favored and $x'=x \cdot f_B(x)$ when phenotype _B_ is favored, where:
$$\begin{aligned}
f_A(x) = \frac{x (1-\rho)(W - w) + \rho W + (1-\rho)w}{x (W - w) + w} \\
f_B(x) = \frac{x (1-\rho)(w - W) + \rho w + (1-\rho)W}{x (w - W) + W}
\end{aligned}$$

We assume $l \ge k$ and check whether fixation of _B_ ($x=0$) is stable, because 
(i) if $x=0$ is not stable when $l \ge k$ then $x=1$ cannot be stable either, as selection is, on the whole, stronger towards 0; and 
(ii) checking the other case (stability of $x=1$ when $k \ge l$) is symmetric, and can be done in the same way by writing a recurrence equation for the frequency _y_ of phenotype _B_ and checking the stability of $y=0$. 

To check whether $x=0$ is stable, we start with a value very close to 0 and check whether after a period of _k+l_ generations the population is closer to or farther from 0 compared to where it started.
This determines the local stability of $x=0$.

For $x_0 = x(t=0) \sim 0$, we use a linear approximation of the form $f_A(x_0) = f_A(0) + o(x_0)$ and $f_B(x_0) = f_B(0) + o(x_0)$, where:
$$\begin{aligned}
f_A(0) =  1+\rho(\frac{W-w}{w}) \\
f_B(0) =  1+\rho(\frac{w-W}{W})
\end{aligned}$$

For _k_ generations in an environment favoring phenotype _A_, and _l_ generations in an environment favoring phenotype _B_, in any given order, we can write:
$$\begin{aligned}
x_{k+l} = x(t=k+l) \approx
x_0 f_A^k(0) f_B^l(0) \Rightarrow \\
\frac{x_{k+l}}{x_0} \approx f_A^k(0) f_B^l(0).
\end{aligned}$$

Thus, starting close enough to zero ($x_0 \sim 0$), the multiplicative change over the _k+l_ generations can be approximated by $f_A^k(0) f_B^l(0)$.

If $f_A^k(0) f_B^l(0) > 1$, then $x=0$ is not stable; since $x=1$ is not stable either (since $l \ge k$), there is a protected polymorphism ($0 < x(t) < 1$ for any generation _t_). 
In contrast, if $f_A^k(0) f_B^l(0) < 1$, then $x=0$ is locally stable.

In the following, we examine the conditions for a protected polymorphism. 
We start with some trivial cases. 
First, in the neutral case ($W = w$), we find that $f_A(x) = f_B(x) \equiv 1$, without an approximation.

Second, with complete oblique transmission $\rho = 0$, the expected phenotype frequency does not change over time.
Indeed, we get $f_A(x) = f_B(x) \equiv 1$.

Third, with complete vertical transmission $\rho = 1$, the model becomes a standard two-allele model with $f_A^k(0) f_B^l(0) = \Big(\frac{W}{w}\Big)^{k-l}$. 
Since $W > w$, we find that
$$
\frac{x_{k+l}}{x_0} = 
\begin{cases}
< 1 &, k < l \\
= 1 &, k = l \\
> 1 &, k > l
\end{cases}
$$

**Result.**
_If $k=l, 0 < w < W, 0 < \rho < 1$, then $f_A^k(0) f_B^l(0) > 1$ and $x^*=0$ is locally unstable. In this case there is a protected polymorphism._

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
_If $k=1$, $w < W$, and $l > 1 + (1-\rho)\frac{W-w}{w}$ then $f_A(0)f_B^l(0) < 1$, and $x^*=0$ is locally stable. In this case, phenotype _B_ will eventually fix in the population._

**Proof.**
Set $n = l - 1$. Then,

\begin{multline}\label{eq:l_g_k_eq_1_A}
n > (1-\rho)\frac{W-w}{w} \Leftrightarrow \\
 n \rho \frac{W-w}{W}  > \rho (1-\rho)\frac{(W-w)^2}{Ww} \Leftrightarrow \\
1 + n \rho \frac{W-w}{W} > 1 + \rho (1-\rho)\frac{(W-w)^2}{Ww} \Leftrightarrow \\
1 >  \frac{1+\rho(1-\rho)\frac{(W-w)^2}{Ww}}{1 + n \rho \frac{W-w}{W}} \\
1 >  \frac{1+\rho(1-\rho)\frac{(W-w)^2}{Ww}}{1 - n \rho \frac{w-W}{W}} \\
\end{multline}

Now, if $w < W$, then $0 \le \frac{W-w}{W} \le 1$, and together with $0 \le \rho \le 1$ we have $-1 \le \rho \frac{w-W}{W} \le 0$. 
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
_If $k \ge 1$ and $l > k \Big( 1 + (1 - \rho) \frac{W - w}{w} \Big)$, then $f_A^k(0)f_B^l(0) < 1$, and $x^*=0$ is locally stable. In this case, phenotype _B_ will eventually fix in the populations._

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
_If $k \ge 1$ and $k < l < k \Big( 1 + \frac{(1-\rho) W (W - w)}{W w + \rho (1-\rho) (W - w)^2} \Big)$ then $f_A^k(0) f_B^l(0) > 1$ so that $x^*=0$ is locally unstable and there is a protected polymorphism._

**Proof.**
First, note that $\frac{(1-\rho) W (W - w)}{W w + \rho (1-\rho) (W - w)^2} = \frac{(1-\rho) \frac{W-w}{w}}{1 + \rho (1-\rho) \frac{(W-w)^2}{W w}}$.
Next, proceed similarly to the previous result, but using a different Bernoulli inequality:

$$\begin{aligned}
(1+x)^n \ge 1+nx, \;\;\; \text{for all} x > -1, \text{and} \in \mathbb{R} \smallsetminus (0,1). \\
\blacksquare
\end{aligned}$$


In general, we find that (@Fig:lk_phase_plane):

- A protected polymorphism exists if $\frac{l}{k} < 1 + \frac{(1-\rho) W (W - w)}{W w + \rho (1-\rho) (W - w)^2}$.
- $x=0$ is a stable equilibrium if $\frac{l}{k} > 1 + (1-\rho)\frac{W-w}{w}$.
- Both of these condition decreae when $\rho$ increases.

![Ratios of selection periods $\frac{l}{k}$ that lead to fixation of phenotype _B_ (red) or polymorphism between phenotypes _A_ and _B_ (blue). _l_ and _k_ are the number of generations in which phenotypes _B_ and _A_ are favored bu selection. Parameters: _W_ = 1.](figures/lk_phase_plane.pdf){#fig:lk_phase_plane}

### _A1B1_ selection regime

When the favored phenotype switches every generation, we can write the following recurrence, which sets $\omega_A=W, \omega_B=w$ in [@Eq:recurrence0] to determine $x'$ and and then sets $\omega_A=w, \omega_B=W$ to determine $x''$:

$$\begin{aligned}
x' = x \frac{x (1-\rho) (W - w) + \rho W + (1-\rho)w}{x (W-w) + w} \\
x'' = x' \frac{x' (1-\rho) (w - W) + \rho w + (1-\rho)W}{x' (w-W) + W}
\end{aligned}$$ {#eq:recurrenceA1B1} 

We seek solutions to $x''=x$, which involves solving a quartic polynomial. 
Two solutions are $x=0$ and $x=1$, but there may be two other potential solutions, which are roots of a quadratic equation $G(x) = 0$ where $G(x) = Ax^2 + Bx + C$ with

$$
A = 1, \; B=- \frac{W (1-\rho) - w (3-\rho)}{(2-\rho)(W - w)}, \; C=- \frac{w}{(2-\rho)(W - w)}.
$$ {#eq:recurrenceA1B1_solution}

Since $0 \le w < W$ and $0 \le \rho \le 1$,
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
\frac{1}{2} - \frac{W + w - \sqrt{(1-\rho)^2(W-w)^2 + 4Ww}}{2(2-\rho)(W-w)}.
\end{aligned}$$ {#eq:recurrenceA1B1_solution_x_star}

In particular, if $\rho=0$ then $x^* = \frac{1}{2}$, and if $\rho=1$ then $x^* = \frac{\sqrt{Ww} - w}{W - w} < \frac{1}{2}$ (because $\sqrt{Ww}-w < W - \sqrt{Ww}$). 
In addition, the stable population mean fitness after each _AB_ cycle as a function of the vertical transmission rate $\rho$ is (@Fig:A1B1_mean_fitness):
$$
\bar{\omega}^* = Wx^* + w(1-x^*) =
\frac{(W+w)(1-\rho) + \sqrt{(W-w)^2(1-p)^2+4Ww}}{2(2-\rho)}.
$$ {#eq:A1B1_mean_fitness}

@Fig:env_A1B1 demonstrates the good fit between $x^*$ (dashed green; @eq:recurrenceA1B1_solution_x_star), iterations of @Eq:recurrenceA1B1 (blue) and the average of finite population model simulations (orange) for several combinations of $\rho$ and _w_.

![Frequency of phenotype _A_ after every two generation in selection regime _A1B1_. Comparison of the finite population model (orange; average of 100 simulations), the infinite population model (blue; @eq:recurrenceA1B1), and the equilibrium solution (dashed green; @eq:recurrenceA1B1_solution_x_star). Parameters: _W_=1, _N=100,000_, initial value $x=0.5$.](figures/env_A1B1.pdf){#fig:env_A1B1}

### Evolutionary stability of oblique transmission

We now consider two modifier alleles in the _A1B1_ selection regime as described in @tbl:modifier_model_table.
Let's assume that _m_ is fixed and that the population is at an equilibrium such that $\vec{x}=(x_1,x_2,x_3,x_4)=(x^*, 1-x^*,0,0)$; see @eq:recurrenceA1B1_solution_x_star for the value of $x^*$.

If another modifier allele _M_ appears in low frequency $x_3=\epsilon_3<\epsilon, x_4=\epsilon_4<\epsilon, \epsilon \ll 1$, can _M_ invade the population and increase in frequency, or is the equilibrium $(x^*, 1-x^*,0,0)$ stable?

Extending @eq:recurrenceA1B1 to include two modifiers as in @eq:recurrence_modifiers, we get the following transformation $T$ which approximates the change in $\vec{x}$ after two generations with error of the order of $O(\epsilon)$:

$$\begin{aligned}
T_1 =  \frac{1}{\bar{\omega}^*} \begin{pmatrix}
W((1-P)x^*+P) & w(1-P)x^* \\
W(1-P)(1-x^*) & w((1-P)(1-x^*) + P)
\end{pmatrix}
\\
T_2 = \frac{1}{\bar{\omega}^{**}} \begin{pmatrix}
w((1-P)x^{**}+P) & W(1-P)x^{**} \\
w(1-P)(1-x^{**}) & W((1-P)(1-x^{**})+P)
\end{pmatrix} = \\
\frac{1}{\bar{\omega}^{*}} \begin{pmatrix}
w((1-P)(1-x^*)+P) & W(1-P)(1-x^*) \\
w(1-P)x^* & W((1-P)x^*+P)
\end{pmatrix}
\\
T = T_2 \cdot T_1
\end{aligned}$$

where $x^{**}=T_1 \cdot x^* = 1-x^*$ and $\bar{\omega}^{**}=x^{**} w + (1-x^{**}) W = \bar{\omega}^*$.

It follows that
\begin{multline}
T = \frac{1}{\bar{\omega}^{*2}} \cdot \\
\begin{pmatrix}
Ww((1-P)^2 x^* (1-x^*) + P) + (w(1-P)x^*)^2 &
W(1-P)(P + x^*(1-P))(W(1-x^*) + wx^*) \\
w(1-P)(1 - x^*(1-P))(W(1-x^*) + wx^*) &
Ww((1-P)^2 x^* (1-x^*) + P) + (W(1-P)(1-x^*))^2
\end{pmatrix}
\end{multline}

The characteristic polynomial of $T$ is $R(\lambda)=det(T-\lambda I)=a_2 \lambda^2 + a_1 \lambda + a_0$, where:

$$\begin{aligned}
a_0 = \frac{P^2 W^2 w^2}{\bar{\omega}^{*4}} \\
a_1 = - \frac{2 P W w + (1-P)^2 (W(1-x^*) + wx^*)^2}{\bar{\omega}^{*2}} \\
a_2 = 1
\end{aligned}$$

Since $T$ is positive, $R(\lambda)$ has two real roots.
Denote $R'(\lambda) = \frac{dR}{d\lambda}(\lambda)$.
Because $R(\lambda)$ is convex ($a_2=1$) and $R(0) = a_0 > 0, R'(0) =a_1 < 0$, both roots are positive.
Therefore, if $R(1)>0$ and $R'(1)>0$, then the largest root - the leading eigenvalue - is less than 1, and _m_ is stable to invasion by _M_.
However, if $R(1)<0$, then the leading eigenvalue is larger than 1, _m_ is unstable, and _M_ can invade _m_ [@Liberman2011].

An important quantity for the analysis of $R(1)$ is
$$
\bar{\omega}^{*2} - Ww = \\
(Wx^* + w(1-x^*))^2 - Ww = \\
(W-w)^2 x^{*2} -2w(W-w) x^* -w(W-w)
$$
Let $J(x) = (W-w)^2 x^2 +2w(W-w) x -w(W-w)$.
This is a convex polynomial with negative root $\frac{w-\sqrt{Ww}}{W-w}$ and positive root $\frac{\sqrt{Ww}-w}{W-w}$, which is the minimal value of $x^*$ given for $\rho=1$.
Therefore, we can determine that $\frac{Ww}{\bar{\omega}^{*2}}  \le 1$, with a strict inequality for $\rho < 1$.

In addition, we have $x^* \le \frac{1}{2}$, so $W(1-x^*) + wx^* \ge Wx^* + w(1-x^*)$ and therefore $\frac{W(1-x^*) + wx^*}{\bar{\omega}^*} \ge 1$, with strict inequality for $\rho > 0$.

Using these identities, we examine $R(1)$ and $R'(1)$ for $P=\rho$, $P=0$, and $P=1$:

$$\begin{aligned}
R(1) |_{P=p} = 
0 \\
R(1) |_{P=0} = 
1 - \Big(\frac{W(1-x^*) + wx^*}{\bar{\omega^*}}\Big)^2 < 0 \\
R'(1) |_{P=0} =
2 - \Big(\frac{W(1-x^*) + wx^*}{\bar{\omega^*}}\Big)^2 > 0 \\
R(1) |_{P=1} = 
\Big(1 - \frac{Ww}{\bar{\omega^*}^2}\Big)^2 > 0 \\
R'(1) |_{P=1} = 
2 \Big(1 - \frac{Ww}{\bar{\omega^*}^2}\Big) > 0 \\
\end{aligned}$$

where the last inequality is strict if $x^* \ne \frac{1}{2}$, which is the case when $\rho > 0$.

We found that in selection regime _A1B1_, an allele _m_ producing vertical transmission rate $\rho$ is stable to the introduction of allele _M_, with associated rate $P$, if $\rho < P$, and it is unstable if $\rho > P$.

Therefore, the rate of vertical transmission is expected to be reduced, similar to the _reduction principle_ for mutation, recombination, and migration rates [@Altenberg2017], and the only transmission mode that is _evolutionary stable_ is complete oblique transmission ($\rho=0$).

@Fig:A1B1_modifier_invasions shows the dynamics when iterating the recurrence equations (@eq:recurrence_modifiers) in selection regime _A1B1_ while introducing modifiers with lower and lower vertical transmission rates. Indeed, the invading modifier alleles sequentially fix and reduce the vertical transmission rate towards zero.
Importantly, reducing the vertical transmission rate also increases the population mean fitness (@Fig:A1B1_mean_fitness).

![Consecutive fixation of modifiers that reduce the vertical transmission rate in environmental regime _A1B1_. The figure shows results of numerical simulations of evolution with two modifier alleles (@eq:recurrence_modifiers). When a modifier allele fixes (frequency>99.9%), a new modifier allele is introduced with a vertical transmission rate one order of magnitude lower (vertical dashed lines). **(A)** The frequency of phenotype _A_ in the population over time. **(B)** The frequency of the invading modifier allele over time. **(C)** The population mean vertical transmission rate over time. Vertical transmission rate of the initial resident modifier allele, $\rho_0 =0.1$; fitness values: _W=1, w=0.1_. The x-axis is in log-scale, as each sequential invasion takes an order of magnitude longer to complete.](figures/A1B1_modifier_invasions.pdf){#fig:A1B1_modifier_invasions}

![Stable population mean fitness (**A**, @eq:A1B1_mean_fitness)  and phenotype _A_ frequency (**B**; @eq:recurrenceA1B1_solution_x_star) in selection regime _A1B1_ as a function of the vertical transmission rate $\rho$ and the fitness ratio $W/w$ between the favored and unfavored phenotype. Parameters: _W=1_.](figures/A1B1_mean_fitness.pdf){#fig:A1B1_mean_fitness}

### _A2B1_ selection regime

In the _A2B1_ selection regime (every two generations in which phenotype _A_ is favored are followed by a single generation in which phenotype _B_ is favored), an analytic solution is not possible, as solving $x'''-x=0$ requires solving a polynomial of degree six.
However, we iterated the relevant recurrence equation:
$$\begin{aligned}
x' = x \frac{x (1-\rho) (W-w) + \rho W + (1-\rho)w}{x (W-w) + w} \\
x'' = x' \frac{x' (1-\rho) (W-w) + \rho W + (1-\rho)w}{x' (W-w) + w} \\
x''' = x'' \frac{x'' (1-\rho) (w-W) + \rho w + (1-\rho)W}{x'' (w-W) + W}
\end{aligned}$$ {#eq:recurrenceA2B1}
and the dynamics are presented in @Fig:env_A2B1.

![Frequency of phenotype _A_ after every three generation in selection regime _A2B1_. Comparison of finite size population simulations (orange; average of 100 simulations) and infinite population iterations (blue; @eq:recurrenceA2B1). Parameters: _W_=1, _N=10,000_, initial population $x=0.5$.](figures/env_A2B1.pdf){#fig:env_A2B1}

### Summary

- Phenotypes _A_ and _B_ coexist in a protected polymorphism if the ratio between generations favoring _B_ and those favoring _A_ is less than $1 + \frac{(1-\rho)W(W-w)}{Ww+\rho(1-\rho)(W-w)^2}$.
- Phenotype _B_ fixation ($x=0$) is stable if the ratio between generations favoring _B_ and those favoring _A_ is more than $1 + (1-\rho)\frac{W-w}{w}$.
- Oblique transmission (low $\rho$ values) and strong selection (high fitness difference $W-w$) promote polymorphism (@Fig:lk_phase_plane).
- With complete vertical transmission ($\rho=1$), fixation of the more frequently favored phenotype is almost certain (@Fig:lk_phase_plane F).
- An explicit expression for the stable frequency of phenotype _A_ in the _A1B1_ selection regime is given by @Eq:recurrenceA1B1_solution_x_star.
- In the _A1B1_ selection regime, modifier alleles that reduce the vertical transmission rate are favored by natural selection (@Fig:A1B1_modifier_invasions) and the only transmission mode that can lead to evolutionary stability is complete oblique transmission ($\rho=0$; see @Fig:A1B1_modifier_invasions).

## Randomly changing selection

Consider a stochastic selection regime in which the fitness of phenotypes _A_ and _B_ at generation _t_ are $1+s_t$ and $1$, respectively, where the random variables $s_t \; (t=0, 1, 2, ...)$ are independent and identically distributed (i.i.d), almost surely positive and finite (there are positive constants _C_ and _D_ such that $P(C \le s_t \le D) = 1$).

The recursion for this model can be rewritten as (based on @eq:recurrence0):
$$
x_{t+1} = x_t \frac{1 + \rho s_t + x_t (1-\rho) s_t}{1 + s_t x_t}.
$$ {#eq:recurrence_random_env}

Our analysis follows @Karlin1975 (see also [@Carja2013]).

**Definition: stochastic local stability.**
_An equilibrium state $x^*$ is said to be _stochastically locally stable_ if for any $\epsilon>0$ there exists $\delta>0$ such that_

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
$$ {#eq:summation_yields}

Let $\mu = \mathbb{E}[\log{(1+\rho s_t)}]$.
Because $\{s_t\}_{t \ge 0}$ are i.i.d. random variables, the strong law of large numbers (SLLN) applies and almost surely
$$
\lim_{t \to \infty}{\frac{1}{t} \sum_{n=0}^{t-1}{\log{(1+\rho s_n)}}} = \mu.
$$

Consider $\xi$ such that $\lim_{t \to \infty}{\frac{1}{t} \sum_{n=0}^{t-1}{\log{(1+\rho s_n(\xi))}}} = \mu, C \le s_t(\xi) \le D$ (_i.e._ such that the SLLN applies) and assume that:
$$
\lim_{t \to \infty}{x_t(\xi)} = 0.
$$ {#eq:T1_assumption}

Because $0 \le \rho \le 1$, 
and $\{s_t(\xi)\}_{t \ge 0}$ are uniformly bounded away from zero and infinity,
we can deduce that
$$
\lim_{t \to \infty}{\frac{1}{t} \sum_{n=0}^{t-1}{\log{\Big(1 - x_n \frac{\rho s_n (1+s_n)}{(1+\rho s_n)(1+x_n s_n)} \Big)}}} = 0 ,
$$
so that we can take the limit of @eq:summation_yields to get
$$
\lim_{t \to \infty}{\frac{1}{t} \Big(\log{x_{t}(\xi)} - 
\log{x_{0}(\xi)}\Big)} = \mu.
$$

However, the hypothesis states that $\mu  > 0$, implying that $\lim_{t \to \infty}{x_{t}(\xi)} = \infty$ (as $x_t \sim x_0 e^{\mu t}$ for large _t_) which is incompatible with the assumption (@eq:T1_assumption). Therefore we must have
$$
P(\lim_{t \to \infty}{x_{t}} = 0) = 0. \; \blacksquare
$$

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

![Stochastic local stability. The figure shows the frequency of phenotype _A_ after $10^6$ generations in a very large population evolving in a stochastic environment (@eq:recurrence_random_env). The fitness of phenotypes _A_ and _B_ are $1+s_t$ and $1$, where $s_t$ is _s_ with probability _p_ and _-s_ with probability _1-p_. The white line marks combinations of _p_ and _s_ for which $\mathbb{E}[\log{(1+\rho s_t)}]=0$; according to our analysis, we expect that  below this line $x^*=0$ will be stochastically locally stable. Parameters: $x_0=0.1$; $\rho=0.1$](figures/stochastic_env_x_t.pdf){#fig:stochastic_env_x_t}

### Evolutionary stability of oblique transmission

Finding a stability criterion for modifiers of the vertical transmission rate under randomly changing selection is challenging.
Therefore, we simulated invasions of modifier alleles that produce lower and lower vertical transmission rates by iterating @eq:recurrence_modifiers and randomly drawing the fitness values of phenotypes _A_ and _B_ at each iteration.
The results (@Fig:stoch_modifier_invasions) suggest that, similar to the case of periodically changing selection (@Fig:A1B1_modifier_invasions), modifier alleles that reduce the vertical transmission rate can invade the population, and the only stable transmission mode is complete oblique transmission ($\rho=0$).

![Consecutive fixation of modifiers that reduce the vertical transmission rate under randomly changing selection. The figure shows results of numerical simulations of evolution with two modifier alleles (@eq:recurrence_modifiers). When a modifier allele fixes (frequency>99.9%), a new modifier allele is introduced with a vertical transmission rate one order of magnitude lower (vertical dashed lines). **(A)** The frequency of phenotype _A_ in the population over time. **(B)** The frequency of the invading modifier allele over time. **(C)** The population mean vertical transmission rate over time. Vertical transmission rate of the initial resident modifier allele, $\rho_0 =0.1$; fitness values: _W=1_ and _w=0.1_ with probability 0.5 and _W=1_ and _w=0.1_ otherwise. The x-axis is in log-scale, as each sequential invasion takes an order of magnitude longer to complete.](figures/stoch_modifier_invasions.pdf){#fig:stoch_modifier_invasions}

### Summary

- If $\mathbb{E}[\log{(1+\rho s_t)}] > 0$, where $1+s_t$ and $1$ are the fitnesses of phenotypes _A_ and _B_, then fixation of phenotype _B_ ($x^*=0$) almost never occurs.
- With complete oblique transmission ($\rho=0$), $\mathbb{E}[\log{(1+\rho s_t)}]=0$ and we cannot determine the local stochastic stability of $x^*=0$.
- In general, the effect of the vertical transmission rate depends on the sign of $\frac{d}{d\rho}\mathbb{E}[1 + \rho s_t] = \mathbb{E}[\frac{s_t}{1+\rho s_t}]$.
- If the fitness of phenotype _B_ is also a random variable, such that the fitnesses of phenotypes _A_ and _B_ are $\tau_t, \sigma_t$, respectively, than we can normalize the fitnesses by $\sigma_t$ and denote $s_t=\frac{\tau_t-\sigma_t}{\sigma_t}$. The above results then apply.
- The above results will stand for any sequence $\{s_t\}_{t \ge 0}$ for which the SLLN applies, even if they are not i.i.d.
- @Fig:stochastic_env_x_t shows $x_{t=10^6}$ with $\rho=0.01$ and initial value $x_0=10^{-3}$ for different selection coefficients _s_ and _p_ the probability of favoring phenotype _A_. The white lines represent _s_ and _p_ values for which $\mathbb{E}[\log{(1 + \rho s_t)}] = 0$; indeed, below this line $x_t$ tends to converge to 0. **TODO: consider changing _s_ or _p_ to $\rho$**.

# Discussion {-}

Non-chromosomal inheritance mechanisms represent an alternative to standard chromosomal vertical transmission. Therefore, such mechanisms are increasingly ackwoledged as important factors for explaining adaptation and diversity [@Rivoire2014].
Here we investigated the evolution of a trait transmitted through a combination of vertical and oblique transmission, copied either from parents or from unrelated individuals in the parental generation, respectively.
We focus on two major evolutionary problems: the maintenance of phenotypic polymorphism and the evolution of the transmission mode itself.

## Maintenance of phenotypic polymorphism

We find that under stable selection, the unfavored phenotype is expected to become extinct, and vertical transmission accelerates its extinction compared to oblique transmission (@Fig:recurrence_example B).
Therefore, if selection fluctuates slowly, such that the population mostly evolves under stable conditions, oblique transmission allows polymorphism to be maintained for faster flactuations compared to vertical transmission.
Indeed, analysis of evolution in periodically changing selection shows that oblique transmission facilitates the mainteneance of phenotypic polymorphism whereas vertical transmission leads to fixation of the more frequently favored phenotype (@Fig:lk_phase_plane)

Moreover, we find that under rapidly changing selection oblique transmission increases the phenotypic variance (@Fig:env_A1B1) and the population mean fitness (@Fig:A1B1_mean_fitness A), indicating an advantage to oblique transmission in such selection regimes. 

**TODO: compare to results from [@Cavalli-Sforza1981, pg. 131-218]**

## Evolution of the transmission mode

In line with the above, we find that if selection fluctuates rapdily, oblique transmission is favored over vertical transmission after the phenotype distribution in the population has reached an eqauilibrium.
@McElreath2008 have suggested that vertical transmission is only effective when selection is relatively stable, and @Aoki2005 have demonstrated numerically that oblique transmission (in the form of social learning) can be favored over vertical transmission (via genetic determination of behavior) when the duration between changes in selection is short.
Our analytic results support these findings: the main factor that determines when vertical or oblique transmission is preferred is the frequency and intensity of changes in selection.


## Comparison to models of social learning

Most models of oblique transmission focused on social learning and how it differs from individual learning in the presence of environmental cues [@Kline2013].
In such models, individual learning is usually costly, but can provide novel phenotypes.
Moreover, phenotypic response to environmental cues, such as individual learning, has been shown to be favored over oblique transmission in rapidly changing selection [@Aoki2005] because it is better able to track selection changes.

First, our model does not include individual learning or environmental cues, but rather focuses on the difference between vertical and oblique transmission, allowing it to capture transmission mechanisms other than learning, such as microbiome transmission in animals and plants, and horizontal gene transfer in microbes.

Second, our model assigns an equal probability for each individual to be the phenotype donor in oblique transmission.
Other interesting forms of oblique transmission that we did not cover here are _many-to-one_, or conformity_; _one-to-many_, or teacher-type transmission;  and intra-familial transmission, such as between grandparents and grandchildren [@Cavalli-Sforza1981, pg. 54; @Aoki2011].
_many-to-one_ transmission will be very effective under constant selection, but since it reduces population variation, it will be diasdvantageous in fluctuating selection [@Aoki2011], unless there are environmental cues or similar mechanisms that introduce generation-to-generation variation.
_one-to-many_ transmission could distort the distribution from which oblique transmission samples the offspring phenotype, and results depend on how individuals become teachers. Intra-familiar oblique transmission, likely common in tribal and ancient human populations, represents a "compromise" between vertical and oblique transmission. 

Third, we assumed a large population size which allowed us to use a deterministic model, although we also presented comparisons to dynamics of population of finite (@Fig:env_A1B1; @Fig:env_A2B1). @Aoki2011 explicitly modeled small population sizes (25 and 125m typical for Pleistocene hominid populations). They also used different transmission modes such as _one-to-many_ and _many-to-one_.

Fourth, we have assumed that both transmission modes have perfect fidelity. However, both vertical and oblique transmission can give rise deleterious phenotypes, for example, due to mutations, epimutations, and unsuccessful learning. Assuming genetic transmission, which is strictly vertical, has higher fidelity than cultural transmission, which combines vertical and oblique transmission, @Cavalli-Sforza1983 have found that under constant selection, cultural transmission will lose to genetic tranmission.  

Lastly, our model does not include a cost for the phenotype donor, and therefore might be more suitable for modeling imitation rather than teaching, at least the latter carries a significant cost.

## Comparison to models of phenotype switching 

Several models of phenotype switching assume that the phenotype is vertically transmitted, but the fidelity of this transmission is determined by a genetic modifier locus (@Leigh1970; @Lachmann1996; @Ishii1989; @Kussell2005; @King2007; @Liberman2011). 
In these models, under fluctuating selection, the evolutionary stable switching rate is $\approx \frac{1}{k}$ if selection fluctuates every _k_ generations, but not if _k_ is random with large variance or if selection is not symmetric [@Liberman2011; @Salathe2009a].

Our model can represent a similar case in which transmission infidelity doesn't result in a random phenotype but rather in a phenotype drawn from the parental population; for example, if offspring sometimes mistakenly imitate unrelated adults instead of their parents, or if a proportion of offspring are reared by foster parents.
In this case, the optimal phenotype distribution is encoded by the population composition, rather than by the genetic modifier locus, and selection favors individuals that draw their phenotype from the population distribution rather than copy the parental phenotype.
This kind of oblique transmission might apply to many species of bacteria that utilize quorum sensing and other cell-to-cell signaling to determine their phenotypes [@Waters2005].

Similarly, @Xue2016 examined a model of phenotype switching in which the phenotype distribution itself is vertically transmitted with parental phenotype effects, as described for sporulation in _Bacillus subtilis_ [Veening2008b] and developmental plasticity the nematode _Pristionchus paciﬁcus_ [@Serobyan2013].
Given the parent trait $\pi$, which determined the probability that the parent acquired phenotype _A_, the probability that the offspring is _A_ is increased to $(1-\eta)\pi + \eta$ if the parent actually acquired phenotype _A_ and decreased to $(1-\eta)\pi$ otherwise (formally similar to @eq:inheritance_rule).
The results by @Xue2016 suggest that with rapidly changing selection, parental phenotype effects are disadvantageous, whereas if selection changes more slowly, parental phenotype effects can increaes the population mean fitness.

There is a clear similarity between these results and ours.
In rapidly changing selection there is a phenotype distribution that optimizes the population mean fitness, commonly called _bet-hedging_ [@King2007].
In @Xue2016, the optimal phenotype distribution is encoded by the trait, which is vertically transmitted with modification. When the optimal trait value appears in the population, selection reduces the tendency for modification [@Altenberg2017] to maintain the optimal phenotype distribution.
In our model, the optimal phenotype distribution is encoded by the population phenotype distribution, and when this distribution reaches the equilibrium state, selection favors oblique transmission, again to maintain the optimal phenotype distribution.

## On evolution with oblique transmission

Before concluding, we emphasize several ideas on how we expect oblique transmission to affect evolution.

First, oblique transmission can increase the _relatedness coefficient_ [@Allison1992] -- the probability that two individuals inherited their phenotype from a common ancestor -- which might help to explain the evolution of cooperation, as recently demonstrated for transmission of cooperative behaviour through host-manipulating microbes [@Lewin-Epstein2017].

Second, because oblique transmission decouples inheritance and reproductive success by allowing non-reproducing individuals to transmit their phenotye to the next generation, oblique transmission effectively reduces the strengh of selection.
Such reduction can facilitate adaptive peak shifts, inflate estimates of effective population size, and lead to accumulation of deleterious mutations, amongh other effects.

Lastly, oblique transmission emerges in several inheritance mechanisms that are very different in terms of the underlying biological and cultural mehchanisms, and are therefore rarely thought of in the same terms.
For example, @Eq:recurrence can model a human population in which offspring learn a behaviour from either their parents or random adults, but it can also model a microbial population in which the allele at a specific locus is either copied during DNA replication, or recombined from free strands of DNA taken up from the environment (likely originating from dead cells from the "parental" generation [@Redfield1993a]).
We suggest that the emerging similarity can be exploited to transfer intuition and even concrete results about the evolutionary causes and consequences of these inheritance mechanisms.

## Conclusions

Here we analyse evolution with a combination of vertical and oblique transmission and focusing on the maintenance of phenotype polymorphism and the evolution of the transmission mode. 
Our analysis applies for a wide range of biological circumstances, as oblique transmission occurs across the tree of life.

\small
_**Acknowledgements.** This research was supported in part by the Stanford Center for Computational, Evolutionary and Human Genomics._
\normalsize

# References {-}