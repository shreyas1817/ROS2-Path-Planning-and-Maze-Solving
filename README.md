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

# Select maze using maze_id:=1 or maze_id:=2 (default is 2)
ros2 launch maze_bot maze_1_robot_camera.launch.py maze_id:=2
```

---

## 🟢 Terminal 2 — Run Maze Solver

```bash
source ~/ROS2-Path-Planning-and-Maze-Solving/path_planning_ws/install/setup.bash

# Select planner_method:=a_star or planner_method:=dijkstra
ros2 run maze_bot maze_solver --ros-args -p planner_method:=a_star
```

### Keyboard controls in Maze (Live) window

```text
1      -> switch planner to Dijkstra
2      -> switch planner to A*
Space  -> start robot motion
Enter  -> start robot motion
R      -> pause robot motion
```

Note: The planner selection and start/pause are now available from the UI overlay in the live window.

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

## ❗ WSL Run Commands (Used During Debugging)

If you are running in WSL Ubuntu 22.04 with ROS2 Humble:

```bash
cd /mnt/c/Users/shrey/shre/sem6/MAR/ROS2-Path-Planning-and-Maze-Solving/path_planning_ws
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
```

Launch order:

```bash
# Terminal 1
source /opt/ros/humble/setup.bash
cd /mnt/c/Users/shrey/shre/sem6/MAR/ROS2-Path-Planning-and-Maze-Solving/path_planning_ws
source install/setup.bash
ros2 launch maze_bot maze_1_robot_camera.launch.py

# Terminal 2
source /opt/ros/humble/setup.bash
cd /mnt/c/Users/shrey/shre/sem6/MAR/ROS2-Path-Planning-and-Maze-Solving/path_planning_ws
source install/setup.bash
ros2 run maze_bot maze_solver
```

If you see `RTPS_TRANSPORT_SHM` errors, clean stale shared memory and restart:

```bash
pkill -f gazebo || true
pkill -f gzserver || true
pkill -f gzclient || true
pkill -f ros2 || true
rm -rf /dev/shm/fastrtps_* /dev/shm/fastdds_* 2>/dev/null || true
```

If you see `Unable to start server[bind: Address already in use]` for Gazebo:

```bash
pkill -f gzclient || true
pkill -f gzserver || true
pkill -f gazebo || true
pkill -f "ros2 launch" || true
pkill -f maze_solver || true
```

If needed, force kill:

```bash
pkill -9 -f gzclient || true
pkill -9 -f gzserver || true
pkill -9 -f gazebo || true
pkill -9 -f "ros2 launch" || true
pkill -9 -f maze_solver || true
```

Check Gazebo master port is free (`11345`):

```bash
ss -lntp | grep 11345 || true
```

Optional DDS fallback in same terminal before launch:

```bash
export ROS_LOCALHOST_ONLY=1
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
```

---

## ❗ If `git push origin main` is rejected (fetch first)

```bash
git fetch origin
git rebase origin/main
git push origin main
```

Optional default setting to use rebase on pull:

```bash
git config --global pull.rebase true
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

