
#!/python3
#sorted order


try:
    x = int(input('Enter an integer (0 to to exit): '))
except ValueError:
    print ('Your entry was not an integer. Exiting...')
num_list = []

while x != 0:
    num_list.append(x)
    try:
        x = int(input('Enter an integer (0 to to exit): '))
    except ValueError:
        print ('Your entry was not an integer. Exiting...')
        
num_list = sorted(num_list)

print (num_list)
