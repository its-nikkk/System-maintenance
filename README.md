---

# System Maintenance Script

This Python script automates routine system maintenance tasks on Debian-based systems. It performs the following operations

1. Updates package repositories and installs updates.
2. Cleans up package cache.
3. Removes old kernel versions.
4. Cleans up temporary files.
5. Clears system logs.
6. Restarts a specified service.

## Usage

To use this script:

1. Ensure that Python 3 is installed on your system.
2. Run the script with root privileges:

```
sudo python3 maintenance_script.py
```

## Configuration

You can configure the script to restart a different service by modifying the `restart_service()` function call in the `main()` function.

For example, to restart the Apache service, change:

```python
restart_service("nginx")
```

to:

```python
restart_service("apache2")
```

Replace `"apache2"` with the appropriate service name.

## Disclaimer

This script performs system-level operations that may affect the stability and functionality of your system. Use it with caution and ensure that you understand the implications of each operation before running the script.

---
