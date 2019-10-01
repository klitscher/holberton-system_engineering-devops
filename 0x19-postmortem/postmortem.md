# Postmortem

## Issue Summary

Between the hours of 13:00:00 and 17:35:08 it was determined that our home page was no longer accessible to 100% of our users, and instead users were met with a 500 error page. This negatively impacted bot our user's experience: No one likes to see an error page. As well as our reputation: with all the competition out there in the ambient music playlist generator scene, even a few minutes of downtime is catastrophic for our bottom line. The root cause was determined to be an incorrectly pushed configuration file by our SRE the night before.The root cause was determined to be an incorrectly pushed configuration file by our SRE the night before. 

![Uh oh](https://media.giphy.com/media/3oFzm0o2jMKftsaBoc/giphy.gif)
## Timeline

 - 12:59:00: SRE merges own pull request
 - 13:00:00: Site goes down
 - 13:00:56: Monitoring alert notifies the SRE that site is not accessible
 - 13:01:00: SRE starts swearing
 - 13:01:30: SRE attempts to restart service, successfully restarts, but error persists.
 - 13:02:00: SRE starts swearing more audibly
 - 13:02:10: SRE looks at processes, history, top etc, and does not find any glaring issues.
 - 13:10:00: SRE is now heard cursing from other end of office
 - 13:11:00: SRE escalates to senior SRE AKA "The error whisperer"
 - 13:12:00: Whisperer runs strace and finds erroneous entry in apache config file
 - 13:12:50: Whisperer fixes config file
 - 13:13:15: Whisperer runs git blame
 - 13:13:16: SRE starts nervously backing away
 - 13:13:20: Whisperer looks at SRE

![Whispers saves the day](
https://media.giphy.com/media/zKOqnQprdq2gU/giphy.gif)

## Root Cause

The problem was a specific line in the config file that had a typo: `.phpp` instead of `.php`. The error was fixed by a quick edit and save of the config file on the web server. This error was the direct result of the SRE being hungover from the night before. He has since be banished to the shadow realm (phone support) temporarily.

![Sad IT](https://media.giphy.com/media/13Xb9HKafusl4k/giphy.gif)  

## Corrective and Preventative Measures

Going forward, the team has decided on new implementations rules for pushing code to production:

 1. Code must be tested extensively before applied
 2. If committing to master, you are not allowed to merge your own pull request
 3. You are not allowed to code while intoxicated or hung-over (or at least make sure #2 is followed!)
 4.  Even if you think your code is the bestest ever, it MUST BE REVIEWED BY SOMEONE ELSE BEFORE BEING MERGED

![NO DRINKING](https://media.giphy.com/media/l41JFwebjfaxdPliU/giphy.gif)
 
