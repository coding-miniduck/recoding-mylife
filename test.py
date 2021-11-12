import json


with open('struct.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)

length_body = len(data['content'])
pr_text = []
for i in range(length_body):
    pr_text.append('')
    print(type(data))
    length_text = len(data['content'][i]['text'])
    for j in range(length_text):
        pr_text[i] += data['content'][i]['text'][j]

print(pr_text)