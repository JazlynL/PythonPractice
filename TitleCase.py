# Complete the solve function below.
def solve(s):
    string = [x[:1].title() + x[1:] for x in s.split(" ")]
    concatStr = " ".join(string)

    return concatStr


if __name__ == '__main__':