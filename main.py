import os
import cv2
from argparse import ArgumentParser


def main(p):
    file_images = []
    refPt = []
    centrePt = []
    cropping = False
    overall_rect = []
    overall_circl = []
    j = 0
    save_file = {}
    extension = 'google-roi.jpeg'

    # mypath = p.imageDir  # '/home/shreyas/PycharmProjects/final_code'
    # save_path = p.saveDir  # '/home/shreyas/PycharmProjects/final_code/sample'
    #

    for dirName, subDirList, fileList in os.walk(p.imageDir):

    onlyfiles = [f for f in os.listdir(p.imageDir) if f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.png')]

    # os.chdir(mypath)
    # for i in onlyfiles:
    #     if i.endswith('.jpeg') or i.endswith('.jpg') or i.endswith('.png'):
    #         file_images.append(i)

# Listening for the mouse events
def click_drag(event, x, y, flags, param):
    global refPt, cropping, overall_circl, overall_rect

    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(image, (x, y), 2, (0, 0, 255), -2)
        # cv2.rectangle(image, (x,y), (x,y),)
        centrePt.append((x, y))
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
    cv2.imshow(i, image)
    clone = image.copy()
    cv2.namedWindow(save_name)
    cv2.setMouseCallback(i, click_drag)

    while True:
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
            overall_rect.remove(refPt)
            refPt = []
            centrePt = []

    cv2.namedWindow("ROI")
    roi = clone[overall_rect[j][0][1]:overall_rect[j][1][1], overall_rect[j][0][0]:overall_rect[j][1][0]]
    cv2.imshow("ROI", roi)
    os.chdir(save_path)
    cv2.imwrite(save_name + extension, roi)
    os.chdir(mypath)
    cv2.waitKey(0)
    cv2.destroyWindow("ROI")
    j += 1


def saveCordinates():

    f = open("co_ordinates-1.txt", 'a')
    f.write("{}\n".format(save_file))
    q = open("rectangular_coord.txt", 'a')
    q.write("{}\n".format(overall_rect))
    f.close()
    q.close()


if __name__ == '__main__':
    args = ArgumentParser()
    args.add_argument('--imageDir', type=str, required=True, help='Directory containing images')
    args.add_argument('--saveDir', type=str, required=True, help='Directory name to save images.')
    p = args.parse_args()
    main(p)
    cv2.destroyAllWindows()
