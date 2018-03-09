Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> s=open("1.txt","w")
>>> s.write("heloooooo")
9
>>> s=open("1.txt","r")
>>> s.read()
'heloooooo'
>>> s(_builtins_)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s(_builtins_)
NameError: name '_builtins_' is not defined
>>> dir
<built-in function dir>
>>> dir(builtin_)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dir(builtin_)
NameError: name 'builtin_' is not defined
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> help(help)
Help on _Helper in module _sitebuiltins object:

class _Helper(builtins.object)
 |  Define the builtin 'help'.
 |  
 |  This is a wrapper around pydoc.help that provides a helpful message
 |  when 'help' is typed at the Python interactive prompt.
 |  
 |  Calling help() at the Python prompt starts an interactive help session.
 |  Calling help(thing) prints help for the python object 'thing'.
 |  
 |  Methods defined here:
 |  
 |  __call__(self, *args, **kwds)
 |      Call self as a function.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

>>> s=open("1.txt","a")
>>> s.append("how are you?")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.append("how are you?")
AttributeError: '_io.TextIOWrapper' object has no attribute 'append'
>>> s=open(1.txt","w")
       
SyntaxError: invalid syntax
>>> s=open("1.txt","w")
>>> s.write("hello ,ada,,how are you")
23
>>> s=open("1.txt","r")
>>> s.read()
'hello ,ada,,how are you'
>>> 
