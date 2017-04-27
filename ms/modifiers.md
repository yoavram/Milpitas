# Modifier model

In a population homogeneous at the modifier locus ($\eta$) the recurrence equation is:

$$\begin{aligned}
x' = x \cdot \frac{\omega_A}{\bar{\omega}} \cdot ((1-\eta)x+\eta) + (1-x) \cdot \frac{\omega_B}{\bar{\omega}} \cdot (1-\eta)x \\
\bar{\omega} = x \omega_A + (1-x) \omega_B
\end{aligned}$$

In a population with two modifiers, $\eta \le H$, define:

- p: freq of $\eta$
- q = 1-p: freq of H
- x: freq of A within $\eta$ population
- 1-x: freq of B within $\eta$ population
- y: freq of A within H population
- 1-y: freq of B within H population

Then the recursion is:

$$\begin{aligned}
p' = \frac{p (x  \omega_A + (1 - x) \omega_a)}{\bar{\omega}} \\
\bar{\omega} = p (x  \omega_A + (1 - x) \omega_a) + q (y \omega_A +  (1 - y) \omega_B) \\
x' = \frac{x \omega_A ((1 - \eta) x + \eta) + (1 - x) \omega_B (1 - \eta) x}
    {x  \omega_A + (1 - x) \omega_B}  \\
y' = \frac{y \omega_A ((1 - H) y + H) + (1 - y) \omega_B (1 - H) y}
    {y \omega_A + (1 - y) \omega_B}
\end{aligned}$$
