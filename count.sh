#!/bin/bash

find ./leetcode/ -name *.py -type f | grep -v '__init__.py' | wc -l
