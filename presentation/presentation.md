slidenumbers: true
slidecount: true
theme:Letters from Sweden, 6

# [fit] Vertical & Oblique Transmission 
# [fit] under Fluctuating Selection
#### :
### Yoav Ram
### October 31, 2017
#### :
#### Work with Marc Feldman & Uri Liberman

![original](images/kelly-sikkema-208098.jpg)

[.footer: Photo by Kelly Sikkema on Unsplash]
[.slidenumbers: false]
---

## The Modern Synthesis

Genetic inheritance as the transmission mode of traits between generations.

> Genetic changes that improve the fitness of individuals will tend to increase in frequency over time.
-- Bergstrom and Dugatkin 2012, ch. 1.1

Considered to be _vertical_: parent to offspring

---

## Non-genetic inheritance

- _Cultural evolution_: Imitation, learning...
- _Epigenetics_ 
- _Microbiome_: symbionts, parasites, pathogens
- _Prions_: infectious proteins such as [Het-s],[PSI+], [URE3], spongiform

_Often non-vertical_

![fit right](images/four_dimensions.jpg)

---

## Non-vertical genetic inheritance

- _Horizontal gene transfer_: transformation, transduction, conjugation (plasmids & transposable elements), integrons
- _Host-parasite gene transfer_
- _Cross-species gene transfer_

---

## Vertical vs. non-vertical transmission

Differences in

- persistence 
- reversibility
- speed
- timing
- direction
- regulation

![right filtered](images/william-bout-264829.jpg)

---

## Oblique transmission

Offspring inherit traits from
non-parental adults.

*Oblique = Diagonal

![](images/samuel-zeller-249358.jpg)

---

## Focus: mixed vertical & oblique transmission

Offspring inherit traits _either_ from parent _or_ from non-parental adults.

__Examples:__

- Social learning in humans, birds, dolphins...
- Microbiome
- Genetic inheritance + horizontal gene transfer

---

## Model
### Phenotypes

Two phenotypes that affect fitness:

|phenotype | A | B |
|----------|---|---|
|freq.| $$x$$ | $$1-x$$ |
|fitness| $$w_A$$ | $$w_B$$ |

![right](images/samantha-scholl-157435.jpg)

---

## Model
### Transmission

Offspring inherit phenotype from:

- parent with probability $$\rho$$ 
- random non-parental adult with probability $$1-\rho$$

where $$\rho$$ is the vertical transmission rate.

---

## Model
### Recurrence equation

The frequency of phenotype $$A$$ in the next generation:

$$
x' = \rho \frac{w_A}{\bar{w}}x + (1-\rho)x
$$

Mean fitness:

$$
\bar{w} = xw_A + (1-x)w_B
$$

---

![fit](figures/recurrence_example_A.pdf)

---

## Constant environment

_Result 1._ If $$A$$ is favored by natural selection over $$B$$ and $$\rho>0$$[^*], fixation of phenotype $$A$$ is globally stable.

![right](images/amy-humphries-227515.jpg)

[^*]: With perfect oblique transmission ($$\rho=0$$) or neutral evolution ($$w_A=w_B$$) the recursion is $$x'=x$$ and there is no evolution.

---

![fit](figures/recurrence_example_B.pdf)

---

##  Periodic environment

![right original](images/aaron-burden-34998.jpg)
![left original](images/jakob-owens-190795.jpg)

---

## Periodic environment

Consider environments $$AkBl$$ that favor $$A$$ for $$k$$ generations and $$B$$ for $$l$$ generations:
- $$A1B1=ABABAB...$$
- $$A2B1=AABAABAAB...$$
- $$A2B3=AABBBBAABBBB...$$

- Fitness of the favored phenotype (whatever it is at a given time) is $$W$$
- Fitness of the unfavored phenotype is $$w$$

---

## [fit] Periodic environment

_Result 2._ If _$$k=l$$_ then fixation of either phenotype is unstable and a _protected polymorphism_ exists.

![right](images/scott-webb-98682.jpg)

---

## Periodic environment

_Result 3._ For general $$k$$ and $$l$$, a protected polymorphism exists if

