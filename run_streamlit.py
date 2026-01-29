# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 23:02:02 2026

@author: Legodi Mahlatse
"""

import subprocess
file = "my_profile.py"

subprocess.Popen(["streamlit","run", file],shell=True)