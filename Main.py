import os

from System.System import System

if __name__ == '__main__':
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(ROOT_DIR, 'Resources\\system\\74182.sys')
    system = System(path)
