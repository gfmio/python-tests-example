'''
Integration tests for module.py module
'''

import os, imp
mod = imp.load_source("src","./src/__init__.py")

def test_square():
	'''Sample test that should fail'''
	assert mod.square.square(3) == 5
