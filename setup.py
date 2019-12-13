# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in woocommerce_erpnext/__init__.py
from woocommerce_erpnext import __version__ as version

setup(
	name='woocommerce_erpnext',
	version=version,
	description='Integration between WooCommerce and ERPNext',
	author='GreyCube Technologies',
	author_email='admin@greycube.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
