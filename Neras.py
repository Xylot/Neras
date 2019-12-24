import os
import argparse
from subprocess import call
from pathlib import Path


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', type=str, default=get_default_cache_folder(), help="Folder that you want to copy from")
    parser.add_argument('-d', '--destination', type=str, required=True, help="Folder that you want to copy to")
    return parser.parse_args()


def resolve_paths(args: argparse.Namespace) -> Path:
    source = Path(args.source).absolute()
    destination = Path(args.destination).absolute()
    return source, destination


def get_default_cache_folder() -> Path:
    local_app_data_folder = os.getenv('LOCALAPPDATA')
    return Path(local_app_data_folder + '/Plex Media Server/').absolute()


def copy_data(source_folder: Path, destination_folder: Path):
    command = []
    command.append('robocopy')
    command.append(str(source_folder))
    command.append(str(destination_folder))
    command.append('/E')
    call(command)


def main():
    args = get_args()
    source, destination = resolve_paths(args)
    copy_data(source, destination)


if __name__ == "__main__":
    main()