from pylab import *

image = imread('voilier.jpg')

def permute(ima2):
    image=ima2.copy()
    n = len(image)
    temp = copy(image[n//2:, :n//2])
    image[n//2:, :n//2] = image[n//2:, n//2:]
    image[n//2:, n//2:] = image[:n//2, n//2:]
    image[:n//2, n//2:] = image[:n//2, :n//2]
    image[:n//2, :n//2] = temp
    return image

image2 = permute(image)
subplot(1, 2, 1)
imshow(image)
subplot(1, 2, 2)
imshow(image2)

show()