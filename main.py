import os
import sys
from src.server import run_server

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
run_server()