from googleapiclient.discovery import build
my_api_key = "AIzaSyCPwsAIim2Ng3ymF4NlmopC3ATQ-oQU3oc"
my_cse_id = "003639206582496359336:pgfqf9m5u9e"

def google_search(search_term, api_key, cse_id):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(
      q='coffee', 
      cx=cse_id).execute()
      pprint.pprint(res)
    return res
result = google_search('Coffee', my_api_key, my_cse_id)
print(result)

