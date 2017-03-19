# Deterministic repetitive environments

Given the recurrence equation in environment _A_ ($\epsilon_t=A$):

$$
x' = x \cdot f_A(x) 
$$

where:
$$
f_A(x) = \frac{x (1-\eta)(\omega^+ - \omega^-) + \eta \omega^+ + (1-\eta) \omega^-}{x (\omega^+ - \omega^-) + \omega^-}
$$

We can use a linear approximation around $x=0$ of the form $f_A(x) = f_A(0) + o(x)$ which gives us:

$$
f_A(x) = 1 - \eta + \eta \frac{\omega^+}{\omega^-} + o(x)
$$

Similarly, $f_B(x) = 1 - \eta + \eta \frac{\omega^-}{\omega^+}$, since in environment _B_, the fitness values flip, and phenotype _A_ has fitness $\omega^-$.

For _k_ generations with environment _A_ and _l_ generations with environment _B_, in any given order, starting with $x=x_0$, we can write:

$$
x_{k+l} = x_0 f_A^k(x_0) f_B^l(x_0) + o(x_0)
$$

so that if we start very close to zero ($x_0 \sim 0$), the multiplicative change over the _k+l_ generations can be approximated by:

$$
\frac{x_{k+l}}{x_0} \approx f_A^k(0) f_B^l(0)
$$

Some cases for estimating this approximation follow.

## $\omega^+ = \omega^-$

In this case, there is no selection and evolution is neutral.
Indeed, we get $f_i(x) \equiv 1$ (without an approximation).

## $\eta = 0$

In this case inheritance does not depend on the phenotype; since there is nothing else that generates variance, evolution is neutral.
Indeed, we get $f_i(x) \equiv 1$.

## $\eta = 1$

In this case, after a single generation the model becomes a standard two-type genetic model with only selection playing a role.
Indeed, we get $f_A(x) = \frac{\omega^+}{x \omega^+ + (1-x) \omega^-}$ and $f_A^k(0) f_B^l(0) = \Big(\frac{\omega^+}{\omega^-}\Big)^{k-l}$. Since $\omega^+ > \omega^-$, we find that $\frac{x_{k+l}}{x_0}$ is

$$
\begin{cases}
< 1 &, k < l \\
= 1 &, k = l \\
> 1 &, k > l
\end{cases}
$$

## $k=l$ 

### Proposition
> If $k=l, 0 < \omega^- < \omega^+, 0 < \eta < 1$, then $f_A^k(0) f_B^l(0) > 1$.

### Proof
First, $f_A^k(0) f_B^l(0) = (f_A(0)f_B(0))^k > 1$ iff $f_A(0)f_B(0)>1$.

To show the latter,

\begin{multline*}
f_A(0) f_B(0) = \\
(1 - \eta + \eta \frac{\omega^+}{\omega^-}) \cdot (1 - \eta + \eta \frac{\omega^-}{\omega^+}) = \\
(1-\eta)^2 + \eta^2 + \eta(1-\eta) \cdot \frac{\omega^+}{\omega^-} \cdot \frac{\omega^-}{\omega^+} = \\
1 - 2\eta(1-\eta) + \eta(1-\eta) \frac{{\omega^+}^2 + {\omega^-}^2}{\omega^+ \omega^-} = \\
1 + \eta (1-\eta)\frac{{\omega^+}^2 - 2 \omega^+ \omega^- + {\omega^-}^2}{\omega^+ \omega^-} = \\
1 + \eta (1-\eta)\frac{(\omega^+ - \omega^-)^2}{\omega^+ \omega^-}
\end{multline*}

which, under the proposition conditions, is _> 1_.
$\blacksquare$

## $k \ne l$ 

To be continued.







