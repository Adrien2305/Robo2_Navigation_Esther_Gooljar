# TP2: TurtleBot3 Waffle Pi Navigation 
                   Author : Esther Adrien, Gooljar Akash, Bhunnoo Naim
  
1. Rendez-vous sur la page Navigation du E-Manual de Robotis (pour noetic)
    - On the Remote PC, run roscore.
2. Lancer les nœuds de navigation et placer le robot sur la map que vous avez générée 
au TP précédent (ou la carte corrigée)
    ```sh
    ssh ubuntu@11.255.255.205
    export TURTLEBOT3_MODEL=waffle
    roslaunch turtlebot3_bringup turtlebot3_robot.launch
    ```
3. Lancer la Navigation sur le  pc.
    ```sh
    export TURTLEBOT3_MODEL=burger
    roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/info/map_tb5_cleaned_full.pgm
    ```
4. Créer un package move_turtle, dans ce package vous devrez créer un nœud qui va
publier sur move_base_simple/goal et envoyer des positions au turtlebot.
    ```sh
        catkin_create_pkg move_turtle rospy roscpp geometry_msgs std_mgs
    ```
5. Dans un premier temps, en utilisant rviz et le bouton 2D pose estimate, 
déterminer 3 coordonnées de point où vous enverrez le robot par la suite.
    ```sh
        rostopic echo /initialpose
    ```
    - Maintenant, on doit positioner 3 differents points en utilisant le bouton ```2D Pose Estimate ```
6. Créer un nœud goto.py ce dernier devra publier sur le topic move_base_simple/goal. Tester le nœud avec un point de la question 5a.
    ```sh
        nano goto.py(on insert le code)
        source devel/setup.bash
        chmod +x goto.py(On donne le droit d'execution)
        rosrun move_turtle goto.py
    ```