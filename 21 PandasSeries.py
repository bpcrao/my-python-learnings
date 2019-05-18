from pandas import Series

#default index
defaultSeries = Series([1,3,5,7,9])
print(defaultSeries)
print(defaultSeries[2])

#custom index
seriesCustomIndex = Series([1,3,5], index = [ 'one','three', 'five'])

print(seriesCustomIndex['three'])


#Dictiionary to series
meanings = {'joy':'happy', 'sad':'bad'}
print(meanings)
dictionarySeries = Series(meanings)
print(dictionarySeries)

#Data frames rows n columns

data = {
        'name':['purna','ramu','darshan'] ,
        'age':[37,37,37]
        'location':['vvn','kphb','kphb']
        }

from pandas import DataFrame
frame = DataFrame(data)
