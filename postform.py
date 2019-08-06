import requests
from bs4 import BeautifulSoup

payload = {
    '__VIEWSTATE': 'xAY02b5aQfbeeMKy9oS2Ofa6WtYo/C8zpjPhZFzzn5rB9X12D4W/hzTWKotylL3qclvhy3mnYb+jfaHgDkAcmu2QRMFEWu+KHRbiwcHMkuuF8vGSdYEwZfJLsppaCytuoX2jZPeUUnaJJtBY/exGsw==',
    '__VIEWSTATEGENERATOR': '0AFBBFE1',
    '__EVENTVALIDATION': 'HjRCYCavARIxXMjr0+bZO0geOlLoUPn+C9Q1A0s+ZzhfCo2n0XDzhCQOjPBIG0oGLmXtm6Qwm6vqua6jh5PrfCUi/8dQOK4iWPqU8gX6u4uy2utJ+rLyuY4xUXh+w39ZEjXukJQ6TEF3jZQ2m/QIhyJLOcii6U1FHgyyvZb+eZlOt64Xo7PDfzW91gSrf63Eykhfi8u4zd+il56irQ0UcxuUfFCXMQeC20GPTyJ9Q35ixgB+d/bVgkvTpYnCqNiLmJp1y71mtWwdQX3/iOByUdip2oXo9508P/v1039JVgeQUCclAe3IjhC740b2etKfgPVxdnYzqJAgJ4mY4jnCSaYX31Bwxaycbsbc5+h1nlb6ACZV91iLBIoezj3xzJmN2FJ8SdRQJLlvY4t7gvRK8kkU/bjn4y21a9XBjFYznTXGCzYG9rKHmWlhtQLmqilkQARBgu6umIdi8JLGvncntthaIZSSn/S6RQJ5iNmlSiTKloQqs9JIyl1Ioql1CtucgiureAIfc+vfejWhwZAyviAg8J8vU0vjbbytEvbCEiLdt+PjB9E0THLrvKxOhdvnserh0dHwpfpmvGPEVDwVFIaQCfH40r7DFvR6YvJ+cgsogutYT2wYcIGRRWmgBY7RNVzZW6MgMFd/rtQcgOiPAithPLZgesleY22/tAVNEwQVdgL7028/ysSCrhM6OUVSkpiextOecS9Wq+J5R5bC10Ali9UqEAaAfLgg4aDFvXvZiHJ/MOmaCsijwDbZDfjyXEnu3C4vFJ2NbtBqb5cMI07ko23xrp2DLj9R0IeOeVrmQwRKKfmFkCb/CIwjEZsJaIVGHFGKB8tu79Un1uL8V8hDqjt6PYCXwGruiaqoznIAXtS4pND252+o9HtKAvGK3yDzstJ8k7CV6gP74ML8tgPntviY3RhTiGddCi63biOlkaccQXUDo1n0uoXH2BVw2Huj+aMfvX9gxa5MFm4+5ZtBCgHcdlH31VwQvrbSxUdPj3dgAm5bGbvEy8+7hdR7xwGZp+2qGGr40qyBhD3Bo0v3C/zlmUdnhGk+UvS9F9MxRu7y9EgahxnyPmz5aexN',
    'ctl00$CntntPlcHldr$ddlTerm': '201910',
    'ctl00$CntntPlcHldr$ddlDept': 'COE'
    }
url = "https://registrar.kfupm.edu.sa/CourseOffering"

response = requests.post(url, data=payload)
soup = BeautifulSoup(response.text, 'html.parser')
listTest = []

for row in soup.find_all("div", class_="trow"):
    listTest.append([]) #creating list of lists of each course
    
    for inner in row.find_all("div", class_="tdata"):
        index = inner.text.index(":")
        tagContent = inner.text[index+1:] #slicing to get only content
        listTest[len(listTest) - 1].append(tagContent) #appending to end of list

# for x in listTest:
#     print(x)