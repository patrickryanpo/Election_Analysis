
count = 0
while count < 1:
    print("Hello World")
    count = count + 0.5

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county, voters in voting_data.items():
#print(f"{voting_data[0]['county']} county has {voting_data[0]['registered_voters']} registered voters.")
#print(f"{voting_data[1]['county']} county has {voting_data[1]['registered_voters']} registered voters.")
#print(f"{voting_data[2]['county']} county has {voting_data[2]['registered_voters']} registered voters.")
#for county, registered_voters in voting_data
    print(f'{voting_data[county]} has {voting_data[registered_voters]}.')
