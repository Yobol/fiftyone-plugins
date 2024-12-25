#!/bin/bash

# fiftyone plugins download \
#     https://github.com/voxel51/fiftyone-plugins \
#     --plugin-names @voxel51/hello-world

export FIFTYONE_DATABASE_URI=mongodb://root:example@localhost:27017/

python3 main.py