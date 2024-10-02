# Pollyanna Generator

## Introduction
My extended family does a [Pollyanna gift exchange](https://en.wikipedia.org/wiki/Pollyanna#:~:text=The%20word%20%22pollyanna%22%20may%20also,surrounding%20areas.) during the holliday season but with a twist. Because we have a larger extended family with 5 different immediate families, we have a rule that you cannot get a Pollyanna who is also from your own immediate family. The purpose of this program is to automatically generate Pollyannas for the entire extended family without breaking any of the rules of the gift exchange.

## Instructions to Run
1. Download PollyannaSample.py and open it in your text editor of choice
2. Find the emailSender and emailPassword variables
3. The emailSender variable will be a string containing the email address you wish to send from
4. the emailPassword variable will be a string containing an App Password
5. Generate an App Password for the email address used in the emailSender variable <br>
&nbsp; a) For gmail, this can be found under Google Account and searching for App Password <br>
&nbsp; b) I am unfamiliar with other email providers, however it is very easy to create a Google Account for this purpose <br>
6. The App Password will contain 4 strings of 4 characters, ex: "aaaa bbbb cccc dddd"
7. Populate the famName and famEmail lists with your families' respective information
8. Execute the python program.
