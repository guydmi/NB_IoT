import re
import numpy as np
import pandas as pd

def extract_cfo_from_data(path: str) -> np.array:
    CFO = []
    with open(path, 'r') as file:
        for line in file:
            cfo_match = re.search(r'CFO:  ([\+\-]\d+\.\d+)', line)
            if cfo_match:
                CFO.append(float(cfo_match.group(1)))
    return np.array(CFO)

def extract_SNR_from_data(path: str) -> np.array:
    SNR = []
    with open(path, 'r') as file:
        for line in file:
            SNR_match = re.search(r'SNR:  (\d+\.\d+)', line)
            if SNR_match:
                SNR.append(float(SNR_match.group(1)))
    return np.array(SNR)


def extract_joint_data(path : str) -> tuple[np.array, np.array]:
    CFO, SNR = [], []
    with open(path, 'r') as file:
        for line in file:
            cfo_match = re.search(r'CFO:  ([\+\-]\d+\.\d+)', line)
            SNR_match = re.search(r'SNR:  (\d+\.\d+)', line)
            if cfo_match and SNR_match:
                CFO.append(float(cfo_match.group(1)))
                SNR.append(float(SNR_match.group(1)))
    return np.array(CFO), np.array(SNR)

def extract_data_csv(path: str):
    df = pd.read_csv(path, delimiter=";")
    print(df.keys())
    return df["cfo"], df["dl_snr"]