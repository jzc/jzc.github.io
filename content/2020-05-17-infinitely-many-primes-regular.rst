==================================================
 Infinitely many primes through regular languages
==================================================
:slug: infinitely-many-primes-regular

Let :math:`M_n` denote the set of strings consisting of just :math:`1`'s 
whose length is a multiple of :math:`n`; i.e.

.. math::
   M_n \triangleq \{1^n\}^*

Clearly, each :math:`M_n` is regular. Additionally, recall that if :math:`A` and :math:`B`
are regular languages, then the intersection :math:`A \cap B` and the complement 
:math:`\bar{A}` are regular. 

By the fundamental theorem of arithmetic, a number is a 
power of :math:`2` exactly when :math:`2` is the only prime number that 
divides it, so if there were finitely many primes 
:math:`\{2, 3, \dots, p\}`, then the set 

.. math::
   A=\{1^{2^k} : k \geq 0\}

of strings of :math:`1`'s whose length is a power of :math:`2` is regular as 
:math:`A` is equal to the 
intersection 
:math:`M_2 \cap \overline{M_3} \cap \dots \cap \overline{M_p}`
of (finitely many) regular languages. 

However, we can show :math:`A` is not regular by using the
`pumping lemma <https://en.wikipedia.org/wiki/Pumping_lemma_for_regular_languages>`_.
For :math:`k \geq 0`, then if we let :math:`w = 1^{2^k}`,
then :math:`w \in A` and :math:`|w| = 2^k \geq k`.
If :math:`w=xyz` for strings 
:math:`x, y, z` with :math:`|xy| \leq k` and :math:`|y| \geq 1`,
then as :math:`|xy^2z| = |xyz| + |y|`, :math:`|xyz| = 2^k`, and 
:math:`|y| \geq 1`, then :math:`|xy^2z| > 2^k`. 
Additionally, as :math:`|xy| \leq k < 2^k` and :math:`|xy| + |z| = |xyz|`,
then :math:`|z| > 0` so

.. math::
   |xy^2z| = |x| + 2|y| + |z| < 2|x|+2|y|+2|z| = 2|xyz|=2^{k+1}.

Therefore, we have :math:`2^k < |xy^2z| < 2^{k+1}`, so the length of :math:`xy^2z` cannot 
be a power of two and thus :math:`xy^2z \notin A`. Thus, by the pumping lemma,
:math:`A` is not regular so there must be infinitely many primes.

This post was adapted from `u/JoshuaZ1's comment thread in r/math <https://www.reddit.com/r/math/comments/ggi065/six_proofs_that_there_are_infinitely_many_primes/fq1aipz/>`_
on different ways of proving the infinitude of primes.
