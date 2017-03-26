'''
Create a script that let the user type in a
search term and then the program opens the browser and searches the term on Google.
'''

import webbrowser

query = input("Enter your google query :")

#url = "https://www.google.com/#q=",str(query),"&*"
url = "https://www.google.com/"
url1 = url + "#q="+str(query)+"&*"
#print(url1)
webbrowser.open(url1)


'''
We're using webbrowser  here which is a standard library
that is used to open a web browser. First, we're getting the
search term through input  and then we construct the URL.
You need to first do a manual search on Google and observe
how Google will construct the URL. You will see that the URL
contains your search term at the end.
Therefore, we concatenate the first part of the URL with
the search term we get from input
'''