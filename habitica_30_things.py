import requests
import pyquery

# Add complex todo in habitica

x-api-user="PRIVATE"
x-api-key="PRIVATE"

URL='https://dojo.ministryoftesting.com/dojo/lessons/30-things-every-new-software-tester-should-learn'

TASK_ID='PRIVATE'

def get_content(url):
    return requests.get(url).content

def list_tasks(content):
    pq = pyquery.PyQuery(content)
    tag = pq('h2')
    tasks = []
    for value in iter(tag):
        tasks.append(value.text[2:])
    tasks.pop()
    return tasks

def send_todo(tasks):
    habitica_task_url=f'https://habitica.com/api/v3/tasks/{TASK_ID}/checklist'
    head={
            "x-api-user": x-api-user,
            "x-api-key": x-api-key
    }
    for key in iter(tasks):
        entry = {"text": key}
        resp = requests.post(url=habitica_task_url, data=entry, headers=head)

goat = get_content(URL)
meat = list_tasks(goat)
send_todo(meat)
