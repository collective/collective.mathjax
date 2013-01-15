from setuptools import setup, find_packages

version = '1.1'

setup(name='collective.mathjax',
      version=version,
      description="MathJax integration for Plone.",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
      ],
      keywords='plone resources',
      author='Johannes Raggam',
      author_email='raggam-nl@adm.at',
      url='http://github.com/collective/collective.mathjax',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
