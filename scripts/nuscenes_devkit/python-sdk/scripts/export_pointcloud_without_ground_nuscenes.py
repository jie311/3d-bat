import os

path_in = '/input/NuScenes/point_clouds/'
path_out = '/input/NuScenes/point_clouds_without_ground/'
for file in sorted(os.listdir(path_in)):
    lines = []
    pointcloud_without_ground = []
    with open(path_in + file) as file_reader:
        lines = file_reader.readlines()
    for i in range(len(lines)):
        if i < 11:
            continue
        point_array = lines[i].split(" ")
        z_value = float(point_array[2])
        if z_value > -1.7:
            pointcloud_without_ground.append(lines[i])

    # write header
    num_points = len(pointcloud_without_ground)
    with open(path_out + file, 'w') as file_writer:
        file_writer.write("# .PCD v0.7 - Point Cloud Data file format\n"
                          + "VERSION 0.7\n"
                          + "FIELDS x y z intensity\n"
                          + "SIZE 4 4 4 4\n"
                          + "TYPE F F F F\n"
                          + "COUNT 1 1 1 1\n"
                          + "WIDTH " + str(num_points) + "\n"
                          + "HEIGHT 1\n"
                          + "VIEWPOINT 0 0 0 1 0 0 0\n"
                          + "POINTS " + str(num_points) + "\n"
                          + "DATA ascii\n")
        for line in pointcloud_without_ground:
            file_writer.write(line)
