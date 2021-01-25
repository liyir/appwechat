import os
import subprocess
import signal

import pytest


@pytest.fixture(scope='module', autouse=True)
def record_vedio():
    cmd = "scrcpy --record file.mp4"
    # 错误输出放到标准输出里，标准输出放到正常的输出管道里，这样的话不论对错的输出都会打出来
    p = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)
