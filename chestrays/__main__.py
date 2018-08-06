import os
import sys
import time
import json
import argparse

import kaggle


def get_fetchparser():
    argparser = argparse.ArgumentParser()

    argparser.add_argument(
        'kernel',
        help="Path to the notebook for which to fetch output from kaggle"
    )
    return argparser


def get_runparser():
    argparser = argparse.ArgumentParser()

    argparser.add_argument(
        '--wait',
        action='store_true',
        help="Wait for notebook to finish executing"
    )
    argparser.add_argument(
        '--fetch',
        action='store_true',
        help="Fetch notebook output"
    )
    argparser.add_argument(
        'kernel',
        help="Path to the notebook to execute on kaggle"
    )
    return argparser


def get_metadata(kernel_dir):
    with open(os.path.join(kernel_dir, 'kernel-metadata.json')) as f:
        return json.load(f)


def wait_for(kernel_name):
    # wait for the kernel to finish running
    while True:
        time.sleep(1)
        print('.', end='', flush=True)
        status = kaggle.api.kernels_status(kernel_name)
        if status['status'] == 'complete':
            print("Kernel finished running")
            break


def run():
    argv = sys.argv[1:]
    args = get_runparser().parse_args(argv)

    kernel_dir = os.path.dirname(args.kernel)

    print('submiting...')

    kaggle.api.kernels_push_cli(kernel_dir)

    metadata = get_metadata(kernel_dir)

    if args.wait or args.fetch:
        wait_for(metadata['id'])

    if args.fetch:
        kaggle.api.kernels_output(metadata['id'],
                                  os.path.join(kernel_dir, 'outputs'))


def fetch():
    argv = sys.argv[1:]
    args = get_fetchparser().parse_args(argv)

    kernel_dir = os.path.dirname(args.kernel)
    metadata = get_metadata(kernel_dir)

    wait_for(metadata['id'])
    kaggle.api.kernels_output(metadata['id'],
                              os.path.join(kernel_dir, 'outputs'))
