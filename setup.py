from setuptools import setup

description = 'Python version of the mutt-notmuch script'
long_desc = open('README.rst').read()

setup(
    name='mutt-notmuch',
    version='1.0.0',
    url='https://github.com/honza/mutt-notmuch-py',
    install_requires=[],
    description=description,
    long_description=long_desc,
    author='Honza Pokorny',
    author_email='me@honza.ca',
    maintainer='Honza Pokorny',
    maintainer_email='me@honza.ca',
    packages=[],
    include_package_data=True,
    scripts=['mutt-notmuch-py'],
)
