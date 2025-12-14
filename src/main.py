# CPU Zamanlama Algoritmaları -
# Python 3.x

import threading
import csv
import copy

CONTEXT_SWITCH_TIME = 0.001
RR_QUANTUM = 2

# ---------------- PROCESS SINIFI ----------------
class Process:
    def __init__(self, pid, arrival, burst, priority):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.priority = priority
        self.finish = 0

# ---------------- CSV OKUMA ----------------

def read_csv(filename):
    priority_map = {
        "high": 1,
        "normal": 2,
        "low": 3
    }
    processes = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            processes.append(Process(
                row['Process_ID'],
                int(row['Arrival_Time']),
                int(row['CPU_Burst_Time']),
                priority_map[row['Priority'].lower()]
            ))
    return processes

# ---------------- FCFS ----------------

def fcfs(processes):
    time = 0
    timeline = []
    cs = 0
    for p in sorted(processes, key=lambda x: x.arrival):
        if time < p.arrival:
            timeline.append((time, 'IDLE', p.arrival))
            time = p.arrival
        timeline.append((time, p.pid, time + p.burst))
        cs += 1
        time += p.burst
        p.finish = time
    return timeline, cs

# ---------------- SJF NON-PREEMPTIVE ----------------

def sjf_np(processes):
    time = 0
    completed = 0
    timeline = []
    cs = 0
    while completed < len(processes):
        ready = [p for p in processes if p.arrival <= time and p.remaining > 0]
        if not ready:
            time += 1
            continue
        p = min(ready, key=lambda x: x.burst)
        timeline.append((time, p.pid, time + p.burst))
        time += p.burst
        p.remaining = 0
        p.finish = time
        completed += 1
        cs += 1
    return timeline, cs

# ---------------- SJF PREEMPTIVE ----------------

def sjf_p(processes):
    time = 0
    timeline = []
    cs = 0
    current = None
    while any(p.remaining > 0 for p in processes):
        ready = [p for p in processes if p.arrival <= time and p.remaining > 0]
        if not ready:
            time += 1
            continue
        p = min(ready, key=lambda x: x.remaining)
        if current != p:
            cs += 1
        current = p
        start = time
        time += 1
        p.remaining -= 1
        if p.remaining == 0:
            p.finish = time
        timeline.append((start, p.pid, time))
    return timeline, cs

# ---------------- ROUND ROBIN ----------------

def round_robin(processes):
    time = 0
    queue = []
    timeline = []
    cs = 0
    processes = sorted(processes, key=lambda x: x.arrival)
    i = 0
    while queue or i < len(processes):
        while i < len(processes) and processes[i].arrival <= time:
            queue.append(processes[i])
            i += 1
        if not queue:
            time += 1
            continue
        p = queue.pop(0)
        cs += 1
        run = min(RR_QUANTUM, p.remaining)
        timeline.append((time, p.pid, time + run))
        time += run
        p.remaining -= run
        if p.remaining == 0:
            p.finish = time
        else:
            queue.append(p)
    return timeline, cs

# ---------------- PRIORITY NON-PREEMPTIVE ----------------

def priority_np(processes):
    time = 0
    completed = 0
    timeline = []
    cs = 0
    while completed < len(processes):
        ready = [p for p in processes if p.arrival <= time and p.remaining > 0]
        if not ready:
            time += 1
            continue
        p = min(ready, key=lambda x: x.priority)
        timeline.append((time, p.pid, time + p.burst))
        time += p.burst
        p.remaining = 0
        p.finish = time
        completed += 1
        cs += 1
    return timeline, cs

# ---------------- PRIORITY PREEMPTIVE ----------------

def priority_p(processes):
    time = 0
    timeline = []
    cs = 0
    current = None
    while any(p.remaining > 0 for p in processes):
        ready = [p for p in processes if p.arrival <= time and p.remaining > 0]
        if not ready:
            time += 1
            continue
        p = min(ready, key=lambda x: x.priority)
        if current != p:
            cs += 1
        current = p
        start = time
        time += 1
        p.remaining -= 1
        if p.remaining == 0:
            p.finish = time
        timeline.append((start, p.pid, time))
    return timeline, cs

# ---------------- METRICS (a–f) ----------------

def metrics(processes, timeline, cs):
    waits, turns = [], []
    for p in processes:
        turnaround = p.finish - p.arrival
        waiting = turnaround - p.burst
        waits.append(waiting)
        turns.append(turnaround)

    throughput = {T: sum(1 for p in processes if p.finish <= T) for T in [50, 100, 150, 200]}

    total_time = timeline[-1][2]
    cpu_time = sum(p.burst for p in processes)
    efficiency = cpu_time / (total_time + cs * CONTEXT_SWITCH_TIME)

    return {
        'max_wait': max(waits),
        'avg_wait': sum(waits) / len(waits),
        'max_turnaround': max(turns),
        'avg_turnaround': sum(turns) / len(turns),
        'throughput': throughput,
        'cpu_efficiency': efficiency,
        'context_switch': cs
    }

# ---------------- THREAD RUNNER ----------------

def run(algo, filename):
    processes = copy.deepcopy(read_csv('processes.csv'))
    timeline, cs = algo(processes)
    result = metrics(processes, timeline, cs)
    with open(filename, 'w') as f:
        f.write(str(timeline) + '\n')
        f.write(str(result))

# ---------------- MAIN ----------------

if __name__ == '__main__':
    threads = [
        threading.Thread(target=run, args=(fcfs, 'fcfs_results.txt')),
        threading.Thread(target=run, args=(sjf_np, 'sjf_nonpreemptive.txt')),
        threading.Thread(target=run, args=(sjf_p, 'sjf_preemptive.txt')),
        threading.Thread(target=run, args=(round_robin, 'round_robin.txt')),
        threading.Thread(target=run, args=(priority_np, 'priority_nonpreemptive.txt')),
        threading.Thread(target=run, args=(priority_p, 'priority_preemptive.txt')),
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print('Tüm CPU zamanlama algoritmaları eş zamanlı olarak çalıştırıldı.')

