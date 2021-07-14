#
**<H1 align = "center">Virtual Painter</H1>**

## Description

**Author** : Susovan Das

**Language** : Python  

**External Module** : [OpenCV][opencv], [Numpy][numpy], [MediaPipe][mediapipe]


![Virtual Painter](/Assets/virtual_painter.gif)

This is GUI Applications where we are drawing on the canvas by moving our hand. This app use our hand as the pointer and draw how our hand moves. This App is Created using _Tkinter_ for the GUI part, for hand and it's landmarks detection we use _Mediapipe_ and for other image related things we use _OpenCV_ Module.

## How to Use

You can use the Command Prompt/Terminal and go to the location of the _virtual_painter.py_ and type `python virtual_painter.py.`

* Use the **Start Button** to start the Hand detection
* For change the color press the **Color Bucket icon**
* For Eraser use the **Eraser icon**
* For display the Hand Landmarks press **Show Hand Button**
* You can increase or decrease pen size use the **+/- Button**
* For clear the canvas the use **Trash icon**

### Key Binding

* Save the Canvas as image : <Control + s>
* Clear the Canvas : <Control + Shift + c>
* Toggle display for the Hand Landmarks : <Control + h>

## How to Download

To download all this projects Click this --> &nbsp; &nbsp; [<img src="https://github.com/DasBabuGH/Virtual-Painter/blob/master/Assets/.download_icon.png" width="20" height="20"/>][DownGit]

## Requirements

This project requir some external modules.
* OpenCV
* Numpy
* MediaPipe

So use the package manager [pip](https://pypi.org/project/pip/) to install those package.

```bash
pip install opencv-python
pip install numpy
pip install mediapipe
```

<br>
<h3 align = "center"> Show some ❤️ by starring this repository!</h3>

<!--Inner Links-->
[opencv]: https://opencv.org/

[numpy]: https://numpy.org/

[mediapipe]: https://mediapipe.dev/

[DownGit]: https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/DasBabuGH/Virtual-Painter/
