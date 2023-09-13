with open('./data/sm content.txt', 'r',encoding='utf-8')as content_file:
    for content_line in content_file.readlines():
        content_line = content_line[:-1]
        year = int(content_line[0:4])
        start = int(content_line[5:7])
        end = int(content_line[8:10])
        with open('./urls/{}.txt'.format(year), 'w',encoding='utf-8')as output:
            for i in range(start, end+1):
                with open('./urls/sm{}.txt'.format(i), 'rt',encoding='utf-8')as sigle_file:
                    print(sigle_file.read(), file=output)


