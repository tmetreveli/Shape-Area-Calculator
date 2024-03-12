import random as rd
import time
import concurrent.futures


class Trapezoid:
    def __init__(self, parameters=None):
        if parameters is None:
            parameters = [0, 0, 0]
        self.a = parameters[0]
        self.b = parameters[1]
        self.h = parameters[2]

    def __str__(self):
        return 'Trapezoid with bases -> {}, {} and height -> {}'.format(self.b, self.a, self.h)

    def area(self):
        return (self.a + self.b) / 2 * self.h

    def __add__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() + other.area()
        return False

    def __sub__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() - other.area()
        return False

    def __mod__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() % other.area()
        return False

class Rectangle(Trapezoid):
    def __init__(self, parameters=None):
        if parameters is None:
            parameters = [0, 0]
        super().__init__([parameters[0], parameters[1], 0])

    def __str__(self):
        return "Rectangle with height -> {}, and width -> {}".format(self.h, self.a)

class Square(Rectangle):
    def __init__(self, side=None):
        if side is None:
            side = 0
        super().__init__([side[0], 0, 0])

    def __str__(self):
        return "Square with side -> {}".format(self.a)


def trapezoid_area(arr):
    for i in arr:
        T = Trapezoid(i)
        T.area()

def rectangle_area(arr):
    for i in arr:
        R = Rectangle(i)
        R.area()

def square_area(arr):
    for i in arr:
        S = Square(i)
        S.area()

# Regular function to calculate areas sequentially
def regular(arr):
    start = time.perf_counter()
    trapezoid_area(arr)
    rectangle_area(arr)
    square_area(arr)
    finish = time.perf_counter()
    print('Regular execution finished in: ', round(finish - start, 2), 'second(s)')

# Using ThreadPoolExecutor to manage threads
def thread_pool_executor(arr):
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(trapezoid_area, arr)
        executor.submit(rectangle_area, arr)
        executor.submit(square_area, arr)
    finish = time.perf_counter()
    print('ThreadPoolExecutor finished in: ', round(finish - start, 2), 'second(s)')

# Using ProcessPoolExecutor to manage processes
def process_pool_executor(arr):
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.submit(trapezoid_area, arr)
        executor.submit(rectangle_area, arr)
        executor.submit(square_area, arr)
    finish = time.perf_counter()
    print('ProcessPoolExecutor finished in: ', round(finish - start, 2), 'second(s)')

# Combining processes and threads
def combined_process_thread_executor(arr, num_processes=5, threads_per_process=20):
    start = time.perf_counter()
    def worker(sub_arr):
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads_per_process) as executor:
            executor.submit(trapezoid_area, sub_arr)
            executor.submit(rectangle_area, sub_arr)
            executor.submit(square_area, sub_arr)

    # Divide the array into sub-arrays for each process
    sub_arrays = [arr[i::num_processes] for i in range(num_processes)]


    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        executor.map(worker, sub_arrays)
    finish = time.perf_counter()
    print('Combined Process and Thread Executor finished in: ', round(finish - start, 2), 'second(s)')

if __name__ == "__main__":
    # Sample data for demonstration
    trapecoids = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for _ in range(1000000)]
    rectangles = [[rd.randint(1, 200), rd.randint(1, 200)] for _ in range(1000000)]
    squares = [rd.randint(1, 200) for _ in range(1000000)]

    regular(trapecoids)
    thread_pool_executor(trapecoids)
    process_pool_executor(trapecoids)
    combined_process_thread_executor(trapecoids)
