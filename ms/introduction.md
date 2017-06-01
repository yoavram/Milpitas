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
    - \usepackage{lineno}
    - \linenumbers
---

# Introduction

Since the formation of the _modern synthesis_ in the 1940s, evolutionary biology has mainly focused on genetic inheritance for the transmission of traits between generations [@Laland2014].
Indeed, most evolutionary biology textbooks begin by describing evolution through natural selection as a process in which _"genetic changes that improve the fitness of individuals will tend to increase in frequency over time"_ [@Bergstrom2012].

However, it is apparent that in animals, and especially in humans, many traits are transmitted through learning and language, leading to the study of _cultural evolution_ [@Cavalli-Sforza1981; @Avital2000].
Additional transmission mechanisms have received increasing attention over the past two decades [@Jablonka2014], including epigenetics [@Verhoeven2016] and symbionts [@Zilber-Rosenberg2008]. 
These mechanisms vary in their speed, timing, and direction when compared to the standard vertical transmission between parent and offspring imposed by genetic inheritance.

Of special interest is _oblique transmission_, in which offspring inherit traits from adults that are not their parents [@Cavalli-Sforza1981; @Bergstrom2012, ch. 19.4].
The first examples that come to mind are from non-genetic inheritance systems that depend on social learning, _i.e._ imitation and teaching [@Kline2013]. For example, in a small Amazon society, in which young individuals frequently interact with older individuals, transmission of botanical knowledge and skills from parental cohort was more significant then transmission from parents [@Reyes-Garcia2009]
In contrast, in tribal Iranian populations, vertical transmission of weaving techniques has a larger effect then oblique transmission [@Tehrani2009, more examples therein]. 
Social learning is also common in birds and mammals, and evidence suggests a role for oblique transmission in inheritance of foraging strategies in dolphins [@Mann2007].

**TODO: niche construction as a form of oblique transmission?**

Another interesting form of oblique transmission is symbiont infection. The microbiome is usually vertically transmitted [@Rosenberg2016], but since pathogens are commonly transmitted between unrelated individuals, leading to infection and severe phenotype change  - disease - it's likely that offspring can be infected with phenotype-determining symboints from non-parent individuals [@Theis2016].

Oblique transmission also occurs through genetic mechanisms. In bacteria, phenotypes might be determined by heritable mobile genetic elements such as phages [@Zinder1952], plasmids [@Lederberg1946], integrons [@Mazel2006], and transposons [@Salyers2004] (**TODO: CRISPR?**).
Similarly, some phenotypes are determined by genes that are commonly converted by uptake of foreign DNA, _i.e._ transformation [@Milkman1990]. In these cases, phenotype inheritance will combine vertical transmission from the parent cell, and oblique transmission from other cells, even if these oblique transmission mechanisms did not originally evolve for that purpose [@Redfield1993a].

Here, we model the dynamics of a phenotype that is inherited by a combination of vertical and oblique transmission. We study properties of the phenotype steady state frequency in constant and fluctuating environments, and find conditions in which oblique transmission is likely to evolve.

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

# References