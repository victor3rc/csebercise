import csv
import argparse

from random import randint


class Road():

    def __init__(self):
        print('Creating a road.')

    def create_file(self, road, file):
        '''
        Method to create a file, containing file generated.

        :param road: Road to write to file
        :param file: file to write to
        '''
        with open(file, 'w') as csvwriter:
            f = csv.writer(csvwriter, delimiter=',')
            f.writerows(road)

    def create_road(self, args):
        '''
        Method to execute the creation of a road.

        :param args: command line args given
        '''
        # number of lanes to create, and length
        lanes = args.lanes
        length = args.kilometres

        # "List Comprehension" to create road, with a list for each kilometer
        road = [[] for lane in range(0, length)]

        # iterate through each kilometer
        for x in range(0, length):
            # iterate through each lane
            for y in range(0, lanes):
                # hole impact on wheels, generated randomly
                hole = randint(0,9)

                # add hole to lane
                road[x].append(hole)

        # create file with road
        self.create_file(road, args.filename)


if __name__ == '__main__':
    road = Road()

    # Required command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--lanes', type=int,
                        help='Number of lanes in road to be generated.')
    parser.add_argument('-k', '--kilometres', type=int,
                        help='Lane length.')
    parser.add_argument('-f', '--filename',
                        default='road.csv',
                        help='File to be created.')

    # execute with arguments given
    road.create_road(parser.parse_args())
