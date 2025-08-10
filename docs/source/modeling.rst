modeling
===========

数学建模的工具

依赖
------

- numpy
- scipy
- pandas

导入
------

.. code-block:: python

   from pythontools.modeling import *

用法
-----

.. currentmodule:: pythontools.modeling.__init__

统计量计算
~~~~~~~~~~

.. autofunction:: corr
.. autofunction:: related_r
.. autofunction:: r_squared
.. autofunction:: adjusted_r_squared
.. autofunction:: p_values

数据处理
~~~~~~~~~~~~

.. autofunction:: remove
.. autofunction:: remove_na

标准化
^^^^^^^^^^^

.. currentmodule:: pythontools.modeling.normalization

.. autoclass:: Normalizer
.. autoproperty:: Normalizer.max
.. autoproperty:: Normalizer.min
.. autoproperty:: Normalizer.mean
.. autoproperty:: Normalizer.std
.. autoproperty:: Normalizer.range
.. automethod:: Normalizer.__init__
.. automethod:: Normalizer.normalize
.. automethod:: Normalizer.denormalize

.. autoclass:: ZScoreNormalizer
.. automethod:: ZScoreNormalizer.normalize
.. automethod:: ZScoreNormalizer.denormalize

.. autoclass:: ZScoreScaler
.. autoclass:: StandardScaler

.. autoclass:: MinMaxNormalizer
.. autoproperty:: MinMaxNormalizer.target
.. automethod:: MinMaxNormalizer.__init__
.. automethod:: MinMaxNormalizer.normalize
.. automethod:: MinMaxNormalizer.denormalize
.. automethod:: MinMaxNormalizer.set_target_range

.. autoclass:: MinMaxScaler
