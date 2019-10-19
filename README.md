# Selfies with sunglasses.

![alt text](https://github.com/shreyas0906/Selfies-with-sunglasses/blob/master/dataset-original.jpg)

This dataset is a collection of images of selfies with sunglasses. The dataset contains 2768 unannotated images and a total of 5536 images. The repository also has the code for annotation. https://www.youtube.com/watch?v=-0QIr6Nv1Yo

Usage: 
```
python main.py --imageDir "directory containing images" --saveDir "name of directory to save cropped images" 
```
Example: 
```
python main.py --imageDir selfies-sunglasses/ --saveDir test
```
To annotate the image,<br>
1. left-click the mouse and drag across the image where you wish to draw the box.<br>
2. To save the coordinates press 's' key. <br>
2. To re-draw the rectangle press 'r' key.<br>
3. To show the next image, press 'n' key.<br>

- [x] Saving multiple cordinates for a single image.<br>
- [ ] Saving cropped images for multiple cordinates from same image.<br> 

If you have any question, please email me at shreyas0906@gmail.com

