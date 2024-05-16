# CPU-Scheduling-Simulator

This project simulates various CPU scheduling algorithms to illustrate their behavior and performance. It supports the following scheduling algorithms

## Sample run

For each algorithm, the simulator generates Gantt charts, calculates average waiting times, and average turnaround times for a simulation period of 200 time units. This tool is useful for studying and comparing different scheduling strategies in operating systems.

<p align="center">
<pre>
<code>
# Define a list of processes with their attributes (name, arrival time, burst time, priority, comeback time)
process_list = [
    MyCollection.Process("Process 1", 0, 10, 0, 2),
    MyCollection.Process("Process 2", 1, 8, 0, 4),
    MyCollection.Process("Process 3", 3, 14, 0, 6),
    MyCollection.Process("Process 4", 4, 7, 0, 8),
    MyCollection.Process("Process 5", 6, 5, 0, 3),
    MyCollection.Process("Process 6", 7, 4, 0, 6),
    MyCollection.Process("Process 7", 8, 6, 0, 9)
]
</code>
</pre>
</p>

<h4 align="center"> First Come First Served (FCFS) </h4>
<p align="center">
  <img width="620" height="345" src="https://github.com/qossayrida/CPU-Scheduling-Simulator/assets/59481839/d7738aaf-74e7-4ccd-95b1-914f7f745d98">
</p>

<h4 align="center"> Shortest Job First (SJF) </h4>
<p align="center">
  <img width="620" height="345" src="https://github.com/qossayrida/CPU-Scheduling-Simulator/assets/59481839/09c05c14-2e21-4e3e-97fc-bf155e2f360b">
</p>

<h4 align="center"> Shortest Remaining Time First (SRTF) </h4>
<p align="center">
  <img width="620" height="345" src="https://github.com/qossayrida/CPU-Scheduling-Simulator/assets/59481839/d31ec105-64ba-442c-9f1c-6aaa1cb3c575">
</p>

<h4 align="center"> Round Robin (RR) with a quantum of 5 </h4>
<p align="center">
  <img width="620" height="345" src="https://github.com/qossayrida/CPU-Scheduling-Simulator/assets/59481839/1f6b88ac-89a6-4924-8e5e-bb096d4c278a">
</p>

<h4 align="center"> Non-preemptive Priority Scheduling with aging </h4>
<p align="center">
  <img width="620" height="345" src="https://github.com/qossayrida/CPU-Scheduling-Simulator/assets/59481839/1a829421-1237-49ef-83a3-3f914058e897">
</p>

<h4 align="center"> Preemptive Priority Scheduling with aging </h4>
<p align="center">
  <img width="620" height="345" src="https://github.com/qossayrida/CPU-Scheduling-Simulator/assets/59481839/678e43ab-a7bb-4f08-88b6-92d64ad9689b">
</p>


## 🔗 Links

[![facebook](https://img.shields.io/badge/facebook-0077B5?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/qossay.rida?mibextid=2JQ9oc)

[![Whatsapp](https://img.shields.io/badge/Whatsapp-25D366?style=for-the-badge&logo=Whatsapp&logoColor=white)](https://wa.me/+972598592423)

[![linkedin](https://img.shields.io/badge/linkedin-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/qossay-rida-3aa3b81a1?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app )

[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/qossayrida)


