from googleapiclient.discovery import build
my_api_key = "AIzaSyCPwsAIim2Ng3ymF4NlmopC3ATQ-oQU3oc"
my_cse_id = '003639206582496359336:pgfqf9m5u9e'

def google_search(search_term):
    service = build("customsearch", "v1", developerKey="AIzaSyCPwsAIim2Ng3ymF4NlmopC3ATQ-oQU3oc")
    res = service.cse().list(
      q='cervantes', 
      cx='003639206582496359336:pgfqf9m5u9e').execute()
    return res
result = google_search('cervantes')
print(result)

