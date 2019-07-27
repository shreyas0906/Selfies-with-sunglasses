import os
import cv2
from os import listdir
from os.path import isfile, join

file_images = []
refPt = []
centrePt = []
cropping = False
overall_rect = []
overall_circl = []
j = 0
save_file = {}
extension = 'google-roi.jpeg'
mypath = '/home/crcv/Documents/final_code_1/selfies-sunglasses/selfies_7'
save_path = '/home/crcv/Documents/final_code_1/selfies-sunglasses/selfies_7/saved_images'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
os.chdir(mypath)

for i in onlyfiles:
    if i.endswith('.jpeg') or i.endswith('.jpg') or i.endswith('.png'):
        file_images.append(i)

print file_images
print len(file_images)

def click_drag(event, x, y, flags, param):

    global refPt, cropping, overall_circl, overall_rect

    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(image,(x,y),2,(0,0,255),-2)
        centrePt.append((x,y))
        overall_circl.append(centrePt)

    elif event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        overall_rect.append(refPt)
        cropping = False
    cv2.rectangle(image, refPt[0], refPt[1], (255, 255, 255), 2)

for i in file_images:
    file_name = i.split('.')
    save_name = file_name[0]
    image = cv2.imread(i)
    cv2.imshow(i,image)
    clone = image.copy()
    image_name = i
    cv2.namedWindow(image_name)
    cv2.setMouseCallback(image_name,click_drag)

    while True:
        cv2.imshow(i, image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("n"):
            refPt = []
            save_file[str(save_name)] = centrePt
            centrePt = []
            print save_file
            cv2.destroyWindow(i)
            break
        elif key == ord("r"):
            image = clone.copy()
            overall_rect.remove(refPt)
            refPt =[]
            centrePt = []

    cv2.namedWindow("ROI")
    roi = clone[overall_rect[j][0][1]:overall_rect[j][1][1],overall_rect[j][0][0]:overall_rect[j][1][0]]
    cv2.imshow("ROI",roi)
    os.chdir(save_path)
    cv2.imwrite(save_name + extension, roi)
    print centrePt
    # save_file[str(i)] = str(centrePt)
    # print save_file
    os.chdir(mypath)
    cv2.waitKey(0)
    cv2.destroyWindow("ROI")
    j+=1

    print j


f = open("co_ordinates-1.txt",'a')
f.write("{}\n".format(save_file))
q = open("rectangular_coord.txt",'a')
q.write("{}\n".format(overall_rect))
f.close()
q.close()

print "rectangle  points: ", overall_rect
print "circle centre:" , overall_circl
print "length of circle", len(overall_circl)
print save_file
cv2.destroyAllWindows()

