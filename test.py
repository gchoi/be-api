import base64
import cv2

img_path = '/Users/alexchoi/Downloads/blocks_candidate_CAD/2361_50G_528_2.png'

img = cv2.imread(img_path)
encoded = base64.b64encode(img)

print(type(encoded))

