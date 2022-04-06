import sys, os
from datetime import datetime, timezone

def printErrors(values):
    try:
        # https://stackoverflow.com/questions/1278705/when-i-catch-an-exception-how-do-i-get-the-type-file-and-line-number
        exc_type, exc_obj, exc_tb = sys.exc_info()
        # print(111,exc_type, exc_obj, exc_tb)
        # print(222,os.path.split(exc_tb.tb_frame.f_code.co_filename))
        # print(333,os.path.split(exc_tb.tb_frame.f_code))
        # print(444)
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(datetime.now(timezone.utc).isoformat(),'-'*7)
        print(datetime.now(timezone.utc).isoformat(),exc_type, fname, exc_tb.tb_lineno)
        print(datetime.now(timezone.utc).isoformat(),'Error type',type(values))
        print(datetime.now(timezone.utc).isoformat(),'Error:',values)
        print(datetime.now(timezone.utc).isoformat(),'-'*7)
    except Exception as errors:
        print(datetime.now(timezone.utc).isoformat(),'Error(287.63527836818395):',errors)
