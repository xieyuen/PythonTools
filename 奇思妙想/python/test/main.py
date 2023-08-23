from mymodule.api.logger import logger
from mymodule.api.exceptions import Finish

from t1 import funcs
from t2 import funcs


try:
    funcs['Hello World']()
    funcs['p']()
    print(funcs['add'](1, 12))
    raise Finish
except Finish:
    logger.catch_exc('Run Finished')
except BaseException as e:
    logger.catch_exc('出现了意外的异常')
    logger.catch_exc("下面为异常信息")
    logger.catch_exc(e)
