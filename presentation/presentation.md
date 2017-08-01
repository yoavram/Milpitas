slidenumbers: true
slidecount: true
theme:Letters from Sweden, 6

# [fit] Vertical and Oblique Transmission
</br>
## Yoav Ram
## August 2, 2017

![original](images/joshua-sortino-228788.jpg)

[.footer: Photo by Joshua Sortino on Unsplash]
[.slidenumbers: false]
---

## The Modern Synthesis

Genetic inheritance as the transmission mode of traits between generations:

> Genetic changes that improve the fitness of individuals will tend to increase in frequency over time.
-- Bergstrom and Dugatkin 2012, ch. 1.1

---

## Non-genetic inheritance

- _Cultural evolution_: Imitation, teaching, learning, communication, niche construction, material inheritance ($$)
- _Epigenetics_ 
- _Microbiome_: symbionts, parasites, pathogens
- _Prions_: infectious proteins such as [Het-s],[PSI+], [URE3], spongiform

![right](images/nathaniel-tetteh-297656.jpg)

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
x' = \rho \frac{w_A}{\bar{w}} + (1-\rho)x
$$

Mean fitness:

$$
\bar{w} = xw_A + (1-x)w_B
$$

---

![fit](figures/recurrence_example_A.png)

---

## Constant environment

Let $$A$$ be favored by natural selection over $$B$$.

_Result 1._ If $$0<\rho\le 1$$[^*] and $$0 < w_B < w_A$$, then fixation of phenotype $$A$$ is globally stable.

![right](images/amy-humphries-227515.jpg)

[^*]: With perfect oblique transmission ($$\rho=0$$) or neutral evolution ($$w_A=w_B$$) the recursion is $$x'=x$$ and there is no evolution.

---

![fit](figures/recurrence_example_B.png)

---

## Extreme selection

If only _one phenotype can survive_ ($$w_A=1, w_B=0$$) then the recursion is 

$$
x'=\rho + (1-\rho)x 
\quad \Rightarrow \quad
x_t = 1-(1-\rho)^t (1-x_0).
$$

The _fixation time_, i.e. frequency change from $$x_0$$ to $$1-\epsilon$$), is

$$
\tau = \frac{\log{\epsilon}}{\log{(1-\rho)}}
$$

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

_Result 2._ If _$$k=l$$_ and $$0<w<W$$ with $$0 < \rho < 1$$ then fixation of $$B$$ is unstable and a _protected polymorphism_ exists.

![right](images/scott-webb-98682.jpg)

---

_Proof._ Rewrite the recurrence equation,
$$
x' = \rho x \frac{w_A}{\bar{w}} + (1-\rho) x = x\Big(1+\rho(1-x)\frac{w_A-w_B}{\bar{w}}\Big)
$$
When $$A$$ is very rare, the change in its frequency when $$A$$ is favored is $$x(1+\rho\frac{W-w}{w})+o(x^2)$$ and when $$B$$ is favored it is $$x(1+\rho\frac{w-W}{W})+o(x^2)$$.

Therefore, the local stability of $$x^*=0$$ is determined by 

$$
\Big[\big(1+\rho\frac{W-w}{w}\big)\big(1+\rho\frac{w-W}{W}\big)\Big]^k = 
\Big[1 + \rho(1-\rho)\frac{(W-w)^2}{Ww}\Big]^k > 1.
$$

---

## Periodic environment

_Result 3._ For general $$k$$ and $$l$$, either fixation of one phenotype is stable, or else there exists a protected polymorphism.

_Note._ For some ratios $$k/l$$ we can determine if polymorphism or fixation occur.

---

![fit](figures/lk_phase_plane.png)

---

## Periodic environment
### A1B1

We saw that when $$k=l$$ there is a protected polymorphism.
We can find it for $$k=1$$.

_Result 4._ In A1B1 with $$0<\rho<1$$ and $$w<W$$, there is a unique stable polymorphism given by

$$
x^* = \frac{1}{2} - \frac{W+w-\sqrt{(1-\rho)^2(W-w)^2+4Ww}}{2(2-\rho)(W-w)}.
$$

---

## A1B1

If vertical transmission rate $$\rho$$ _increases_:

$$0\to 1$$

then stable frequency $$x^*$$ _decreases_:

$$\frac{1}{2} \to \frac{\sqrt{Ww}-w}{W-w}$$

![right fit](figures/A1B1_stable_x.png)

---

## A1B1

So, with vertical transmission, the frequency of $$A$$ decreases just before it is favored again.

That is _not good_.

![right fit](figures/A1B1_stable_x.png)

---

## Random environment

![](images/jack-hamilton-320934.jpg)

---

## [fit] Random environment

An environment that changes randomly such that
$$w_A$$ is a _random variable_ and $$w_B = 1$$ is constant[^$].

![right](images/jack-hamilton-320934.jpg)

[^$]: We only really care about the ratio $$w_A/w_B$$ so everything works if $$w_B$$ is also random.

---

## Stochastic local stability - SLS

_Definition:_ an equilibrium $$x^*$$ is _SLS_ if for any initial $$x_0$$ sufficiently near $$x^*$$, we know that $$x_t$$ is very likely to converge to $$x^*$$.

That is, for any $$\epsilon>$$ there exists $$\delta>0$$ such that  $$|x_0-x^*| < \delta$$ implies that

$$P\left(\lim_{t\to\infty}x_t =x^*\right)\ge 1-\epsilon$$

---

## Random environment

_Result 5._ If $$E[\log{(1+\rho (w_A-w_B))}]>0$$ then fixation of $$B$$ ($$x^* = 0$$) **is not** stochastically locally stable.
In fact, $$P\left(\lim_{t\to\infty}x_t = 0\right) = 0$$.

