'''
lease download the attached urls.txt file. The file contains some broken URLs. Here's what the file contains:

https:/www.google.com
https:/www.yahoo.com
https:/www.stackoverflow.com
https:/www.pythonhow.com
Please use Python to remove the "s" from "https" and add another forward slash next to the existing slash, so the content looks like in the expected output.

Expected output:

http://www.google.com
http://www.yahoo.com
http://www.stackoverflow.com
http://www.pythonhow.com
'''

with open("urls.txt","r") as f:
    lst = f.readlines()

# lst = [i.replace("https","http").strip("\n") for i in lst ]
# lst = [i.replace("/","//") for i in lst]
print(lst)

with open("urls_corrected.txt","w") as f:
    for line in lst:
        line_remove_s = line.replace("s","",1)
        line_remove_s_add_slash = line_remove_s[:6]+"/"+line_remove_s[6:]
        f.write(line_remove_s_add_slash)
