import cv2

print("请输入文件名：")
root = input()
crop_size = (1080, 719)
img = cv2.imread(root)
img_new = cv2.resize(img, crop_size, interpolation=cv2.INTER_CUBIC)
cv2.imwrite(root,img_new)