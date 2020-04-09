import json
file = open('/home/viethoang/web_crawler/vnexpress_crawler/result.json','r')
contents = json.load(file)
news_file=open('/home/viethoang/web_crawler/vnexpress_crawler/new.txt','w')
print(contents)
for content in contents:
    news_file.write(content['content']+'\n')
news_file.close()