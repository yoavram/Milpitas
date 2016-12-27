Title         : Evolution of Learning
Author        : Yoav Ram
Affiliation   : Department of Biology, Stanford University Stanford, CA 94305-5020
Email         : yoavram@stanford.edu

Author        : Uri Liberman
Affiliation   : School of Mathematical Sciences, Tel Aviv University, Tel Aviv, Israel 69978
Email         : uril@tauex.tau.ac.il

Author        : Marcus W. Feldman
Affiliation   : Department of Biology, Stanford University Stanford, CA 94305-5020
Email         : mfeldman@stanford.edu

Colorizer     : javascript
Bib style     : plainnat
Bibliography  : example
Logo          : True

Doc class     : [10pt]article

[TITLE]

~ Abstract
There is more in you of good than you know, child of the kindly West.
Some courage and some wisdom, blended in measure. If more of us valued
food and cheer and song above hoarded gold, it would be a merrier world.
~

# Model     { #sec-model }

## Definitions

- $\phi_k$: phenotype of individual k, one of A, B.
- $\pi_k$: probability that individual k has phenotype A; $0 \le \pi_k \le 1$.
- $f(\pi)$: frequency of individuals with $\pi$; $0 \le f(\pi) \le 1$, $\int_0^1{f(\pi) d\pi} = 1$.
- $f(\phi_A)$: frequency of individuals with $\phi_i$; $0 \le f(\phi_i) \le 1$, $\sum_k{f(\phi_k)} = 1$.
- $\epsilon_t$: the environment at time t, one of A, B.
- $\omega_{\phi}^{\epsilon}$: fitness of phenotype $\phi$ in environment $\epsilon$.
- $\eta$: epimutation rate, $0 \le \eta \le 1$.

The inherited trait is $\pi$. The probability that a new offspring k of parent j will become phenotype A is

$$
\pi_k=(1-\eta) \cdot \pi_j + \eta \cdot \delta_{A,\phi_j}
$$

where $\delta_{A,\phi_j}$ is  1 if parent had phenotype A and 0 otherwise.

## Recurrence equation


Here we follow how the frequency of phenotype $\phi_A$ rather then the trait $\pi$ 
changes from generation to generation according to this recurrence equation:

~ Equation { #recurrence }
\bar{\omega}(t) \cdot  f_{t+1}(\phi_A) =
\int_0^1{f_t(\pi_A) \Big[\pi_A \cdot \omega_A^{\epsilon_t} \cdot ((1-\eta)\pi_A + \eta) +
 (1-\pi_A) \cdot \omega_B^{\epsilon_t} \cdot (1-\eta)\pi_A \Big] \; d\pi_A}
~

where $\bar{\omega}(t)$ is a normalization factor. The integrand is built from the frequency of $\pi_A$, 
multiplied by probability that the parent is $\phi_i$ (based on $\pi_A$), 
the probability that the parent reproduces, $\omega_{i}^{\epsilon_t}$), 
and the probability that the offspring, with an updated trait, becomes $\phi_A$.

In general, for a random variable $X$ with density function $f(x)$ and continuous function $g(x)$,
$\int{f(x) \cdot g(x) dx} = E[g(x)]$. We apply this to [#recurrence]:

~ Equation {#moments}
\bar{\omega}(t) \cdot  f_{t+1}(\phi_A) = 
  E_t[\pi_A] (\eta \cdot \omega_A^{\epsilon_t} + (1-\eta) \cdot \omega_B^{\epsilon_t}) + 
  E_t[\pi_A^2] \cdot (1- \eta) \cdot (\omega_A^{\epsilon_t}-\omega_B^{\epsilon_t})
~

Reordering the RHS of  [#moments] we can get $E_t[\pi_A-\pi_A^2](\eta \omega_A + (1-\eta) \omega_B) + \omega_A E_t[\pi_A^2]$, 
and after adding and substracting $\omega_A E_t[\pi_A]$, we have

~ Equation
\bar{\omega}(t) \cdot  f_{t+1}(\phi_A) = \omega_A \cdot E_t[\pi_A] - (1-\eta) (\omega_A-\omega_B) E_t[\pi_A-\pi_{A}^2]
~

We treat the number of individuals with phenotype $\phi_A$ as a continous Poisson binomial random variable:

- The expected number of individuals at time _t_ with phenotype $\phi_A$ in a population of size _N_ is
$E_t[\phi_A] = N E_t[\pi_A]$, where the first expectation is over realizations and the second is over the population. 
- The variance of the number of $\phi_A$ individuals is $V_t[\phi_A] = N E_t[\pi_A-(1-\pi_A)]$,
for a constant population size _N_
(again, the variance is over realizations and the expectation is over the population).
- The frequency of individuals at time _t_ with phenotype $\phi_A$ is $f_t(\phi_A)=E_t[\phi_A]/N$.

So, we can write the last equation as:

~ Equation
\bar{\omega}(t) \cdot  E_{t+1}[\phi_A] = \omega_A \cdot E_t[\phi_A] - (1-\eta) (\omega_A-\omega_B) V_t[\phi_A]
~