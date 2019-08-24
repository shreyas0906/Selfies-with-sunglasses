import os
import cv2
from argparse import ArgumentParser


def main(p):

    for dirName, subDirList, fileList in os.walk(p.imageDir):
        processDir(dirName, fileList)

def processDir(dirName, fileList):

    imageList = []

    for imageFile in fileList:
        if imageFile.endswith('.png') or imageFile.endswith('.jpeg') or imageFile.endswith('.jpg'):
            imageList.append(imageFile)

    startProcessDir(dirName, imageList)


def startProcessDir(dirName, imageList):

    checkAndCreateSaveDir(p)

    for fileName in imageList:

        image = cv2.imread(os.path.join(dirName, fileName))
        imageClone = image.copy()
        cv2.namedWindow(fileName)
        cv2.setMouseCallback(image, clickDrag)

        while True:

            cv2.imshow(fileName, image)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("n"):
                saveCordinates(fileName)
                cv2.destroyWindow(fileName)
                break

            elif key == ord("r"):
                image = imageClone
                overallRect.remove(refPt)
                global refPt

def saveCordinates(fileName):
    
    saveDir = p.saveDir + 'coordinates'
    textName = fileName.split('.')[0] + '.txt'
    
    with open(saveDir + '/' + textName, 'w') as f:
        f.write(overallRect +'\n')
        f.write(overallCircle)

def checkAndCreateSaveDir(p):

    saveCordinatesDir = p.saveDir + 'coordinates'
    
    if not p.saveDir in os.listdir(os.getcwd()):
        os.makedirs(os.path.join(os.getcwd(), p.saveDir))
    
    if not saveCordinatesDir in os.listdir(os.getcwd()):
        os.makedirs(os.path.join(os.getcwd(), saveCordinatesDir))


# Listening for the mouse events
def clickDrag(event, x, y, flags, param):
    global refPt, cropping, overallCircle, overallRect
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(image, (x, y), 2, (0, 0, 255), -2)
        # centrePt.append((x, y))
        overallCircle.append(centrePt)

    elif event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        overallRect.append(refPt)
        cropping = False
    cv2.rectangle(image, refPt[0], refPt[1], (255, 255, 255), 2)





for i in file_images:

    file_name = i.split('.')
    save_name = file_name[0]
    image = cv2.imread(i)
    cv2.imshow(i, image)
    clone = image.copy()
    cv2.namedWindow(save_name)
    cv2.setMouseCallback(i, clickDrag)

    while True
        cv2.imshow(i, image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("n"):
            # refPt = []
            save_file[str(save_name)] = centrePt
            # centrePt = []

            cv2.destroyWindow(i)
            break
        elif key == ord("r"):
            image = clone.copy()
            overallRect.remove(refPt)
            refPt = []
            centrePt = []

    cv2.namedWindow("ROI")
    roi = clone[overallRect[j][0][1]:overallRect[j][1][1], overallRect[j][0][0]:overallRect[j][1][0]]
    cv2.imshow("ROI", roi)
    os.chdir(save_path)
    cv2.imwrite(save_name + extension, roi)
    os.chdir(mypath)
    cv2.waitKey(0)
    cv2.destroyWindow("ROI")
    j += 1

def checkCreateDir():

    if not p.saveDir in os.listdir(os.getcwd()):
        os.makedirs(os.getcwd() + '/' + p.saveDir)


if __name__ == '__main__':
    args = ArgumentParser()
    args.add_argument('--imageDir', type=str, required=True, help='Directory containing images')
    args.add_argument('--saveDir', type=str, required=True, help='Directory name to save images.')
    p = args.parse_args()
    main(p)
    cv2.destroyAllWindows()
