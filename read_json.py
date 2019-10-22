import sys
import urllib.request
import requests
import json

import openpyxl


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

    def __str__(self):
        return f"issue_body = {self.issue_body}  issue_number = {self.issue_number} issue_title = {self.issues_title} issue_status = {self.issues_status} create_time = {self.create_time} closed_time = {self.closed_time}  label_name list = {self.label_name_list}"

    def result(self):
        return f"issue_body = {self.issue_body}  issue_number = {self.issue_number} issue_title = {self.issues_title} issue_status = {self.issues_status} create_time = {self.create_time} closed_time = {self.closed_time}  label_name list = {self.label_name_list}"

    def result_xl(self):
        return self.issue_body,self.issue_number,self.issues_title,self.issues_status,self.create_time,self.closed_time,str(self.label_name_list)

def write07Excel(path,value):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(value.result_xl())
    wb.save(path)


def open_json(path):
    try:
        fp = open(path,'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't open {path}")
    else:
        with fp:
            return json.load(fp)

def read_json(path):
    file = open_json(path)
    for i in file:
        issue_dict[i["title"]] = Repositories(i["number"],i["title"],i["state"],i["milestone"]["created_at"],i["milestone"]["closed_at"],i['body'])

        # append label name to label list
        for j in i["labels"]:
            issue_dict[i["title"]].label_name_list.append(j["name"])


if __name__=="__main__":
    path="ss.json"
    read_json(path)

    for i in issue_dict.values():
        write07Excel("opensss.xlsx",i)
    
    