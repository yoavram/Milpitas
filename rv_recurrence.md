# Model with recurrence on random variable

We define $\pi_t$ to be the probability that a randomly drawn individual in generation $t$ develops to phenotype $\phi_A$.

Then, given the model presented in Xue & Leibler (2016), the probability that a random individual in generation $t+1$ develops to phenotype $\phi_A$ conditioned on $\pi_t$ as:

$$
\pi_{t+1}|\pi_t = 
\pi_t \cdot \frac{\omega_{A,t}}{\bar{\omega}_t} \cdot (\pi_t (1-\eta) + \eta) +
(1-\pi_t) \cdot \frac{\omega_{B,t}}{\bar{\omega}_t} \cdot (\pi_t \cdot (1 - \eta))
$$

where:

- $\omega_{i,t}$ is the fitness of phenotype $i$ at generation $t$
- $\eta$ is the "learning" rate
- $\bar{\omega}_t$ is the population mean fitness
