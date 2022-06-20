from startup import configurateParser

def parseArgs():
    parser = configurateParser()
    return parser.parse_args()

if __name__ == "__main__":
    args = parseArgs()

exit()
