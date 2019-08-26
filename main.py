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
    global image
    for fileName in imageList:

        image = cv2.imread(os.path.join(dirName, fileName))
        imageClone = image.copy()
        cv2.namedWindow(fileName)
        cv2.setMouseCallback(fileName, clickDrag)

        while True:

            cv2.imshow(fileName, image)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("n"):
                saveCordinates(fileName)
                cv2.destroyWindow(fileName)
                continue

            elif key == ord("r"):
                image = imageClone
                cv2.setMouseCallback(fileName, clickDrag)

            elif key == ord("q"):
                cv2.destroyWindow(fileName)
                break

def checkAndCreateSaveDir(p):

    saveCordinatesDir = p.saveDir + 'Coordinates'
    
    if not p.saveDir in os.listdir(os.getcwd()):
        os.makedirs(os.path.join(os.getcwd(), p.saveDir))
    
    if not saveCordinatesDir in os.listdir(os.getcwd()):
        os.makedirs(os.path.join(os.getcwd(), saveCordinatesDir))


# Listening for the mouse events
def clickDrag(event, x, y, flags, param):

    global refPt, centrePt, overallCircle, overallRect

    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(image, (x, y), 2, (0, 0, 255), -2)
        overallCircle.append((x,y))

    elif event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x,y)]
        print("refPt: {}".format(refPt))

    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x,y))
        cv2.rectangle(image, refPt[0], refPt[1], (255, 255, 255), 1)

def saveCordinates(fileName):
    saveDir = p.saveDir + 'coordinates'
    textName = fileName.split('.')[0] + '.txt'

    with open(saveDir + '/' + textName, 'w') as f:
        f.write(overallRect + '\n')
        f.write(overallCircle)



if __name__ == '__main__':
    args = ArgumentParser()
    args.add_argument('--imageDir', type=str, required=True, help='Directory containing images')
    args.add_argument('--saveDir', type=str, required=True, help='Directory name to save images.')
    p = args.parse_args()
    main(p)
    cv2.destroyAllWindows()
