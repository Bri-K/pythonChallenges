

nothing = '90052'


while True:
    try:
        with open(f'channel/{nothing}.txt', 'r') as f:
            f_read = f.read()
            print(f_read)
            next_nothing = f_read.split()[-1]
            nothing = next_nothing
    except:
        break

# Breaks at 46145.txt; text is "Collect the comments."
