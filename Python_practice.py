#print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"] 

for i in range(len(counties)): 
    print(counties[i])

numbers = [0,1,2,3,4]
for num in range(5): 
    print(num)

#counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}

#for county,voters in counties_dict.items():
    #print(county,voters)

counties_dict = {"Arapahoe": 422829, "Denver":463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)



#if "Arapahoe" in counties and "El Paso" not in counties: 
    #print("Only Arapahoe is in the list of counties.") 
#else: print("Arapahoe is in the list of counties and El Paso is not in the list.")