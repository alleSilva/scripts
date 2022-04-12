import re
file1 = open('links.txt', 'w')
array_links = []

for index in range(1,11): 
  with open("/home/alesandro/Downloads/message({}).txt".format(index)) as file:
          for line in file:
              re_url = re.findall('width":1280.*\.mp4', line)
              url = re_url[0][47:].split(",")[0]
              url= re.sub(r'.*:','https:', url)
              url =re.sub(r'"+','', url)
              array_links.append(url + "\n")

file1.writelines(array_links)