---
layout: post
title: Infinitely many primes through regular languages
---

Let $$M_n$$ denote the set of strings consisting of just $$1$$'s 
whose length is a multiple of $$n$$; i.e.

$$M_n \triangleq \{1^n\}^*$$

Clearly, each $$M_n$$ is regular. Additionally, recall that if $$A$$ and $$B$$ are regular 
languages, then the intersection $$A \cap B$$ and the complement 
$$\bar{A}$$ are regular. 

By the fundamental theorem of arithmetic, a number is a 
power of $$2$$ exactly when $$2$$ is the only prime number that 
divides it, so if there were finitely many primes 
$$\{2, 3, \dots, p\}$$, then the set 

$$A=\{1^{2^k} : k \geq 0\}$$

of strings of $$1$$'s whose length is a power of $$2$$ is regular as 
$$A$$ is equal to the 
intersection 
$$M_2 \cap \bar{M_3} \cap \dots \cap \bar{M_p}$$
of (finitely many) regular languages. 

However, we can show $$A$$ is not regular by using the [pumping lemma](https://en.wikipedia.org/wiki/Pumping_lemma_for_regular_languages).
For $$k \geq 0$$, then if we let $$w = 1^{2^k}$$, then $$w \in A$$ and $$|w| = 2^k \geq k$$.
If $$w=xyz$$ for strings 
$$x, y, z$$ with $$|xy| \leq k$$ and $$|y| \geq 1$$,
then as $$|xy^2z| = |xyz| + |y|$$, $$|xyz| = 2^k$$, and 
$$|y| \geq 1$$, then $$|xy^2z| > 2^k$$. 
Additionally, as $$|xy| \leq k < 2^k$$ and $$|xy| + |z| = |xyz|$$,
then $$|z| > 0$$ so

 $$|xy^2z| = |x| + 2|y| + |z| < 2|x|+2|y|+2|z| = 2|xyz|=2^{k+1}.$$

Therefore, we have $$2^k < |xy^2z| < 2^{k+1}$$, so the length of $$xy^2z$$ cannot 
be a square and thus $$xy^2z \notin A$$. Thus, by the pumping lemma,
$$A$$ is not regular so there must be infinitely many primes.

This post was adapted from [u/JoshuaZ1's comment thread in r/math](https://www.reddit.com/r/math/comments/ggi065/six_proofs_that_there_are_infinitely_many_primes/fq1aipz/)
on different ways of proving the infinitude of primes.