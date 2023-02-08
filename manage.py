import uvicorn
from core.const import *
import sys

import os

def __main__():
    if sys.argv[1] == 'runserver':
        if len(sys.argv[1:]) == 1:
            uvicorn.run(app="app.main:app",port=PORT,host=HOST)
        else:
            raise Exception('The command is invalid')
        
__main__()