# encoding: utf-8
"""Installer for the buildout.jenkins.test package."""

from setuptools import find_packages
from setuptools import setup





setup(
        name='buildout.jenkins.test',
        version='1.0a1',
        description="An add-on for Plone",
        author='Sebastien Sirtoli',
        author_email='sirtoli.dev@gmail.com',
        url='https://pypi.python.org/pypi/buildout.jenkins.test',
        license='GPL version 2',
        packages=find_packages('src', exclude=['ez_setup']),
        namespace_packages=['buildout','buildout.jenkins'],
        package_dir={'': 'src'},
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            # -*- Extra requirements: -*-
            'plone.api',
            'Products.GenericSetup>=1.8.2',
            'setuptools',
            'z3c.jbot',
        ],
        extras_require={
            'test': [
                'plone.app.testing',
                # Plone KGS does not use this version, because it would break
                # Remove if your package shall be part of coredev.
                # plone_coredev tests as of 2016-04-01.
                'plone.testing>=5.0.0',
                'plone.app.contenttypes',
                'plone.app.robotframework[debug]',
            ],
        },
        entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)