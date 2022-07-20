"""
Author: Vinay Bagde
Modifier: Anurag Guda
Maintainer: Andrew Liu, Anurag Guda
Copyright (c) 2018 NVIDIA Corporation.  All rights reserved.
"""
import sys
import os
from collections import OrderedDict

tile_map = {1:(1,1), 2: (1,2), 4:(2,2), 6:(2,3), 8:(2,4), 10:(2,5), 12:(3,4), 15:(3,5), 18:(3,6)}
tile_map = OrderedDict(tile_map)

def read_camera_file():
    camera_path = '/etc/config'
    files = os.listdir(camera_path)
    camera_ips = []
    for file in files:
        current_file = os.path.join(camera_path,file)
        if os.path.isfile(current_file):
            camera_file = open(current_file)
            camera_ip = camera_file.readline()
            camera_ip = camera_ip.strip("\n")
            camera_file.close()
            camera_ips.append(camera_ip)
    return camera_ips


def main():
    ips = read_camera_file()
    print(ips)
    print(len(ips))
    n_rows = None
    n_columns = None
    for key,val  in tile_map.items():
        if len(ips) < key:
            break
        n_rows = val[0]
        n_columns = val[1]

    write_list = []
    if len(ips) != 0:

        with open(sys.argv[2]) as fp:
            line = fp.readline()
            while line:
                pair = line.split("=")
                if pair[0] == "rows":
                    pair[1] = str(n_rows)
                elif pair[0] == "columns":
                    pair[1] = str(n_columns)
                elif pair[0] == "batch-size":
                    pair[1] = str(len(ips))
                output = line
                if len(pair) > 1:
                    output = "=".join(pair)
                output = output.replace('\n','')
                write_list.append(output)
                line = fp.readline()
        fp.close()
    else:
        with open(sys.argv[2]) as fp:
            line = fp.readline()
            while line:
                pair = line.split("=")
                if pair[0] == "rows":
                    pair[1] = str("1")
                elif pair[0] == "columns":
                    pair[1] = str("1")
                elif pair[0] == "num-sources":
                    pair[1] = str("1")
                elif pair[0] == "file-loop":
                    pair[1] = str("1")
                elif pair[0] == "batch-size":
                    pair[1] = str("1")
                output = line
                if len(pair) > 1:
                    output = "=".join(pair)
                output = output.replace('\n','')
                write_list.append(output)
                line = fp.readline()
        fp.close()


    

    if len(ips) != 0:
        for index,ip in enumerate(ips):
            write_list.append("\n")
            write_list.append("[source{}]".format(index))
            write_list.append("enable=1")
            write_list.append("type=4")
            write_list.append("uri={}".format(ip))
            write_list.append("num-sources=1")
            write_list.append("gpu-id=0")
            write_list.append("cudadec-memtype=0")
            write_list.append("\n")

        write_list.append("[sink0]")
        write_list.append("enable=1")
        write_list.append("type=4")
        write_list.append("container=1")
        write_list.append("codec=1")
        write_list.append("sync=0")
        write_list.append("bitrate=2000000")
        write_list.append("profile=0")
        write_list.append("output-file=out.mp4")
        write_list.append("source-id=0")


    if len(ips) == 0:
        write_list.append("\n")
        write_list.append("[sink0]")
        write_list.append("enable=1")
        write_list.append("type=1")
        write_list.append("sync=1")
        write_list.append("codec=1")
        write_list.append("bitrate=4000000")
        write_list.append("rtsp-port=8554")
        write_list.append("udp-port=5400")
        write_list.append("source-id=0")
        write_list.append("gpu-id=0")
        write_list.append("nvbuf-memory-type=0")
        write_list.append("\n")
        write_list.append("[sink2]")
        write_list.append("enable=1")
        write_list.append("type=4")
        write_list.append("container=1")
        write_list.append("codec=1")
        write_list.append("sync=1")
        write_list.append("bitrate=2000000")
        write_list.append("rtsp-port=8554")
        write_list.append("udp-port=5400")
        write_list.append("profile=0")
        write_list.append("output-file=out.mp4")
        write_list.append("source-id=0")

    write_file = os.path.join(os.path.dirname(sys.argv[2]),'run.txt')
    with open(write_file,"w") as file:
        for line in write_list:
            file.write(line)
            file.write("\n")
    file.close()
    print(write_file)
    os.system("{} -c {}".format(sys.argv[1],write_file))


if __name__ == '__main__':
    main()
