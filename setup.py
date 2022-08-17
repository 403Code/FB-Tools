'''
	Made by Nanta XE
	Enjoy the features.
'''

import shutil, os
from distutils.core import setup, Extension
from Cython.Build import cythonize

def install(main_file = 'run.c', module_name = 'faith', args = ['build_ext', '--inplace', '--force', '-j 5']):
	setup(
		name = module_name,
		ext_modules = [Extension(module_name, [main_file])],
		script_args = args
	)
	if os.path.exists(main_file):
		try: shutil.rmtree('build/')
		except:0
		try: os.remove(main_file)
		except:0
	else:
		print('Please install from full source')

install()
