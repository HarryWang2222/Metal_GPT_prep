import pandas as pd

names = locals()
for num in range(2000, 2022):
    names['doi_list_%s' % num] = list()

for i in range(1,5):
    data_read = pd.read_csv('./data_5/pm{}.csv'.format(i))
    year_list = data_read['Volume year'].values
    csv_doi_list = data_read['DOI'].values
    for ind in range(0, len(year_list)):
        year = year_list[ind]
        if year in range(2000,2022):
            names['doi_list_%s' % year].append(csv_doi_list[ind])
        else:
            continue

for year in range(2000, 2022):
    with open('./pm_urls/pm{}.txt'.format(year), 'w', encoding='utf-8')as file_write:
        for line in names['doi_list_%s' % year]:
            print('https://sci.bban.top/pdf/' + str(line) + '.pdf', file=file_write)






'''

    with open ('./data_4/acmm{}.txt'.format(i), 'rt', encoding='utf-8')as file_read:
        with open('./urls/acmm{}.txt'.format(i), 'w')as file_write:
            for line in file_read.readlines():
                if line.startswith('https'):
                    line = line.lower()    #acmm1990-1994 do not need lower
                    if line.find('(') != -1:
                        # for acta metallurgica and materialia
                        print('https://sci.bban.top/pdf/' + line[16:33] + '%2528' + line[34:36] + '%2529' + line[-9:-2] + '.pdf?download=true',
                              file=file_write)
                    else:
                        print('https://sci.bban.top/pdf/' + line[16:-2] + '.pdf?download=true', file=file_write)
'''
#10.1016/j.jallcom.2019.153073
#https://doi.org/10.1016/j.pmatsci.2020.100671.
#https://doi.org/10.1016/S0079-6425(20)30043-8.
#https://sci.bban.top/pdf/10.1016/s0925-8388%252803%252900420-1.pdf?download=true

#acta metallurgica and materialia
#https://doi.org/10.1016/0956-7151(95)00132-F.