import csv


class DATA:
    def __init__(self):
        print("DATALOADER")

    def load(self, path, amount=5, maxSize=1000):
        data = []

        with open(path) as csvfile:
            # change contents to floats
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            print("reader", reader)
            for row in reader:  # each row is a list
                data.append(row)

        # remove header
        data.pop(0)
        # data = data[:amount]

        packages = []

        iterations = len(data) / amount
        if iterations >= maxSize:
            iterations = maxSize

        for pI in range(0, int(iterations)):
            d = []
            for i in range(0, len(data)):
                d.append(data[i])
            packages.append(d)

        return packages
