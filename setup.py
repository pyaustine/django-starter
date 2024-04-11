from setuptools import setup, find_packages
import subprocess
import os

wrapper_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in wrapper_version:
    # when not on tag, igt describe outputs: "1.3.3-22-gdf81228"
    # pip has got strict version numbers
    # so change it to: "1.3.3+.git.gdf81228"
    # see: https://www.python.org/pep-0440/#local-version-segments
    v,i,s = wrapper_version.split("-")
    wrapper_version =  v + "+" + i + ".git." + s

assert "-" not in wrapper_version
assert "." in wrapper_version

assert os.path.exists("start_django/version.py")
with open("start_django/version.py", "w") as fh:
    fh.write( "%s\n" % wrapper_version)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='start_django',
    version=wrapper_version,
    packages=find_packages(),
    author='Austine',
    author_email='ayahaustine@gmail.com',
    description='A Python wrapper for the OpenWeatherMap API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={'start_django': ['VERSION']},
    url='https://github.com/pyaustine/start_django.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'start_django = start_django.main:main',
        ],
    },
    install_requires=[
        'Django',
    ],
)