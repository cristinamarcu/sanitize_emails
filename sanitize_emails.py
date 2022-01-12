import re

'''
This function finds email addresses in a text and validates them against an allowed list of domains
Returns the email addresses which are not allowed/valid
'''
def sanitize_emails(text: str, allowlist: list[str]) -> list[str]:
    emailadressre = re.compile(r'([a-zA-Z0-9_.+]+@([a-zA-Z0-9_.+]+))')
    text1 = emailadressre.findall(text)
    notallowlist = []
    for elem in text1:
        if elem[1] not in allowlist:
            notallowlist.append(elem[0])

    return notallowlist




notallowedemails = sanitize_emails(
    "my email address is cristina@yahoo.com . Your email is cosmin@gmail.com . David has the address david@co.uk",
    ["yahoo.com", "gmail.com"])
print(notallowedemails)
