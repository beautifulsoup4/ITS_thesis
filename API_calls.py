import json
from urllib.parse import urlparse, urlencode
import xml.etree.ElementTree as ET
import datetime

import httplib2 as http

if __name__ == "__main__":
    # Authentication parameters
    headers = {'AccountKey': '***',
               'accept': 'application/json'}  # this is by default

    # API parameters
    #http://datamall2.mytransport.sg/ltaodataservice/TrafficSpeedBands
    uri = 'http://datamall2.mytransport.sg/'  # Resource URL
    path = '/ltaodataservice/TrafficSpeedBands'

    # Build query string & specify type of API call
    target = urlparse(uri + path)
    print(target.geturl())
    method = 'GET'
    body = ''

    # Get handle to http
    h  = http.Http()

    # Obtain results
    response, content = h.request(
        target.geturl(),
        method,
        body,
        headers)


   #    Parse JSON to print
    jsonObj = json.loads(content.decode('utf-8'))
   # print(json.dumps(jsonObj, sort_keys=True, indent=4))
    # Save result to file
    with open("traffic_speedbands.json", "w") as outfile:
        # Saving jsonObj["d"]
        json.dump(jsonObj, outfile, indent=2)
                  #sort_keys=True, indent=2,
              #ensure_ascii=False)
