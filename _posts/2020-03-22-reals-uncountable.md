---
layout: post
title: Uncountability of the reals through nested intervals
---

From Ebbinghaus, Flum, and Thomas' *Mathematical Logic*, chapter 2, exercise 1.3:

> Let $$\alpha : \mathbb{N} \to \mathbb{R}$$ be given. For $$a, b \in \mathbb{R}$$ such that 
> $$a < b$$ show that there is a point $$c$$ in the closed interval $$I = [a,b]$$ such that 
> $$c \notin \{\alpha(n) : n \in \mathbb{N}\}$$. Conclude from this that $$I$$, and hence 
> $$\mathbb{R}$$ also, are uncountable. (Hint: By induction define a sequence $$I = I_0 \supset I_1 \supset \dots $$
> of closed intervals such that $$\alpha(n) \notin I_{n+1}$$ and use the fact that 
> $$\bigcap_{n \in \mathbb{N}} I_n \ne \varnothing$$.)

Define $$I_0 = [a,b]$$. For any $$n \geq 0$$, if $$I_n = [a_n, b_n]$$, let $$m = \frac{a_n+b_n}{2}$$ and define 

$$
I_{n+1} = \begin{cases}
    [a_n, m] & \text{if } \alpha(n) > m \\
    [m, b_n] & \text{if } \alpha(n) < m \\
    [a_n, \frac{a_n+m}{2}] & \text{if } \alpha(n) = m \\
\end{cases}
$$

For any $$n \geq 0$$, we can see that for any value of $$\alpha(n)$$, we have 
$$\alpha(n) \notin I_{n+1}$$, so $$\alpha(n) \notin \bigcap_{k\in\mathbb{N}} I_k$$
Therefore, if $$c \in \bigcap_{n\in\mathbb{N}} I_n$$, then $$c \neq \alpha(n)$$ for any $$n \in \mathbb{N}$$.

As $$a < b$$, we have that $$\bigcap_{n\leq0} I_n = I_0 = [a, b] \ne \varnothing$$. Let $$k \in \mathbb{N}$$, 
and suppose $$\bigcap_{n \leq k} I_n = I_k \neq \varnothing$$. For any value of $$\alpha(k)$$, we have that $$I_{k+1} \neq \varnothing$$.
Additionaly, we have $$I_{k+1} \subset I_k = \bigcap_{n \leq k} I_n$$, so

$$\bigcap_{n \leq k+1} I_n = \left(\bigcap_{n \leq k} I_n \right) \cap I_{k+1} = I_{k+1} \ne \varnothing,$$ 

which gives us $$\bigcap_{n\in\mathbb{N}} I_n \neq \varnothing$$.
Hence, there is some $$c \in \bigcap_{n\in\mathbb{N}} I_n$$, and 
for this $$c$$, we have $$c \in I_0=[a,b]$$ (and $$c \in \mathbb{R}$$) and $$c \neq \alpha(n)$$ for any $$n \in \mathbb{N}$$,
so for any given $$\alpha$$, then $$\alpha$$ is not surjective onto $$[a,b]$$ (and $$\mathbb{R}$$).
Therefore, $$[a,b]$$ (and $$\mathbb{R}$$) is not countable.
