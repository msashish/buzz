#!/usr/bin/env bash

python3.6 -m pytest -v
UNITTEST_RESULT=$?
exit $UNITTEST_RESULT
