#### Do What Now ?
<pre>
This example writes the current date and time to a text file.
</pre>


#### Python Installation
<pre>
install latest python 
    e.g. C:\Python312
install for all users
enable everything that puts python in PATH
copy python.exe and paste a duplicate with a different name, e.g. python_ht.exe
this will allow the *.bat file to check if this specific instance of python script is running
</pre>


#### How to set up task scheduler
<pre>

Task Scheduler > Create Basic Task

Trigger(s)    • When the computer starts (at system startup) Enabled  
Action        • Start a program

Start a Program
    - browse to the *.bat file
    - Program/script: <full path to *.bat file> e.g. C:\from_git\WinStartAutoPy\hello_time.bat
    - start in (optional): <folder containing *.bat file> C:\from_git\WinStartAutoPy\
        ○ this ensures that the output is in this folder

☑ Open the Properties dialog for this task when I click Finish
  Properties

    General
        • Run whether user is logged on or not
        ☑ Run with highest privileges
        Configure for: Windows 10

    Triggers
        At startup Repeat task every: <x_minutes>
            ☑ Repeat task every: [5 minutes]    for a duration of: [indefinitely]
            ☑ Enabled
                
        At task creation / modification
            ☑ Repeat task every: [5 minutes]    for a duration of: [indefinitely]
            ☑ Enabled

                
    Conditions
        ☐ Stop if the computer switches to battery power
        ☐ Start the task only if the computer is on AC power
        ☑ Wake the computer to run this task

                
    Settings
        ☐ Allow task to be run on command
        ☑ Run task as soon as possible after a scheduled start is missed
        ☑ If the task fails, restart every: [1 minute]
            Attempt to restart up to: [3] times
        ☐ Stop the task if it runs longer than:
    
        If the task is running, then the following rule applies
        Run a new instance in parallel    v
            note: this option assumes that what is being run will check for a duplicate presence and not generate a duplicate

</pre>
