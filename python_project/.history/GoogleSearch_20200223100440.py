from googlesearch.googlesearch import GoogleSearch
response = GoogleSearch().search("coffe")
for result in response.results:
    print("Title: " + result.title)
    print("Content: " + result.getText())