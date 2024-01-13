## How to set up task scheduler
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
    
    Conditions
        ☐ Stop if the computer switches to battery power
        ☐ Start the task only if the computer is on AC power
        ☑ Wake the computer to run this task
    
    Settings
        ☑ Allow task to be run on command
        ☐ Stop the task if it runs longer than:
    
        If the task is running, then the following rule applies
        Do not start a new instance    v

</pre>
