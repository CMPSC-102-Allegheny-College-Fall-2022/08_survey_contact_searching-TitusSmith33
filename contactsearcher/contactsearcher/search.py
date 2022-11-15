"""Search for an email address given a fragment of a job description."""

from typing import List

# import csv

# note: see https://docs.python.org/3/library/csv.html


def search_for_email_given_job(job_description: str, contacts: str) -> List[str]:
    """Search for and return job description(s)."""
    # Create an empty list of the jobs
    job_list = []
    # job_list = []
    # iterate through the file, parsing it line by line
    for line in contacts.splitlines():
        # email_str = line[: line.find(",")]
        # find the job for each person
        job_str = line[line.find(",") + 1 :].replace('"', "")
        # if the job you are looking for is in the job title execute this code
        if job_description.lower() in job_str.lower():
            # add the job and email to the list
            job_list.append(job_str)
        # current_contact_job = contact_line[1]
    # return the list with job information
    return job_list


def find_email(job_description: str, contacts: str) -> List[str]:
    """Find the email correspoding to the jpb we are looking for."""
    # create an empty list for the emails
    email_list = []
    # iterate through the csv
    for line in contacts.splitlines():
        # find the email per line
        email_str = line[: line.find(",")]
        # find the job per line
        job_str = line[line.find(",") + 1 :].replace('"', "")
        # if the job you are looking for is in the job title execute this code
        if job_description.lower() in job_str.lower():
            # add the email to the list
            email_list.append(email_str)
    # return the list of emails with the index corresponding to the job list
    return email_list
