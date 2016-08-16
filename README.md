# Let's get the badge!! #
[![Build Status](https://travis-ci.org/yoon-gu/ci-sample.svg?branch=master)](https://travis-ci.org/yoon-gu/ci-sample)
[![codecov](https://codecov.io/gh/yoon-gu/ci-sample/branch/master/graph/badge.svg)](https://codecov.io/gh/yoon-gu/ci-sample)
[![Coverage Status](https://coveralls.io/repos/github/yoon-gu/ci-sample/badge.svg?branch=master)](https://coveralls.io/github/yoon-gu/ci-sample?branch=master)
## `tox` ##
* https://testrun.org/tox/latest/

### Example ###
1. `pip install tox` or `sudo pip install tox`
1. add `tox.ini` in your root folder.
```ini
[tox]
envlist = py27-{dj17,dj18,dj19}

[testenv]
deps=
	coverage
	coveralls

commands=coverage run manage.py test
```

1. run `tox`

## `coveralls.io` ##
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repudiandae, dolor, doloremque. Sit aperiam fugiat, id!

## `codecov.io` ##
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis ducimus, sequi dignissimos.