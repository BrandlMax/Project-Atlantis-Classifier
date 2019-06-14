import csv


class DATA:
    def __init__(self):
        print("DATALOADER")

    def load(self, path, amount=100):
        data = []

        with open(path) as csvfile:
            # change contents to floats
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            print("reader", reader)
            for row in reader:  # each row is a list
                data.append(row)

        # remove header
        data.pop(0)
        data = data[:amount]
        return data
