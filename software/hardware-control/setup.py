# Copyright (C) 2023 SCHUTZWERK GmbH
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pathlib import Path
from setuptools import setup, find_packages

projectDir = Path(__file__).parent

with open(Path(projectDir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='proboter',
    version='1.0.0',
    description='PROBoter - Hardware control service',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Environment :: Console'
    ],
    keywords='PROBoter pentesting embedded automotive',
    url='https://github.com/schutzwerk/PROBoter',
    author='fweber@SCHUTZWERK GmbH',
    author_email='info@schutzwerk.com',
    license='GNU General Public License v3 (GPLv3)',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'aiohttp',
        'quart',
        'quart-schema',
        'quart-cors',
        'tortoise-orm',
        'pydantic',
        'pyudev',
        'pyserial',
        'pyserial-asyncio',
        'scipy',
        'numpy',
        'opencv-python-headless',
        'disjoint-set'
    ],
    python_requires='>=3.8',
)
