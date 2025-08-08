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

数据处理
~~~~~~~~~~~~

.. autofunction:: pythontools.modeling.__init__.remove
.. autofunction:: pythontools.modeling.__init__.remove_na

标准化

.. autoclass:: pythontools.modeling.normalization.Normalizer
.. autoclass:: pythontools.modeling.normalization.ZScoreNormalizer
.. autoclass:: pythontools.modeling.normalization.ZScoreScaler
.. autoclass:: pythontools.modeling.normalization.StandardScaler
.. autoclass:: pythontools.modeling.normalization.MinMaxNormalizer
.. autoclass:: pythontools.modeling.normalization.MinMaxScaler

统计量计算
~~~~~~~~~~

.. autofunction:: pythontools.modeling.__init__.corr
.. autofunction:: pythontools.modeling.__init__.related_r
.. autofunction:: pythontools.modeling.__init__.r_squared
.. autofunction:: pythontools.modeling.__init__.adjusted_r_squared
.. autofunction:: pythontools.modeling.__init__.p_values
