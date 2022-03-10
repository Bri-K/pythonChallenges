import zipfile

# Same skeleton as py_challenge_6a.py but now we collect comments.

nothing = '90052'

comments = []

with zipfile.ZipFile('channel.zip', 'r') as archive:

    while True:
        try:
            with open(f'channel/{nothing}.txt', 'r') as f:
                f_read = f.read()

                comment = archive.getinfo(f'{nothing}.txt').comment.decode()
                comments.append(comment)
                next_nothing = f_read.split()[-1]
                nothing = next_nothing
        except:
            break

print(''.join(comments))

# Prints HOCKEY spelled with the letters of 'oxygen'
# After replacing extension with hockey.html we see
# "it's in the air. look at the letters."
# Finally, replace extension with oxygen.html.
