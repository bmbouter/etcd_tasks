from setuptools import setup

setup(
    name='cabbage',
    version='0.1a1',
    homepage='https://github.com/bmbouter/cabbage/',
    description='A Python distributed task system based on etcd',
    url='http://github.com/bmbouter/cabbage',
    author='Brian Bouterse',
    author_email='bmbouter@gmail.com',
    license='GPLv3',
    packages=['cabbage'],
    install_requires=[
        'aio_etcd',
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
