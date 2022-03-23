"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

#open the sales report
f = open('sales-report.txt')

#read each line from the report
for line in f:
    #remove the whitespace at the end
    line = line.rstrip()
    #put each word into a list
    entries = line.split('|')
    #get sale person's name
    salesperson = entries[0]
    #get the total number of melonds sold by the sale's person
    melons = int(entries[2])

    #if the sales person already in the list
    if salesperson in salespeople:
        #find the index of the sales person in the list
        position = salespeople.index(salesperson)
        #update the corresponding number of melonds sold by the sale's person
        melons_sold[position] += melons
        
    else:
        #if the sales person is not in the list
        #record the name of the person and the number of melons sold by
        #this person
        salespeople.append(salesperson)
        melons_sold.append(melons)

#show the name of the sales person and the total numbers of melon sold by
#each of them
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')