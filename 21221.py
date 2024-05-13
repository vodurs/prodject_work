from os import strerror
exet=''
g=''
o=[]
src_name = input('ведите имя файла')
while exet =='quit':
    src_name = input('ведите имя файла')
    try:
        src_file = open(src_name,'r')
    except:
        print(f'не удалось открыть{strerror(IOError.errno)}')
    try:
        chr = '0'
        g+=' '
        count_chr=1
        while chr !='':
            chr = src_file.read(1)
            g+=chr 
        print(f'готово сим {count_chr}')
    except:
        print(f'{strerror(IOError.errno)}')
    src_file.close()
    o.append(g)
    g=''
    exet =input('введите quit есди хотите выйти ')
for i in o:
    for




