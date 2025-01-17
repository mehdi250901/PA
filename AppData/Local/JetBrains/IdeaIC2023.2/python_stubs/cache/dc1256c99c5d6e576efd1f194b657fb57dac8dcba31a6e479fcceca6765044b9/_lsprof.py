# encoding: utf-8
# module _lsprof
# from (built-in)
# by generator 1.147
""" Fast profiler """
# no imports

# no functions
# classes

class Profiler(object):
    """
    Profiler(timer=None, timeunit=None, subcalls=True, builtins=True)
    
        Builds a profiler object using the specified timer function.
        The default timer is a fast built-in one based on real time.
        For custom timer functions returning integers, timeunit can
        be a float specifying a scale (i.e. how long each integer unit
        is, in seconds).
    """
    def clear(self): # real signature unknown; restored from __doc__
        """
        clear()
        
        Clear all profiling information collected so far.
        """
        pass

    def disable(self): # real signature unknown; restored from __doc__
        """
        disable()
        
        Stop collecting profiling information.
        """
        pass

    def enable(self, subcalls=True, builtins=True): # real signature unknown; restored from __doc__
        """
        enable(subcalls=True, builtins=True)
        
        Start collecting profiling information.
        If 'subcalls' is True, also records for each function
        statistics separated according to its current caller.
        If 'builtins' is True, records the time spent in
        built-in functions separately from their caller.
        """
        pass

    def getstats(self): # real signature unknown; restored from __doc__
        """
        list of profiler_entry objects.
        
        getstats() -> list of profiler_entry objects
        
        Return all information collected by the profiler.
        Each profiler_entry is a tuple-like object with the
        following attributes:
        
            code          code object
            callcount     how many times this was called
            reccallcount  how many times called recursively
            totaltime     total time in this entry
            inlinetime    inline time in this entry (not in subcalls)
            calls         details of the calls
        
        The calls attribute is either None or a list of
        profiler_subentry objects:
        
            code          called code object
            callcount     how many times this is called
            reccallcount  how many times this is called recursively
            totaltime     total time spent in this call
            inlinetime    inline time (not in further subcalls)
        """
        return []

    def __init__(self, timer=None, timeunit=None, subcalls=True, builtins=True): # real signature unknown; restored from __doc__
        pass


class profiler_entry(tuple):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    callcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how many times this was called"""

    calls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """details of the calls"""

    code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """code object or built-in function name"""

    inlinetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """inline time in this entry (not in subcalls)"""

    reccallcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how many times called recursively"""

    totaltime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """total time in this entry"""


    n_fields = 6
    n_sequence_fields = 6
    n_unnamed_fields = 0
    __match_args__ = (
        'code',
        'callcount',
        'reccallcount',
        'totaltime',
        'inlinetime',
        'calls',
    )


class profiler_subentry(tuple):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    callcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how many times this is called"""

    code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """called code object or built-in function name"""

    inlinetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """inline time (not in further subcalls)"""

    reccallcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how many times this is called recursively"""

    totaltime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """total time spent in this call"""


    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0
    __match_args__ = (
        'code',
        'callcount',
        'reccallcount',
        'totaltime',
        'inlinetime',
    )


class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x00000199639C28E0>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x00000199639C2980>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x00000199639C2A20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x00000199639C2AC0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x00000199639C2B60>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x00000199639C2CA0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x00000199639C2DE0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x00000199639C2F20>)>, 'load_module': <classmethod(<function _load_module_shim at 0x00000199639C1C60>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_lsprof', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

