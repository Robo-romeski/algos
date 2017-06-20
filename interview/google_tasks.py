"""
You have a long list of tasks that you need to do today. Task i is 
specified by the deadline by which you have to complete it (Di) and 
the number of minutes it will take you to complete the task (Mi). 
You need not complete a task at a stretch. You can complete a part of 
it, switch to another task and then switch back.
You've realized that it might not actually be possible complete all the 
tasks by their deadline, so you have decided to complete them so that the maximum amount
by which a task's completion time overshoots its deadline is minimized.
Input:
The first line contains the number of tasks T. Each of the next T lines contains 
two integers Di and Mi.
Output:
Output T lines. The ith line should contain the minimum maximum overshoot you 
can obtain by optimally scheduling the first i tasks on your list. See the sample
input for clarification.
"""
