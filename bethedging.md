In  Xue & Leibler 2016 [@Xue2016], the authors argued that:

> Now, suppose that the environment switches repeatedly during
> that timescale $\tau_{ad}$; _i.e._, the typical duration of an environment, $\tau_{env}$, is much shorter than $\tau_{ad}$. Then, through the learning mechanism, the phenotype probability distribution $\pi_i$ converges to a steady distribution $\pi_i^*$ and fluctuates around it... which yields $\pi_i^*=p_i$... This distribution, being proportional to the environment frequency, exactly recorvers the optimal bet-hedging strategy.

They presented analysis (eq. [3]) that shows that when selection is extreme, $\bar{\pi}_i$ fluctuates around $p_i$, the empirical frequency of the environment. The analysis is presented in Materials and Methods (eq. [10]) and assumes both extreme selection (fitness in the unfavorable environment is 0) and $\eta << 1$ via eq. [13]. 
In addition, they analyse the case of non-extreme selection (see SI), and suggest that $\bar{\pi}_i$ fluctuates around $\pi_i^*$ which satisfies (see eq. S6 in SI):

$$
pi_i^* = \sum_{j}{p_j \cdot \frac{\omega_i^j \pi_i^*}{\sum_k{\omega_k^j \pi_k^*}}}
$$

where the outer sum is over the different environments/phenotypes and $p_j$ is the frequency of environment _j_.

We examined these analyses. First, we solve the above equation for two environments _A_ and _B_ to find that for $0 < p_A < 1, \omega_A \ne \omega_B$:

$$
\pi_A^* = \frac{p_A (\omega_0 + \omega_1) - \omega_1}{\omega_0 - \omega_1}
$$

where $p_A$ is the frequency of environment _A_, $\omega_0$ is the fitness of phenotype _i_ in environment _i_, and $\omega_1$ is the fitness of phenotype _i_ in environment _i_ ($i \ne j$).

Second, we focus on environments in which the environment is drawn at every generation from a coin flip with 70% for A and 30% for B. Population size N=100,000, initial $\pi_A$ values for each individual is drawn from $Norm(0.5, 0.05)$, and the fitness of individuals is $\omega_0=2.0$ in a favorable environment and $\omega_1 = 0.2$ or $0.0$ in an unfavorable environment. These values result in $\pi_A^*$ = 0.7 or 0.744, respectively.

We look at simulations with different learning rates $\eta$ and look at $\bar{\pi}_A$, the population mean value of $\pi_A$, over time.

![$\bar{\pi}_A$ over time for different $\eta$ values (columns) and extreme (bottom) or non-extreme (top) selection ($\omega_1 =0$ or $0.2$, respectively). The red lines represent $\pi_A^*$, the blue lines represent $p_A$, the empirical frequency of environment _A_.](bethedging_timeseries.png){#fig:bethedging_timeseries}

With extreme selection ([@Fig:bethedging_timeseries], bottom row) $\bar{\pi}_A$ does seem to fluctute around $p_A=0.7$ (blue dashed lines), and fluctuations increase with $\eta$. This is in accordance with [@Xue2016].

With non-extreme selection ([@Fig:bethedging_timeseries], top row), $\bar{\pi}_A$ (black lines for multiple simulations) fluctuates around $\pi_A^*=0.744..$ (red lines) which is **higher** then $p_A=0.7$ (blue lines). 
These fluctuations increase with $\eta$ (from $\eta=0$ in the leftmost panel to $\eta=0.1$ in second panel from the right), except for $\eta=1$ for which almost all individuals are $\pi_A=1$ (rightmost panel). 

We also examine the histograms of $\bar{\pi}_A$ in the above simulations, but only for $t>250$, so that we ignore the time required for the population to adapt from $\bar{\pi}_A \approx 0.5$ to $\bar{\pi}_A \approx \pi_A^*$.

![Histograms of  $\bar{\pi}_A$ in multiple simulations](bethedging_histograms.png){#fig:bethedging_histograms}

The layout [@Fig:bethedging_histograms] is the same as [@Fig:bethedging_timeseries], but it shows histograms of $\bar{\pi}_A$ for _t>250_. The red line represent $\pi_A^*$, and the blue dashed lines represent $p_A$. Note that colums have different x-scale; we can get an impression of relative x-scales from the y-scales in [@Fig:bethedging_timeseries].

With extreme selection ([@Fig:bethedging_histograms], bottom), indeed $\bar{\pi}_A$ fluctuates around $p_A=0.7$ as the histograms are more or less centered around 0.7 (dashed blue line), as expected from [@Xue2016].

With non-extreme selection, the histograms are not centered around $p_A=0.7$ but rather around $\pi_A^*=0.744..$, which does not coincide with $p_A=0.7$ ([@Fig:bethedging_timeseries], bottom panel).

# References
