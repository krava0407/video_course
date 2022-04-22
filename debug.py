data1 = ['WorkSpace', 'React', 'Angular', 'Veu', 'Classified', 'General', 'Downloads', 'Word File.doc',
         'Excel File.doc']
data2 = ['workspace', 'react', 'angular', 'veu', 'classified', 'general', 'downloads', 'wordFile', 'excelFile']

data1 = str(data1).replace(' ', '').lower().replace('.doc', '')
print(data1)
data2 = str(data2).lower().replace(' ', '')
print(data2)
assert data1 == data2
