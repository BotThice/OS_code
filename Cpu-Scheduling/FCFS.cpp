#include <iostream>
using namespace std;

struct Process {
    int pid;  // Process ID
    int bt;   // Burst Time
    int at;   // Arrival Time
};

// Function to find the waiting time for all processes
void findWaitingTime(Process proc[], int n, int wt[]) {
    int service_time[n];
    service_time[0] = proc[0].at;
    wt[0] = 0;

    // calculating waiting time
    for (int i = 1; i < n; i++) {
        // Add burst time of previous processes
        service_time[i] = service_time[i - 1] + proc[i - 1].bt;

        // Find waiting time for current process
        wt[i] = service_time[i] - proc[i].at;

        // If waiting time for a process is in negative
        // that means it is already in the ready queue before
        // CPU becomes idle so its waiting time is 0
        if (wt[i] < 0)
            wt[i] = 0;
    }
}

// Function to calculate turn around time
void findTurnAroundTime(Process proc[], int n, int wt[], int tat[]) {
    // calculating turnaround time by adding bt[i] + wt[i]
    for (int i = 0; i < n; i++)
        tat[i] = proc[i].bt + wt[i];
}

// Function to calculate average time
void findavgTime(Process proc[], int n) {
    int wt[n], tat[n], total_wt = 0, total_tat = 0;

    // Function to find waiting time of all processes
    findWaitingTime(proc, n, wt);

    // Function to find turn around time for all processes
    findTurnAroundTime(proc, n, wt, tat);

    // Display processes along with all details
    cout << "Processes  " << " Burst time  "
         << " Arrival time  " << " Waiting time  " << " Turn around time\n";

    // Calculate total waiting time and total turn around time
    for (int i = 0; i < n; i++) {
        total_wt = total_wt + wt[i];
        total_tat = total_tat + tat[i];
        cout << "   " << proc[i].pid << "\t\t" << proc[i].bt << "\t\t"
             << proc[i].at << "\t\t" << wt[i] << "\t\t  " << tat[i] << endl;
    }

    cout << "Average waiting time = "
         << (float)total_wt / (float)n;
    cout << "\nAverage turn around time = "
         << (float)total_tat / (float)n;

    cout << endl;
}

int main() {
    // Process id's, burst time and arrival time
    Process processes1[] = {
        {1, 3, 0}, {2, 5, 2}, {3, 7, 4}, {4, 2, 6}, {5, 8, 8}, {6, 4, 10}, {7, 6, 12}, {8, 3, 14}, {9, 5, 16}, {10, 7, 18},
        {11, 25, 20}, {12, 22, 22}, {13, 28, 24}, {14, 30, 26},
        {15, 37, 28}, {16, 39, 30},
        {17, 3, 32}, {18, 6, 34}, {19, 4, 36}, {20, 7, 38}
    };
    Process processes2[] = {
        {1, 3, 0}, {2, 5, 2}, {3, 7, 4}, {4, 2, 6}, {5, 8, 8}, {6, 4, 10}, {7, 6, 12}, {8, 3, 14}, {9, 5, 16}, {10, 7, 18},
        {11, 3, 20}, {12, 6, 22}, {13, 4, 24}, {14, 7, 26}, {15, 5, 28}, {16, 8, 30}, {17, 2, 32}, {18, 6, 34}, {19, 4, 36}, {20, 7, 38},
        {21, 25, 40}, {22, 22, 42}, {23, 28, 44}, {24, 30, 46}, {25, 27, 48}, {26, 23, 50}, {27, 29, 52}, {28, 21, 54},
        {29, 37, 56}, {30, 39, 58}, {31, 36, 60}, {32, 38, 62},
        {33, 3, 64}, {34, 6, 66}, {35, 4, 68}, {36, 7, 70}, {37, 5, 72}, {38, 8, 74}, {39, 2, 76}, {40, 6, 78}
    };
    Process processes3[] = {
        {1, 3, 0}, {2, 5, 2}, {3, 7, 4}, {4, 2, 6}, {5, 8, 8}, {6, 4, 10}, {7, 6, 12}, {8, 3, 14}, {9, 5, 16}, {10, 7, 18},
        {11, 3, 20}, {12, 6, 22}, {13, 4, 24}, {14, 7, 26}, {15, 5, 28}, {16, 8, 30}, {17, 2, 32}, {18, 6, 34}, {19, 4, 36}, {20, 7, 38},
        {21, 3, 40}, {22, 6, 42}, {23, 4, 44}, {24, 7, 46}, {25, 5, 48}, {26, 8, 50}, {27, 2, 52}, {28, 6, 54}, {29, 4, 56}, {30, 7, 58},
        {31, 25, 60}, {32, 22, 62}, {33, 28, 64}, {34, 30, 66}, {35, 27, 68}, {36, 23, 70}, {37, 29, 72}, {38, 21, 74},
        {39, 37, 76}, {40, 39, 78}, {41, 36, 80}, {42, 38, 82},
        {43, 3, 84}, {44, 6, 86}, {45, 4, 88}, {46, 7, 90}, {47, 5, 92}, {48, 8, 94}, {49, 2, 96}, {50, 6, 98},
        {51, 3, 100}, {52, 6, 102}, {53, 4, 104}, {54, 7, 106}, {55, 5, 108}, {56, 8, 110}, {57, 2, 112}, {58, 6, 114}, {59, 4, 116}, {60, 7, 118}
    };
    
    int n1 = sizeof(processes1) / sizeof(processes1[0]);
    int n2 = sizeof(processes2) / sizeof(processes2[0]);
    int n3 = sizeof(processes3) / sizeof(processes3[0]);

    findavgTime(processes1, n1);
    findavgTime(processes2, n2);
    findavgTime(processes3, n3);

    return 0;
}