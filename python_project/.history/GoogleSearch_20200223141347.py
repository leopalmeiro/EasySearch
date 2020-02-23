from googleapiclient.discovery import build
my_api_key = "AIzaSyCPwsAIim2Ng3ymF4NlmopC3ATQ-oQU3oc"
my_cse_id = "003639206582496359336:pgfqf9m5u9e"

def google_search(search_term):
    service = build("customsearch", "v1", developerKey=my_api_key)
    res = service.cse().list(
      q=search_term, 
      cx=my_cse_id).execute()
    return res
result = google_search('Coffee')
print(result)

