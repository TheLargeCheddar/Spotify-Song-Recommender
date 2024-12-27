import pandas as pd

tracks = pd.read_csv('C:/Users/jack3/Downloads/CPTS_315_REPOS/RealProj315/result.csv')
#to filter out more obscure results...
tracks = tracks[tracks.popularity > 50]

#the song id's can be found as the first 22 digit sequence of characters following '..track/' in the URL
# sample input(enter this sequence): 1xK1Gg9SxG8fy2Ya373oqb,1xQ6trAsedVPCdbtDAmk0c,7ytR5pFWmSjzHJIeQkgog4,079Ey5uxL04AKPQgVQwx5h,0lizgQ7Qw35od7CYaoMBZb,7r9ZhitdQBONTFOiJW5mr8,3ee8Jmje8o58CHK66QrVC2,3ZG8N7aWw2meb6UrI5ZmnZ,5cpJFiNwYyWwFLH0V6B3N8,26w9NTiE9NGjW1ZvIOd1So,7BIy3EGQhg98CsRdKYHnJC,2374M0fQpWi3dLnB54qaLX,2IVsRhKrx8hlQBOWy4qebo,40riOy7x9W7GXjyGp4pjAv,4evmHXcjt3bTUHD1cvny97,0MF5QHFzTUM2dYm6J7Vngt,0TrPqhAMoaKUFLR7iYDokf,07KXEDMj78x68D884wgVEm,6gxKUmycQX7uyMwJcweFjp
ids = input('Enter comma-separated ids of your favorite songs\n> ').strip().split(',')

# search the specified ids in this dataset and get the tracks
favorites = tracks[tracks.id.isin(ids)]

# code to sort find out the maximum occuring cluster number according to user's favorite track types
cluster_numbers = list(favorites['type'])
clusters = {}
for num in cluster_numbers:
  clusters[num] = cluster_numbers.count(num)

# sort the cluster numbers and find out the number which occurs the most
user_favorite_cluster = [(k, v) for k, v in sorted(clusters.items(), key=lambda item: item[1])][0][0]

print('\nFavorite cluster:', user_favorite_cluster, '\n')

# finally get the tracks of that cluster
suggestions = tracks[tracks.type == user_favorite_cluster]

# now print the first 5 rows of the data frame having that cluster number as their type
pd.set_option("display.max_rows", 1000, "display.min_rows", 200, "display.max_columns", None, "display.width", None)
print(suggestions.head())
