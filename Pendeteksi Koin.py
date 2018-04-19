from SimpleCV import *
quarterSize = 24.26 #mm
sizeRatio = 0
objectSize = 0
Total = 0
Coin = 0
img = Image('coins.png', sample=True)
segmented = img.hueDistance(Color.BLACK)
coins = img.invert().findBlobs(minsize=200)
#mencari diameter koin
if coins:
    c = coins[-1]
    diameter = c.radius() * 2
    sizeRatio = quarterSize / diameter

for coin in coins:
    Coin += 1
    size = (coin.radius() * 2) * sizeRatio
    #Definisi nama koin dan hitung jumlah total koin berdasarkan sizenya
    if size > 18 and size < 20:
        text = "Type: penny"
        Total += 3 
    elif size > 20 and size < 23:
        text = "Type: nickel"
        Total += 1
    elif size > 16 and size < 18:
        text = "Type: dime"
        Total += 5
    elif size > 23 and size < 26:
        text = "Type: quarter"
        Total += 4
    else:
        text = "unknown"
        Total += 2
    #Print nama koin dan ukurannya    
    text = text + ", Size:" + str(size) + "mm"
    img.drawText(text, coin.x, coin.y)

img.show()
print "Jumlah Koin :", Coin, "Koin"
print "Total Koin :", Total, "Sen"

