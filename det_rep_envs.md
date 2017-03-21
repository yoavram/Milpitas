# Deterministic repetitive environments

Given the recurrence equation in environment _A_ ($\epsilon_t=A$):

$$
x' = x \cdot f_A(x) 
$$

where:

\begin{eqnarray*}
f_A(x) = \frac{x (1-\eta)(W - w) + \eta W + (1-\eta) w}{x (W - w) + w} \\
f_B(x) = \frac{x (1-\eta)(w - W) + \eta w + (1-\eta) w}{x (w - W) + W} \\
\end{eqnarray*}

We can use a linear approximation around $x=0$ of the form $f_A(x) = f_A(0) + o(x)$ and $f_B(x) = f_B(0) + o(x)$, where:

\begin{eqnarray}
f_A(0) =  1+\eta(\frac{W-w}{w}) \\
f_B(0) =  1+\eta(\frac{w-W}{W})
\end{eqnarray}

Similarly, $f_B(x) = 1 - \eta + \eta \frac{w}{W}$, since in environment _B_, the fitness values flip, and phenotype _A_ has fitness $w$.

For _k_ generations with environment _A_ and _l_ generations with environment _B_, in any given order, starting with $x=x_0$, we can write:

$$
x_{k+l} = x_0 f_A^k(x_0) f_B^l(x_0) + o(x_0)
$$

so that if we start very close to zero ($x_0 \sim 0$), the multiplicative change over the _k+l_ generations can be approximated by:

$$
\frac{x_{k+l}}{x_0} \approx f_A^k(0) f_B^l(0)
$$

Some cases for estimating this approximation follow.

## $W = w$

In this case, there is no selection and evolution is neutral.
Indeed, we get $f_i(x) \equiv 1$ (without an approximation).

## $\eta = 0$

In this case inheritance does not depend on the phenotype; since there is nothing else that generates variance, evolution is neutral.
Indeed, we get $f_i(x) \equiv 1$.

## $\eta = 1$

In this case, after a single generation the model becomes a standard two-type genetic model with only selection playing a role.
Indeed, we get $f_A(x) = \frac{W}{x W + (1-x) w}$ and $f_A^k(0) f_B^l(0) = \Big(\frac{W}{w}\Big)^{k-l}$. Since $W > w$, we find that $\frac{x_{k+l}}{x_0}$ is

$$
\begin{cases}
< 1 &, k < l \\
= 1 &, k = l \\
> 1 &, k > l
\end{cases}
$$

## $k=l$ 

### Proposition
If $k=l, 0 < w < W, 0 < \eta < 1$, then $f_A^k(0) f_B^l(0) > 1$.

### Proof
First, $f_A^k(0) f_B^l(0) = (f_A(0)f_B(0))^k > 1$ iff $f_A(0)f_B(0)>1$.

To show the latter,

\begin{multline*}
f_A(0) f_B(0) = \\
(1 - \eta + \eta \frac{W}{w}) \cdot (1 - \eta + \eta \frac{w}{W}) = \\
(1-\eta)^2 + \eta^2 + \eta(1-\eta) \cdot \frac{W}{w} \cdot \frac{w}{W} = \\
1 - 2\eta(1-\eta) + \eta(1-\eta) \frac{{W}^2 + {w}^2}{W w} = \\
1 + \eta (1-\eta)\frac{{W}^2 - 2 W w + {w}^2}{W w} = \\
1 + \eta (1-\eta)\frac{(W - w)^2}{W w}
\end{multline*}

which, under the proposition conditions, is _> 1_.
$\blacksquare$

## $k \ne l$ 

### Proposition: $k=1$
If $k=1$ and $n>(1-\eta)\frac{W-w}{w}$ then $f_A(0)f_B(0)^n<1$.

### Proof

Assuming $W>w, 0 \le \eta \le 1$, we have $0 \le \frac{W-w}{W} \le 1$ and $0 \le \eta \le 1$ means that $-1 \le \eta \frac{w-W}{W} \le 0$. This allows us to use the the inequality:

$$
(1+x)^n \le \frac{1}{1 - nx}, \;\;\; \forall x \in [-1,0], \forall n \in N.
$$

So we have: 

$$
\Big(1+\eta \frac{w-W}{W}\Big)^n \le \frac{1}{1 - n \eta \frac{w-W}{W}},
$$

and therefore

\begin{multline*}
f_A(0) f_B^n(0) = \\
\Big(1+\eta(1-\eta)\frac{(W-w)^2}{Ww}\Big)\Big(1+\eta\frac{w-W}{W}\Big)^n \le \\
\frac{1+\eta(1-\eta)\frac{(W-w)^2}{Ww}}{1 - n \eta \frac{w-W}{W}}
\end{multline*}

Next:

\begin{multline*}
n > (1-\eta)\frac{W-w}{w} \Leftrightarrow \\
-n < (1-\eta)\frac{w-W}{w} \Leftrightarrow \\
-n \eta \frac{W-w}{W} < \eta (1-\eta)\frac{(W-w)^2}{Ww} \Leftrightarrow \\
-n \eta \frac{w-W}{W} > \eta (1-\eta)\frac{(W-w)^2}{Ww} \Leftrightarrow \\
1 - n \eta \frac{w-W}{W} > 1 + \eta (1-\eta)\frac{(w-W)^2}{Ww} \Leftrightarrow \\
\frac{1+\eta(1-\eta)\frac{(W-w)^2}{Ww}}{1 - n \eta \frac{w-W}{W}} < 1 \\
\blacksquare
\end{multline*}





