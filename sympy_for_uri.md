​_Jan 15, 2016, v.1_

Given this recurrence equation:
$$
x^{'} = x \frac{(1-\eta)x(\omega_A - \omega_B)+(\eta \omega_A + (1-\eta)\omega_B)}{x(\omega_A-\omega_B)+\omega_B}
$$

$$
x^{''}=x' \frac{(1-\eta)x'(\omega_B - \omega_A)+(\eta \omega_B + (1-\eta)\omega_A)}{x(\omega_B-\omega_A)+\omega_B}
$$



We are looking for a solution to $x''=x$, which evaluates to a quartic polynomial. Two solutions are 0 and 1 (assign to eq 1), but there are two more potential solutions solutions, such that $x''-x=x(1-x)(Ax^2+Bx+C)$.

Using [SymPy](http://sympy.org/) (a Python library for symbolic mathematics, a free alternative to Wolfram Mathematica™), we find all four solution of $x''-x$, such that we find $A,B,C$:
$$
x''- x = x(1-x)(x^2 + x \frac{\omega_A (1-\eta) -\omega_B (3-\eta)}{(\eta-2)(\omega_A - \omega_B)}) + \omega_B
$$
The following figure shows the "negative" solution ( _i.e._ corresponding to $\frac{-B-\sqrt{B^2-4AC}}{2A}$) in dashed lines and the numerical iteration of eqs. 1 and 2 in solid lines for a several combinations of $\eta, \omega_A, \omega_B$. All iterations started with $x(0)=0.5$.

![Solution examples.](figures/sympy_for_uri.pdf)

