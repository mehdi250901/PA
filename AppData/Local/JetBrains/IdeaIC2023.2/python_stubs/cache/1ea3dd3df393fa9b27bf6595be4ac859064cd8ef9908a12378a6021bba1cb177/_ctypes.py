# encoding: utf-8
# module _ctypes
# from C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\DLLs\_ctypes.pyd
# by generator 1.147
""" Create and manipulate C compatible data types in Python. """
# no imports

# Variables with simple values

FUNCFLAG_CDECL = 1
FUNCFLAG_HRESULT = 2
FUNCFLAG_PYTHONAPI = 4
FUNCFLAG_STDCALL = 0

FUNCFLAG_USE_ERRNO = 8
FUNCFLAG_USE_LASTERROR = 16

RTLD_GLOBAL = 0
RTLD_LOCAL = 0

_cast_addr = 140733168139776

_memmove_addr = 140733168816880

_memset_addr = 140733168818592

_string_at_addr = 140733168140524

_wstring_at_addr = 140733168140616

__version__ = '1.1.0'

# functions

def addressof(C_instance): # real signature unknown; restored from __doc__
    """
    addressof(C instance) -> integer
    Return the address of the C instance internal buffer
    """
    return 0

def alignment(C_type): # real signature unknown; restored from __doc__
    """
    alignment(C type) -> integer
    alignment(C instance) -> integer
    Return the alignment requirements of a C instance
    """
    return 0

def buffer_info(*args, **kwargs): # real signature unknown
    """ Return buffer interface information """
    pass

def byref(C_instance, offset=0): # real signature unknown; restored from __doc__
    """
    byref(C instance[, offset=0]) -> byref-object
    Return a pointer lookalike to a C instance, only usable
    as function argument
    """
    pass

def call_cdeclfunction(*args, **kwargs): # real signature unknown
    pass

def call_function(*args, **kwargs): # real signature unknown
    pass

def CopyComPointer(src, dst): # real signature unknown; restored from __doc__
    """ CopyComPointer(src, dst) -> HRESULT value """
    pass

def FormatError(integer=None): # real signature unknown; restored from __doc__
    """
    FormatError([integer]) -> string
    
    Convert a win32 error code into a string. If the error code is not
    given, the return value of a call to GetLastError() is used.
    """
    return ""

def FreeLibrary(handle): # real signature unknown; restored from __doc__
    """
    FreeLibrary(handle) -> void
    
    Free the handle of an executable previously loaded by LoadLibrary.
    """
    pass

def get_errno(*args, **kwargs): # real signature unknown
    pass

def get_last_error(*args, **kwargs): # real signature unknown
    pass

def LoadLibrary(name, load_flags): # real signature unknown; restored from __doc__
    """
    LoadLibrary(name, load_flags) -> handle
    
    Load an executable (usually a DLL), and return a handle to it.
    The handle may be used to locate exported functions in this
    module. load_flags are as defined for LoadLibraryEx in the
    Windows API.
    """
    pass

def POINTER(*args, **kwargs): # real signature unknown
    pass

def pointer(*args, **kwargs): # real signature unknown
    pass

def PyObj_FromPtr(*args, **kwargs): # real signature unknown
    pass

def Py_DECREF(*args, **kwargs): # real signature unknown
    pass

def Py_INCREF(*args, **kwargs): # real signature unknown
    pass

def resize(*args, **kwargs): # real signature unknown
    """ Resize the memory buffer of a ctypes instance """
    pass

def set_errno(*args, **kwargs): # real signature unknown
    pass

def set_last_error(*args, **kwargs): # real signature unknown
    pass

def sizeof(C_type): # real signature unknown; restored from __doc__
    """
    sizeof(C type) -> integer
    sizeof(C instance) -> integer
    Return the size in bytes of a C instance
    """
    return 0

def _check_HRESULT(*args, **kwargs): # real signature unknown
    pass

def _unpickle(*args, **kwargs): # real signature unknown
    pass

# classes

class ArgumentError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Array(_CData):
    """ XXX to be provided """
    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class CFuncPtr(_CData):
    """ Function Pointer """
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    argtypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """specify the argument types"""

    errcheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """a function to check for errors"""

    restype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """specify the result type"""



class COMError(Exception):
    """ Raised when a COM method call failed. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Structure(_CData):
    """ Structure base class """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Union(_CData):
    """ Union base class """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class _Pointer(_CData):
    """ XXX to be provided """
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    contents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the object this pointer points to (read-write)"""



class _SimpleCData(_CData):
    """ XXX to be provided """
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __ctypes_from_outparam__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """current value"""



# variables with complex values

_pointer_type_cache = {
    None:  # (!) real value is "<class 'ctypes.c_wchar'>"
        None # (!) real value is "<class 'ctypes.LP_c_wchar'>"
    ,
    None:  # (!) real value is "<class 'ctypes.c_char'>"
        None # (!) real value is "<class 'ctypes.LP_c_char'>"
    ,
    None: None, # (!) real value is "<class 'ctypes.c_void_p'>"
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C942C48820>'

__spec__ = None # (!) real value is "ModuleSpec(name='_ctypes', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C942C48820>, origin='C:\\\\Program Files\\\\WindowsApps\\\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\\\\DLLs\\\\_ctypes.pyd')"

