#!/usr/bin/env python3
import os
import subprocess

def update_packages():
    print("Updating package repositories and installing updates...")
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "upgrade", "-y"])

def clean_package_cache():
    print("Cleaning up package cache...")
    subprocess.run(["sudo", "apt", "clean"])

def remove_old_kernels():
    print("Removing old kernel versions...")
    subprocess.run(["sudo", "apt", "autoremove", "--purge"])

def clean_temp_files():
    print("Cleaning up temporary files...")
    subprocess.run(["sudo", "rm", "-rf", "/tmp/*"])

def clear_system_logs():
    print("Clearing system logs...")
    subprocess.run(["sudo", "journalctl", "--vacuum-size=50M"])

def restart_service(nginx):
    print(f"Restarting {nginx} service...")
    subprocess.run(["sudo", "systemctl", "restart", nginx])

def main():
    update_packages()
    clean_package_cache()
    remove_old_kernels()
    clean_temp_files()
    clear_system_logs()
    restart_service("nginx")

    print("System maintenance completed.")

if __name__ == "__main__":
    main()
