for i in range(1,285):
    with open ('./data_3/ijp{}.txt'.format(i), 'rt', encoding='utf-8')as file_read:
        with open('./urls/ijp{}.txt'.format(i), 'w')as file_write:
            for line in file_read.readlines():
                if line.startswith('https'):
                    line = line.lower()
                    if line.find('(') != -1:
                        print('https://sci.bban.top/pdf/' + line[16:34] + '%2528' + line[35:37] + '%2529' + line[-9:-2] + '.pdf?download=true',
                              file=file_write)
                    else:
                        print('https://sci.bban.top/pdf/' + line[16:-2] + '.pdf?download=true', file=file_write)

#10.1016/j.jallcom.2019.153073
#https://doi.org/10.1016/j.pmatsci.2020.100671.
#https://doi.org/10.1016/S0079-6425(20)30043-8.
#https://sci.bban.top/pdf/10.1016/s0925-8388%252803%252900420-1.pdf?download=true