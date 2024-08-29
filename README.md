# FTP Brut3F0rc3r

`FTP Brut3F0rc3r` is a Python script that performs a brute force attack on an FTP server by trying different username and password combinations. The script supports multithreading to speed up the process and can log the results to a file.

## Features

- **Brute Force Attack**: Attempts to login to an FTP server using a list of potential passwords.
- **Multithreading**: Utilize multiple threads to speed up the brute-forcing process.
- **Custom Console Title**: Sets a custom console title for Windows users.
- **Clear Console**: Clears the console before running the attack.
- **Logging**: Optionally logs successful login attempts to a file.

## Prerequisites

- Python 3.x
- The following Python modules: `ftplib`, `argparse`, `getpass`, `threading`, `logging`, `os`, `ctypes`, `queue`

## Installation

1. Clone or download this repository.
2. Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
