data = [
  {
    "title": "BBMP Tender 50361016: 50361016tender for development and improvement to roads and...",
    "description": "50361016tender for development and improvement to roads and drains in surrounding area of kalakesari udaykumar park in nagapura ward no. 49 | Due Date: Aug 8, 2025 | Tender ID: 50361016",
    "date": "2025-07-27",
    "location": "Bangalore",
    "url": "https://www.tenderdetail.com/government-tenders/bruhat-bangalore-mahanagara-palike-tenders/1?agid=265",
    "source": "BBMP Tenders",
    "scraped_at": "2025-07-27T03:43:44.053837+00:00"
  },
  {
    "title": "BBMP Tender 50361013: 50361013tender for improvements roads and drains in vinayaknagara...",
    "description": "50361013tender for improvements roads and drains in vinayaknagara, marutinagara, sannakibayalu and surrounding areas  vrushabhavathinagar in ward no.53 | Due Date: Aug 8, 2025 | Tender ID: 50361013",
    "date": "2025-07-27",
    "location": "Bangalore",
    "url": "https://www.tenderdetail.com/government-tenders/bruhat-bangalore-mahanagara-palike-tenders/1?agid=265",
    "source": "BBMP Tenders",
    "scraped_at": "2025-07-27T03:43:44.053837+00:00"
  },
  {
    "title": "BBMP Tender 50360466: 50360466tender for hire charges for supply...",
    "description": "50360466tender for hire charges for supply, fixing, wiring, servicing & various maintenance works in south division:- 4 feet 36-40 watt watts led type tube light fitting with accessories. 1) upto 3 days, 2) upto 7 days  3) upto 15 days 4) upto one month  150 watt | Due Date: Aug 1, 2025 | Tender ID: 50360466",
    "date": "2025-07-27",
    "location": "Bangalore",
    "url": "https://www.tenderdetail.com/government-tenders/bruhat-bangalore-mahanagara-palike-tenders/1?agid=265",
    "source": "BBMP Tenders",
    "scraped_at": "2025-07-27T03:43:44.053837+00:00"
  },
  {
    "title": "BBMP Tender 50359271: 50359271tender for quotation for data rates of electrical...",
    "description": "50359271tender for   quotation for data rates of electrical items for bbmp (quotation tender for data rate) | Due Date: Aug 1, 2025 | Tender ID: 50359271",
    "date": "2025-07-27",
    "location": "Bangalore",
    "url": "https://www.tenderdetail.com/government-tenders/bruhat-bangalore-mahanagara-palike-tenders/1?agid=265",
    "source": "BBMP Tenders",
    "scraped_at": "2025-07-27T03:43:44.053837+00:00"
  },
  {
    "title": "BBMP Tender 50358887: 50358887tender for improvements to roads...",
    "description": "50358887tender for improvements to roads, drains and footpath at vittalmallya cross roads and surrounding area in ward no.167 ashokanagara (old no 111) for the year 2025-26 | Due Date: Aug 4, 2025 | Tender ID: 50358887",
    "date": "2025-07-27",
    "location": "Bangalore",
    "url": "https://www.tenderdetail.com/government-tenders/bruhat-bangalore-mahanagara-palike-tenders/1?agid=265",
    "source": "BBMP Tenders",
    "scraped_at": "2025-07-27T03:43:44.053837+00:00"
  },
]

import json 
from schema import get_schema
import base64
from vector import VectorDBManager
from batch_writer import batch_write_to_firestore
from dotenv import load_dotenv

load_dotenv()
try: 
    index = VectorDBManager()
except Exception as e:
    pass

if data:
    # Decode the base64 encoded data
    decoded_data = data #-> list of jsons
    batch = []
    for news in decoded_data:
        raw = str(news)
        schema = get_schema(raw)

        if schema == False: 
            continue
            
        if (schema["validity"]["final_weighted_score"] >.75): 
            try: 
                if index._load_existing_entries() or index._find_closest_matching_in_memory(): 
                    pass
                else :
                    index._add_to_vector_index(schema['hash']['embedding'])
            except: 
                pass 
        
        #cords = geocode_location(schema['location']['name'])
        cords = [12.9716, 77.5946]
        if "hash" in schema:
            del schema["hash"]
        if "validity" in schema:
            del schema["validity"]
        if "entities" in schema:
            del schema['entities']
        if "nid" in schema:
            del schema['nid']
        if "media" in schema:
            del schema['media']
        schema['location']['latitude'] = cords[0]
        schema['location']['longitude'] = cords[1]
    
        batch.append(schema)
        if len(batch) >= 5:
            batch_write_to_firestore(batch, "events")
            batch = []
    
    if batch:
        batch_write_to_firestore(batch, "events")
        

else:
    decoded_data = {}