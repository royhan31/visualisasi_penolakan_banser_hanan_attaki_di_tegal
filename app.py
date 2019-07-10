import pandas as pd

data = pd.read_csv('hasil_crawl.csv')
COLNAMES = ['id','tweet','screen_name']
data.columns = COLNAMES

#print(data)

#jumlah per kata
freq_word = pd.Series(' '.join(data['tweet']).split()).value_counts()
print('Jumlah perkata : \n'+str(freq_word))

#bersihkan tweet duplikat
data_not_duplicate = data.drop_duplicates(['tweet'])
print('heheh')
dfx = data.duplicated()
dfx.to_csv("kontoru.csv")
print(x['tweet'])
print('########')

#jumlah data duplikat
print('jumlah data duplikat : '+str(len(data) - len(data_not_duplicate)))

#jumlah data tidak duplikat
print('data tidak duplikat : '+str(len(data_not_duplicate)))

#jumlah data asli
print('jumlah data asli : '+str(len(data)))
#print(data_not_duplicate)

#jumlah tweet per user
print('data tweet per user : \n'+str(data['screen_name'].value_counts()))
