# Model

## Definitions

- $\phi_k$: phenotype of individual k, one of A, B.
- $\pi_k$: probability that individual k has phenotype A; $0 \le \pi_k \le 1$.
- $f(\pi)$: frequency of individuals with $\pi$; $0 \le f(\pi) \le 1$, $\sum_k{f(\pi_k)} = 1$.
- $\epsilon_t$: the environment at time t, one of A, B.
- $\omega_{\phi}^{\epsilon}$: fitness of phenotype $\phi$ in environment $\epsilon$.
- $\eta$: epimutation rate, $0 \le \eta \le 1$.

The inherited trait is $\pi$. The probability that a new offspring k of parent j will become phenotype A is

$$
\pi_k=(1-\eta) \cdot \pi_j + \eta \cdot \delta_{A,\phi_j}
$$

where $\delta_{A,\phi_j}$ is  1 if parent had phenotype A and 0 otherwise.

**Note**: the parent of an individual with $\pi$ can be a phenotype A individual with $\frac{\pi-\eta}{1-\eta}$ or a phenotype B individual with $\frac{\pi}{1-\eta}$.

## Recurrence equation


Here we follow how the frequency of phenotype $\phi_A$ rather then the trait $\pi$ changes from generation to generation according to this recurrence equation:

$$
\bar{\omega}(t) \cdot  f_{t+1}(\phi_A) =
\int_0^1{f_t(\pi_A) \cdot \omega_A^{\epsilon_t} \cdot \pi_A \cdot ((1-\eta)\pi_A + \eta) \; d\pi_A} +
\int_0^1{f_t(\pi_A) \cdot \omega_B^{\epsilon_t}\cdot (1-\pi_A) \cdot (1-\eta)\pi_A \; d\pi_A}
$$

where $\bar{\omega}(t)$ is a normalization facotr, calculated as the integral of the RHS of the equation for $0 \le \pi \le 1$.

This can be simplified to:

$$
\bar{\omega}(t) \cdot  f_{t+1}(\phi_A) = \int_0^1{f_t(\pi_A) \Big[\Big(\frac{\omega_A}{\omega_B} - 1\Big)(1-\eta)\pi_A^2 + \frac{\omega_A}{\omega_B} \pi_A \Big]\; d\pi_A}
$$
