from setuptools import setup, find_packages
import sys, os

version = '0.9.1'

setup(name='configpy',
      version=version,
      description="Configuration parser with real python types",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Jared Rodriguez',
      author_email='jared@blacknode.net',
      url='https://github.com/jr0d/configpy',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
