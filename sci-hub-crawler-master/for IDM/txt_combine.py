import re

with open('./data/sm content.txt', 'r',encoding='utf-8')as content_file:
    for content_line in content_file.readlines():
        content_line = content_line[:-1]
        if len(content_line) < 4:
            break
        content_split = re.split('\s|-', content_line)
        year = int(content_split[0])
        start = int(content_split[1])
        end = int(content_split[2])
        with open('./urls/{}.txt'.format(year), 'w', encoding='utf-8')as output:
            for i in range(start, end+1):
                with open('./urls/sm{}.txt'.format(i), 'rt',encoding='utf-8')as sigle_file:
                    print(sigle_file.read(), file=output)
                    print('test', file=output)
