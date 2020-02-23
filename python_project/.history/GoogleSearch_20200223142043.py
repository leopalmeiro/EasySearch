import pprint

from googleapiclient.discovery import build


def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build("customsearch", "v1",
            developerKey="AIzaSyCPwsAIim2Ng3ymF4NlmopC3ATQ-oQU3oc")

  res = service.cse().list(
      q='lectures',
      cx='003639206582496359336:pgfqf9m5u9e',
    ).execute()
  pprint.pprint(res)

if __name__ == '__main__':
  main()