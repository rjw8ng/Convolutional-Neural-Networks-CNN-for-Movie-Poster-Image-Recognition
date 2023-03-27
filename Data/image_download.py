%%time

for i in range(len(df)):
  try:
    print('\nGet:', img_url[i])
    urllib.request.urlretrieve(str(img_url[i]), filename = f"/content/drive/MyDrive/DeepLearningData/FinalProject/{imdbId[i]}.jpg")
  except Exception as ex:
        print('Failed to download:', img_url[i], ex)
