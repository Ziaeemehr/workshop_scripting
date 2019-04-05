# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_example', [dirname(__file__)])
        except ImportError:
            import _example
            return _example
        if fp is not None:
            try:
                _mod = imp.load_module('_example', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _example = swig_import_helper()
    del swig_import_helper
else:
    import _example
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


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


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
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
        except Exception:
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

class ComplexVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ComplexVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ComplexVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _example.ComplexVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _example.ComplexVector___nonzero__(self)

    def __bool__(self):
        return _example.ComplexVector___bool__(self)

    def __len__(self):
        return _example.ComplexVector___len__(self)

    def __getslice__(self, i, j):
        return _example.ComplexVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _example.ComplexVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _example.ComplexVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _example.ComplexVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _example.ComplexVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _example.ComplexVector___setitem__(self, *args)

    def pop(self):
        return _example.ComplexVector_pop(self)

    def append(self, x):
        return _example.ComplexVector_append(self, x)

    def empty(self):
        return _example.ComplexVector_empty(self)

    def size(self):
        return _example.ComplexVector_size(self)

    def swap(self, v):
        return _example.ComplexVector_swap(self, v)

    def begin(self):
        return _example.ComplexVector_begin(self)

    def end(self):
        return _example.ComplexVector_end(self)

    def rbegin(self):
        return _example.ComplexVector_rbegin(self)

    def rend(self):
        return _example.ComplexVector_rend(self)

    def clear(self):
        return _example.ComplexVector_clear(self)

    def get_allocator(self):
        return _example.ComplexVector_get_allocator(self)

    def pop_back(self):
        return _example.ComplexVector_pop_back(self)

    def erase(self, *args):
        return _example.ComplexVector_erase(self, *args)

    def __init__(self, *args):
        this = _example.new_ComplexVector(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _example.ComplexVector_push_back(self, x)

    def front(self):
        return _example.ComplexVector_front(self)

    def back(self):
        return _example.ComplexVector_back(self)

    def assign(self, n, x):
        return _example.ComplexVector_assign(self, n, x)

    def resize(self, *args):
        return _example.ComplexVector_resize(self, *args)

    def insert(self, *args):
        return _example.ComplexVector_insert(self, *args)

    def reserve(self, n):
        return _example.ComplexVector_reserve(self, n)

    def capacity(self):
        return _example.ComplexVector_capacity(self)
    __swig_destroy__ = _example.delete_ComplexVector
    __del__ = lambda self: None
ComplexVector_swigregister = _example.ComplexVector_swigregister
ComplexVector_swigregister(ComplexVector)

class ComplexVector2(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ComplexVector2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ComplexVector2, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _example.ComplexVector2_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _example.ComplexVector2___nonzero__(self)

    def __bool__(self):
        return _example.ComplexVector2___bool__(self)

    def __len__(self):
        return _example.ComplexVector2___len__(self)

    def __getslice__(self, i, j):
        return _example.ComplexVector2___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _example.ComplexVector2___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _example.ComplexVector2___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _example.ComplexVector2___delitem__(self, *args)

    def __getitem__(self, *args):
        return _example.ComplexVector2___getitem__(self, *args)

    def __setitem__(self, *args):
        return _example.ComplexVector2___setitem__(self, *args)

    def pop(self):
        return _example.ComplexVector2_pop(self)

    def append(self, x):
        return _example.ComplexVector2_append(self, x)

    def empty(self):
        return _example.ComplexVector2_empty(self)

    def size(self):
        return _example.ComplexVector2_size(self)

    def swap(self, v):
        return _example.ComplexVector2_swap(self, v)

    def begin(self):
        return _example.ComplexVector2_begin(self)

    def end(self):
        return _example.ComplexVector2_end(self)

    def rbegin(self):
        return _example.ComplexVector2_rbegin(self)

    def rend(self):
        return _example.ComplexVector2_rend(self)

    def clear(self):
        return _example.ComplexVector2_clear(self)

    def get_allocator(self):
        return _example.ComplexVector2_get_allocator(self)

    def pop_back(self):
        return _example.ComplexVector2_pop_back(self)

    def erase(self, *args):
        return _example.ComplexVector2_erase(self, *args)

    def __init__(self, *args):
        this = _example.new_ComplexVector2(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _example.ComplexVector2_push_back(self, x)

    def front(self):
        return _example.ComplexVector2_front(self)

    def back(self):
        return _example.ComplexVector2_back(self)

    def assign(self, n, x):
        return _example.ComplexVector2_assign(self, n, x)

    def resize(self, *args):
        return _example.ComplexVector2_resize(self, *args)

    def insert(self, *args):
        return _example.ComplexVector2_insert(self, *args)

    def reserve(self, n):
        return _example.ComplexVector2_reserve(self, n)

    def capacity(self):
        return _example.ComplexVector2_capacity(self)
    __swig_destroy__ = _example.delete_ComplexVector2
    __del__ = lambda self: None
ComplexVector2_swigregister = _example.ComplexVector2_swigregister
ComplexVector2_swigregister(ComplexVector2)

class my_class(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, my_class, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, my_class, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _example.new_my_class()
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def set_value(self, a, arg3):
        return _example.my_class_set_value(self, a, arg3)

    def half(self, arg2):
        return _example.my_class_half(self, arg2)

    def half2(self, arg2):
        return _example.my_class_half2(self, arg2)

    def print_value(self):
        return _example.my_class_print_value(self)
    __swig_destroy__ = _example.delete_my_class
    __del__ = lambda self: None
my_class_swigregister = _example.my_class_swigregister
my_class_swigregister(my_class)

# This file is compatible with both classic and new-style classes.


