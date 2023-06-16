from time import time
from multiprocessing import cpu_count, Pool


def factorize(number, cb)->int:
    for num in number:
        list_1 = []
        for i in range(1, num + 1):
            if not num % i:
                list_1.append(i)
        cb(f'{num} == {list_1}')


if __name__ == '__main__':
    numbers = [128, 255, 99999, 10651060, 888888888]
    start_time = time()
    factorize(numbers, print)
    timer = time() - start_time
    print(f'factorize is done in {timer}\n')

    print(f'Count CPU: {cpu_count()}')
    start_time_mp = time()
    pool = Pool(cpu_count())
    result = pool.apply_async(factorize, (numbers, print,))
    print(result.get())
    timer_mp = time() - start_time_mp
    print(f'factorize multiprocessing is done in {timer_mp}')

