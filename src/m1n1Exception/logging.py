import inspect
DEBUG = False

def set_debug(val):
  global DEBUG
  DEBUG = val
 
// loggers
def info(msg):    print(msg)
def warn(msg):    print(f"[WARNING] {msg}")
if DEBUG:
    def debug(msg):
        funcname = inspect.stack()[1].function
        print(f"{funcname}: {msg}")
else:
    def debug(msg):
        pass
