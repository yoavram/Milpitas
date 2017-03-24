Define $\pi_t$ as the population distribution of the probability to develop into phenotype $\phi_A$ at time $t$. 

The probability mass function for $\pi_t$ is $f_t$ (I use pmf instead of pdf because of a) computational feasibility, and b) a continuous distribution is just an approximation for a discrete distribution as population size is finite.

Set $\eta=0.1$ and $\omega_{i}^{\epsilon_t}$ is equal to 1 if $i=\epsilon_t$ or 0.9 otherwise ($i, \epsilon_t \in \{A,B\}$).

We start with $f_0(x) = 1/n \; \forall x \in \{\frac{k}{n-1} | 0 \le k < n\}$ and $n=500$ (this approximates the continuous uniform distribution with a discrete one).

We then define $f_t$ as a function of $f_{t-1}$ and  $\epsilon_{t-1}$:

\begin{eqnarray}
\forall x \in \{y \in [0,1] | f_{t-1}(y) > \frac{1}{N} \} \\
f_{t}(x \cdot (1 - \eta) + \eta) = 
z \cdot f_{t-1}(x) \cdot x \cdot \omega_A^{\epsilon_t} \\
f_{t}(x \cdot (1 - \eta)) = 
z \cdot f_{t-1}(x) \cdot (1-x) \cdot \omega_B^{\epsilon_t}
\end{eqnarray}

where $z$ is a normalizing factor such that $\sum_x{f_t(x)} = 1$ and $N=10000$ is the population size.


