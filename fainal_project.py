import colorgram

# 画像ファイルのパスを指定
image_path = 'path/to/your/image.jpg'

# 画像からカラー情報を抽出
colors = colorgram.extract("image.jpg", 10)  # 最大10色を抽出

c = []
for color in colors:
    rgb = color.rgb
    c.append([rgb[0], rgb[1], rgb[2]])
print(c)

colo = [[253, 251, 247], [253, 248, 252], [235, 252, 243], [198, 13, 32],
 [248, 236, 25], [40, 76, 188], [244, 247, 253],
 [39, 216, 69], [238, 227, 5], [227, 159, 49]]

