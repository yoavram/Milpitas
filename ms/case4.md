#### Case 4.

We assume constant environment, learning, and non-extreme selection such that $\omega_A > \omega_B$.

The recurrence formula is:

$$
\bar{\omega}_t f_{t+1}(\pi) = 
f_t(\frac{\pi-\eta}{1-\eta}) \frac{\pi-\eta}{1-\eta} \omega_A + 
f_t(\frac{\pi}{1-\eta}) (1 - \frac{\pi}{1-\eta}) \omega_B 
$$

Let's show that $f_t(\pi) = \left\{\begin{matrix}
1 & \pi = 1\\ 
0 & \pi < 1
\end{matrix}\right.$ is a static distribution, that is $f_{t+1}(\pi) = f_t(\pi)$.

First, $\bar{\omega}_t = 1$.

Now for $\pi = 1$, assume $\omega_A = 1$ and $\omega_B=1-s$:

$$
f_{t+1}(1) = 
f_t(\frac{1-\eta}{1-\eta}) \frac{1-\eta}{1-\eta} \cdot 1 + 
f_t(\frac{1}{1-\eta}) (1 - \frac{1}{1-\eta}) (1-s) = \\
f_t(1) \cdot 1 \cdot  1 + 
0 \cdot (1 - \frac{1}{1-\eta}) (1-s) = 1
$$

so indeed $f_{t+1}(1) = 1$.

Now for $\pi < 1$:

$$
f_{t+1}(\pi) = 
f_t(\frac{\pi-\eta}{1-\eta}) \frac{\pi-\eta}{1-\eta} \cdot 1 + 
f_t(\frac{\pi}{1-\eta}) (1 - \frac{\pi}{1-\eta}) (1-s) = \\
0 + 
f_t(\frac{\pi}{1-\eta}) (1 - \frac{\pi}{1-\eta}) (1-s)
$$

the only $\pi$ for which this does not vanish is $\pi=1-\eta$:

$$
f_{t+1}(1-\eta) = 
f_t(\frac{1-\eta}{1-\eta}) (1 - \frac{1-\eta}{1-\eta}) (1-s) = \\
f_t(1) (1 - 1) (1-s) = 1 \cdot 0 \cdot (1-s) = 0
$$

so indeed $f_{t+1} = 0 \; \pi <1$, and so $f(\pi) = \delta_{\pi,1}$ is a static distribution.

What about $f_t(\pi) = \left\{\begin{matrix}
1 & \pi = 0\\ 
0 & \pi > 0
\end{matrix}\right.$?

First, $\bar{\omega}_t=(1-s)$.

Now, in the formula for $f_{t+1}(\pi)$, the RHS terms vanish except for $\pi=\eta$ and $\pi=0$.

First $\pi=\eta$:

$$
(1-s) \cdot f_{t+1}(\eta) = 
f_t(\frac{\eta-\eta}{1-\eta}) \frac{\eta-\eta}{1-\eta} \cdot 1 + 
f_t(\frac{\eta}{1-\eta}) (1 - \frac{\eta}{1-\eta}) (1-s) = \\
1 \cdot 0 \cdot 1 + 
0 (1 - \frac{\eta}{1-\eta}) (1-s) = 0
$$

and now $\pi = 0$, for which the first term doesn't apply ($\pi < \eta$ doesn't get a $\phi_A$ term as it cannot be reached by adding $\eta$):

$$
(1-s) \cdot f_{t+1}(0) = 
f_t(0) (1 - \frac{0}{1-\eta}) (1-s) = \\
1 \cdot 1 \cdot (1-s) = (1-s) \Rightarrow
f_{t+1}(0) = 1
$$

and we find that $f_t(\pi) = \left\{\begin{matrix}
1 & \pi = 0\\ 
0 & \pi > 0
\end{matrix}\right.$ is a stable distribution.
