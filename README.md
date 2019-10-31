Get the contents of the github issues info through the github api from closed or open issues

Grab issue_number  issues_title  issues_status create_time  closed_time  label_name_list issue_body to excel


Guide:
    change line 76 repos url, EX: https://api.github.com/repos/numpy/numpy/issues?state=closed&page={i}
    run python, input start page to end page
