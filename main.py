import os
import cv2
import sys
from argparse import ArgumentParser
import pickle


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
    global image, fileName, imageClone

    for fileName in imageList:

        image = cv2.imread(os.path.join(dirName, fileName))
        imageClone = image.copy()
        cv2.namedWindow(fileName)
        cv2.setMouseCallback(fileName, clickDrag)

        while True:

            cv2.imshow(fileName, image)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("n"):
                cv2.destroyWindow(fileName)
                saveCroppedImage(fileName)
                break

            if key == ord("s"):
                saveCordinates(refPt)

            elif key == ord("r"):
                image = imageClone
                cv2.setMouseCallback(fileName, clickDrag)

            elif key == ord("q"):
                cv2.destroyAllWindows()
                sys.exit()

def checkAndCreateSaveDir(p):
    saveCordinatesDir = p.saveDir + 'Coordinates'

    if not p.saveDir in os.listdir(os.getcwd()):
        os.makedirs(os.path.join(os.getcwd(), p.saveDir))

    if not saveCordinatesDir in os.listdir(os.getcwd()):
        os.makedirs(os.path.join(os.getcwd(), saveCordinatesDir))


# Listening for the mouse events
def clickDrag(event, x, y, flags, param):
    global refPt

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cv2.rectangle(image, refPt[0], refPt[1], (255, 255, 255), 1)

def saveCroppedImage(fileName):

    pklName = fileName.split('.')[0] + '.pkl'
    i = 0

    with open(os.path.join(p.saveDir + 'Coordinates', pklName), 'rb') as fp:
        pointsList = pickle.load(fp)

    for points in pointsList:
        croppedImage = imageClone[points[0][1]:points[1][1], points[0][0]:points[1][0]]
        saveName = fileName.split('.')[0] + '-' + str(i) + '.jpg'
        i+=1
        cv2.imwrite(p.saveDir + '/' + saveName, croppedImage)
        print("cropped " + str(i) + '/' + str(len(pointsList)) + " image from " + fileName.split('.')[0] + '.jpg')

def saveCordinates(rect):

    saveDir = p.saveDir + 'Coordinates'
    pklName = fileName.split('.')[0] + '.pkl'

    if os.path.exists(os.path.join(saveDir,pklName)):

        with open(os.path.join(saveDir,pklName), 'rb') as fp:
            coord = pickle.load(fp)

        coord += [rect]

        with open(os.path.join(saveDir,pklName), 'wb') as fp:
            pickle.dump(coord, fp)

    else:

        with open(os.path.join(saveDir,pklName), 'wb') as fp:
            pickle.dump([rect], fp)

if __name__ == '__main__':
    args = ArgumentParser()
    args.add_argument('--imageDir', type=str, required=True, help='Directory containing images')
    args.add_argument('--saveDir', type=str, required=True, help='Directory name to save images.')
    p = args.parse_args()
    main(p)
    cv2.destroyAllWindows()
