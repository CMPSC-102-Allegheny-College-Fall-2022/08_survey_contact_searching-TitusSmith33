# Contact Searching

## Titus Smith

## Program Output

### What is the output from running the following commands?

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

```
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "engineer":

  joe70@yahoo.com is a Network engineer
  torresjames@white.info is a Electrical engineer
  grahamjoel@castillo-gilbert.net is a Engineer, technical sales
  gsutton@miller.com is a Engineer, maintenance
  gharris@villarreal-snow.com is a Water engineer
  williamsondavid@lopez.com is a Automotive engineer
  ronald83@yahoo.com is a Maintenance engineer
  zmarshall@yahoo.com is a Control and instrumentation engineer
  christopher35@yahoo.com is a Civil engineer, consulting
  jacquelinedavid@hotmail.com is a Engineer, electronics
  espinozadaryl@hill-maddox.com is a Engineering geologist
  edwardsjacob@gmail.com is a Chemical engineer

Wow, we found some contacts! Email them to learn about your job!
```

- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`

```
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "neer":

  joe70@yahoo.com is a Network engineer
  torresjames@white.info is a Electrical engineer
  grahamjoel@castillo-gilbert.net is a Engineer, technical sales
  gsutton@miller.com is a Engineer, maintenance
  gharris@villarreal-snow.com is a Water engineer
  williamsondavid@lopez.com is a Automotive engineer
  ronald83@yahoo.com is a Maintenance engineer
  zmarshall@yahoo.com is a Control and instrumentation engineer
  christopher35@yahoo.com is a Civil engineer, consulting
  jacquelinedavid@hotmail.com is a Engineer, electronics
  espinozadaryl@hill-maddox.com is a Engineering geologist
  edwardsjacob@gmail.com is a Chemical engineer

Wow, we found some contacts! Email them to learn about your job!
```

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

```
from contactsearcher import search
```

This line of code is what makes the functions that are executed in the `search` module, available in the `main` module.This line of code is simple, yet makes the program much easier to read, understand, and execute. It is saying that from the `contactsearcher` which contains multiple modules, including `main` and `search`, look inside that file. Inside that file should be a module `search` and it wants to import everything from that module to be available for use in the `main`.

#### The source code statement that extracts the current job description for a contact

```
job_description: str = typer.Option(..., prompt=True)
```

This line of code can be found in the information about the `main` function. This allows for the user to include the job they are searching for inside the command line. This makes it easier rather than asking the user to import it after the function has began, just including the `job_description` variable as a string to be filled in the command line makes the program much easier and faster for the user.

#### Invocation of the function called `search_for_email_given_job`

```
job_value = search.search_for_email_given_job(job_description, contacts_text)
```

This line is calling the `search_for_email_given_job` function and assigning the return of that function to the variable `job_value`, which is a list of strings. The variable is set equal to "search." which tells the program that the next part of the code will be from the `search` module, which was imported earlier. The period is then followed by the name of the function that needs to be called. The function is the passed with variables that match the expected inputs from the `search` module, however the variables have meaning within the `main` module and function. This then sets the list that the `search_for_email_given_job` returns, which is filled with all of the jobs that match what is being searched for.

#### Test case for the function called `search_for_email_given_job`

```
def test_find_zero_matching_result():
    """Check to ensure that search for contacts works for one match."""
    contacts_database = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    contacts_list = search.search_for_email_given_job("nurse", contacts_database)
    assert len(contacts_list) == 0
    contacts_list = search.search_for_email_given_job(
        "physical therapit", contacts_database
    )
    assert len(contacts_list) == 0
```

This is one of the example test case for the program to ensure the program is executing as expected. These test suits test different aspects of the program, such as if there are no matches, only one match, multiple matches, and more. This particular test is making sure the program can correctly identify when there are no matches. The test gives a sample data base with a few contacts and jobs and then runs the program to see if it gets the expected output. This test searches for jobs that can not be found in the sample data base so the list that the program outputs should have a length of 0, and this test is calling the function with the fake data base and jobs that don't exists to see if the function works correctly.

#### Execute trace of the `contactsearcher` program

The function first imports the functions from `search` at the top of the `main` module. The function then calls the two functions from `search` that I needed for my method of implementation. Within the `main` function it runs the first function, `search_for_email_given_job` and sets that list (which is the list of all the jobs that match the description) equal to the variable `job_value`. It then uses a similar function call to call the function `find_email` which returns a list of the emails that match with the jobs we are searching for. It then assigns this list to the variable `email_value`. My reasoning for this method was I figured if I did two different functions that searched through the same CSV file that the indexing would be the same as long as the iteration in the functions look through the same thing. So the index of the emails and jobs are the same in the two lists which made the printing process much easier. I then looped through with a counter variable to print of the email from the `email_value` and the job from the `job_value`. The command line gives the functions both the file and the job description it is looking for.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

One area that I have struggled with so far this semester is understanding and implementing outside libraries into my programs. Outside libraries offer a lot of help towards making a lot of coding much easier, because someone has already likely thought through the code you are struggling with just for a simple aspect of your program, so instead of wasting your time with that, using imports will make your life so much easier. I have overcome this issue through our projects and reading more about the imports we are using in our projects. We import a lot of the same things so I have looked into what those imports are actually accomplishing.

### Based on your experiences with this project, what is one way in which you want to improve?

This project has shown that I could still use some more work studying how to work with CSV files and different aspects of them. I understand the way I implemented this function is probably not the easiest, as well as not the most efficient, so I hope to become better equipped with how to work with CSV files. I hope to continue to work with CSVs because they are clearly an import way of filing data, and working with this information can be extremely helpful when studying large data sets.
