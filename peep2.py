emails  =  """zuck@facebook.com
sunder33@google.com
jeff42"""

# Split into individual addresses
email_list = emails.splitlines()

for email in email_list:
    if "@" in email:
        user_id, domain_full = email.split("@")
        if "." in domain_full:
            domain, suffix = domain_full.split(".")
            print(f"Email: {email}")
            print(f"  User ID: {user_id}")
            print(f"  Domain: {domain}")
            print(f"  Suffix: {suffix}")
        else:
            print(f"Email: {email} → domain missing suffix")
    else:
        print(f"'{email}' is not a valid email address")
