import cv2
import numpy as np


def main():
    img = cv2.imread("data/chinese.png")
    cv2.imshow("img", img)

    cnt = np.array([
            [[64, 49]],
            [[122, 11]],
            [[391, 326]],
            [[308, 373]]
        ])
    # find the exact rectangle enclosing the text area
    # rect is a tuple consisting of 3 elements: the first element is the center
    # of the rectangle, the second element is the width, height, and the
    # third element is the detected rotation angle.
    # Example output: ((227.5, 187.50003051757812),
    # (94.57575225830078, 417.98736572265625), -36.982906341552734)
    rect = cv2.minAreaRect(cnt)
    print("rect: {}".format(rect))

    box = cv2.boxPoints(rect)
    box = np.int0(box)

    # print("bounding box: {}".format(box))
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
    cv2.imshow("img.jpg", img)

    # img_crop will the cropped rectangle, img_rot is the rotated image
    img_crop, img_rot = crop_rect(img, rect)
    cv2.imshow("cropped_img.jpg", img_crop)
    cv2.waitKey(0)


def crop_rect(img, rect):
    # get the parameter of the small rectangle
    center, size, angle = rect[0], rect[1], rect[2]
    center, size = tuple(map(int, center)), tuple(map(int, size))

    # get row and col num in img
    height, width = img.shape[0], img.shape[1]

    # calculate the rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, 1)
    # rotate the original image
    img_rot = cv2.warpAffine(img, M, (width, height))

    # now rotated rectangle becomes vertical and we crop it
    img_crop = cv2.getRectSubPix(img_rot, size, center)

    return img_crop, img_rot


if __name__ == "__main__":
    main()