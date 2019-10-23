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
    def result_txt(self):
        return f"issue_body = {self.issue_body}  issue_number = {self.issue_number} issue_title = {self.issues_title} issue_status = {self.issues_status} create_time = {self.create_time} closed_time = {self.closed_time}  label_name list = {self.label_name_list}"

    def result_xl(self):
        return self.issue_body,self.issue_number,self.issues_title,self.issues_status,self.create_time,self.closed_time,str(self.label_name_list)



def get_issue_json(url):
    r=requests.get(url)
    return r.json()

def read_json(url):
    file = get_issue_json(url)
    for i in file:
        issue_dict[i["title"]] = Repositories(i["number"],i["title"],i["state"],i["created_at"],i["closed_at"],i['body'])

        # append label name to label list
        for j in i["labels"]:
            issue_dict[i["title"]].label_name_list.append(j["name"])

def write07Excel(path,value,sheet):

    sheet.append(value.result_xl())
    wb.save(path)


if __name__=="__main__":
    
    start = input("input page start number: ")
    end = input("input page end number: ")

    for i in range(int(start),int(end)):
        url=f"https://api.github.com/repos/numpy/numpy/issues?state=closed&page={i}"
        read_json(url)
        print('processing %d out od %d items...'%(i+1,int(end)),'\r',end='')

    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["issue_body","issue_number","issues_title","issues_status","create_time","closed_time","label_name_list"])
    for i in issue_dict.values():
        write07Excel(f"closed_{start}_{end}.xlsx",i,sheet)

    #https://api.github.com/repos/numpy/numpy/issues?state=closed&page={i}          get closed issues
    #https://api.github.com/repos/numpy/numpy/issues?page={i}&q=is%3Aissue+is%3Aopen
   
    