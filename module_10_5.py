from multiprocessing import Pool
from time import time


def read_info(name):
    all_data = []
    with open(name) as f:
        for line in f:
            all_data.append(line)


# Линейный вызов

# start = time()
# filenames = [f'./file {number}.txt' for number in range(1, 5)]
# # read_info(str(filenames[0]))
# end = time()
# print(f'Работа потоков: {end - start}', '\n')

# Многопроцессный
filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start = time()
    with Pool(4) as p:
        p.map(read_info, filenames)
    end = time()
    print(f'Работа процессов: {end - start}', '\n')