_Result 6._ If $$E[\log{(1+\rho (w_A-w_B))}]<0$$ then fixation of $$B$$ ($$x^* = 0$$) **is** stochastically locally stable.

_Note._ $$x^*=0$$ and $$x^*=1$$ cannot both be stable.

---

## [fit] Random environment

Frequency of phenotype $$A$$ after $$10^6$$ generations.

$$w_A=\begin{cases}1+s, & p\\1-s, & 1-p\end{cases}$$ and $$w_B=1$$

white line marks $$E[\log{(1+\rho (w_A-w_B)}]=0$$, below this line fixation of $$B$$ is stochastically locally stable.

![right fit](figures/stochastic_env_x_t.pdf)

[.footer: Parameters: $$x_0=0.1$$, $$\rho=0.1$$.]
---

## Evolution of the transmission mode

Can the transmission mode itself evolve due to second-order selection?

![](images/matthew-henry-134263.jpg)

---

## Modifier model

We model competition between _two modifier alleles_:

- $$m$$ with vertical transmission rates $$\rho$$,
- $$M$$ with vertical transmission rates $$P$$.

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

## Modifier model

- Start with population with only allele $$m$$.
- Equilibrium between phenotypes $$A$$ and $$B$$.
  - Frequency of $$A$$ is $$x^*$$, as before.
- Now, allele $$M$$ is introduced in low frequency.

_Can $$M$$ increase in frequency and invade the population, or is $$m$$ stable to invasion?_

---

## Periodic environment
### A1B1

_Result 7._ A modifier allele with vertical transmission rate $$\rho$$ is:

- stable to invasion of allele with rate $$P$$ if $$P>\rho$$,
- unstable if $$P<\rho$$. 

---

## [fit] Periodic environment
### A1B1

- $$w_A$$ and $$w_B$$ switch between $$1$$ and $$0.1$$ every generation.
- Initial resident modifier: $$\rho_0 = 0.1$$.
- Invaders reduce rate by $$1/10$$.

![fit right](figures/A1B1_modifier_invasions.pdf)

---

## [fit] Random environment

- $$w_A$$ and $$w_B$$ take on $$1$$ and $$0.1$$ by a coin flip.
- Initial resident $$\rho_0 = 0.1$$.
- Invaders reduce rate by $$1/10$$.

![fit right](figures/stoch_modifier_invasions.png)

---

## Reduction principle

![](images/brendan-church-182747.jpg)

---

## [fit] Reduction principle for vertical transmission

In the $$A1B1$$ environment cycle, evolution tends to _reduce vertical transmission_ and _increase oblique transmission_.

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
- _Random environment:_ ?

![right](images/tatiana-lapina-6807.jpg)

[.build-lists: true]
---

## Evolution of oblique transmission

- _Constant environment:_ when the favored phenotype is rare, a modifier that increases vertical transmission can invade.
- _Rapidly changing environment_: when the phenotype frequency is at equilibrium, a modifier that increases oblique transmission can invade - reduction principle for vertical transmission.

---

## Environmental cues

In a _rapidly changing environments_, phenotypic response to environmental cues is favored over oblique transmission - better tracking of selection changes[^&].

Example: individual learning.

![right](images/oscar-sutton-251737.jpg)

[^&]: Aoki et al. 2005

[.build-lists: true]
---

## Other forms of oblique transmission

- _Conformity_, or many-to-one: good for constant, bad in rapidly changing.
- _Teacher-type_, or one-to_many: depends on teachers are chosen.
- _Intra-familial_, such as between grandparents and grandchildren.

---

## Transmission fidelity

Both vertical and oblique transmission likely produce errors.

If fidelity of genetic inheritance > cultural transmission (mix of vertical & oblique), then genetic inheritance will win in a constant environment[^%].

[^%]: Cavalli-Sforza & Feldman, 1983

---

## Phenotype switching

Several studies[^Q] assumed
- periodic changing environment
- vertical transmission of phenotype
- phenotype switch by transmission fidelity
- fidelity determined by modifier

[^Q]: Leigh 1970, Ishii et al. 1989, Jablonka 1996, Kussel & Leibler 2005, King & Masel 2007, Liberman et al. 2011

---

## [fit] Phenotype switching

- Switching rate evolves toward $$1/n$$ where $$n$$ is the period length[^D].
- _Environmental statistics encoded by the modifier._

![right](images/jakob-owens-209001_cropped.jpg)

[^D]: Doesn't work if $$Var(n)$$ is large or if selection not symmetric.

---
## Phenotype switching

_With oblique transmission:_

- Phenotype switch caused by oblique transmission rather then transmission errors.
- _Environmental statistics encoded by the stable population phenotype distribution._

---

## [fit] Evolution with oblique transmission

Oblique transmission can increase _relatedness_[^R]

Outcomes might be similar to _Microbes can help explain the evolution of host altruism_[^L]

![right](images/bill-wegener-280985_cropped.jpg)

[^L]: Lewin-Epstein et al. 2017

[^R]: Allison 1992

---

## [fit] Evolution with oblique transmission

Effective reduction of selection due to _decoupling of reproduction & inheritance_.

Outcomes might be similar to _With a little help from my friends_[^O]

![right](images/nathan-anderson-122047.jpg)

[^O]: Obolski et al. 2017

---
# Acknowledgments

- Marc Feldman, Stanford University
- Uri Liberman, Tel-Aviv University
- Funding: Stanford Center for Evolution and Human Genomics

---

# Thank you!

![](images/coffee.jpg)

[.autoscale:true]