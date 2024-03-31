import requests
import random
from multiprocessing import Process
import argparse
import sys

def calll_api(route="division-multiplication",server="localhost",services="division",a=5, b=7,port=31264):


    url = f"http://{server}:{port}/{route}/api/v1/math/{services}?a={a}&b={b}"
    payload={}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    value=response.text

    print (f"Server: {server}, Port: {port}, Service: {services}, a: {a}, b: {b}, Response: {value}")

    return value
def main(math_add_subtract=31181,math_division_multiplication=31181):
    processes = []
    for i in range (0,1000):
        random_number = random.randint(0,500)
        server="localhost"



        calls = [
            ('division-multiplication',server,"multiplication",random_number,random.randint(0,500),math_division_multiplication),
            ('division-multiplication',server,"division",random_number,random.randint(0,1),math_division_multiplication),

            ('add-subtract',server,"subtract",random_number,random.randint(500,9500),math_add_subtract),
            ('add-subtract',server,"add",random_number,random.randint(-500,1000),math_add_subtract),
        ]




        for call in calls:
            p = Process(target=calll_api, args=call)
            p.start()
            processes.append(p)

        # Wait for all processes to finish
    for p in processes:
        p.join()


if __name__ == '__main__':
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Perform basic math operations.')
    parser.add_argument(choices=['math-add-subtract', 'math-division-multiplication'],help='The math operation to perform')

    #math_add_subtract=31181,math_division_multiplication=31181
    parser.add_argument('math_add_subtract', type=int, help='add or subtract')
    parser.add_argument('math_division_multiplication', type=int, help='multiplication or division')

    # Parse arguments
    args = parser.parse_args()
    math_add_subtract = args.math_add_subtract
    math_division_multiplication = args.math_division_multiplication

    main(math_add_subtract=math_add_subtract,math_division_multiplication=math_division_multiplication)
