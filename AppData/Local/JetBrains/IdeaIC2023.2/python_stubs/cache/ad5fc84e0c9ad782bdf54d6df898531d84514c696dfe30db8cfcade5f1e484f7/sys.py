# encoding: utf-8
# module sys
# from (built-in)
# by generator 1.147
"""
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session
excepthook -- called to handle any uncaught exception other than SystemExit
  To customize printing in an interactive session or to install a custom
  top-level exception handler, assign other functions to replace these.

stdin -- standard input file object; used by input()
stdout -- standard output file object; used by print()
stderr -- standard error object; used for error messages
  By assigning other file objects (or objects that behave like files)
  to these, it is possible to redirect all of the interpreter's I/O.

last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are only available in an interactive session after a
  traceback has been printed.

Static objects:

builtin_module_names -- tuple of module names built into this interpreter
copyright -- copyright notice pertaining to this interpreter
exec_prefix -- prefix used to find the machine-specific Python library
executable -- absolute path of the executable binary of the Python interpreter
float_info -- a named tuple with information about the float implementation.
float_repr_style -- string indicating the style of repr() output for floats
hash_info -- a named tuple with information about the hash algorithm.
hexversion -- version information encoded as a single integer
implementation -- Python implementation information.
int_info -- a named tuple with information about the int implementation.
maxsize -- the largest supported length of containers.
maxunicode -- the value of the largest Unicode code point
platform -- platform identifier
prefix -- prefix used to find the Python library
thread_info -- a named tuple with information about the thread implementation.
version -- the version of this interpreter as a string
version_info -- version information as a named tuple
dllhandle -- [Windows only] integer handle of the Python DLL
winver -- [Windows only] version number of the Python DLL
_enablelegacywindowsfsencoding -- [Windows only]
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!
__displayhook__ -- the original displayhook; don't touch!
__excepthook__ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in builtins._
excepthook() -- print an exception and its traceback to sys.stderr
exc_info() -- return thread-safe information about the current exception
exit() -- exit the interpreter by raising SystemExit
getdlopenflags() -- returns flags to be used for dlopen() calls
getprofile() -- get the global profiling function
getrefcount() -- return the reference count for an object (plus one :-)
getrecursionlimit() -- return the max recursion depth for the interpreter
getsizeof() -- return the size of an object in bytes
gettrace() -- get the global debug tracing function
setdlopenflags() -- set the flags to be used for dlopen() calls
setprofile() -- set the global profiling function
setrecursionlimit() -- set the max recursion depth for the interpreter
settrace() -- set the global debug tracing function
"""
# no imports

# Variables with simple values

api_version = 1013

base_exec_prefix = 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0'

base_prefix = 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0'

byteorder = 'little'

copyright = 'Copyright (c) 2001-2023 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'

dllhandle = 140732070428672

dont_write_bytecode = True

executable = 'C:\\Users\\mehdi\\venv\\Scripts\\python.exe'

exec_prefix = 'C:\\Users\\mehdi\\venv'

float_repr_style = 'short'

hexversion = 50990064

maxsize = 9223372036854775807
maxunicode = 1114111

platform = 'win32'
platlibdir = 'lib'

prefix = 'C:\\Users\\mehdi\\venv'

pycache_prefix = None

version = '3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)]'

winver = '3.10'

_base_executable = 'C:\\Users\\mehdi\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\python.exe'

_framework = ''

_home = 'C:\\Users\\mehdi\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0'

# functions

def addaudithook(*args, **kwargs): # real signature unknown
    """ Adds a new audit hook callback. """
    pass

def audit(event, *args): # real signature unknown; restored from __doc__
    """
    audit(event, *args)
    
    Passes the event to any audit hooks that are attached.
    """
    pass

def breakpointhook(*args, **kws): # real signature unknown; restored from __doc__
    """
    breakpointhook(*args, **kws)
    
    This hook function is called by built-in breakpoint().
    """
    pass

def call_tracing(*args, **kwargs): # real signature unknown
    """
    Call func(*args), while tracing is enabled.
    
    The tracing state is saved, and restored afterwards.  This is intended
    to be called from a debugger from a checkpoint, to recursively debug
    some other code.
    """
    pass

def displayhook(*args, **kwargs): # real signature unknown
    """ Print an object to sys.stdout and also save it in builtins._ """
    pass

def excepthook(*args, **kwargs): # real signature unknown
    """ Handle an exception by displaying it with a traceback on sys.stderr. """
    pass

