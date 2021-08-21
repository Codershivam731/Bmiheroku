# importing required library
from pywebio.input import *
from pywebio.output import *


# Function that calculate bmi
def bmicalculator():
    put_image(src='https://www.graphicsfactory.com/clip-art/image_files/image/4/615024-BFM0171.gif', width='150px')
    put_text("BMI CALCULATOR")
    height = input("Please enter the height in cm", type=FLOAT)
    weight = input("Please enter the weight in kg", type=FLOAT)
    bmi = weight / (height / 100) ** 2

    bmi_output = [(16, "Severely underweight"), (18.5, 'underweight'), (25, 'normal'),
                  (30, 'overweight'), (35, 'Moderately obsese'), (float('inf'), 'Severely obese')]
    for tuple1, tuple2 in bmi_output:
        if bmi <= tuple1:
            put_text('Your BMI is : %.1f and the person is :%s' % (bmi, tuple2))
            break


if __name__ == '__main__':
    import argparse
    from pywebio.platform.tornado_http import start_server

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(bmicalculator,port=args.port)
