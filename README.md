ROS2 Maze Solver Setup Guide (Ubuntu 20.04)

## 📌 Project Overview

This project simulates a robot navigating and solving a maze using:

* ROS2 Foxy
* Gazebo
* OpenCV
* Custom path planning + motion logic

---

# 🖥️ System Requirements

* Ubuntu 20.04
* ROS2 Foxy
* Python 3.8+

---

# ⚙️ Step 1: Install ROS2 Foxy

```bash
sudo apt update
sudo apt install curl gnupg lsb-release -y

sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

sudo sh -c 'echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2.list'

sudo apt update
sudo apt install ros-foxy-desktop -y
```

### Add ROS2 to environment:

```bash
echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

# 📦 Step 2: Install Dependencies

```bash
sudo apt install python3-colcon-common-extensions -y
sudo apt install python3-opencv -y
sudo apt install ros-foxy-gazebo-ros-pkgs -y
sudo apt install gazebo11 libgazebo11-dev -y
```

---

# 📁 Step 3: Clone Repository

```bash
git clone <YOUR_GITHUB_LINK>
cd ROS2-Path-Planning-and-Maze-Solving/path_planning_ws
```

---

# 🔨 Step 4: Build Workspace

```bash
colcon build --symlink-install
```

Then source:

```bash
source install/setup.bash
```

---

# ▶️ Step 5: Run the Simulation

## 🟢 Terminal 1 — Launch Gazebo + Robot

```bash
source ~/ROS2-Path-Planning-and-Maze-Solving/path_planning_ws/install/setup.bash

ros2 launch maze_bot maze_1_robot_camera.launch.py
```

---

## 🟢 Terminal 2 — Run Maze Solver

```bash
source ~/ROS2-Path-Planning-and-Maze-Solving/path_planning_ws/install/setup.bash

ros2 run maze_bot maze_solver
```

---

# 🎯 Expected Output

* Gazebo window opens with maze
* Robot spawns inside maze
* Robot starts navigating automatically
* Path planning + movement visible

---

# ⚠️ Important Notes

## ❗ Always source workspace in every new terminal

```bash
source ~/ROS2-Path-Planning-and-Maze-Solving/path_planning_ws/install/setup.bash
```

---

## ❗ If build fails

```bash
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

---

## ❗ If robot doesn’t move

Check topics:

```bash
ros2 topic list
```

---

# 🧪 Optional

## Run different maze:

```bash
ros2 launch maze_bot maze_2_robot_camera.launch.py
```

## Run RViz manually:

```bash
ros2 launch maze_bot rviz.launch.py
```

---

# 🧑‍💻 Author Notes

* Simulation runs in Gazebo
* Solver logic is in `maze_solver.py`
* Launch files only start environment (not solver)

---

# ✅ Quick Run (TL;DR)

```bash
# Terminal 1
colcon build --symlink-install
source install/setup.bash

# Terminal 2
ros2 launch maze_bot maze_1_robot_camera.launch.py

# Terminal 3
ros2 run maze_bot maze_solver
```

---

🔥 Done! Robot should now solve the maze automatically.

