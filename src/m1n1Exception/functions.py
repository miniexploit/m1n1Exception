import subprocess
import os, sys
import inspect
from .exceptions import *

PACKAGE_NAME = None
locked = False

def set_package_name(name):
	global locked
	if not locked:
		locked = True
		global PACKAGE_NAME
		PACKAGE_NAME = name

def detachret(cond, err, dir):
	if (PACKAGE_NAME is None) and (not locked):
		sys.exit('Internal error: PACKAGE_NAME was not set!')
	if not (cond):
		caller_frame = inspect.stack()[1]
		caller = os.path.basename(caller_frame.filename)
		subprocess.run(('hdiutil','detach',dir), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		raise m1n1Exception(PACKAGE_NAME, err, caller)

def retassure(cond, err):
	if (PACKAGE_NAME is None) and (not locked):
		sys.exit('Internal error: PACKAGE_NAME was not set!')
	if not (cond):
		caller_frame = inspect.stack()[1]
		caller = os.path.basename(caller_frame.filename)
		raise m1n1Exception(PACKAGE_NAME, err, caller)

def retcustomassure(cond, exception):
	if not (cond):
		raise exception

def reterror(err):
	if (PACKAGE_NAME is None) and (not locked):
		sys.exit('Internal error: PACKAGE_NAME was not set!')
	caller_frame = inspect.stack()[1]
	caller = os.path.basename(caller_frame.filename)
	raise m1n1Exception(PACKAGE_NAME, err, caller)

def unlock():
	global locked
	locked = False