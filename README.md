# Shape Area Calculator

This Python program demonstrates the calculation of areas for various geometric shapes including trapezoids, rectangles, and squares. It showcases different approaches to handling computational tasks: sequentially, using threading, using multiprocessing with pools, and a combined approach of multiprocessing with multithreading.

## Features
Calculation of areas for trapezoids, rectangles, and squares.
Sequential processing for baseline performance comparison.
Multithreaded calculations using ThreadPoolExecutor.
Multiprocessing calculations using ProcessPoolExecutor.
Combined multiprocessing and multithreading approach for enhanced performance on multi-core systems.

## Requirements
Python 3.6 or higher

## Setup
No additional libraries are required beyond the Python standard library. Simply clone this repository or download the .py file to your local machine.

## Usage
To run the program, navigate to the directory containing the script and execute it with Python:
  ` python trapezoid.py
  `
The program will automatically generate random dimensions for 1000 instances of each shape type (trapezoid, rectangle, square) and calculate their areas using different processing techniques. The execution time for each method will be printed to the console, providing a comparison of performance between sequential, multithreaded, and multiprocessing approaches.

## Implementation Details
The Trapezoid, Rectangle, and Square classes define the shapes and include methods for calculating their areas.
The regular() function calculates areas sequentially for a baseline performance metric.
The thread_pool_executor() function uses a thread pool to calculate areas concurrently.
The process_pool_executor() function uses a process pool to leverage multiple CPU cores for calculations.
The combined_process_thread_executor() function demonstrates a hybrid approach, creating multiple processes, each of which spawns multiple threads for calculations.
