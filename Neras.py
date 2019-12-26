import os
import argparse
import subprocess
import RegistryTool
from pathlib import Path

OUTPUT_LOG = False

PLEX_DIRECTORY = 'Software\\Plex, Inc.\\Plex Media Server'
PATH_KEY_NAME = 'LocalAppDataPath'
TEST_KEY_NAME = 'Neras'


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', type=str, default=get_default_cache_folder(), help="Folder that you want to copy from")
    parser.add_argument('-d', '--destination', type=str, required=True, help="Folder that you want to copy to")
    parser.add_argument("-v", "--verbosity", action='store_true', help="Increase output verbosity")
    return parser.parse_args()


def resolve_paths(args: argparse.Namespace) -> Path:
    if args.verbosity:
        global OUTPUT_LOG
        OUTPUT_LOG = True

    source = Path(args.source).absolute()
    destination = Path(args.destination).absolute()

    print('Moving data from {} to {}'.format(str(source), str(destination)))

    return source, destination, destination.parent


def get_default_cache_folder() -> Path:
    local_app_data_folder = os.getenv('LOCALAPPDATA')
    return Path(local_app_data_folder + '/Plex Media Server/').absolute()


def copy_data(source_folder: Path, destination_folder: Path):
    print('Copying data... (This may take awhile)')
    command = []
    command.append('robocopy')
    command.append(str(source_folder))
    command.append(str(destination_folder))
    command.append('/E')
    call_subprocess(command)


def rename_old_directory(directory: Path, new_folder_name: str = 'Plex Media Server old'):
    directory.rename(new_folder_name)


def call_subprocess(command):
    if OUTPUT_LOG:
        subprocess.call(command)
    else:
        subprocess.call(command, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def change_path_registry_value(new_path: Path, key_name: str = PATH_KEY_NAME):
    print('Changing LocalAppDataPath registry value...')
    registy = RegistryTool.connect()
    key = RegistryTool.open_key(registy, PLEX_DIRECTORY)
    RegistryTool.set_key_value(key, key_name, 1, str(new_path))


def main():
    args = get_args()
    source, destination, destination_parent_directory = resolve_paths(args)
    copy_data(source, destination)
    change_path_registry_value(destination_parent_directory)
    rename_old_directory(destination)
    print('Complete! Make sure to remove the old data folder once you ensure no data was lost')


if __name__ == "__main__":
    main()
