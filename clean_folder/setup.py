from setuptools import setup

setup(
    name='usefull',
    version='0.0.1',
    description='Very usefull code',
    url="http://github.com/dummy_user/useful",
    author="Flying Circus",
    author_email="flyingcircus@example.com",
    license="MIT",
    packages=["clean_folder"],
    install_requires=[
        'markdown'
        ],
    zip_safe=False
)