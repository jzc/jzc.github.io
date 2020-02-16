---
layout: post
title: Polynomial interpolation 
---

From Axler's *Linear Algebra Done Right*, chapter 4, exercise 5:

> Suppose $$m$$ is a nonnegative integer, $$z_1, \dots, z_{m+1}$$ are distinct elements of 
> $$\mathbb{F}$$, and $$w_1, \dots, w_{m+1} \in \mathbb{F}$$. Prove that there exists a unique polynomial
> $$p \in \mathcal{P}_m(\mathbb{F})$$ such that 
> $$
p(z_j) = w_j
> $$
> for $$j = 1, \dots, m+1$$
>
> [*This result can be proved without using linear algebra. However, try to
> find the clearer, shorter proof that uses some linear algebra.*]

If $$p \ne 0$$ then as $$p$$ is at most degree $$m$$, there are at most $$m$$ 
distinct $$z$$'s such that $$p(z)=0$$. Equivalently, if $$p$$ had at least $$m+1$$ distinct 
$$z$$'s such that $$p(z)=0$$, then $$p=0$$. Letting 

$$
Z = 
\begin{bmatrix}
    1 & z_1 & z_1^2 & \dots & z_1^m \\
    1 & z_2 & z_2^2 & \dots & z_2^m \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    1 & z_{m+1} & z_{m+1}^2 & \dots & z_{m+1}^m \\
\end{bmatrix}
$$

then the previous statement implies that $$\text{null } Z = \{0\}$$, 
so $$Z$$ is injective. As $$Z$$ is square, [Axler 3.69] implies that 
$$Z$$ is invertible. Hence, if

$$
\begin{aligned}
Z^{-1}\left(\begin{bmatrix} w_1 \\ w_2 \\ \vdots \\ w_{m+1}\end{bmatrix}\right) = \begin{bmatrix} a_0 \\ a_1 \\ \vdots \\ a_{m}\end{bmatrix}
\end{aligned}
$$

then the polynomial $$p(z)=a_0 + a_1 z + a_2 z^2 + \dots + a_m z^m$$ is the unique
polynomial such that $$p(z_j) = w_j$$ for $$j = 1, \dots, m+1$$.