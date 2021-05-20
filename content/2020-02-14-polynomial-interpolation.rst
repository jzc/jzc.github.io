Polynomial interpolation
------------------------
:slug: polynomial-interpolation

From Axler's *Linear Algebra Done Right*, chapter 4, exercise 5:

  Suppose :math:`m` is a nonnegative integer, :math:`z_1, \dots, z_{m+1}` are distinct elements of
  :math:`\mathbb{F}`, and :math:`w_1, \dots, w_{m+1} \in \mathbb{F}`.
  Prove that there exists a unique polynomial :math:`p \in \mathcal{P}_m(\mathbb{F})`
  such that :math:`p(z_j) = w_j` for :math:`j = 1, \dots, m+1`
 
  [*This result can be proved without using linear algebra. However, try to
  find the clearer, shorter proof that uses some linear algebra.*]

If :math:`p \ne 0` then as :math:`p` is at most degree :math:`m`,
there are at most :math:`m` distinct :math:`z`'s such that :math:`p(z)=0`.
Equivalently, if :math:`p` had at least :math:`m+1` distinct 
:math:`z`'s such that :math:`p(z)=0`, then :math:`p=0`. Letting 

.. math::
   Z = 
   \begin{bmatrix}
   1 & z_1 & z_1^2 & \dots & z_1^m \\
   1 & z_2 & z_2^2 & \dots & z_2^m \\
   \vdots & \vdots & \vdots & \ddots & \vdots \\
   1 & z_{m+1} & z_{m+1}^2 & \dots & z_{m+1}^m \\
   \end{bmatrix}

then the previous statement implies that :math:`\text{null } Z = \{0\}`, 
so :math:`Z` is injective. As :math:`Z` is square, [Axler 3.69] implies that 
:math:`Z` is invertible. Hence, if

.. math::
   \begin{aligned}
   Z^{-1}\left(\begin{bmatrix} w_1 \\ w_2 \\ \vdots \\ w_{m+1}\end{bmatrix}\right)
   = \begin{bmatrix} a_0 \\ a_1 \\ \vdots \\ a_{m}\end{bmatrix}
   \end{aligned}

then the polynomial :math:`p(z)=a_0 + a_1 z + a_2 z^2 + \dots + a_m z^m` is the unique
polynomial such that :math:`p(z_j) = w_j` for :math:`j = 1, \dots, m+1`.
