#!/bin/bash

find ./leetcode/*.py -type f | grep -c -v '__init__.py'
