from setuptools import setup, find_packages

version = '1.2.2.dev0'

long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CHANGES.rst").read(),
    ]
)

setup(
    name='collective.pluggablelogin',
    version=version,
    description="Turns Plone's login form into a portlet manager for easier customization",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
      "Framework :: Plone :: Addon",
      "Framework :: Plone :: 5.2",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3.8",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='',
    author='David Glick, Groundwire',
    author_email='dglick@gmail.com',
    url='http://github.com/collective/collective.pluggablelogin',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=['setuptools-git'],
    install_requires=[
        'setuptools',
        'Products.CMFPlone',
    ],
    extras_require={
        "test": [
            "plone.api",
            "plone.app.testing",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
