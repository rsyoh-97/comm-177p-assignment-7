import os
import requests


def main():
    api_key = os.environ["PROPUBLICA_API_KEY"]
    members = get_members_data(api_key)
    sorted_members = sort(members)
    final_list = print_names(sorted_members)

def get_members_data(api_key):
    headers = {'X-API-Key': api_key }
    url = "https://api.propublica.org/congress/v1/116/senate/members.json"
    request = requests.get(url, headers=headers)
    total = request.json()
    members = total["results"][0]["members"]
    return members 

def sort(members): 
    democrats = []
    repub = []
    sorted_members = []
    for person in members:
        if person["party"] == "D":
            democrats.append(person)
            sorted_dem = sorted(democrats, key=lambda x:x["votes_against_party_pct"], reverse=True) 
            top_five_dem = sorted_dem[0:5]
        elif person["party"] == "R": 
            repub.append(person)
            sorted_repub = sorted(repub, key=lambda x:x["votes_against_party_pct"], reverse=True) 
            top_five_repub = sorted_repub[0:5]
    sorted_members.append(top_five_dem)
    sorted_members.append(top_five_repub)
    return sorted_members

def print_names(sorted_members):
        print("Democrat:")
        for x in sorted_members[0]:
            first_name_dem = x["first_name"]
            last_name_dem = x["last_name"]
            state_dem = x["state"]
            against_pct_dem = str(x["votes_against_party_pct"])
            txt = "{} {} ({}) votes against the party {}% of the time." 
            print(txt.format(first_name_dem, last_name_dem, state_dem, against_pct_dem))
            
        print('\n'+ "Republican:")
        for x in sorted_members[1]:
            first_name_repub = x["first_name"]
            last_name_repub = x["last_name"]
            state_repub = x["state"]
            against_pct_repub = str(x["votes_against_party_pct"])
            txt = "{} {} ({}) votes against the party {}% of the time." 
            print(txt.format(first_name_repub, last_name_repub, state_repub, against_pct_repub))

        data = {}
        return data

if __name__ == "__main__":
    main()
