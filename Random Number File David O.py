import random 

def main():
    num_rand = int(input('How many random numbers do you want this file to hold?'))
    outfile = open('random_numbers.txt', 'w')
    
    for num in range(1, num_rand+1):
        rand_num = random.randint(1,500)
        outfile.write(str(rand_num) + '\n')
        
outfile.close()

print('Random Numbers have been written to random_numbers.txt.')

main()

    