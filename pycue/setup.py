#  Copyright (c) 2018 Sony Pictures Imageworks Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
from setuptools import find_packages
from setuptools import setup

pycue_dir = os.path.abspath(os.path.dirname(__file__))

version = 'unknown'
possible_version_paths = [
    os.path.join(pycue_dir, 'VERSION'),
    os.path.join(os.path.dirname(pycue_dir), 'VERSION'),
]
for possible_version_path in possible_version_paths:
    if os.path.exists(possible_version_path):
        with open(possible_version_path) as fp:
            version = fp.read().strip()

with open(os.path.join(pycue_dir, 'README.md')) as fp:
    long_description = fp.read()

setup(
    name='pycue',
    version=version,
    description='The OpenCue Python API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/imageworks/OpenCue',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(exclude=['tests']),
    package_data={
        'opencue': ['default.yaml'],
    },
)