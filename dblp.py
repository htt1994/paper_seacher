# -*- coding: UTF-8 -*-


r"""
http://history.ccf.org.cn/sites/ccf/paiming.jsp

计算机图形学与多媒体
http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903940690854

人工智能
http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903940690839

人机交互与普适计算

http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903940690320
"""

from downers.dblp_helper import get_titles

from downers.ai import main as aimain
from downers.nips import main as nipsmain

from downers.acmmm import main as acmmmain
from downers.eccv import main as eccvmain
from downers.aaai import main as aaaimain

if __name__ == "__main__":
    # aimain()
    # nipsmain()
    # acmmmain()
    # eccvmain()
    aaaimain()

