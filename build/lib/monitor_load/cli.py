#!/usr/bin/env python3
import argparse
import os
import subprocess
import time
import signal

RESUME_FLAG = "/tmp/resume.flag"

def get_load_avg():
    """Returns the 1-minute system load average"""
    return os.getloadavg()[0]

def monitor_load(max_load, command):
    """Monitor system load and pause/resume the process based on load average."""
    print(f"Monitoring system load... (Threshold: {max_load})")
    process = subprocess.Popen(command, shell=True, preexec_fn=os.setsid)
    print(f"Started process PID: {process.pid}")
    
    try:
        while True:
            load_avg = get_load_avg()
            print(f"Current Load Avg: {load_avg}")

            if load_avg > max_load:
                print(f"Load exceeded {max_load}, pausing process...")
                os.killpg(os.getpgid(process.pid), signal.SIGSTOP)
                
                print("Waiting for user input to resume process...")
                while True:
                    resume_input = input(f"Load exceeded {max_load}. Type 'yes' to resume the process: ").strip().lower()
                    if resume_input == "yes":
                        print("Resuming process...")
                        os.killpg(os.getpgid(process.pid), signal.SIGCONT)
                        break
                    else:
                        print("Invalid input. Type 'yes' to resume the process.")

            if process.poll() is not None:
                print("Process completed.")
                break

            time.sleep(5)
    except KeyboardInterrupt:
        print("\nTerminating process...")
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)

        
def main():
    parser = argparse.ArgumentParser(
        description="Monitor system load and pause/resume a process."
    )
    parser.add_argument("--load", type=float, required=True, help="Max allowed load avg before pausing.")
    parser.add_argument("command", nargs=argparse.REMAINDER, help="Command to run and monitor.")

    args = parser.parse_args()
    if not args.command:
        print("Error: No command provided. Example usage:\n  monitor --load 40 python app.py")
    else:
        monitor_load(args.load, " ".join(args.command))

if __name__ == "__main__":
    main()
