from mymodule import divide
import sys
print(sys.path)
# ['/Users/michaelmcguiness/Dropbox/CompSci/Web Programming/flask-rest-apis/python_refresher/29_imports_in_python', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload', '/Users/michaelmcguiness/Library/Python/3.8/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages']

print(divide(10, 2))
print(__name__)
# mymodule.py:  mymodule
# 5.0
# mymodule.py:  mymodule
# __main__
