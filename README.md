### Veloparser

Veloparser is a simple application which does following:

- Supports just Velodyne lidars VLP16 (recommended) and VPL32C.
- Takes a pcap file recorded by Velodyne lidar as input.
- Extracts all Frames from the pcap file.
- Saves both data-frames and position-frames.
- **Data frames** are saved as **Point Clouds (.pcd)** and/or as **plain Text-File**.
- **Position frames** are saved only as **Text-File**
- Converts frame's timestamps to GPS Week of Second format for synchronization with IMU/GNSS devices
- Can be parameterized by yaml file. The default mode is no gps data available (position frames are not saved)

##### Usage

1. Clone the repository

```bash
git clone https://github.com/M-Bahy/veloparser.git
```

2. Install the required packages

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
python main.py -p [FULL PATH TO THE PCAP FILE] -o [FULL PATH TO THE OUTPUT FOLDER] -c params.yaml -t [VLP16 or VLP32C]
```

Note, The `-t` and its parameter are optional also the `params.yaml` can be updated if you want. For example, specifying whether GPS was available.

##### Output

Below a sample out of 2 Points in a **point cloud file**

`Time [musec], X [m], Y [m], Z [m], ID, Intensity, Latitude [Deg], Longitudes [Deg], Distance [m]
2795827803, 0.032293, 5.781942, -1.549291, 0, 6, 0.320, -15.000, 5.986
2795827806, 0.083565, 14.399564, 0.251350, 1, 6, 0.333, 1.000, 14.402`

They can also be opened and visualized with any point-cloud rendering software like [CloudCompare](https://www.danielgm.net/cc/)
