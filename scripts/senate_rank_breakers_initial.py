"""
A script to find senators most likely to break
ranks on impeachment votes.

We use the ProPublica Congress Members API
to find senators most likely to vote
against their own party.


USAGE:

From the command-line:

    python senate_rank_breakers.py

OUTPUT:

    A list of top 5 most likely to break ranks
    from each major party.

"""
import os
import requests


# The entry point for our script, which calls
# other functions defined below. 
# See the bottom of the script for a common
# Python "idiom" for invoking the "main" function.
def main():
    api_key = os.environ["PROPUBLICA_API_KEY"]
    members = get_members_data(api_key)
    democrats_results = democrat_sort(members)
    republican_results = republican_sort(members)
    dem_list = print_dem(democrats_results)
    repub_list = print_repub(republican_results)

    # TODO: invoke the other functions
    # you create to sort candidates, print
    # the report on top 5 candidates, etc.

### TASK-SPECIFIC FUNCTIONS GO HERE ###
#   for each party (D) or (R) 
#   sort by votes_against_party_pct (high to low)
#   

# For example, here's a function one to get you started
def get_members_data(api_key):
    headers = {'X-API-Key': api_key }
    url = "https://api.propublica.org/congress/v1/116/senate/members.json"
    request = requests.get(url, headers=headers)
    total = request.json()
    members = total["results"][0]["members"]
    return members 

def democrat_sort(members):
    democrats = []
    sorted_dem = []
    for person in members:
        if person["party"] == "D":
            democrats.append(person)
    sorted_dem = sorted(democrats, key=lambda x:x["votes_against_party_pct"], reverse=True) 
    top_five_dem = sorted_dem[0:5]
    return top_five_dem 
    # print(top_five_dem)

def republican_sort(members):
    repub = []
    sorted_repub = []
    for person in members:
        if person["party"] == "R":
            repub.append(person)
    sorted_repub = sorted(repub, key=lambda x:x["votes_against_party_pct"], reverse=True) 
    top_five_repub = sorted_repub[0:5]
    return top_five_repub
    # print(top_five_repub)

def print_dem(top_five_dem):
    print("Democrat")
    for x in top_five_dem:
        first_name_dem = x["first_name"]
        last_name_dem = x["last_name"]
        state_dem = x["state"]
        against_pct_dem = str(x["votes_against_party_pct"])
        txt = "{} {} ({}) votes against the party {}% of the time" 
        print(txt.format(first_name_dem, last_name_dem, state_dem, against_pct_dem))
    # print('\n')

def print_repub(top_five_repub):
    print('\n' + "Republican")
    for x in top_five_repub:
        first_name_repub = x["first_name"]
        last_name_repub = x["last_name"]
        state_repub = x["state"]
        against_pct_repub = str(x["votes_against_party_pct"])
        txt = "{} {} ({}) votes against the party {}% of the time" 
        print(txt.format(first_name_repub, last_name_repub, state_repub, against_pct_repub))

# initial printing idea:  
# def print_dem(top_five_dem):
#     print("Democrat")
#     for x in top_five_dem:
#         print(x["first_name"] + " " + x["last_name"] + "(" + x["state"] + ")" + " votes against the party " + str(x["votes_against_party_pct"]) + "% of the time.") 

# def print_repub(top_five_repub):
#     print("Republican")
#     for x in top_five_repub:
#             print(x["first_name"] + " " + x["last_name"] + "(" + x["state"] + ")" + " votes against the party " + str(x["votes_against_party_pct"]) + "% of the time.") 


            

    # Lastly, below is a placeholder "data" value that
    # you should replace with actual data from the ProPublica API
    data = {}
    return data


# Use the standard convention for triggering
# the "main" function when the script is
# invoked on the command line:
# https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    main()
