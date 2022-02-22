import numpy as np
import pandas as pd


def to_zomf_corridor(input_name, output_name, save_header, max_angle, corridor_width):
    df = pd.read_csv(input_name, sep='\t', skiprows=13, usecols=np.arange(7), dtype=np.float64, names=save_header.split())
    df.iloc[:, 6] = max_angle
    df.iloc[:, 5] = corridor_width
    df.iloc[:, 4] = df.iloc[:, 3]
    df.iloc[:, 3] = 0
    df.to_csv(output_name, sep='\t', index=False)


def run():
    input_name = 'cmp_vel.corr'
    output_name = 'zomf.corr'
    save_header = 'XCoord	YCoord	V	A	T	DeltaV	DeltaA'
    max_angle = 1.55334
    corridor_width = 500
    to_zomf_corridor(input_name, output_name, save_header, max_angle, corridor_width)


if __name__ == '__main__':
    run()

