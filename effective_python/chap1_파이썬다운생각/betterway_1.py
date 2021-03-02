import sys

"""
1. 사용중인 python의 버전을 알자
* 사용중인 python 버전을 정확히 알아내려면, 다음과 같이 --version 플래그를 이용하면 된다
* 파이썬에 내장된 sys 모듈 안의 값을 조사하여, 런타임에 사용 중인 파이썬 버전을 알아낼 수 있다.

2. 정리
* 파이썬에는 CPython, Jython, IronPython, PyPy 같은 다양한 런타임이 있다
* 시스템에서는 파이썬을 실행하는 명령이 사용하고자 하는 파이썬 버전인지를 확인해야한다
"""


print(sys.version_info)
# sys.version_info(major=3, minor=7, micro=9,releaselevel='final', serial=0)
print(sys.version)
# 3.7.9 (default, Nov 20 2020, 11:31:38)
