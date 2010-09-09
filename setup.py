from setuptools import setup, find_packages
import os

version = '1.2'

setup(name='Products.LocalFS',
      version=version,
      description="A package which take generic methods",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Affinitic',
      author_email='info@affinitic.be',
      url='http://svn.affinitic.be/Arsia/python/arsia.cerise',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools'])
