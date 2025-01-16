#importing os, it lets the user interact with the native OS Python is currently running on.

import os
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

#the following code tells us if the key is up and running. 
if google_api_key:
    print("successful")
else:
    print("OMG")