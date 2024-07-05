# Change_the_file_creation_time_in_batches
The range is random, including the creation time and modification time
# Random File Timestamp Setter

This is a Python script designed to randomly set the access and modification timestamps for all files within a specified directory. The timestamps are randomly generated between user-specified start and end dates.

## Features

- Randomly sets file timestamps.
- Compatible with Windows operating systems.
- User-friendly command-line interface.

## System Requirements

- Python 3.x
- Windows operating system

## Usage

1. Ensure Python 3.x is installed on your system.
2. Save this script as a `.py` file, for example, `randomize_timestamps.py`.
3. Open Command Prompt or PowerShell and navigate to the directory where the script is located.
4. Run the script:
python randomize_timestamps.py

5. Follow the prompts to enter the directory path and the date range.

## Script Parameters

- `folder_path`: The path to the directory whose files' timestamps you want to update.
- `start_date`: The earliest possible date for the timestamps.
- `end_date`: The latest possible date for the timestamps.

## Example

After running the script, you will be prompted to enter the following information:
Please enter the folder path:
Please enter the earliest time (format like YYYY-MM-DD HH:MM:SS):
Please enter the latest time (format like YYYY-MM-DD HH:MM:SS):


## Notes

- Make sure you have the necessary permissions to modify the files in the specified directory.
- This script is only compatible with Windows operating systems as it uses the `win32file` library.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

This script is for educational and research purposes only. Please ensure you comply with all applicable laws and regulations when using it. The author assumes no responsibility for any loss or damage caused during its use.
