# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_example')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_example')
    _example = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_example', [dirname(__file__)])
        except ImportError:
            import _example
            return _example
        try:
            _mod = imp.load_module('_example', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _example = swig_import_helper()
    del swig_import_helper
else:
    import _example
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _example.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _example.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _example.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _example.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _example.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _example.SwigPyIterator_equal(self, x)

    def copy(self):
        return _example.SwigPyIterator_copy(self)

    def next(self):
        return _example.SwigPyIterator_next(self)

    def __next__(self):
        return _example.SwigPyIterator___next__(self)

    def previous(self):
        return _example.SwigPyIterator_previous(self)

    def advance(self, n):
        return _example.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _example.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _example.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _example.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _example.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _example.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _example.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _example.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _example.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _example.IntVector___nonzero__(self)

    def __bool__(self):
        return _example.IntVector___bool__(self)

    def __len__(self):
        return _example.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _example.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _example.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _example.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _example.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _example.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _example.IntVector___setitem__(self, *args)

    def pop(self):
        return _example.IntVector_pop(self)

    def append(self, x):
        return _example.IntVector_append(self, x)

    def empty(self):
        return _example.IntVector_empty(self)

    def size(self):
        return _example.IntVector_size(self)

    def swap(self, v):
        return _example.IntVector_swap(self, v)

    def begin(self):
        return _example.IntVector_begin(self)

    def end(self):
        return _example.IntVector_end(self)

    def rbegin(self):
        return _example.IntVector_rbegin(self)

    def rend(self):
        return _example.IntVector_rend(self)

    def clear(self):
        return _example.IntVector_clear(self)

    def get_allocator(self):
        return _example.IntVector_get_allocator(self)

    def pop_back(self):
        return _example.IntVector_pop_back(self)

    def erase(self, *args):
        return _example.IntVector_erase(self, *args)

    def __init__(self, *args):
        this = _example.new_IntVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _example.IntVector_push_back(self, x)

    def front(self):
        return _example.IntVector_front(self)

    def back(self):
        return _example.IntVector_back(self)

    def assign(self, n, x):
        return _example.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _example.IntVector_resize(self, *args)

    def insert(self, *args):
        return _example.IntVector_insert(self, *args)

    def reserve(self, n):
        return _example.IntVector_reserve(self, n)

    def capacity(self):
        return _example.IntVector_capacity(self)
    __swig_destroy__ = _example.delete_IntVector
    __del__ = lambda self: None
IntVector_swigregister = _example.IntVector_swigregister
IntVector_swigregister(IntVector)

class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _example.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _example.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _example.DoubleVector___bool__(self)

    def __len__(self):
        return _example.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _example.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _example.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _example.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _example.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _example.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _example.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _example.DoubleVector_pop(self)

    def append(self, x):
        return _example.DoubleVector_append(self, x)

    def empty(self):
        return _example.DoubleVector_empty(self)

    def size(self):
        return _example.DoubleVector_size(self)

    def swap(self, v):
        return _example.DoubleVector_swap(self, v)

    def begin(self):
        return _example.DoubleVector_begin(self)

    def end(self):
        return _example.DoubleVector_end(self)

    def rbegin(self):
        return _example.DoubleVector_rbegin(self)

    def rend(self):
        return _example.DoubleVector_rend(self)

    def clear(self):
        return _example.DoubleVector_clear(self)

    def get_allocator(self):
        return _example.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _example.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _example.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        this = _example.new_DoubleVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _example.DoubleVector_push_back(self, x)

    def front(self):
        return _example.DoubleVector_front(self)

    def back(self):
        return _example.DoubleVector_back(self)

    def assign(self, n, x):
        return _example.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _example.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _example.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _example.DoubleVector_reserve(self, n)

    def capacity(self):
        return _example.DoubleVector_capacity(self)
    __swig_destroy__ = _example.delete_DoubleVector
    __del__ = lambda self: None
DoubleVector_swigregister = _example.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)

class IntVector2(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector2, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _example.IntVector2_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _example.IntVector2___nonzero__(self)

    def __bool__(self):
        return _example.IntVector2___bool__(self)

    def __len__(self):
        return _example.IntVector2___len__(self)

    def __getslice__(self, i, j):
        return _example.IntVector2___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _example.IntVector2___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _example.IntVector2___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _example.IntVector2___delitem__(self, *args)

    def __getitem__(self, *args):
        return _example.IntVector2___getitem__(self, *args)

    def __setitem__(self, *args):
        return _example.IntVector2___setitem__(self, *args)

    def pop(self):
        return _example.IntVector2_pop(self)

    def append(self, x):
        return _example.IntVector2_append(self, x)

    def empty(self):
        return _example.IntVector2_empty(self)

    def size(self):
        return _example.IntVector2_size(self)

    def swap(self, v):
        return _example.IntVector2_swap(self, v)

    def begin(self):
        return _example.IntVector2_begin(self)

    def end(self):
        return _example.IntVector2_end(self)

    def rbegin(self):
        return _example.IntVector2_rbegin(self)

    def rend(self):
        return _example.IntVector2_rend(self)

    def clear(self):
        return _example.IntVector2_clear(self)

    def get_allocator(self):
        return _example.IntVector2_get_allocator(self)

    def pop_back(self):
        return _example.IntVector2_pop_back(self)

    def erase(self, *args):
        return _example.IntVector2_erase(self, *args)

    def __init__(self, *args):
        this = _example.new_IntVector2(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _example.IntVector2_push_back(self, x)

    def front(self):
        return _example.IntVector2_front(self)

    def back(self):
        return _example.IntVector2_back(self)

    def assign(self, n, x):
        return _example.IntVector2_assign(self, n, x)

    def resize(self, *args):
        return _example.IntVector2_resize(self, *args)

    def insert(self, *args):
        return _example.IntVector2_insert(self, *args)

    def reserve(self, n):
        return _example.IntVector2_reserve(self, n)

    def capacity(self):
        return _example.IntVector2_capacity(self)
    __swig_destroy__ = _example.delete_IntVector2
    __del__ = lambda self: None
IntVector2_swigregister = _example.IntVector2_swigregister
IntVector2_swigregister(IntVector2)


def average(v):
    return _example.average(v)
average = _example.average

def half(v):
    return _example.half(v)
half = _example.half

def halve_in_place(v):
    return _example.halve_in_place(v)
halve_in_place = _example.halve_in_place

def reshape_2d(x1d, N):
    return _example.reshape_2d(x1d, N)
reshape_2d = _example.reshape_2d

def averagePair(v1, v2):
    return _example.averagePair(v1, v2)
averagePair = _example.averagePair
# This file is compatible with both classic and new-style classes.


