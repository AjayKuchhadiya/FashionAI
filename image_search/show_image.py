from similar_images import image_search
import matplotlib.pyplot as plt
import cv2

input_image = input('Please enter the path to your input image: ')

# path =  ['/kaggle/input/h-and-m-personalized-fashion-recommendations/images/010/0108775051.jpg', '/kaggle/input/h-and-m-personalized-fashion-recommendations/images/049/0496762022.jpg', '/kaggle/input/h-and-m-personalized-fashion-recommendations/images/056/0566745006.jpg', '/kaggle/input/h-and-m-personalized-fashion-recommendations/images/085/0856060003.jpg', '/kaggle/input/h-and-m-personalized-fashion-recommendations/images/078/0784143001.jpg', '/kaggle/input/h-and-m-personalized-fashion-recommendations/images/035/0355569046.jpg']

path_list = image_search(input_image.replace('\\', '/'))


x= []
for file in path_list:
    x.append('C:/FashionAI- RS/' + '/'.join(file.split('/')[4:]))

print(x)


# Display the images using Matplotlib
def show_images(image_paths):
    plt.figure(figsize=(15, 5))
    for i, img_path in enumerate(image_paths):
        img = cv2.imread(img_path)
        if img is None:
            print(f"Error: Could not load image at {img_path}")
            continue
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.subplot(1, len(image_paths), i + 1)
        plt.imshow(img)
        plt.axis('off')
    plt.show()

show_images(x)