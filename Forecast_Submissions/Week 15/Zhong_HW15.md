# Forecast_Submissions

## Name: Xiang Zhong

### Date: 12/6/2021

### Assignment Number: 15
----
### Summary
1. What resources did you request on Ocelote? How long did you wait in the queue for your job to run and how long did it take to run?
    
    I did not use Ocelote, but on Puma I just asked for 1 node and 4 cores and 20 Gb of memory for 1 minute as written in Zhong_HW15.sh. I tested my whole running time is only about 40 seconds in total so changed 5 minutes to 1 minute. I didn't really find the waiting time, and the exact running time disappeared after the job is finished, but before I remember the task needs ~39 seconds. I used a timer to roughly estimate the waiting time, after I changed request time from 5 minutes to 1 minute, the waiting time is about 4.5 minutes, before, 5-minute request time needs a little bit more time to wait. I guess the detailed performance could be checked on tomorrow morning as written in the .out file. 


2. What was the most confusing part to you about setting up and running your job on Ocelote?
    
    I am not sure why I have to type "interactive" before trying to submit a job. I forgot to do so before, then pip install and the whole submitting steps cannot be done. Also, I believe there should be a way to check the waiting time and running time, I just do not know how. Others are fine.


3. Where else did you run your job? How did the setup compare to your run on Ocelote?
    
    At the beginning, I tried to use UA HPC's Jupyter server to run an Ipython notebook, but somehow request for a server starts from 1 hour to ask. I worried it would make me wait for too long, so changed to run an Ipython notebook on google Colab.


    Google Colab does not need to setup too much things, it is its running logic a little bit different from running a script on PC. Like how to link local drive's file with it, apparently they have some complex ways to achieve that, but to save time, I just uploaded the input files onto google drive instead. In that way, it hinted me that google drive will clear all files every 1 hour, so my solution will definitely fail when we need more time.


4. What questions do you still have after doing this?
    
    I have a lot of questions.
    
    Like is qbs more convenient than the approach we are using right now?
    
    How to check each jobs' details like I wrote in problem #2.
    
    Is running codes on Google Colab also faster?
    
    How many nodes or cores can we use on Google Colab?
    
    How to write a .sh file to ask for more execution information?

---
### Submission
For the submission, the output file for Puma is:
- slurm-2722607.out

Output for google colab is a screen shot:
- Screen Shot 2021-12-06 at 11.11.54 AM

Python script run on Puma is:
- Zhong_HW15.py

On google colab is:
- Zhong_HW15.ipynb

The submission script is:
- Zhong_HW15.sh

On google colab I did not use submission script.
