from tripdata import Trip_details
from datetime import datetime
import json
l_of_dict=[
    Trip_details("Ponmudi","10-10-2025","Fresh Air"),
    Trip_details("Munnar","15-12-2025","Landcsape"),
    Trip_details("Athirappally","29-12-2025","Waterfalls")
]
formatted_trips = []
for trip in l_of_dict: 
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    
    formatted_date = date_obj.strftime("%B %d, %Y")
    formatted_trip = {
        "city": trip["city"],
        "date": formatted_date,
        "comment": trip["comment"]
    }
    formatted_trips.append(formatted_trip)

#  Convert to JSON string 
json_output = json.dumps(formatted_trips)
print(json_output)
