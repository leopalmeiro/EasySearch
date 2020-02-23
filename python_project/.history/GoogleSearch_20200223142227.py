from googleapiclient.discovery import build
my_api_key = "AIzaSyCPwsAIim2Ng3ymF4NlmopC3ATQ-oQU3oc"
my_cse_id = '003639206582496359336:pgfqf9m5u9e'

def google_search():
    service = build("customsearch", "v1", developerKey="AIzaSyCPwsAIim2Ng3ymF4NlmopC3ATQ-oQU3oc")
    res = service.cse().list(
      q='lectures', 
      cx='003639206582496359336:pgfqf9m5u9e'
      ).execute()
    print(res)

google_search()

import pprint

from googleapiclient.discovery import build


def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build("customsearch", "v1",
            developerKey="AIzaSyDRRpR3GS1F1_jKNNM9HCNd2wJQyPG3oN0")

  res = service.cse().list(
      q='lectures',
      cx='017576662512468239146:omuauf_lfve',
    ).execute()
  pprint.pprint(res)

if __name__ == '__main__':
  main()