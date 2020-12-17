import os
import cv2


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

imgaray = load_images_from_folder("Data/zz_bloomers")
imageIndex = 0
dsize = (128, 128)

for img in imgaray:
    dst = img
    img = cv2.resize(img, (128, 128))
    cv2.imwrite( "Augmented/photo" + str(imageIndex) + ".jpg", img)
    img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite( "Augmented/photo90Clockwise" + str(imageIndex) + ".jpg", img_rotate_90_clockwise)
    img_rotate_90_counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite( "Augmented/photo90ConterClockwise" + str(imageIndex) + ".jpg", img_rotate_90_counterclockwise)
    img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
    cv2.imwrite( "Augmented/photo180" + str(imageIndex) + ".jpg", img_rotate_180)
    img_flip_ud = cv2.flip(img, 0)
    cv2.imwrite( "Augmented/photoFlipVertical" + str(imageIndex) + ".jpg", img_flip_ud)
    img_flip_lr = cv2.flip(img, 1)
    cv2.imwrite( "Augmented/photoFlipHorizontal" + str(imageIndex) + ".jpg", img_flip_lr)
    img_flip_ud_lr = cv2.flip(img, -1)
    cv2.imwrite( "Augmented/photoFlipBoth" + str(imageIndex) + ".jpg", img_flip_ud_lr)
    grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite( "Augmented/Grayscalephoto" + str(imageIndex) + ".jpg", grayScale)
    img_rotate_90_clockwise = cv2.rotate(grayScale, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite( "Augmented/Grayscalephoto90Clockwise" + str(imageIndex) + ".jpg", img_rotate_90_clockwise)
    img_rotate_90_counterclockwise = cv2.rotate(grayScale, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite( "Augmented/Grayscalephoto90ConterClockwise" + str(imageIndex) + ".jpg", img_rotate_90_counterclockwise)
    img_rotate_180 = cv2.rotate(grayScale, cv2.ROTATE_180)
    cv2.imwrite( "Augmented/Grayscalephoto180" + str(imageIndex) + ".jpg", img_rotate_180)
    img_flip_ud = cv2.flip(grayScale, 0)
    cv2.imwrite( "Augmented/GrayscalephotoFlipVertical" + str(imageIndex) + ".jpg", img_flip_ud)
    img_flip_lr = cv2.flip(grayScale, 1)
    cv2.imwrite( "Augmented/GrayscalephotoFlipHorizontal" + str(imageIndex) + ".jpg", img_flip_lr)
    img_flip_ud_lr = cv2.flip(grayScale, -1)
    cv2.imwrite( "Augmented/GrayscalephotoFlipBoth" + str(imageIndex) + ".jpg", img_flip_ud_lr)

    imageIndex = imageIndex + 1

