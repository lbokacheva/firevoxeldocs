=============================
Dynamic Contrast-Enhanced MRI
=============================

.. |br| raw:: html

    <br />

.. contents::
   :depth: 1
   :local:
   :backlinks: none

Dynamic contrast-enhanced MRI (DCE MRI) is performed
after a bolus injection of gadolinium-based contrast agent (GBCA),
followed by acquisition of T1-weighted images
as the contrast exchanges between the blood vessels
and extracellular, extravascular space (EES) (:numref:`ContrastExchange`).

   .. _ContrastExchange:
   .. figure:: ../images/Contrast_Exchange.png
      :alt: Compartments in MRI voxel include plasma in vessels and EES.
      :align: center
      :scale: 70 %
      :figwidth: 80 %
      :figclass: align-center

      Compartments inside MRI voxel include plasma in vessels and EES.


Area under the curve (AUC)
--------------------------

Area under the curve - info

Upslope of enhancement
----------------------

Upslope of enhancement - info

Tofts Model
-----------

DCE-MRI data are often analyzed with the extended
Tofts model [Tofts1999]_ that predicts
the concentration-time curve in the tissue of interest,
:math:`C_t(t)` :eq:`tofts`:

.. math::
   :label: tofts

   C_t(t) &= v_p C_p(t)\! +
             K^{trans} \int_{0}^{t} C_p(\tau) e^{-k_{ep}(t-\tau)} d\tau

where :math:`C_p(t)` is the arterial input function (AIF).
The model parameters are
the vascular volume fraction :math:`v_p`,
the transfer constant :math:`K^{trans}`
and the rate constant :math:`k_{ep} = K^{trans}/v_e`,
where :math:`v_e` is the fractional volume
of extracellular extravascular space (EES).
In general, :math:`K^{trans}` reflects
a combination of tissue perfusion and vascular permeability.

Reference Region Model
----------------------

Reference region models (RRMs)
can quantify tissue perfusion in DCE MRI
without an AIF [Yankeelov2007]_.


.. [Tofts1999] Tofts PS, Brix G, Buckley DL, et al.
           Estimating kinetic parameters from dynamic contrast-enhanced
           T(1)-weighted MRI of a diffusable tracer: standardized quantities
           and symbols. J Magn Reson Imaging. 1999; 10(3):223-32.
           `PMID: 10508281 <https://www.ncbi.nlm.nih.gov/pubmed/10508281>`_

.. [Yankeelov2007] Yankeelov TE, Cron GO, Addison CL, et al.
                   Comparison of a reference region model
                   with direct measurement of an AIF in the analysis of DCE-MRI data.
                   Magn Reson Med. 2007;57(2):353-61.
                   `PMID: 17260371 <https://www.ncbi.nlm.nih.gov/pubmed/17260371>`_
