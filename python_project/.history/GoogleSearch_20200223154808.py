from googleapiclient.discovery import build
my_api_key = "AIzaSyCPwsAIim2Ng3ymF4NlmopC3ATQ-oQU3oc"
my_cse_id = "003639206582496359336:lgzfdwdn2kb"

def google_search(parmsSearch):
    service = build("customsearch", "v1", developerKey=my_api_key)
    res = service.cse().list(
      q=parmsSearch, 
      cx=my_cse_id,
      ).execute()
    print(res)

google_search("Cervantes books")
