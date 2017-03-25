'''
 Please create an empty file (manually as you normally create
 Python files) and name it requests.py . Make sure the file has that name exactly.

Then just paste the following code in the file (manually):


Executing the script will throw an error. Please fix that error
so that you get the expected output and explain why the error happened.

Expected output:

<!DOCTYPE html>
<!--[if IE 7]>
<html class="ie ie7" lang="en-US" prefix="og: http://ogp.me/ns#">
'''

import requests


r = requests.get("http://www.pythonhow.com")
print(r.text[:100])