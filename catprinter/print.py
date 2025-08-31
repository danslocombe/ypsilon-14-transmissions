#!/usr/bin/env python
import argparse
import asyncio
import logging
import sys
import os

from catprinter import logger
from catprinter.cmds import PRINT_WIDTH, cmds_print_img
from catprinter.ble import run_ble
from catprinter.img import read_img, show_preview

def load_img(path):
    img_binarization_algo = 'none'
    return read_img(
        path,
        PRINT_WIDTH,
        img_binarization_algo,
    )

def main():
    args_builder = argparse.ArgumentParser(
        description='prints an image on your cat thermal printer')
    args_builder.add_argument('filepath', type=str)
    args = args_builder.parse_args()

    image = load_img(args.filepath)
    data = cmds_print_img(image, dark_mode=True, no_feed=True)

    #logger.info(f'Generated BLE commands: {len(data)} bytes')
    device_auto_discover = ""
    asyncio.run(run_ble(data, device=device_auto_discover))


if __name__ == '__main__':
    main()