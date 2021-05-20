======================================================
 Uncountability of the reals through nested intervals
======================================================
:slug: reals-uncountable

From Ebbinghaus, Flum, and Thomas' *Mathematical Logic*, chapter 2, exercise 1.3:

  Let :math:`\alpha : \mathbb{N} \to \mathbb{R}` be given. For :math:`a, b \in \mathbb{R}`
  such that :math:`a < b` show that there is a point :math:`c` in the closed interval
  :math:`I = [a,b]` such that :math:`c \notin \{\alpha(n) : n \in \mathbb{N}\}`.
  Conclude from this that :math:`I`, and hence  :math:`\mathbb{R}` also, are uncountable.
  (Hint: By induction define a sequence :math:`I = I_0 \supset I_1 \supset \dots`
  of closed intervals such that :math:`\alpha(n) \notin I_{n+1}` and use the fact that 
  :math:`\bigcap_{n \in \mathbb{N}} I_n \ne \varnothing`.)

Define :math:`I_0 = [a,b]`. For any :math:`n \geq 0`, if :math:`I_n = [a_n, b_n]`,
let :math:`m = \frac{a_n+b_n}{2}` and define 

.. math::
   I_{n+1} = \begin{cases}
   [a_n, m] & \text{if } \alpha(n) > m \\
   [m, b_n] & \text{if } \alpha(n) < m \\
   [a_n, \frac{a_n+m}{2}] & \text{if } \alpha(n) = m \\
   \end{cases}

For any :math:`n \geq 0`, we can see that for any value of :math:`\alpha(n)`, we have 
:math:`\alpha(n) \notin I_{n+1}`, so :math:`\alpha(n) \notin \bigcap_{k\in\mathbb{N}} I_k`
Therefore, if :math:`c \in \bigcap_{n\in\mathbb{N}} I_n`, then :math:`c \neq \alpha(n)`
for any :math:`n \in \mathbb{N}`.

As :math:`\bigcap_{n\in\mathbb{N}} I_n \neq \varnothing` there is some
:math:`c \in \bigcap_{n\in\mathbb{N}} I_n`, and for this :math:`c`, we have
:math:`c \in I_0=[a,b]` (and :math:`c \in \mathbb{R}`) and :math:`c \neq \alpha(n)`
for any :math:`n \in \mathbb{N}`, so for any given :math:`\alpha`, then :math:`\alpha`
is not surjective onto :math:`[a,b]` (and :math:`\mathbb{R}`).
Therefore, :math:`[a,b]` (and :math:`\mathbb{R}`) is not countable.
