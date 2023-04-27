#!/usr/bin/env python3
#
# logic - april 27, 2023
#
# Program to take a list of email addresses consisting of letters and numbers
# and report the most common base letters, and optionally output a new list
# of email addresses with those base letters and an optional range of numbers.

import argparse
import re

# Function to read in a file and store valid emails in a list
def read_file(filename):
    # Open the file
    f = open(filename, "r")
    # Initialize the list of emails
    emails = []
    # Read in each line of the file
    for line in f:
        # Split the line into a list of words
        words = line.split()
        # For each word in the line
        for word in words:
            # If the word is a valid email
            if is_valid_email(word):
                # Add it to the list of emails
                emails.append(word)
    # Close the file
    f.close()
    # Return the list of emails
    return emails

# Function to check if a string is a valid email address
def is_valid_email(candidate):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, candidate))

# Function to get the base letters of an email address
def get_base_letters(email):
    # Initialize the base letters
    base_letters = ""
    # For each character in the email
    for char in email:
        # If the character is a letter
        if char.isalpha():
            # Add it to the base letters
            base_letters += char
        # If the character is a number
        elif char.isdigit():
            # Stop looking for base letters
            break
    # Return the base letters
    return base_letters

parser = argparse.ArgumentParser(
    description='Analyze a provided list of email addresses and report the most common base letters.')
parser.add_argument('-i', '--input', type=str, help='the name of the file to analyze')
parser.add_argument('-o', '--output', type=str, help='the name of the file to output the new list of emails to')

args = parser.parse_args()

emails = read_file(args.input)
base_letters = dict()
for email in emails:
    # print(email)
    base_letters[get_base_letters(email)] = base_letters.get(get_base_letters(email), 0) + 1
sorted_base = sorted(base_letters.items(), key=lambda x: x[1], reverse=True)
two_chars = list()
three_chars = list()
for key, value in sorted_base:
    if len(key) == 2:
        # print(f"{key}: {value}")
        two_chars.append(key)
    if len(key) == 3:
        # print(f"{key}: {value}")
        three_chars.append(key)
print(f"There are {len(two_chars)} unique 2char base letters.")
print(f"There are {len(three_chars)} unique 3char base letters.")
print(f"There are {len(sorted_base)} unique base letters.")

if args.output:
    output_file = open(args.output, "w")
    for two_char in two_chars:
        for num in range(151, 201):
            output_file.write(f"{two_char}{num}\n")
    output_file.close()

