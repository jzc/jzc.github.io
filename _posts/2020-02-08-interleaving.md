---
layout: post
title: Regular languages are closed under interleaving
---

Let $$\otimes$$ be an operation recursively defined on strings of the 
same length such that 

$$
\begin{aligned}
\epsilon \otimes \epsilon &= \epsilon\\
xa \otimes yb &= (x \otimes y)ab
\end{aligned}
$$

so that the action of $$\otimes$$ on two strings "interleaves" the two strings.
For example, $$ab \otimes 12 = a1b2$$.

Similarly, for languages $$A, B \subseteq \Sigma^*$$, let 

$$
A \otimes B = \{ x \otimes y : x \in A, y \in B, |x|=|y|\}
$$

be the set of all string obtained from interleaving a string in A with a string in B. 
Note that $$\otimes$$ is bijective, so each string in $$A \otimes B$$ is uniquely 
defined by its operands.

### **Proposition:** If $$A$$ and $$B$$ are regular, then $$A \otimes B$$ is regular.

*Proof.* As $$A$$ and $$B$$ are regular, let $$M_A = (Q_A, \Sigma, \delta_A, s_A, F_A)$$
and $$M_B = (Q_b, \Sigma, \delta_B, s_B, F_B)$$ be DFAs such that 
$$L(M_A)=A$$ and $$L(M_B)=B$$. Define the DFA 

$$N=(Q_A \times Q_B \times \{L, R\}, \Sigma, \delta_N, (s_A, s_B, L), F_A \times F_B \times \{L\})$$  

where $$\delta_N$$ is defined as follows:

$$
\begin{aligned}
\delta_N((q_A, q_B, L), a) &= (\delta_A(q_A, a), q_B, R)\\
\delta_N((q_A, q_B, R), a) &= (q_A, \delta_A(q_B, a), L)
\end{aligned}
$$

We want to show that $$L(N)=A \otimes B$$. First, we prove the lemma

$$\hat{\delta_N}((s_A, s_B, L), x \otimes y) = (\hat{\delta_A}(s_A, x), \hat{\delta_B}(s_B, y), L)$$

for all $$x,y \in \Sigma^*$$ such that 
$$ |x| = |y| $$ by induction.

*Basis.* We have

$$
\hat{\delta_N}((q_A,q_B,L), \epsilon) = (q_A,q_B,L) = (\hat{\delta_A}(q_A, \epsilon), \hat{\delta_B}(q_B, \epsilon), L),
$$

so the induction hypothesis holds for $$\epsilon$$.

*Induction step.* Suppose the induction hypothesis (I.H.) holds for some
$$x, y \in \Sigma^*$$ with $$|x|=|y|$$. For $$a, b \in \Sigma$$, we have

$$
\begin{aligned}
    \hat{\delta_N}((q_A,q_B,L), xa \otimes yb) &= \hat{\delta_N}((q_A,q_B,L), (x \otimes y)ab) & (\text{def of } \otimes)\\
    &= \hat{\delta_N}( \hat{\delta_N}((q_A,q_B,L), x \otimes y), ab) & (\text{def of } \hat{\delta_N})\\
    &= \hat{\delta_N}( (\hat{\delta_A}(s_A, x), \hat{\delta_B}(s_B, y), L), ab) & \text{(I.H.)}\\
    &= \delta_N(\delta_N((\hat{\delta_A}(s_A, x), \hat{\delta_B}(s_B, y), L), a), b) & (\text{def of } \hat{\delta_N}) \\
    &= \delta_N((\delta_A(\hat{\delta_A}(s_A, x), a), \hat{\delta_B}(s_B, y), R), b) & (\text{def of } \delta_N)\\
    &= \delta_N((\hat{\delta_A}(s_A, xa), \hat{\delta_B}(s_B, y), R), b) & (\text{def of } \hat{\delta_N}) \\
    &= (\hat{\delta_A}(s_A, xa), \delta_B(\hat{\delta_B}(s_B, y), b), L) & (\text{def of } \delta_N) \\
    &= (\hat{\delta_A}(s_A, xa), \hat{\delta_B}(s_B, yb), L) & (\text{def of } \hat{\delta_N}), \\
\end{aligned}
$$

so the I.H. for $$x$$ and $$y$$ implies the I.H. for $$xa$$ and $$yb$$.

From the lemma, we have

$$
\begin{aligned}
x \otimes y \in A \otimes B &\iff x \otimes y \in L(M_A) \otimes L(M_B) \\ 
&\iff x \in A \text{ and } y \in B \\
&\iff \hat{\delta_A}(s_A, x) \in F_A \text{ and } \hat{\delta_B}(s_B, y) \in F_B\\
&\iff (\hat{\delta_A}(s_A, x), \hat{\delta_B}(s_B, y), L) \in F_A \times F_B \times \{L\} \\
&\iff \hat{\delta_N}((s_A, s_B, L), x \otimes y) \in F_A \times F_B \times \{L\} \\
&\iff x \otimes y \in L(N)
\end{aligned}
$$

Hence, $$A \otimes B = L(N)$$, so $$A \otimes B$$ is regular.