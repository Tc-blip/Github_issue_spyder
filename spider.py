import sys
import urllib.request
import requests
import json
'''
issue_dict = { key:value}  where key is issue title, value is class Repositories

title:
    number
    title
    status
    create_time
    closed_time
    []            Labels name list  EX: ['bug','sample']
    body          

'title': title,
                      'body': body,
                      'created_at': created_at,
                      'closed_at': closed_at,
                      'updated_at': updated_at,
                      'assignee': assignee,
                      'milestone': milestone,
                      'closed': closed,
                      'labels': labels}}
'''
issue_dict = {}

class Repositories:
    def __init__(self,number,title,status,create_time,closed_time,body):
        self.issue_number = number
        self.issues_title = title
        self.issues_status = status
        self.create_time = create_time
        self.closed_time = closed_time
        self.label_name_list = []            #Labels may have a lot
        self.issue_body = body



def get_issue_json(url):
    r=requests.get(url)
    return r.json()

def read_json(url):
    file = get_issue_json(url)
    for i in file:
        issue_dict[i["title"]] = Repositories(i["number"],i["title"],i["state"],i["milestone"]["created_at"],i["milestone"]["closed_at"],i['body'])

        # append label name to label list
        for j in i["labels"]:
            issue_dict[i["title"]].label_name_list.append(j["name"])

  

if __name__=="__main__":
    url="https://api.github.com/repos/Tc-blip/ssw599/issues"
    read_json(url)
    print(issue_dict)

    