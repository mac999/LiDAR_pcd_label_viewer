# Description
pcd_label_viewer. 3D point cloud label dataset viewer

p.s. there is good tool such as cloudcompare but it's difficult to load and visualize labeling dataset, so I added some functions by using Open3D library.

<img src="img_girl.jpg" alt="screen" width="500">

# Install
pip install open3d
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

