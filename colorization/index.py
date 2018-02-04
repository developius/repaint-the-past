import sys
import handler
import json
import os

def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf

def read_head():
    buf = ""
    while(True):
        line = sys.stdin.readline()
        buf += line

        if line == "\r\n":
            break
    return buf

if(__name__ == "__main__"):
    binary_mode = os.getenv('minio_authority') == None
    url_mode = os.getenv('url_mode') != None

    if binary_mode == True:
        st = sys.stdin.read()

        if url_mode:
            st = st.strip("\\n") # fix for leading/trailing whitespace in URLs

        handler.handle(st)
    else:
        st = get_stdin()
        print(json.dumps(handler.handle(st)))
