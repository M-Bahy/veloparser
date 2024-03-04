"""
The `main` function is the entry point of the program. It reads the command line arguments and calls the `read_params` function to read the configuration file.
It then creates an instance of the `VelodyneManager` class and calls the `run` method to start processing the pcap file.
"""

import argparse
import yaml

from lidar_manager import VelodyneManager


# Reads the configuration file (params.yaml)
def read_params(path):
    try:
        f = open(path, "rb")
    except Exception as ex:
        print(str(ex))

    params = yaml.safe_load(f.read())
    return params


# Initializes the command line parser to read the inputted paths
def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Path to the pcap file", required=True)
    parser.add_argument(
        "-o", "--out-dir", help="Path to the output directory", required=True
    )
    parser.add_argument(
        "-c", "--config", help="Path of the configuration file", required=True
    )
    # Optional argument to specify the lidar type (default is VLP16)
    parser.add_argument(
        "-t", "--type", help="Lidar name", required=False, default="VLP16"
    )

    return parser


# Decode the command line arguments and create an instance of the VelodyneManager class to start processing the pcap file
def main(args):
    pcap_path = args["path"]
    lidar_type = args["type"]
    out_directory = args["out_dir"]
    configuration_file = args["config"]

    configuration_parameters = read_params(configuration_file)

    if "VLP" in lidar_type.lower():
        lidar_manager = VelodyneManager(
            lidar_type, pcap_path, out_directory, configuration_parameters
        )
        lidar_manager.run()
    else:
        print("Lidar type not supported")


# This method is responsible for starting the program by reading the command line arguments and sending them to the main function.
if __name__ == "__main__":
    parser = init_parser()
    arguments = vars(parser.parse_args())
    main(arguments)
