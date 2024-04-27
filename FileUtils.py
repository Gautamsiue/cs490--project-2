def readFile(file):
        data = []
        with open(file, 'r') as f:
            data = [line.strip() for line in f]
        return data


def write_file(file, data):
     with open(file, 'w') as f:
         for d in data:
             f.write(d + '\n')


def create_file(path, ranges):
    with open(path, 'w') as f:
        if 'negatives.bed' in path:
            for range in ranges:
                f.write('\t'.join(str(val) for val in range) + '\n')
        else:
            for range in ranges:
                f.write(range[-1] + '\n')



def wayOne(file):
    data1D = readFile(file)
    data2D = [line.split() for line in data1D]
    return data2D

def wayTwo(file):
    data = list()
    with open(file, 'r') as f:
        data = [line.strip().split() for line in f]
    return data
