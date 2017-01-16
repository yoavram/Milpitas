_Jan 16, 2017, v.3_

Given this recurrence equation:
$$
x^{'} = x \frac{(1-\eta)x(\omega_A - \omega_B)+(\eta \omega_A + (1-\eta)\omega_B)}{x(\omega_A-\omega_B)+\omega_B}
$$

$$
x^{''}=x' \frac{(1-\eta)x'(\omega_B - \omega_A)+(\eta \omega_B + (1-\eta)\omega_A)}{x(\omega_B-\omega_A)+\omega_A}
$$

We are looking for a solution to $x''=x$, which evaluates to a quartic polynomial. Two solutions are 0 and 1 (assign to eq 1), but there are two more potential solutions solutions, such that $0=x''-x=x(1-x)G(x)$ where $G(x)=Ax^2+Bx+C$. 

Using [SymPy](http://sympy.org/) (a Python library for symbolic mathematics, a free alternative to Wolfram Mathematica™), we find all four solution of $x''-x​=0$:

$$
0=x''- x = x(1-x)(x^2 - \frac{\omega_A (1-\eta) - \omega_B (3-\eta)}{(2-\eta)(\omega_A - \omega_B)} x - \frac{\omega_B}{(2-\eta)(\omega_A - \omega_B)})
$$

or 

$$
G(x) = x^2 - \frac{\omega_A (1-\eta) - \omega_B (3-\eta)}{(2-\eta)(\omega_A - \omega_B)} x - \frac{\omega_B}{(2-\eta)(\omega_A - \omega_B)}
$$
Assume $\omega_A , \omega_B >0, 0 \le \eta \le 1$. The *discriminant* of $G(x)$ is $\Delta=\sqrt{(\omega_A+\omega_B)^2-\eta(2-\eta)(\omega_A-\omega_B)^2}$. Becaue $\eta(2-\eta)$ has a maximum at maximized at $\eta=1$, its minimum in $[0,1]$ is at 0, so
$$
(\omega_A+\omega_B)^2-\eta(2-\eta)(\omega_A-\omega_B)^2 > (\omega_A+\omega_B)^2-(\omega_A-\omega_B)^2=4\omega_A\omega_B>0
$$
and the discriminant is positive and there are two solutions to $G(x)$. Also, assuming $\omega_A>\omega_B$,
$$
G(0) = \frac{-\omega_B}{(2-\eta)(\omega_A - \omega_B)} < 0
$$

$$
G(1) = 
1 - \frac{\omega_A (1-\eta) - \omega_B (3-\eta)}{(2-\eta)(\omega_A - \omega_B)} - \frac{\omega_B}{(2-\eta)(\omega_A - \omega_B)} = \\
\frac{\omega_A}{(2-\eta)(\omega_A - \omega_B)} > 0
$$

and $lim_{x-> \pm \infty}{G(x)} = +\infty$.  If instead $\omega_B>\omega_A$, then $G(0)>0, G(1)<0$. 

Therefore, there are two roots to $G(x)$. If $\omega_A>\omega_B$, then one of them is negative and one of them, $\tilde{x}$, is positive and below 1. If $\omega_B>\omega_A$, then both are positive but only one of them, $\tilde{x}$,  is below 1.


The following figure shows the "negative" solution (_i.e._ corresponding to $\frac{-B-\sqrt{B^2-4AC}}{2A}$) in dashed lines and the numerical iteration of eqs. 1 and 2 in solid lines for a several combinations of $\eta, \omega_A, \omega_B$. All iterations started with $x(0)=0.5$. Note that the figure shows _x_ in every other generation.

Single solution between 0 and 1...

![Solution examples.](figures/sympy_for_uri.pdf)

