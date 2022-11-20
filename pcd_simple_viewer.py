import copy
import numpy as np
import open3d as o3d
import argparse, readline

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
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_pcd', type=str, required=True)    # pcd format is txt. xyzrgb
    parser.add_argument('--input_label', type=str, required=True)
    args = parser.parse_args() 
    
    label = np.loadtxt(args.input_label)
    label = label.astype(np.int32)

    # print('label')
    # print(cmap[label])

    pcd_origin = np.loadtxt(args.input_pcd, delimiter=' ')
    pcd = o3d.geometry.PointCloud()
    # pcd.points = pcd_origin
    pcd.points = o3d.utility.Vector3dVector(pcd_origin[:,0:3]) # XYZ points
    pcd.colors = o3d.utility.Vector3dVector(cmap[label])  #open3d requires colors (RGB) to be in range[0,1]

    o3d.visualization.draw_geometries([pcd])
    print('end')


