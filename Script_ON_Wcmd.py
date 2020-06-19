#!/usr/local/bin/python3
"""
# =============================================================================
 @author: IvanC-IT
 
  This code runs the script directly from the Windows console
  by independently importing the missing libraries. '''
# =============================================================================
"""
try:
    import   _# Inserire il nome della libreria da installare
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', ' Insert here library name to install '])
    import _ # Insert here library name to import
    
'''Windows cmd open '''
import os
os.system("start/b   Insert here Python file to run .py") # 

"""
# =============================================================================
#   Script
# =============================================================================
"""
