# 세팅
### 세팅
1. MVC모델 패키지 세팅
2. https://parksrazor.tistory.com/93 => 필요 파일 다운 + 코드 카피
3. https://parksrazor.tistory.com/670 => 필수 라이브러리 설치
### 에러
- systemerror: java.nio.file.invalidpathexception - 버전/경로 에러
  1. 파일탐색기에서 konlpy 경로로 이동
  2. vsc로 jvm.py 를 열고 아래 코드로 수정
```python
from __future__ import absolute_import

import logging
import os
import sys
try:
    import jpype
except ImportError:
    pass

from konlpy import utils


def init_jvm(jvmpath=None, max_heap_size=1024):
    """Initializes the Java virtual machine (JVM).
    :param jvmpath: The path of the JVM. If left empty, inferred by :py:func:`jpype.getDefaultJVMPath`.
    :param max_heap_size: Maximum memory usage limitation (Megabyte). Default is 1024 (1GB). If you set this value too small, you may got out of memory. We recommend that you set it 1024 ~ 2048 or more at least. However, if this value is too large, you may see inefficient memory usage.
    """

    if jpype.isJVMStarted():
        logging.warning('JVM is already running. Do not init twice!')
        return

    folder_suffix = [
        # JAR
        '{0}',
        # Java sources
        '{0}{1}bin',
        '{0}{1}',
        # Hannanum
        '{0}{1}jhannanum-0.8.4.jar',
        # Kkma
        '{0}{1}kkma-2.0.jar',
        # Komoran3
        '{0}{1}aho-corasick.jar',
        '{0}{1}shineware-common-1.0.jar',
        '{0}{1}shineware-ds-1.0.jar',
        '{0}{1}komoran-3.0.jar',
        # Twitter (Okt)
        '{0}{1}snakeyaml-1.12.jar',
        '{0}{1}scala-library-2.12.3.jar',
        '{0}{1}open-korean-text-2.1.0.jar',
        '{0}{1}twitter-text-1.14.7.jar',
        '{0}{1}'
    ]

    javadir = '%s%sjava' % (utils.installpath, os.sep)

    args = [javadir, os.sep]
    classpath = os.pathsep.join(f.format(*args) for f in folder_suffix)

    jvmpath = jvmpath or jpype.getDefaultJVMPath()

    # NOTE: Temporary patch for Issue #76. Erase when possible.
    if sys.platform == 'darwin'\
            and jvmpath.find('1.8.0') > 0\
            and jvmpath.endswith('libjvm.dylib'):
        jvmpath = '%s/lib/jli/libjli.dylib' % jvmpath.split('/lib/')[0]

    if jvmpath:
        jpype.startJVM(jvmpath, '-Djava.class.path=%s' % classpath,
                                '-Dfile.encoding=UTF8',
                                '-ea', '-Xmx{}m'.format(max_heap_size),
                                convertStrings=True)
    else:
        raise ValueError("Please specify the JVM path.")
```
  
- Resource punkt not found. - NLTK 다운이 잘 안됨
```python
import nltk
nltk.download('punkt')
```
- oserror: cannot open resource - 워드클라우드 폰트 설정
```python
font_path="[ttf파일경로]"
```

- TypeError - Object of type ‘int64’ is not JSON serializable : 자료구조 내 원소 int64타입을 인식 못함
  - 데이터타입을 int, str로 전부 바꿔줌
# gitignore
### 