# ROS_demo  
##千葉工業大学 2016年 ロボットシステム学 課題2 提出用  

---

###概要
[2016年度ロボットシステム学](http://lab.ueda.asia/?page_id=1152)の課題2  

---

###課題の内容  
- ROS(Robot Operating System)でなにか作る
- Youtube等にデモをアップする
- 電子メールで報告する

---

###行ったこと  
- ROSのシミュレータGazebo上でkobukiというロボットを動かした
- [Youtubeリンク](https://www.youtube.com/watch?v=xTsugC_q2-4)

---

###シミュレータの実行方法  
####環境 
- PC : Ubuntu14.04 Desktop
- ROS : ROS Indigo  

gazeboにkobukiをインストール
```
$ sudo apt-get install ros-indigo-kobuki-gazebo
```
起動
```
$ roslaunch kobuki_gazebo kobuki_empty_world.launch
```

---

###参考  
####小倉祟 著 工学社 I/O BOOKS 「ROSではじめるロボットプログラミング」 
第8章 「シミュレータ」上の「ロボット」を動かす
