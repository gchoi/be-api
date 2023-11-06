#!/usr/bin/env python

import yaml
import argparse


def get_configurations(config_yaml_path: str) -> dict:
    with open(config_yaml_path) as f:
        configs = yaml.load(f, Loader=yaml.FullLoader)
    return configs


def main():
    parser = argparse.ArgumentParser(description='Input environment yaml path.')
    parser.add_argument(
        '--env',
        type=str,
        help="",
        default="./env.yaml"
    )
    args = parser.parse_args()

    envs = get_configurations(args.env)

    with open('.env', 'w') as fpath:
        for _key in envs.keys():
            fpath.write(f"{_key} = {envs[_key]}\n")

    return


if __name__ == "__main__":
    main()
