
# storage

[raid0 on coreos](https://github.com/openshift/release/blob/a8f595533e72b4e3411accbd5d04d49222104603/clusters/build-clusters/01_cluster/machine_config/m5d4x_machineconfig.yaml#L7)

```
# lsblk
NAME                         MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
nvme1n1                      259:0    0 279.4G  0 disk
`-nvme1n1p1                  259:1    0 279.4G  0 part
  `-md127                      9:127  0 558.6G  0 raid0
nvme2n1                      259:2    0 279.4G  0 disk
`-nvme2n1p1                  259:3    0 279.4G  0 part
  `-md127                      9:127  0 558.6G  0 raid0
nvme0n1                      259:4    0   300G  0 disk
|-nvme0n1p1                  259:5    0   384M  0 part  /boot
|-nvme0n1p2                  259:6    0   127M  0 part  /boot/efi
|-nvme0n1p3                  259:7    0     1M  0 part
`-nvme0n1p4                  259:8    0 299.5G  0 part
  `-coreos-luks-root-nocrypt 253:0    0 299.5G  0 dm    /sysroot

# cat /proc/mdstat
Personalities : [raid0]
md127 : active raid0 nvme2n1p1[1] nvme1n1p1[0]
      585670656 blocks super 1.2 512k chunks

unused devices: <none>

# mdadm --detail /dev/md/containerraid
/dev/md/containerraid:
           Version : 1.2
     Creation Time : Wed Apr 15 08:28:08 2020
        Raid Level : raid0
        Array Size : 585670656 (558.54 GiB 599.73 GB)
      Raid Devices : 2
     Total Devices : 2
       Persistence : Superblock is persistent

       Update Time : Wed Apr 15 08:28:08 2020
             State : clean
    Active Devices : 2
   Working Devices : 2
    Failed Devices : 0
     Spare Devices : 0

        Chunk Size : 512K

Consistency Policy : none

              Name : any:containerraid
              UUID : d8a17b8b:3f762a35:e9037e63:a54a5cd3
            Events : 0

    Number   Major   Minor   RaidDevice State
       0     259        1        0      active sync   /dev/nvme1n1p1
       1     259        3        1      active sync   /dev/nvme2n1p1
```
