'''
	made by Nanta XE
	Nikmati saja fiturnya.
'''

import shutil, os
from distutils.core import setup, Extension
from Cython.Build import cythonize

main_file = 'run.c'

def install():
	setup(
		name = "faith",
		ext_modules = [Extension("faith", [main_file])],
		script_args = ['build_ext', '--inplace', '--force', '-j 5']
	)
	if os.path.exists(main_file):
		try: shutil.rmtree('build/')
		except:0
		try: os.remove(main_file)
		except:0
	else:
		print('Please install from full source')

install()
