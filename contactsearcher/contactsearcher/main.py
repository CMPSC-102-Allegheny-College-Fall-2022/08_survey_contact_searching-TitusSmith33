"""Define the command-line interface for the contact searching program."""

import typer
from typing import Optional
from pathlib import Path
from contactsearcher import search


# Create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def contactsearcher(
    job_description: str = typer.Option(..., prompt=True),
    contacts_file: Optional[Path] = typer.Option(None),
) -> None:
    """Search for either an email address of a contact who has a job in the file."""
    # declare an empty contacts_text
    contacts_text = ""
    # display details about the file provided on the command line
    # --> the file was not specified so we cannot continue using program
    if contacts_file is None:
        typer.echo("No contacts file specified!")
        raise typer.Abort()
    # --> the file was specified and it is valid so we should read and check it
    if contacts_file.is_file():
        contacts_text = contacts_file.read_text()
        contacts_line_count = len(contacts_text.splitlines())
        typer.echo(
            f"The contacts file contains {contacts_line_count} people in it! Let's get searching!"
        )
    # --> the file was specified but it does not exist so we cannot continue using program
    elif not contacts_file.exists():
        typer.echo("The contacts file does not exist!")
    # display details about the search key for the job provided on the command line
    typer.echo("")
    typer.echo(
        f'  We are looking for contacts who have a job related to "{job_description}":'
    )
    print()
    # Perform the search for all of the relevant email addresses and jobs
    job_value = search.search_for_email_given_job(job_description, contacts_text)
    email_value = search.find_email(job_description, contacts_text)
    # begin a counter
    counter = 0
    # iterate through the email list
    for item in email_value:
        # print the email with the corresponding job
        print(f"  {email_value[counter]} is a {job_value[counter]}")
        # add to the counter
        counter += 1
    print()
    print("Wow, we found some contacts! Email them to learn about your job!")
