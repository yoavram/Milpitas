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

# Introduction

Since the emergence of the *modern synthesis* in the 1940s, evolutionary
biology has been structured around genetic inheritance as the mode of
transmission of traits between generations [@Laland2014].
Indeed, most evolutionary biology textbooks begin by describing evolution
through natural selection as a process in which *"genetic changes that
improve the fitness of individuals will tend to increase in frequency
over time"* [@Bergstrom2012].

However, it is apparent that in many animals, and especially in humans,
many traits are transmitted through imitation, teaching and learning,
and other forms of communication that comprise *cultural evolution*
[@Cavalli-Sforza1973; @Cavalli-Sforza1981; @Boyd1985; @Avital2000; @Whiten2017; @Laland2017].
Other phenotype-modifying transmission vehicles have received increasing
attention over the past two decades [@Jablonka2014], including
epigenetics [@Verhoeven2016] and symbionts [@Zilber-Rosenberg2008].
These transmission mechanisms vary in their persistence, speed, timing, and direction when compared to the kind of vertical transmission between parent and offspring that is restricted to genetic inheritance.

Of special interest is *oblique transmission*, in which offspring
inherit traits from adults that are not their parents [@Cavalli-Sforza1981; @Bergstrom2012, ch. 19.4], for example, by social learning (_e.g._, imitation and teaching [@Kline2013]).
For example, in a small Amazon society, in which young individuals
frequently interact with older individuals, transmission of botanical
knowledge and skills from the parental cohort was more significant than
transmission from parents [@Reyes-Garcia2009].
In contrast, in tribal Iranian populations, transmission of weaving techniques from parents has a larger effect then oblique transmission [@Tehrani2009, more examples therein].
Social learning is also common in birds and mammals [@Creanza2016], and evidence suggests a role for oblique transmission in inheritance of foraging strategies in dolphins [@Mann2007; @Whitehead2014; @Creanza2016].

**TODO: niche construction as a form of oblique transmission?**

Infection with symbionts may also be regarded as a form of oblique
transmission.
The microbiome is commonly vertically transmitted [@Rosenberg2016], but pathogens may also be transmitted between unrelated individuals, and can lead to phenotype change in the host.
Transmission of symbionts from non-parental individuals of the parents’ generation may then be regarded as oblique [@Theis2016].

Oblique transmission also occurs through mechanisms involving DNA.
In bacteria, phenotypes might be determined by heritable mobile genetic
elements such as phages [@Zinder1952], plasmids [@Lederberg1946], integrons [@Mazel2006], and transposons [@Salyers2004] (**TODO: CRISPR?**).
Similarly, some phenotypes are determined by genes that are commonly converted by uptake of foreign DNA, *i.e.* transformation [@Milkman1990].
In these cases, inheritance of a phenotype may combine vertical transmission from the parent cell, and oblique transmission from other cells, even if the latter did not originally evolve for that purpose [@Redfield1993].

Here, we model the dynamics of a phenotype that is inherited by a
combination of vertical and oblique transmission. We study properties of
the steady state phenotypic frequencies of variants in constant and
fluctuating environments, and find conditions under which oblique
transmission is likely to evolve.

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