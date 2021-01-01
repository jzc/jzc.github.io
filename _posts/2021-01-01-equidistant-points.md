---
layout: post
title: Equidistant points from a pair of points
---

In the figure below, visually, 
it is not too hard to believe that the points
equidistant from $$u$$ and $$v$$ are exactly the 
the points on the dashed line. A description of the dashed line 
seems to be "the line running perpendicularly through the midpoint 
of the segment between $$u$$ and $$v$$." This turns out to be 
true, and perhaps is a standard exercise in Euclidean geometry. 
However, we can formulate this using linear algebra and obtain 
a result that generalizes to higher dimensions, yet the
proof is still "strategized" by our visual intuition.

<figure>
    <img src="/assets/line-equidistant.svg">
</figure>

**Theorem.** Let $$u$$ and $$v$$ be two points in $$\mathbb{R}^n$$.
Let $$A \triangleq \{ w \in \mathbb{R}^n : \lVert w-u \rVert = \lVert w-v \rVert\}$$
be the set of points equidistant from $$u$$ and $$v$$,
and let $$m \triangleq \dfrac{u+v}{2}$$ be the midpoint of the segment between $$u$$ and $$v$$. Then,
$$A$$ is equal to the the orthogonal complement of the line through 
$$u$$ and $$v$$ plus $$m$$; i.e.

$$m + \text{span}(v-u)^\bot = A$$

*Proof.* Let $$m+w \in m + \text{span}(v-u)^\bot$$, so that $$\langle w, v-u \rangle = 0$$.
Note that $$w$$ and $$m-u$$ are orthogonal, as

$$
\begin{aligned}
\left\langle w, m-u \right\rangle &= \left\langle w, -\frac{u}{2}+\frac{v}{2} \right\rangle \\
&= \frac{1}{2} \langle w, v-u \rangle \\
&= 0.
\end{aligned}
$$

Similarly, $$w$$ and $$m-v$$ are orthogonal. As $$m-u = -\left(m-v\right)$$,
we have $$\left\lVert m-u \right\rVert = \left\lVert m-v \right\rVert$$. Then, with 
the Pythagorean theorem,

$$
\begin{aligned}
    \left\lVert \left(m+w\right)-u \right\rVert^2 &= \left\lVert m-u\right\rVert^2+ \lVert w \rVert^2 \\ 
    &= \left\lVert m-v\right\rVert^2+ \lVert w \rVert^2 \\
    &= \left\lVert \left(m+w\right)-v \right\rVert^2,
\end{aligned}
$$

so $$m+w$$ is equidistant from $$u$$ and $$v$$, and thus, 
$$m + \text{span}(v-u)^\bot \subseteq A$$.


<figure>
    <img src="/assets/decomposition.svg">
    <figcaption markdown="span">
    Decomposition of the distance from $$u$$ [or $$v$$] to our given
    vector, $$m+w$$, into orthogonal parts.
    </figcaption>
</figure>

Conversely, suppose $$w \in A$$, so that $$\lVert w-u \rVert = \lVert v-u \rVert$$.
We can form a rhombus using $$w$$, $$u$$, and $$v$$ so that the diagonals 
of this rhombus are $$(u-w)+(v-w)=u+v-2w$$ and $$(u-w)-(v-w)=v-u$$. Note 
that for any $$a$$ and $$b$$, we have 

$$
\begin{aligned}
\langle a+b, a-b \rangle &= \langle a, a \rangle - \langle a, b \rangle + \langle b, a \rangle - \langle b, b \rangle \\
&= \lVert a \rVert^2 - \lVert b \rVert^2.
\end{aligned}
$$

Therefore, we have $$\langle u+v-2w, v-u \rangle = \lVert u-w \rVert^2 - \lVert v-w \rVert^2 = 0$$,
so $$u+v-2w$$ is orthogonal to $$v-u$$. Furthermore,

$$
\begin{aligned}
m-\frac{1}{2}(u+v-2w) &= \frac{u+v}{2} - \frac{u+v}{2} + w\\ 
&= w,
\end{aligned}
$$

so $$w \in m+\text{span}(v-u)^\bot$$, and thus, $$m+\text{span}(v-u)^\bot = A$$.

<figure>
    <img src="/assets/rhombus.svg">
    <figcaption markdown="span">
    Forming a rhombus with $$u$$, $$v$$, and $$w$$.
    </figcaption>
</figure>