---
layout: post
title: Partitions, equivalence relations, and surjections 
---

Let $$X$$ be a set and $$P$$ be a collections of subsets of $$X$$. If for all $$A, B \in P$$,

1. Every set in $$P$$ is nonempty: $$A \ne \varnothing$$
2. The union of all the sets in $$P$$ is equal to $$X$$: $$\bigcup_{A_i \in P} A_i = X$$
3. The sets of $$P$$ are pairwise disjoint: $$A \ne B \implies A \cap B = \varnothing$$

then we call $$P$$ a partition of $$X$$. From this definition, we can see that 
each element in $$X$$ lies in exactly one set from $$P$$.

Let $$\sim$$ be a relation on $$X$$. If for all $$a, b, c \in X$$,

1. If $$a \sim a$$, then we say $$\sim$$ is *reflexive*.
2. If $$a \sim b$$ implies $$b \sim a$$, then we say $$\sim$$ is *symmetric*.
3. If $$a \sim b$$ and $$b \sim c$$ implies $$a \sim c$$, then we say $$\sim$$ is *transitive*.

If $$\sim$$ is reflexive, symmetric, and transitive, then we say $$\sim$$ is an *equivalence relation*.

### **Claim:** Every partition generates an equivalence relation.

*Proof.* Let $$P$$ be a partition. Let $$a, b, c \in X$$. Condition (2) of the partition definition 
implies that there are sets $$A, B, C \in P$$ such that $$a \in A, b \in B, c \in C$$. We will 
define $$a \sim_P b$$ if $$a$$ lies in the same set of $$P$$ that $$b$$ is in, i.e.
$$a \sim_P b$$ iff $$a \in B$$.

As $$a \in A$$, we have $$a \sim_P a$$, so $$\sim_P$$ is reflexive.
If $$a \sim_P b$$, then $$a \in B$$, so $$A \cap B \ne \varnothing$$. 
By condition (3) of the partition defintion, we must have $$A = B$$ and therefore $$b \sim_P a$$,
so $$\sim_P$$ is symmetric.
If $$ a \sim_P b$$ and $$b \sim_P c$$, then by a similar argument,
we have $$A = B$$ and $$B = C$$, so $$A = C$$. Therefore, we 
have $$a \in C$$ so $$a \sim_P c$$ and thus $$\sim_P$$ is transitive.

### **Claim:** Every equivalence relation generates a partition.

*Proof.* Let $$\sim$$ be an equivalence relation on $$X$$. For $$x \in X$$, define 
the *equivalence class of $$x$$* as 

$$[x] = \{y \in X : y \sim x \}$$

We have that $$x \in [x]$$ as $$x \sim x$$ by reflexivity of $$\sim$$, so each equivalence class is nonempty. 
This also implies that every element in $$X$$ is in some equivalence class, 
namely the one formed by itself. For $$y \in X$$, if $$[x] \cap [y] \ne \varnothing$$,
then there is a $$z \in [x] \cap [y]$$, so $$z \sim x$$ and $$z \sim y$$ and 
$$x \sim y$$ by symmetry and transitivity of $$\sim$$.

