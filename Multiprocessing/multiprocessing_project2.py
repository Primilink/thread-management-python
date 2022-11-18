import time
from multiprocessing import Pool
import logging
import cv2 as cv
import os

# Relative path to the images
REL = "Multiprocessing\\"

# debugging print format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
)


def process_image(filename, threshold):  # Function to be executed in parallel
    process_id = str(os.getpid()).zfill(5)  # Get the process id
    # debugging print
    logging.debug(f'{process_id}: Processing {filename} - {threshold}')
    image = cv.imread(REL+filename)  # read image
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # convert to grayscale
    ret, thresh = cv.threshold(
        gray, threshold, 255, cv.THRESH_BINARY)  # threshold
    cv.imwrite(f'{REL+"result/"}processed_{filename}_{threshold}.jpg',
               thresh)  # save image
    logging.debug(f'{process_id}: Finished {filename} - {threshold}')


if __name__ == '__main__':
    # Create a multiprocessing Pool (if no argument is given, it will use all the cores)
    p = Pool()
    for filename in ["image.jpg", "image_2.jpg", "image_3.jpg", "image_4.jpg", "image_5.jpg"]:
        for thresh in range(0, 256, 1):  # for each threshold
            # apply the function to the image
            p.apply_async(process_image, args=(filename, thresh))
    p.close()  # close the pool
    p.join()  # wait for all processes to finish
