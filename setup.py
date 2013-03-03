#!/usr/bin/env python
"""
    Python "publish-subscribe" framework
    
    Created on 2012-01-19
    @author: Jean-Lou Dupont
"""
__author__  ="Jean-Lou Dupont"
__version__ ="0.1.0"


from distutils.core import setup
from setuptools import find_packages

DESC="""
Overview
--------

This package offers a "publish-subscribe"


"""

setup(name=         'pysubpub',
      version=      __version__,
      description=  'Publish-Subscribe framework',
      author=       __author__,
      author_email= 'jl@jldupont.com',
      url=          'http://www.systemical.com/doc/opensource/pysubpub',
      package_dir=  {'': "src",},
      packages=     find_packages("src"),
      zip_safe=False
      ,install_requires=[
                         ]
      ,long_description=DESC
      )

#############################################

f=open("latest", "w")
f.write(str(__version__)+"\n")
f.close()