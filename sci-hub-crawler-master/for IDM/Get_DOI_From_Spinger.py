import pandas as pd


for year in range(1975,2020 + 1):
    data_read = pd.read_csv('./data_3/{}.csv'.format(year))
    doi_list = data_read['Item DOI'].values
    with open('./urls/mta{}.txt'.format(year), 'w') as file_write:
        for item in doi_list:
            line = str(item).lower()
            url = 'https://sci.bban.top/pdf/' + line + '.pdf'
            print(url, file=file_write)
'''
           
            
            for line in file_read.readlines():
                if line.startswith('https'):
                    line = line.lower()
                    if line.find('(') != -1:
                        print('https://sci.bban.top/pdf/' + line[16:34] + '%2528' + line[35:37] + '%2529' + line[-9:-2] + '.pdf?download=true',
                              file=file_write)
                    else:
                        print('https://sci.bban.top/pdf/' + line[16:-2] + '.pdf?download=true', file=file_write)
                        
                        10.1007/s11661-020-05954-3

'''
#https://sci-hub.ren/10.1016/S0925-8388(00)01205-6
#https://sci.bban.top/pdf/10.1016/s0925-8388%252800%252901205-6.pdf?download=true

#10.1007/s11661-019-05118-y
#https://sci.bban.top/pdf/10.1007/s11661-019-05118-y.pdf