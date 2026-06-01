![[Pasted image 20260221120919.png]]
## Fundamentals and Functionalities of Operating Systems
### Executive Summary
- An Operating System (OS) serves as the indispensable system software that acts as a primary interface between a computer's hardware and the end user. 
- Without an OS, interacting with hardware would require users to write complex, repetitive programs for every specific task, such as printing a document or executing a process.
- The two primary objectives of an OS are:-
	1. Convenience
	2. Throughput.
#### Example
While Windows has historically dominated the market by prioritizing user convenience, Linux has gained traction by focusing on throughput—the number of tasks executed per unit of time. Beyond providing an interface, an OS performs critical management roles, including resource allocation, process scheduling, memory and storage management, and system security.

--------------------------------------------------------------------------------
# Conceptual Framework of the Operating System
### Definition and Interface
- The Operating System is defined as system software that facilitates interaction between the user and the computer hardware. It functions as a layer of abstraction; the user interacts with the OS, and the OS, in turn, manages the hardware.
- Hardware Components Managed
- The OS manages several critical hardware categories:
	• **CPU:** Often referred to as the "brain" of the system.
	• **Main Memory (RAM):** The volatile memory where active processes reside.
	• **Secondary Memory:** Permanent storage devices such as Hard Disks.
	• **Input/Output (I/O) Devices:** Includes keyboards, mice, printers, and scanners.

### The Necessity of an OS
- In the absence of an operating system, the interaction between user and hardware would be prohibitively complex:
	• **Repetitive Programming:** Users would need to write individual programs for every device interaction (e.g., a specific program just to tell a printer to print).
	• **Lack of Authority:** Without an intermediary, there would be no authority to manage resource sharing. One user could monopolize a hardware device without a mechanism to release it for others.
--------------------------------------------------------------------------------
### Primary Goals: Convenience vs. Throughput
The evolution and market share of various operating systems are driven by two competing goals:

| Goal            | Description                                                                                | Representative OS                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| **Convenience** | Focuses on making the system easy to use for the average person.                           | **Windows:** Historically held 95% of the market; currently holds approximately 82% (as of 2018 data). |
| **Throughput**  | Defined as the number of tasks executed per unit of time. Focuses on efficiency and speed. | **Linux:** Increasing in popularity as tasks become more complex and time-efficiency becomes critical. |

_Note: Other significant operating systems include Apple’s Macintosh (Mac OS)._

--------------------------------------------------------------------------------
### Core Functionalities of an Operating System

The OS performs five major functions that ensure the system operates efficiently and securely:
##### Resource Governor (Resource Manager)
- The OS manages hardware allocation, which is particularly vital in parallel processing environments or at the server level where multiple users send simultaneous requests.
- It determines how much hardware is provided to each user and for what duration, ensuring the system is neither overloaded nor underutilized.
##### Process Management
- This involves managing the execution of multiple concurrent processes (e.g., running Microsoft Word, a media player, and a game simultaneously).
• **CPU Scheduling:** The OS uses various algorithms to decide how and when a process (a program in execution) moves to the CPU for processing. 
##### Storage Management
- This function concerns the permanent storage of data on secondary devices like hard disks.
• **File Systems:** The OS manages data via file systems such as NFS (Networked File System) and CIFS (Common Internet File System).

• **Physical Organization:** It manages how data is stored across the tracks and sectors of the disk architecture.

##### Memory Management (RAM)
- **Unlike storage management, memory management is constrained by the limited size of RAM.
		• **Multi-tasking/Multi-programming:** Processes must be brought into the RAM before being transferred to the CPU.
		• **Allocation and Deallocation:** The OS must efficiently allocate space for new processes and deallocate space once a process is complete.
		• **Swapping:** If the RAM is full, the OS manages "swapping" processes in and out of memory to ensure continuous execution.
##### Security and Privacy
- The OS protects both the system and individual user data:
	• **Authentication:** Providing password protection to ensure only authorized users gain access. Windows, for example, utilizes the **Kerberos** security protocol.
	• **Process Isolation:** The OS prevents processes from interfering with one another. If a process attempts to access memory outside its allocated segment (e.g., Process B trying to access Process A's data), the OS will instantly block that process.
--------------------------------------------------------------------------------

### User Interaction and System Mechanisms
Users can access the OS and hardware through two primary methods:
1. **Applications (GUI):** Most users interact through a Desktop interface and applications (like Microsoft Office). When a user clicks "Print," the application communicates with the OS, which then handles the hardware interaction. The interface is designed so the user "doesn't even feel" they are accessing hardware.
2. **Shell/Terminal:** Advanced users can access the OS "kernel" directly via a Command Prompt (Windows) or Terminal (Linux).

##### The Role of System Calls
- Regardless of the interaction method, the OS operates through **System Calls**. These are specific instructions that invoke OS functions. Common examples include:
	• **Open:** Used to access a file.
	• **Read/Write:** Used to handle data within files.
	• **Print:** Invokes the necessary hardware commands.
Every user action, from a double-click to a command-line entry, eventually triggers a system call that allows the OS to mediate between the application and the hardware.

