---
youtubeId: watch?v=-0QIr6Nv1Yo
---

### Selfies with sunglasses

This dataset is a collection of images of selfies with sunglasses. The dataset contains 2768 unannotated images and a total of 5536 images.
The repository also has the code for iamge annotation.

{{% include youtubePlayer.html id=page.youtubeId %}}

## Usage:
```
python main.py --imageDir "directory containing images" --saveDir "name of directory to save cropped images"
```
Example:
```
python main.py --imageDir selfies-sunglasses/ --saveDir test
```

To annotate the image,<br>
1. left-click the mouse and drag across the image where you wish to draw the box.<br>
2. To save the coordinates of each box drawn, press 's' key. <br>
3. To re-draw the rectangle press 'r' key.<br>
4. To show the next image, press 'n' key.<br>
5. To stop the program press 'q' key. <br>

- [x] Saving multiple cordinates for a single image.<br>
- [x] Saving cropped images for multiple cordinates from same image.<br>
- [x] Reset coordinates.

After completing annotation, the script creates two directories. One containing the cropped images and the
other containing the pickled coordinates. <br>

If you have any questions, please email me at shreyas0906@gmail.com
