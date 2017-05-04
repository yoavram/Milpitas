# Diffusion equation

In addition to the recurrence equation approximation, we develop a diffusion equation approximation [@Otto2007, ch. 15], which takes into account the variance due to the development process. 

Specifically, we derive the mean of $x'-x$:

$$
\mu(x) = \eta x (1-x) E\Big[ \frac{\omega_A - \omega_B}{\bar{\omega}} \Big]
$$
and the mean of $(x'-x)^2$:
$$
\sigma^2(x) = \eta^2 x (1-x) E\Big[ \frac{(1-x) \omega_A + x \omega_B}{\bar{\omega}} \Big]
$$

and we use these quantities to write the diffusion equation (or the _forward Kolmogorov equation_):
$$
\frac{\partial f(x, t)}{\partial t} = -\mu \frac{\partial f(x, t)}{\partial x} +\frac{1}{2} \sigma^2 \frac{\partial^2 f(x, t)}{\partial x^2}
$$ {#eq:diffusion}

![Comparison of recurrence and diffusion approximations. Recurrence equation approximation (black line; solved by iteration of @eq:recurrence) and diffusion equation approximation (color lines; solved by stochastic integration of @eq:diffusion). **(A)** Environment constant at _A_. **(B)** Environment randomly changes between _A_ and _B_ every generation. **(C)** Environment changes between _A_ and _B_ exactly every 50 generations. Parameters: $\eta=0.1, W=1, w=0.1$.](figures/sde_example.pdf){#fig:sde_example}

![Probability for fixation at $\pi=1$. The figure shows the fixation probability at $\pi=1$ for variable initial $\pi$ and for different (A) fitness values or (B) phenotype inheritance rate. Calculated using the diffusion equation approximation [@Otto2007, recipe 15.1]. Parameters: (A) $\eta=0.1$; (B) W=1, w=0.1.](figures/diffusion_fix_prob.pdf){#fig:diffusion_fix_prob}