# logic

Unfortunately named during a brief period where I thought it was clever to use the daily wordle as the name for new programs. The purpose of this program is to analyze a list of enumerated email addresses that have a base set of alpha characters and incrementing numbers at the end, to identify the most common base letters for further enumeration.

For example: js1, js2, js3 are going to increment and be used much more quickly than zq1, yz1, etc

## email list analyzer

```
usage: logic.py [-h] [-i INPUT] [-o OUTPUT]

Analyze a provided list of email addresses and report the most common base letters.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        the name of the file to analyze
  -o OUTPUT, --output OUTPUT
                        the name of the file to output the new list of emails to
```