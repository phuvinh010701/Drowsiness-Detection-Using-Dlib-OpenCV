[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fphuvinh010701%2FDrowsiness-Detection-Using-Dlib-OpenCV&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=views&edge_flat=false)](https://hits.seeyoufarm.com)
# Real-time Drowsiness Detection Using Dlid and OpenCV
---
## Install packages

Ubuntu

<pre>
$ wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
$ bzip2 -dk shape_predictor_68_face_landmarks.dat.bz2
$ rm shape_predictor_68_face_landmarks.dat.bz2
</pre>
* Install packages for dlib
<pre>
$ sudo apt-get install build-essential cmake
$ sudo apt-get install libgtk-3-dev
$ sudo apt-get install libboost-all-dev
</pre>

* Install prerequisites packages
<pre>
pip install -r requirements.txt
</pre>

## Run 

Ubuntu

<pre>
python3 drowsiness_detection.py
</pre>
---
<img src='images/chart.png' style='display: block; margin-left: auto;margin-right: auto;'>

### EAR equation:

<img src='images/blink_detection_plot.jpg' style='width:50%;display: block; margin-left: auto;margin-right: auto; '>

<img src='images/blink_detection_equation.jpg' style='width:50%; display: block; margin-left: auto;margin-right: auto;'>

* source: [Real-Time Eye Blink Detection using Facial Landmarks](http://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf)

### Demo
<img src='images/example.gif' style='width:50%;display: block; margin-left: auto;margin-right: auto; '>