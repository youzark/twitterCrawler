#!/usr/bin/env python
def funcLogger(origFunc):
    from functools import wraps
    import logging
    from os.path import expanduser
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    fileHandler = logging.FileHandler(expanduser(f"~/Computer/crawler/twitter/log/{origFunc.__name__}.log"))
    formatter = logging.Formatter(f"%(asctime)s-%(levelname)s:%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    @wraps(origFunc)
    def wrapper(*args, **kwargs):
        logger.info(
                f'func: {origFunc.__name__} args: {args} kwargs: {kwargs}'
                )
        return origFunc(*args,*kwargs)
    return wrapper

def threadLogger(origFunc):
    from functools import wraps
    import logging
    from os.path import expanduser
    import threading
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    fileHandler = logging.FileHandler(expanduser(f"~/Computer/crawler/twitter/log/{origFunc.__name__}.log"))
    formatter = logging.Formatter(f"%(asctime)s-%(levelname)s:%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    @wraps(origFunc)
    def wrapper(*args, **kwargs):
        logger.info(
                f'func:{origFunc.__name__} args: {args} kwargs: {kwargs} thread:{threading.current_thread().name}'
                )
        return origFunc(*args,*kwargs)
    return wrapper