$$
-\frac{\log{(1+\rho\frac{w-W}{W})}}{\log{(1+\rho\frac{W-w}{w})}} < \frac{l}{k} < -\frac{\log{(1+\rho\frac{W-w}{w})}}{\log{(1+\rho\frac{w-W}{W})}}
$$

otherwise fixation of one phenotype is stable.

---

![fit](figures/lk_phase_plane.pdf)

---

## Periodic environment
### A1B1

We saw that when $$k=l$$ there is a protected polymorphism.
We can find it for $$k=1$$.

_Result 4._ For A1B1 there is a unique stable polymorphism[^x]

$$
x^* = \frac{1}{2} - \frac{W+w-\sqrt{(1-\rho)^2(W-w)^2+4Ww}}{2(2-\rho)(W-w)}.
$$

[^x]: $$x^*$$ is the frequency of $$A$$ at the end of even generations

---

## A1B1

If vertical transmission rate $$\rho$$ _increases_

$$0\to 1$$

then stable frequency $$x^*$$ _decreases_

$$\frac{1}{2} \to \frac{\sqrt{Ww}-w}{W-w}$$

![right fit](figures/A1B1_equilibrium_A.pdf)

---

## A1B1

So, with vertical transmission, the frequency of $$A$$ decreases just before it is favored again.

That is _not good_.

![right fit](figures/A1B1_equilibrium_A.pdf)

---

## A1B1

Indeed, the stable mean fitness decreases with the vertical transmission rate:

$$\frac{1}{2}(W+w) \to \sqrt{Ww}-w$$

![right fit](figures/A1B1_equilibrium_B.pdf)

---

## Evolution of the transmission mode

Can the transmission mode itself evolve due to second-order selection?

![](images/matthew-henry-134263.jpg)

---

## Modifier model

We model competition between _two modifier alleles_:

- $$m$$ with vertical transmission rate $$\rho$$,
- $$M$$ with vertical transmission rate $$P$$.

![right](images/cloudvisual-208962.jpg)

---

## Modifier model

| Pheno-genotype     | $$mA$$  | $$mB$$     | $$MA$$  | $$MB$$     |
|------|-----|--------|-----|--------|
| frequency    | $$x_1$$  | $$x_2$$ | $$x_3$$  | $$x_4$$ |
| fitness    | $$w_A$$ | $$w_B$$    | $$w_A$$ | $$w_B$$    |
| rate | $$\rho$$   | $$\rho$$      | $$P$$   | $$P$$      |

---

## Modifier model
### Recurrence equation

$$
\bar{w} x_1' = x_1 w_A ((1-\rho)(x_1 + x_3)+\rho) + x_2 w_B(1-\rho)(x_1 + x_3)
$$

$$
...
$$

$$
...
$$

$$
...
$$

---

## Modifier model
### Recurrence equation

$$
\bar{w} x_1' = x_1 w_A ((1-\rho)(x_1 + x_3)+\rho) + x_2 w_B(1-\rho)(x_1 + x_3)
$$

$$
\bar{w} x_2' = x_1 w_A (1-\rho)(x_2 + x_4) + x_2 w_B ((1-\rho)(x_2 + x_4) + \rho)
$$

$$
\bar{w} x_3' = x_3 w_A ((1-P)(x_1 + x_3) + P) + x_4 w_B (1-P)(x_1 + x_3)
$$

$$
\bar{w} x_4' = x_3 w_A (1-P)(x_2 + x_4) + x_4 w_B ((1-P)(x_2 + x_4) + P)
$$

$$
\bar{w} = w_A (x_1 + x_3) + w_B (x_2 + x_4)
$$

---

# Stability analysis

![](images/austin-neill-130037.jpg)

[.footer: Photo by Austin Neill on Unsplash]

---

## Modifier model

- Initial population:
  - only with modifier allele $$m$$
  - at equilibrium between phenotypes $$A$$ and $$B$$ ($$x^*$$)
- Now, allele $$M$$ is introduced at a low frequency

_Can $$M$$ increase in frequency and invade the population, or is $$m$$ stable to invasion?_

