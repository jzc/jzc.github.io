==========================================
 Equidistant points from a pair of points
==========================================

In the figure below, visually, 
it is not too hard to believe that the points
equidistant from :math:`u` and :math:`v` are exactly the 
the points on the dashed line. A description of the dashed line 
seems to be "the line running perpendicularly through the midpoint 
of the segment between :math:`u` and :math:`v`." This turns out to be 
true, and perhaps is a standard exercise in Euclidean geometry. 
However, we can formulate this using linear algebra and obtain 
a result that generalizes to higher dimensions, yet the
proof is still "strategized" by our visual intuition.
      
.. figure:: {attach}/equidistant-points/line-equidistant.svg

**Theorem.** Let :math:`u` and :math:`v` be two points in :math:`\mathbb{R}^n`.
Let :math:`A \triangleq \{ w \in \mathbb{R}^n : \lVert w-u \rVert = \lVert w-v \rVert\}`
be the set of points equidistant from :math:`u` and :math:`v`,
and let :math:`m \triangleq \dfrac{u+v}{2}` be the midpoint of the segment between
:math:`u` and :math:`v`.
Then, :math:`A` is equal to the the orthogonal complement of the line through 
:math:`u` and :math:`v` plus :math:`m`; i.e.

.. math::
   m + \text{span}(v-u)^\bot = A

*Proof.* Let :math:`m+w \in m + \text{span}(v-u)^\bot`, so that :math:`\langle w, v-u \rangle = 0`.
Note that :math:`w` and :math:`m-u` are orthogonal, as

.. math::
   \begin{aligned}
   \left\langle w, m-u \right\rangle &= \left\langle w, -\frac{u}{2}+\frac{v}{2} \right\rangle \\
   &= \frac{1}{2} \langle w, v-u \rangle \\
   &= 0.
   \end{aligned}

Similarly, :math:`w` and :math:`m-v` are orthogonal. As :math:`m-u = -\left(m-v\right)`,
we have :math:`\left\lVert m-u \right\rVert = \left\lVert m-v \right\rVert`. Then, with 
the Pythagorean theorem,

.. math::
   \begin{aligned}
       \left\lVert \left(m+w\right)-u \right\rVert^2
       &= \left\lVert m-u\right\rVert^2+ \lVert w \rVert^2 \\ 
       &= \left\lVert m-v\right\rVert^2+ \lVert w \rVert^2 \\
       &= \left\lVert \left(m+w\right)-v \right\rVert^2,
   \end{aligned}
   
so :math:`m+w` is equidistant from :math:`u` and :math:`v`, and thus, 
:math:`m + \text{span}(v-u)^\bot \subseteq A`.


.. figure:: {attach}/equidistant-points/decomposition.svg

   Decomposition of the distance from :math:`u` [or :math:`v`] to our given
   vector, :math:`m+w`, into orthogonal parts.

Conversely, suppose :math:`w \in A`, so that :math:`\lVert w-u \rVert = \lVert v-u \rVert`.
We can form a rhombus using :math:`w`, :math:`u`, and :math:`v` so that the diagonals 
of this rhombus are :math:`(u-w)+(v-w)=u+v-2w` and :math:`(u-w)-(v-w)=v-u`. Note 
that for any :math:`a` and :math:`b`, we have 

.. math::
   \begin{aligned}
   \langle a+b, a-b \rangle
   &= \langle a, a \rangle - \langle a, b \rangle + \langle b, a \rangle - \langle b, b \rangle \\
   &= \lVert a \rVert^2 - \lVert b \rVert^2.
   \end{aligned}
   

Therefore, we have
:math:`\langle u+v-2w, v-u \rangle = \lVert u-w \rVert^2 - \lVert v-w \rVert^2 = 0`,
so :math:`u+v-2w` is orthogonal to :math:`v-u`. Furthermore,

.. math::
   \begin{aligned}
   m-\frac{1}{2}(u+v-2w)
   &= \frac{u+v}{2} - \frac{u+v}{2} + w\\ 
   &= w,
   \end{aligned}
   
so :math:`w \in m+\text{span}(v-u)^\bot`, and thus, :math:`m+\text{span}(v-u)^\bot = A`.

.. figure:: {attach}/equidistant-points/rhombus.svg

   Forming a rhombus with :math:`u`, :math:`v`, and :math:`w`.
