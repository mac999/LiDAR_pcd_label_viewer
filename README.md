# Description
pcd_label_viewer. 3D point cloud label dataset viewer
<br/>
p.s. there is good tool such as cloudcompare but it's difficult to load and visualize labeling dataset, so I added some functions by using Open3D library.
<br/>
1. labeling point cloud dataset
<img src="https://github.com/mac999/pcd_label_viewer/blob/main/img/img2.png" alt="screen" width="300">
<img src="https://github.com/mac999/pcd_label_viewer/blob/main/img/img3.png" alt="screen" width="500">
2. view point cloud with label 
<img src="https://github.com/mac999/pcd_label_viewer/blob/main/img/img1.png" alt="screen" width="500">

# Install
pip install open3d
<br/>
git clone https://github.com/mac999/pcd_label_viewer

# Functions
Load and visualize point cloud dataset, label data, mesh file

# Support file format
.labels for labeling data
.ply .stl .fbx .obj .off .gltf .glb
Triangle mesh files (.ply, .stl, .fbx, .obj, .off, .gltf, .glb)
.txt .xyz .xyzn .xyzrgb .ply .pcd .pts
Point cloud files (.txt, .xyz, .xyzn, .xyzrgb, .ply, .pcd, .pts)

# Run
python pcd_label_viewer.py

# Author
Taewook Kang (laputa99999@gmail.com).
<br/>
MIT license.
