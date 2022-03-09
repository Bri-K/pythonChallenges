import urllib.request

nothing = 12345

lst = []

for i in range(400):
    request_url = urllib.request.urlopen(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}')
    new_nothing = request_url.read().decode().split()[-1]
    lst.append(new_nothing)
    nothing = new_nothing

print(lst)
