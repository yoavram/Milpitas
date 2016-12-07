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

The frequency of a trait $\pi$ (with specific value) changes from generation to generation according to this recurrence equation:

$$
\bar{\omega}(t) \cdot  f_{t+1}(\pi) =
f_{t}\big( \frac{\pi-\eta}{1-\eta} \big) \cdot \frac{\pi-\eta}{1-\eta} \cdot \omega_A^{\epsilon(t)} + 
f_{t}\big( \frac{\pi}{1-\eta} \big) \cdot \big( 1- \frac{\pi}{1-\eta} \big) \cdot \omega_B^{\epsilon(t)}
$$

where $\bar{\omega}(t) = \int_0^1{f_t(\pi) \cdot [\pi ֿ\cdot\omega_A^{\epsilon(t)} + (1-\pi) \cdot\omega_B^{\epsilon(t)} ] \; d \pi}$ is the population mean fitness at generation t.

# Simple cases

## Constant environment, extreme selection, no epimutation

Set a constant environment $\forall t, \epsilon(t) = A$, extreme selection $\omega_A^\epsilon = 1, \omega_B^\epsilon = 0$, and no epimutation $\eta = 0$.

The recurrence equation now becomes:

$$
f_{t+1}(\pi) =  \frac{f_{t}( \pi) \cdot \pi}{\int_0^1{f_t(y) y dy}}
$$

The solution, using induction, is:

$$
f_t(\pi) = \frac{f_0(\pi) \cdot \pi^t}{\int_0^1{f_0(y) y^t d y}}
$$

For example, assume that the initial distribution of $\pi$ is uniform, that is, $f_0(\pi)=1$ is the density function of $U(0, 1)$, the continuous uniform distribution on $[0,1]$, then:

$$
f_t(\pi) = \frac{\pi^t}{\int_0^1{y^t d y}} = (t+1) \cdot \pi^t
$$

Therefore, take the expected value over the entire population at time t, we get:

$$
E_t[\pi] = \int_0^1{(t+1) \cdot \pi^t d \pi} = \frac{n+1}{n+2} \to_{t \to \infty} 1
$$

Note this means that the distribution of $\pi$ in the population converges to a single value, that is, the limit $f_{\infty}(\pi) = \delta_{\pi, 1}$.
 
## Constant environment, non-extreme selection, no epimutation

We consider the same case as above, only now $\omega_B^\epsilon = 1 - s$.

$$
f_{t+1}(\pi) =  \frac{f_{t}( \pi) (\pi + (1-\pi)(1-s)) }{\int_0^1{f_t(y) [y + (1-y)(1-s)] dy}}
$$

Similar to above, the solution is:

$$
f_t(\pi) = \frac{f_0(\pi) (1 -s +s \pi)^t}{\int_0^1{f_0(y) (1 -s +sy)^t dy}}
$$

and assuming the initial distribution of $\pi$ is uniform, as above, $f_0(\pi)=1$:

$$
f_t(\pi) = \frac{s(t+1)(1-s+s\pi)^t}{1-(1-s)^{t+1}}
$$

and

$$
E_t[\pi] = \int_0^1{\pi \frac{s(t+1)(1-s+s\pi)^t}{1-(1-s)^{t+1}} d \pi} = \frac{(1-s)^{t+2} + ts + 2s - 1}{(t+2)s(1-(1-s)^{t+1})} \approx_{t>>1}  \frac{s(t+2) - 1}{s(t+2)} \to_{t \to \infty} 1
$$

and again this means that the distribution of $\pi$ converges to $f_{\infty}(\pi) = \delta_{\pi,1}$.

## Constant environment, extreme selection, with epimutation

Set a constant environment $\forall t, \epsilon(t) = A$, extreme selection $\omega_A^\epsilon = 1, \omega_B^\epsilon = 0$, and this time with epimutation $\eta > 0$.

$$
f_{t+1}(\pi) =
\frac{
	f_{t} 
	\big(
		\frac{\pi-\eta}{1-\eta} 
	\big) \cdot 
	\frac{\pi-\eta}{1-\eta}
}{
 \int_0^1{f_{t}(y) y dy}
}
$$

Let's define this recurrence $g_n$:
$$
g_0(\pi) = \pi \\
g_{n+1}(\pi) = (1-\eta) g_n(\pi) + \eta \\
$$
and it's inverse, such that $g_n(h_n(\pi))=\pi$:
$$
h_0(\pi) = \pi \\
h_{n+1}(\pi) = \frac{h_n(\pi) - \eta}{1 - \eta}
$$

The solutions to these recurrences are:
$$
g_n(\pi) = 1 - (1-\pi)(1 - \eta)^n \\
h_n(\pi) = 1 - \frac{1-\pi}{(1-\eta)^n}
$$

Now we can redefine $f_n$ using $g_n$:
$$
f_{n+1}(g_{n+1}(\pi)) = f_0(\pi) \cdot \Pi_{k=0}^n{g_k(\pi)} 
$$

and because $g_n(h_n) = \pi$, substitute in the last equation $\pi->h_{n+1}(\pi)$:

$$
f_{n+1}(\pi) = f_0(h_{n+1}(\pi)) \cdot \Pi_{k=0}^n{g_k(h_{n+1}(\pi))} 
$$

CHECK:
But $g_k(h_{n+1}(\pi)) = h_{n-k+1}(\pi)$:

$$
= f_0\big(1-\frac{1-\pi}{(1-\eta)^{n+1}}\big) \cdot \Pi_{k=0}^n{\big( 1-\frac{1-\pi}{(1-\eta)^{n-k+1}} \big)}
$$



