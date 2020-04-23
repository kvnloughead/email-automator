# Email Automater

A fairly simple email automation program, written in Python using the `email` and `smtplib` packages.  Now with a handy command line interface.

### Usage

Just run `python3 main.py` in your terminal and follow instructions.  If you don't want to deal with entering full path names, put your contact 
listing and message template in the same folder.   

  - The contact listing should be a .csv file with headers.  
    - Minimally it must contain all of your contacts email addresses, but additionally it can contain other parameters to be passed into the message template.  
  - Optionally you may include the names of any files that you want to attach.  
  - When writing your message template, any variables from your contacts csv file get referenced by `$header` where header is the header in the appropriate column.  

A minimal example can be found in this repo involving the following files:

  - `sample.csv` (enter your own email into this file for testing)
  - `sample.txt`
  - `attach_me.txt`

### Limitiations

Currently you still need to edit `main.py` if you are going to change any of the fields in the csv.  Here are the parts to edit:

```python3
for first_name, last_name, email, fav_lang in zip(contacts['first_name'], contacts['last_name'], contacts['email'], contacts['fav_lang']):
    # create a message
    msg = MIMEMultipart()
    
    # fill in template fields
    message = message_template.substitute(FIRST_NAME=first_name.title(), LAST_NAME=last_name.title(), FAV_LANG=fav_lang.title())
```

Its a pain, I need to refactor this.



