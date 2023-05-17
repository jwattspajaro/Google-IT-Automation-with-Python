### Introduction to Python Email Library
Email messages look simple in an email client. But behind the scenes the client is doing a lot of work to make that happen! Email messages -- even messages with images and attachments -- are actually complicated text structures made entirely of readable strings!

The [Simple Mail Transfer Protocol (SMTP)](https://tools.ietf.org/html/rfc2821.html) and [Multipurpose Internet Mail Extensions (MIME)](https://tools.ietf.org/html/rfc2045) standards define how email messages are constructed. You could read the standards documentation and create email messages all on your own, but you don't need to go to all that trouble. The email built-in Python module lets us easily construct email messages.

We'll start by using the email.message.EmailMessage class to create an empty email message.
