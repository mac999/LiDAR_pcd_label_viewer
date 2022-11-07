# examples/Python/Basic/working_with_numpy.py

import copy
import numpy as np
import open3d as o3d

cmap = np.array([[1.00, 1.00, 1.00], [0.00, 0.00, 0.00], \
                    [1.00, 0.00, 0.00], [1.00, 0.00, 0.40], \
                    [1.00, 0.00, 0.80], [1.00, 0.20, 1.00], \
                    [1.00, 0.60, 1.00], [0.60, 0.80, 1.00], \
                    [0.20, 0.80, 1.00], [0.20, 0.80, 0.60], \
                    [0.20, 0.80, 0.00], [0.20, 0.40, 0.00], \
                    [0.20, 0.45, 0.40], [0.20, 0.40, 0.80], \
                    [0.60, 0.40, 0.80], [0.60, 0.80, 0.80], \
                    [0.60, 0.80, 0.40], [1.00, 0.60, 0.80]],'f')

if __name__ == "__main__":
    # file = "/home/ktw/projects/randla-net-tf2/test/Log_2022-11-05_13-35-40/predictions/UNF1.labels"
    # file = "/home/ktw/projects/randla-net-tf2/test/Log_2022-11-05_13-35-40/predictions/birdfountain1.labels"
    file = "/home/ktw/projects/randla-net-tf2/test/Log_2022-11-05_13-35-40/predictions/castleblatten1.labels"
    label = np.loadtxt(file)
    label = label.astype(np.int32)

    # print('label')
    # print(cmap[label])

    pcd_origin = np.loadtxt("/home/ktw/data/semantic3d/original_data/castleblatten_station1_intensity_rgb.txt", delimiter=' ')
    pcd = o3d.geometry.PointCloud()
    # pcd.points = pcd_origin
    pcd.points = o3d.utility.Vector3dVector(pcd_origin[:,0:3]) # XYZ points
    pcd.colors = o3d.utility.Vector3dVector(cmap[label])  #open3d requires colors (RGB) to be in range[0,1]

    # pcd = o3d.io.read_point_cloud("./test/PUNKTSKY_1km_6181_724.txt")

    o3d.visualization.draw_geometries([pcd])
    print('end')