def exc_info(*args, **kwargs): # real signature unknown
    """
    Return current exception information: (type, value, traceback).
    
    Return information about the most recent exception caught by an except
    clause in the current stack frame or in an older stack frame.
    """
    pass

def exit(*args, **kwargs): # real signature unknown
    """
    Exit the interpreter by raising SystemExit(status).
    
    If the status is omitted or None, it defaults to zero (i.e., success).
    If the status is an integer, it will be used as the system exit status.
    If it is another kind of object, it will be printed and the system
    exit status will be one (i.e., failure).
    """
    pass

def getallocatedblocks(*args, **kwargs): # real signature unknown
    """ Return the number of memory blocks currently allocated. """
    pass

def getdefaultencoding(*args, **kwargs): # real signature unknown
    """ Return the current default encoding used by the Unicode implementation. """
    pass

def getfilesystemencodeerrors(*args, **kwargs): # real signature unknown
    """ Return the error mode used Unicode to OS filename conversion. """
    pass

def getfilesystemencoding(*args, **kwargs): # real signature unknown
    """ Return the encoding used to convert Unicode filenames to OS filenames. """
    pass

def getprofile(*args, **kwargs): # real signature unknown
    """
    Return the profiling function set with sys.setprofile.
    
    See the profiler chapter in the library manual.
    """
    pass

def getrecursionlimit(*args, **kwargs): # real signature unknown
    """
    Return the current value of the recursion limit.
    
    The recursion limit is the maximum depth of the Python interpreter
    stack.  This limit prevents infinite recursion from causing an overflow
    of the C stack and crashing Python.
    """
    pass

def getrefcount(): # real signature unknown; restored from __doc__
    """
    Return the reference count of object.
    
    The count returned is generally one higher than you might expect,
    because it includes the (temporary) reference as an argument to
    getrefcount().
    """
    pass

def getsizeof(p_object, default=None): # real signature unknown; restored from __doc__
    """
    getsizeof(object [, default]) -> int
    
    Return the size of object in bytes.
    """
    return 0

def getswitchinterval(*args, **kwargs): # real signature unknown
    """ Return the current thread switch interval; see sys.setswitchinterval(). """
    pass

def gettrace(*args, **kwargs): # real signature unknown
    """
    Return the global debug tracing function set with sys.settrace.
    
    See the debugger chapter in the library manual.
    """
    pass

def getwindowsversion(*args, **kwargs): # real signature unknown
    """
    Return info about the running version of Windows as a named tuple.
    
    The members are named: major, minor, build, platform, service_pack,
    service_pack_major, service_pack_minor, suite_mask, product_type and
    platform_version. For backward compatibility, only the first 5 items
    are available by indexing. All elements are numbers, except
    service_pack and platform_type which are strings, and platform_version
    which is a 3-tuple. Platform is always 2. Product_type may be 1 for a
    workstation, 2 for a domain controller, 3 for a server.
    Platform_version is a 3-tuple containing a version number that is
    intended for identifying the OS rather than feature detection.
    """
    pass

def get_asyncgen_hooks(*args, **kwargs): # real signature unknown
    """
    Return the installed asynchronous generators hooks.
    
    This returns a namedtuple of the form (firstiter, finalizer).
    """
    pass

def get_coroutine_origin_tracking_depth(*args, **kwargs): # real signature unknown
    """ Check status of origin tracking for coroutine objects in this thread. """
    pass

def get_int_max_str_digits(*args, **kwargs): # real signature unknown
    """ Return the maximum string digits limit for non-binary int<->str conversions. """
    pass

def intern(*args, **kwargs): # real signature unknown
    """
    ``Intern'' the given string.
    
    This enters the string in the (global) table of interned strings whose
    purpose is to speed up dictionary lookups. Return the string itself or
    the previously interned string object with the same value.
    """
    pass

def is_finalizing(*args, **kwargs): # real signature unknown
    """ Return True if Python is exiting. """
    pass

def setprofile(function): # real signature unknown; restored from __doc__
    """
    setprofile(function)
    
    Set the profiling function.  It will be called on each function call
    and return.  See the profiler chapter in the library manual.
    """
    pass

def setrecursionlimit(*args, **kwargs): # real signature unknown
    """
    Set the maximum depth of the Python interpreter stack to n.
    
    This limit prevents infinite recursion from causing an overflow of the C
    stack and crashing Python.  The highest possible limit is platform-
    dependent.
    """
    pass

