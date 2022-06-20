import argparse

def configurateParser():
    parser = argparse.ArgumentParser(description="> Down Tube by Frodo1337 - Download videos from youtube <")

    parser.add_argument("-i", help="youtube video url", required=True)
    parser.add_argument("-o", help="output save location (uses current directory as default)", required=False)
    parser.add_argument("-f", help="output file format (uses .mp4 as default)", required=False)

    return parser
