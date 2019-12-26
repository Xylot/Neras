# Neras
Change the cache folder path for Plex Media Server on Windows with a single command

## Requirements
- Windows
- Python 3
- Plex Media Server

## Dependencies
Install all of the project's package dependencies by running:
    
    pip install -r requirements.txt

## Interface
|      Argument     | Value |                             Description                            |              Default              |
|:-----------------:|:-----:|:------------------------------------------------------------------:|:---------------------------------:|
| -s, --source      |  PATH |    Source path of the Plex Cache Directory that you want to move   | %LOCALAPPDATA%\Plex Media Server\ |
| -d, --destination |  PATH | Destination path of the Plex Cache Directory that you want to move |                                   |
| -v, --verbosity   |  BOOL |                       Show all console output                      |               FALSE               |

## Running the Tool
To change from the default data path to a new one, run:
    
    python Neras.py -d "your/new/directory/here/"

To change from a user-defined data path to a new one, run:

    python Neras.py -s "Source/data/directory/" -d "your/new/directory/here"

To show all console output, append the `-v` flag

Once the data has been successfully copied over, the script changes the `LocalAppDataPath` registry value located in `Computer\HKEY_CURRENT_USER\Software\Plex, Inc.\Plex Media Server` to the new path specified by the user.

## Post-run
To ensure no data loss, this script does not remove any data from the previous Plex cache directory. Once you ensure that your data has been moved successfully and Plex is in working order, be sure to delete the previous plex media cache folder.

## WARNING
This script does access and edit your registry! If you do not feel comfortable tweaking values in the registry, do not run this script!