import json
import requests
from collections import defaultdict

def fuction(integerer):
    r = requests.get("https://mach-eight.uc.r.appspot.com/")
    data_json = json.loads(r.text)
    players = data_json["values"]

    aux = defaultdict(list)
    for player in players:
        aux[int(player['h_in'])].append(player['first_name'] + " " + player['last_name'])

    return [player + " & " + aux2
        for height in aux
            if integerer - height in aux
                for aux2 in aux[integerer - height]
                    for player in aux[height]
                        if player < aux2
    ]

def main():
    integerer = int(input("Ingrese el número: "))
    result = fuction(integerer)
    
    return result
    
if __name__=="__main__":
    
    result = main()
    stop_here = len(result)
    
    while stop_here == 0:
    
        print("No matches found, please try with a new number")
        result = main()
        stop_here = len(result)

    print(result)