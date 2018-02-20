import os

__version__ = '1.0'


def version(libname):
    """
    Returns library version
    """
    try:
        _module =  __import__(str(libname))
    except ImportError:
        return None
    if hasattr(_module, '__version__'):
        return _module.__version__
    else:
        return None

def get_dir(libname):
    """
    Returns absolute path of the library directory
    """
    try:
        _module = __import__(str(libname))
    except ImportError:
        return None
    if getattr(_module, '__file__', None):
        return os.path.dirname(_module.__file__)
    else:
        return None

def get_path(libname):
    """
    Returns absolute path of the library
    """
    try:
        _module = __import__(str(libname))
    except ImportError:
        return None
    if hasattr(_module, '__file__'):
        return _module.__file__ 
    else:
        return None

