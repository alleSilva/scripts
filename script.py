import re
file1 = open('links.txt', 'w')
array_links = []

for index in range(1,11):
    with open("message({}).txt".format(index)) as file:
        for line in file:
            re_url = re.findall(r'width":1280.*\.mp4"', line)
            if re_url == []:
                array_links.append("### link not found - aula {} ###\n".format(index))
            else:
                url = re_url[0].split(",")[3]
                url= re.sub(r'.*:','https:', url)
                #url =re.sub(r'"+','', url)
                array_links.append(url[:-1] + "\n")
file1.writelines(array_links)
