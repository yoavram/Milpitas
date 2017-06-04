---
title: Evolution with vertical and oblique transmission in fluctuating environments
author:
- Yoav Ram^[Department of Biology, Stanford University, Stanford, CA 94305-5020, yoav@yoavram.com]
- Uri Liberman^[School of Mathematical Sciences, Tel Aviv University, Tel Aviv, Israel 69978, uril@tauex.tau.ac.il]
- Marcus W. Feldman^[Department of Biology, Stanford University, Stanford, CA 94305-5020, mfeldman@stanford.edu; Corresponding author]
year: 2017
abstract: |
    TODO
chapters: True
chaptersDepth: 1
chapDelim: ""
header-includes:
#    - \usepackage{lineno}
#    - \linenumbers
---

# Discussion (_under construction_)

"It has been suggested that an inheritance system that couples weak vertical transmission with strong oblique transmission ($\rho \ll 1$) might prevent traits from being eliminated more than if vertical transmission was coupled with horizontal transmission, in which traits are transmitted between same-generation individuals" [@Cavalli-Sforza1981, pg. 315].

"They suggest on the basis of the results of a
modeling exercise that vertical transmission is only effective
when the environment is relatively stable and risk of
mortality is such that survival to parenthood is itself an
indicator of an individual's worth as a cultural role model. [@McElreath2008]" // rephrase

Most models of oblique transmission focused on social learning and how it differs from individual learning, usually in the presence of environmental cues [@Kline2013].
In contrast, our model (i) does not include individual learning, (ii) assigns an equal probability for each (naturally selected) individual to be the phenotype donor in oblique transmission, rather then more specific schemes such as teachers (one-to-many) or conformity (many-to-one) [@Aoki2011], and (iii) does not include a cost for the phenotype donor - and therefore might be more suitable for modeling imitation rather than teaching.
Instead, our model focuses on the difference between vertical and oblique transmission, be it via learning or other mechanisms.
Therefore, our model is able to capture other inheritance modes except learning, such as horizontal gene transfer in asexual microbes.
As such, the main factor that determines when vertical or oblique transmission is preferred is the frequency and intensity of environmental changes.

Previous theoretical studies predicted vertical transmission will be favored over oblique transmission for phenotypes that determine fitness (@Aoki2011 and @McElreath2008 cited by @Kline2013). **NO ENVIRONMENTAL FLUCTUATIONS?**
Our results suggest that in a maladapted population vertical transmission (high $\rho$ values) are favored, but after the population has reached a steady state in phenotype frequencies, oblique transmission can be favored in rapidly fluctuating environments (@Fig:A1B1_EGS_eta_0).

@Cavalli-Sforza1983

@Allison1992

## EGS of $\eta=0$

@Xue2016 have shown numerically (in SI) that with extreme selection, in a rapidly changing environment, $\eta^* \to 0$, whereas if environmental changes are farther apart (>9), then $\eta^* > 0$. This was done by maximizing mean fitness, which has been shown (@Carja2014) to fit with simulation results in analyses of evolution of stable modification rates.

There has been a body of work on models in which the phenotype is genetically encoded by two alleles (_A_ and _a_) and the transition between these alleles is determined by a mutation modifier allele [see summary in @Liberman2011]. In these models, under fluctuating environment, the evolutionary stable mutation rate is ~1/n if the favored allele changes deterministicly every _n_ generations, but can be different if _n_ is random or if selection is not symmetric. In the model presented in @Xue2016, however, the phenotype switching rate is (epi)genetically encoded, and mutation is not needed for transitioning between the phenotypes. Moreover, the transition rate is modified by the phenotype (@Eq:learning_rule). If  we assume that the rate of this modification, $\eta$, is determined by a modifier locus, then the dynamics of alleles at this modifier locus are different from those of a mutation modifier locus.

# References