---

## Periodic environment: A1B1

_Result 7._ A modifier allele with vertical transmission rate $$\rho$$ is:

- stable to invasion of allele with rate $$P$$ if $$P>\rho$$,
- unstable if $$P<\rho$$. 

---

## [fit] Periodic environment: A1B1

- $$w_A$$ and $$w_B$$ switch between $$1$$ and $$0.1$$ every generation.
- Initial resident modifier: $$\rho_0 = 0.1$$.
- Invaders reduce rate by $$1/10$$.

![fit right](figures/A1B1_modifier_invasions.pdf)

---

## Reduction principle

![](images/brendan-church-182747.jpg)

[.footer: Photo by Brendan Church on Unsplash]

---

## [fit] Reduction principle for vertical transmission

In the $$A1B1$$ selection regime, evolution tends to _reduce vertical transmission_ and _increase oblique transmission_.

---

## The plot thickens...

![original](images/cindy-tang-25654.jpg)

[.footer: Photo by Cindy Tang on Unsplash]

---

## Periodic environment: AkBk

More generally, there is __no__ reduction of the vertical transmission rate.

With environmental periods $$k=l>2$$ the stable vertical transmission rate is high (>0.4).

![fit right](figures/AkBk_stable_optimal_rate_B.pdf)

---

## Periodic environment: AkBk

Moreover, the stable transmission rate __does not__ maximize the geometric mean fitness[^g].

![fit right](figures/AkBk_stable_optimal_rate.pdf)

[^g]: Geometric average of the population mean fitness over $$2k$$ generations. 

---

## Periodic environment: AkBk

Moreover, the stable transmission rate __does not__ maximize the geometric mean fitness[^g].

_Reminder:_ these modifiers are __not__ neutral as they reduce effect of selection.

![fit right](figures/AkBk_stable_optimal_rate.pdf)

[^g]: Geometric average of the population mean fitness over $$2k$$ generations. 

---

## Model applications

Human/bird/mammal population with social learning from parents ($$\rho$$) or random adults ($$1-\rho$$) due to
 - Error in parent identification
 - Adoption
 - Babysitting
 - Alloparenting & cooperative breeding
 - Cooperation

![right](images/ray-hennessy-118049.jpg)

---

## Model applications

Microbial population, phenotype determined by specific locus that is copied by DNA replication ($$\rho$$) and sometimes received by external DNA ($$1-\rho$$):
- Plasmids
- Chromosomal integrative & conjugative elements
- Transduction with viruses
- Integrons
- Transformation & competence

---

## Polymorphism

- _Constant environment:_ polymorphism lasts longer with oblique transmission.
- _Periodic environment:_ polymorphism is maintained in shorter periods with oblique transmission

![right](images/tatiana-lapina-6807.jpg)

[.build-lists: true]
---

## Evolution of oblique transmission

- Rapidly changing environments favor _oblique_ transmission.
- Slow and constant environments favor _vertical_ transmission.

---

## Phenotype switching

Several studies[^ξ] assumed
- periodically changing environment
- _vertical_ transmission of phenotype
- phenotype switch by transmission fidelity
- fidelity determined by a genetic modifier

[^ξ]: Leigh 1970, Ishii et al. 1989, Jablonka 1996, Kussel & Leibler 2005, King & Masel 2007, Liberman et al. 2011

---

## [fit] Phenotype switching

- Switching rate evolves toward $$1/n$$ where $$n$$ is the period length[^μ].
- _Environmental statistics encoded by the modifier._

![right](images/jakob-owens-209001_cropped.jpg)

[^μ]: Doesn't work if $$Var(n)$$ is large or if selection not symmetric.

---
## Phenotype switching

With _oblique_ transmission:

- Phenotype switch caused by oblique transmission rather then transmission errors.
- _Environmental statistics encoded by the stable population phenotype distribution_ if environmental changes are frequent and selection is weak. 

---

# Acknowledgments

Funding: Stanford Center for Evolution and Human Genomics

![inline 200%](images/cehg.png)

---

# Thank you!

![](images/coffee.jpg)

[.autoscale:true]