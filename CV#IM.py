import cv2
import urllib.request
import numpy as np
import os

# Here we are getting the images from the internet and rescaling them, changing them into grayscale images
# we get the negative images and the positive images
# negative images = images with anything but the object
# positive images = images with the object


def store_raw_images():
    # neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00463246'
    # neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03489162'
    # neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n09287968'
    # neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02729837'
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n13104059'
    # opening the link and reading the images
    neg_images_urls = urllib.request.urlopen(neg_images_link).read().decode()

    # if we don't have an directory
    if not os.path.exists('neg'):
        os.makedirs('neg')

    # iterating through the pictures and saving them
    pic_num = 781

    # spliting by line as on the website every new url is on  a new line
    for i in neg_images_urls.split('\n'):
        try:
            print(i)
            # getting the pictures
            urllib.request.urlretrieve(i, "neg/" + str(pic_num) + '.jpg')
            # modifying the image
            img = cv2.imread("neg/" + str(pic_num) + '.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/" + str(pic_num) + '.jpg', resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))


# store_raw_images()
# removing useless images

def find_uglies():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type) + '/' + str(img)
                    ugly = cv2.imread('uglies/' + str(ugly))
                    question = cv2.imread(current_image_path)
                    # if the images are exact same dimension
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly, question).any()):
                        print(current_image_path)
                        print('useless pic')
                        # removing the image
                        os.remove(current_image_path)

                except Exception as e:
                    print(str(e))


# find_uglies()


def create_pos_n_neg():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type + '/' + img + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)

            elif file_type == 'pos':
                line = file_type + '/' + img + ' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)

                    
create_pos_n_neg()
