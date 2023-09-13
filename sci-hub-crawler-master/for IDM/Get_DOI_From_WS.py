
# for i in range(1,64):
#     with open ('./data/jac{}.txt'.format(i), 'rt', encoding='utf-8')as file_read:
#         with open('./urls/jac{}.txt'.format(i), 'w')as file_write:
#             for line in file_read.readlines():
#                 if line.startswith('DI'):
#                     print('https://sci.bban.top/pdf/' + line[3:-1] + '.pdf?download=true', file=file_write)

#https://sci.bban.top/pdf/10.1016/j.jallcom.2019.153073.pdf?download=true


for i in range(54,57):
    with open ('./data/jac{}.txt'.format(i), 'rt', encoding='utf-8')as file_read:
        with open('./urls/jac{}.txt'.format(i), 'w')as file_write:
            for line in file_read.readlines():
                if line.startswith('DI'):
                    line = line.lower()
                    if line.find('(') != -1:
                        print('https://sci.bban.top/pdf/' + line[3:21] + '%2528' + line[22:24] + '%2529' + line[-8:-1] + '.pdf?download=true',
                              file=file_write)
                    else:
                        print('https://sci.bban.top/pdf/' + line[3:-1] + '.pdf?download=true', file=file_write)




#DOI before 2003
#10.1016/S0925-8388(03)00420-1
#https://sci.bban.top/pdf/10.1016/s0925-8388%252803%252900420-1.pdf?download=true
#10.1016/S0925-8388(03)00323-2
#https://sci.bban.top/pdf/10.1016/s0925-8388%252803%252900323-2.pdf?download=true
#10.1016/S0925-8388(02)01132-5
#https://sci.bban.top/pdf/10.1016/s0925-8388%252802%252901132-5.pdf?download=true
#https://sci-hub.ren/10.1016/S0925-8388(00)01205-6
#https://sci.bban.top/pdf/10.1016/s0925-8388%252800%252901205-6.pdf?download=true
#https://sci.bban.top/pdf/10.1016/s1359-6454%252803%252900387-2.pdf?download=true
#https://sci.bban.top/pdf/10.1016/s1359-6454%252803%252900387-2.pdf?download=true
