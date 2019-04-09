import re

def parse_string(qstr, i, j):
    parser = re.compile("^(?:w|b)(([a-i][1-9])|([a-i][1-9](v|h)))$")
    while(True):
        ipt =str(input(""))
        m = parser.match(ipt)
        print m.group()
if __name__ == "__main__":
    parse_string(1, 2, 3)