def setswitchinterval(*args, **kwargs): # real signature unknown
    """
    Set the ideal thread switching delay inside the Python interpreter.
    
    The actual frequency of switching threads can be lower if the
    interpreter executes long sequences of uninterruptible code
    (this is implementation-specific and workload-dependent).
    
    The parameter must represent the desired switching delay in seconds
    A typical value is 0.005 (5 milliseconds).
    """
    pass

def settrace(function): # real signature unknown; restored from __doc__
    """
    settrace(function)
    
    Set the global debug tracing function.  It will be called on each
    function call.  See the debugger chapter in the library manual.
    """
    pass

def set_asyncgen_hooks(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set_asyncgen_hooks(* [, firstiter] [, finalizer])
    
    Set a finalizer for async generators objects.
    """
    pass

def set_coroutine_origin_tracking_depth(*args, **kwargs): # real signature unknown
    """
    Enable or disable origin tracking for coroutine objects in this thread.
    
    Coroutine objects will track 'depth' frames of traceback information
    about where they came from, available in their cr_origin attribute.
    
    Set a depth of 0 to disable.
    """
    pass

def set_int_max_str_digits(*args, **kwargs): # real signature unknown
    """ Set the maximum string digits limit for non-binary int<->str conversions. """
    pass

def unraisablehook(*args, **kwargs): # real signature unknown
    """
    Handle an unraisable exception.
    
    The unraisable argument has the following attributes:
    
    * exc_type: Exception type.
    * exc_value: Exception value, can be None.
    * exc_traceback: Exception traceback, can be None.
    * err_msg: Error message, can be None.
    * object: Object causing the exception, can be None.
    """
    pass

def _clear_type_cache(*args, **kwargs): # real signature unknown
    """ Clear the internal type lookup cache. """
    pass

def _current_exceptions(*args, **kwargs): # real signature unknown
    """
    Return a dict mapping each thread's identifier to its current raised exception.
    
    This function should be used for specialized purposes only.
    """
    pass

def _current_frames(*args, **kwargs): # real signature unknown
    """
    Return a dict mapping each thread's thread id to its current stack frame.
    
    This function should be used for specialized purposes only.
    """
    pass

def _deactivate_opcache(*args, **kwargs): # real signature unknown
    """ Deactivate the opcode cache permanently """
    pass

def _debugmallocstats(*args, **kwargs): # real signature unknown
    """
    Print summary info to stderr about the state of pymalloc's structures.
    
    In Py_DEBUG mode, also perform some expensive internal consistency
    checks.
    """
    pass

def _enablelegacywindowsfsencoding(*args, **kwargs): # real signature unknown
    """
    Changes the default filesystem encoding to mbcs:replace.
    
    This is done for consistency with earlier versions of Python. See PEP
    529 for more information.
    
    This is equivalent to defining the PYTHONLEGACYWINDOWSFSENCODING
    environment variable before launching Python.
    """
    pass

def _getframe(*args, **kwargs): # real signature unknown
    """
    Return a frame object from the call stack.
    
    If optional integer depth is given, return the frame object that many
    calls below the top of the stack.  If that is deeper than the call
    stack, ValueError is raised.  The default for depth is zero, returning
    the frame at the top of the call stack.
    
    This function should be used for internal and specialized purposes
    only.
    """
    pass

def __breakpointhook__(*args, **kwargs): # real signature unknown
    """
    breakpointhook(*args, **kws)
    
    This hook function is called by built-in breakpoint().
    """
    pass

def __displayhook__(*args, **kwargs): # real signature unknown
    """ Print an object to sys.stdout and also save it in builtins._ """
    pass

def __excepthook__(*args, **kwargs): # real signature unknown
    """ Handle an exception by displaying it with a traceback on sys.stderr. """
    pass

def __interactivehook__(): # reliably restored by inspect
    # no doc
    pass

def __unraisablehook__(*args, **kwargs): # real signature unknown
    """
    Handle an unraisable exception.
    
    The unraisable argument has the following attributes:
    
    * exc_type: Exception type.
    * exc_value: Exception value, can be None.
    * exc_traceback: Exception traceback, can be None.
    * err_msg: Error message, can be None.
    * object: Object causing the exception, can be None.
    """
    pass

# classes

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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x000001AED4842320>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x000001AED48423B0>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x000001AED4842440>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x000001AED48424D0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x000001AED4842560>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x000001AED4842680>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x000001AED48427A0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x000001AED48428C0>)>, 'load_module': <classmethod(<function _load_module_shim at 0x000001AED48417E0>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

argv = [] # real value of type <class 'list'> skipped

builtin_module_names = () # real value of type <class 'tuple'> skipped

flags = (
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    False,
    0,
    0,
    -1,
)

float_info = (
    1.7976931348623157e+308,
    1024,
    308,
    2.2250738585072014e-308,
    -1021,
    -307,
    15,
    53,
    2.220446049250313e-16,
    2,
    1,
)

hash_info = (
    64,
    2305843009213693951,
    314159,
    0,
    1000003,
    'siphash24',
    64,
    128,
    0,
)

implementation = None # (!) real value is "namespace(name='cpython', cache_tag='cpython-310', version=sys.version_info(major=3, minor=10, micro=11, releaselevel='final', serial=0), hexversion=50990064)"

int_info = (
    30,
    4,
    4300,
    640,
)

meta_path = [
    None, # (!) real value is '<_distutils_hack.DistutilsMetaFinder object at 0x000001AED49D0A90>'
    None, # (!) real value is '<_virtualenv._Finder object at 0x000001AED494E260>'
    __loader__,
    None, # (!) real value is "<class '_frozen_importlib.FrozenImporter'>"
    None, # (!) real value is "<class '_frozen_importlib_external.PathFinder'>"
    None, # (!) real value is '<six._SixMetaPathImporter object at 0x000001AED52D00D0>'
]

modules = {} # real value of type <class 'dict'> skipped

orig_argv = [
    'C:\\Users\\mehdi\\venv\\Scripts\\python.exe',
    '-B',
    '-c',
    'from multiprocessing.spawn import spawn_main; spawn_main(parent_pid=26604, pipe_handle=1088)',
    '--multiprocessing-fork',
]

path = [
    'C:\\Users\\mehdi\\AppData\\Roaming\\JetBrains\\IdeaIC2023.2\\plugins\\python-ce\\helpers',
    'C:\\Users\\mehdi\\AppData\\Roaming\\JetBrains\\IdeaIC2023.2\\plugins\\python-ce\\helpers\\generator3',
    'C:\\Users\\mehdi\\AppData\\Roaming\\JetBrains\\IdeaIC2023.2\\plugins\\python-ce\\helpers',
    'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\\python310.zip',
    'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\\DLLs',
    'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\\lib',
    'C:\\Users\\mehdi\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0',
    'C:\\Users\\mehdi\\venv',
    'C:\\Users\\mehdi\\venv\\lib\\site-packages',
    'C:/Program Files/WindowsApps/PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0/DLLs',
    'C:/Program Files/WindowsApps/PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0/lib',
    'C:/Users/mehdi/venv',
    'C:/Users/mehdi/venv/Lib/site-packages',
]

path_hooks = [
    None, # (!) real value is "<class 'zipimport.zipimporter'>"
    None, # (!) real value is '<function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x000001AED4843910>'
]

path_importer_cache = {} # real value of type <class 'dict'> skipped

stderr = None # (!) real value is "<_io.TextIOWrapper name='<stderr>' mode='w' encoding='cp1252'>"

stdin = None # (!) real value is "<_io.TextIOWrapper name=3 mode='r' encoding='utf-8'>"

stdlib_module_names = None # (!) real value is "frozenset({'filecmp', 'resource', '_warnings', 'uu', 'urllib', 'cgitb', '_heapq', 'locale', 'poplib', 'sre_constants', 'atexit', 'xmlrpc', 'zipimport', '_sqlite3', 'contextvars', 'tokenize', '__future__', 'posix', '_json', 'fractions', 'inspect', 'webbrowser', '_contextvars', 'fcntl', 'calendar', 'msilib', 'base64', 'shlex', 'sre_compile', 'time', '_zoneinfo', 'gzip', 'imp', '_lzma', '_crypt', 'chunk', 'string', 'pyclbr', 'builtins', 'getopt', '_bz2', '_pyio', 'colorsys', '_ast', '_sha256', '_signal', 'crypt', '_sha1', '_opcode', 'grp', '_elementtree', 'hmac', '_abc', 'genericpath', 'http', 'cmd', 'json', 'mimetypes', 'nntplib', 'traceback', 'winsound', 'wsgiref', 'typing', '_datetime', '_codecs_jp', '_imp', 'profile', '_posixsubprocess', 'concurrent', 'shutil', '_frozen_importlib_external', 'linecache', '_uuid', 'doctest', 'imghdr', '_winapi', 'threading', 'signal', 'graphlib', 'turtledemo', 'token', '_codecs_iso2022', 'select', 'nturl2path', 'gettext', 'telnetlib', 'wave', '_blake2', 'faulthandler', 'opcode', 'statistics', 'bisect', '_multiprocessing', 'subprocess', '_weakref', 'platform', 'tty', 're', 'pathlib', 'bdb', '_py_abc', 'pprint', 'unittest', 'ast', 'reprlib', 'smtplib', 'weakref', '_multibytecodec', '_overlapped', '_posixshmem', 'asyncore', 'audioop', 'functools', 'html', '_compat_pickle', 'glob', 'ipaddress', 'ensurepip', 'math', 'msvcrt', 'netrc', 'ntpath', 'aifc', '_statistics', '_string', 'marshal', 'socket', '_ssl', '_sre', 'copyreg', '_codecs', '_compression', 'binascii', 'decimal', 'email', 'lib2to3', 'sndhdr', '_hashlib', 'tabnanny', 'this', 'plistlib', 'fnmatch', 'sys', '_struct', '_threading_local', 'nis', 'sysconfig', 'stringprep', 'hashlib', 'pdb', 'compileall', 'curses', 'pty', 'difflib', 'symtable', 'secrets', '_socket', 'zipfile', 'rlcompleter', 'modulefinder', '_random', 'idlelib', 'dis', '_md5', 'operator', 'tracemalloc', 'uuid', '_sha3', 'smtpd', '_frozen_importlib', '_markupbase', 'enum', '_curses', '_codecs_tw', '_tracemalloc', '_collections_abc', 'copy', 'random', '_weakrefset', 'shelve', '_locale', 'asyncio', 'spwd', 'io', '_codecs_cn', 'cProfile', 'queue', '_pickle', 'timeit', '_scproxy', 'dbm', '_lsprof', 'mailcap', 'cgi', 'os', '_collections', 'sqlite3', 'tkinter', 'winreg', 'trace', '_functools', 'code', 'contextlib', 'collections', '_curses_panel', 'ossaudiodev', 'textwrap', 'pwd', 'codecs', 'sre_parse', 'nt', 'datetime', 'cmath', 'antigravity', 'asynchat', '_codecs_kr', 'numbers', 'pickletools', 'runpy', 'pstats', 'sunau', 'termios', 'struct', 'tarfile', 'types', 'binhex', 'lzma', 'optparse', 'zlib', '_sitebuiltins', '_tkinter', 'gc', 'imaplib', 'xml', 'itertools', 'stat', 'pyexpat', '_osx_support', '_strptime', 'socketserver', '_stat', 'dataclasses', '_bootsubprocess', 'array', '_csv', '_gdbm', 'ftplib', '_msi', 'warnings', 'xdrlib', 'turtle', 'unicodedata', 'site', 'heapq', 'encodings', 'zipapp', 'importlib', 'codeop', 'quopri', 'bz2', 'pkgutil', 'abc', 'configparser', 'zoneinfo', '_aix_support', '_queue', 'posixpath', 'selectors', '_bisect', '_dbm', 'keyword', 'multiprocessing', '_decimal', 'ctypes', 'mailbox', 'mmap', 'fileinput', 'distutils', 'pickle', '_pydecimal', 'argparse', 'errno', 'tempfile', '_codecs_hk', '_asyncio', 'getpass', 'logging', 'venv', '_sha512', '_symtable', 'pydoc', 'syslog', '_ctypes', 'readline', '_operator', 'py_compile', 'ssl', '_thread', '_io', 'pipes', 'pydoc_data', 'sched', 'csv'})"

stdout = None # (!) forward: __stdout__, real value is "<_io.TextIOWrapper name='<stdout>' mode='w' encoding='cp1252'>"

thread_info = (
    'nt',
    None,
    None,
)

version_info = (
    3,
    10,
    11,
    'final',
    0,
)

warnoptions = []

_git = (
    'CPython',
    'tags/v3.10.11',
    '7d4cc5a',
)

_xoptions = {}

__spec__ = None # (!) real value is "ModuleSpec(name='sys', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

__stderr__ = stderr

__stdin__ = None # (!) real value is "<_io.TextIOWrapper name='<stdin>' mode='r' encoding='cp1252'>"

__stdout__ = None # (!) real value is "<_io.TextIOWrapper name='<stdout>' mode='w' encoding='cp1252'>"

# intermittent names
exc_value = Exception()
exc_traceback=None
