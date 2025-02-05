---

# **monitor-load**

A CLI tool designed to monitor system load and automatically pause or resume a process based on the system's load.

**Why this tool?**  
As a team using servers daily, we often face the issue of servers going down due to excessive load. To support our team and ensure smooth operations, I developed `monitor-load` to help prevent processes from overwhelming the system by pausing them when the load is too high.

---

## **Installation**

Install using pip:

```sh
pip install monitor-load
```

---

## **Usage**

### **Basic Command**

```sh
monitor_load --load <LOAD> <COMMAND>
```

- `<LOAD>`: System load threshold (e.g., `0.75` for 75% CPU usage).
- `<COMMAND>`: The command to run (e.g., `python app.py`).

### **Example Usage**

1. **Run a Python Script and Pause if Load Exceeds 80%:**

```sh
monitor_load --load 40 python app.py
```

In this example, the tool will monitor the system load while running `python app.py`. If the system load exceeds 80%, it will automatically pause the script until the load drops below the threshold.

---

## **Uninstalling**

To uninstall, run:

```sh
pip uninstall monitor-load
```

---
Contact for issues: adupanithinsai@gmail.com
