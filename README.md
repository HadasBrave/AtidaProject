# AtidaProject
Corona management system for HMO
## Installation
Use the package manager [pip] to install.
pip install Flask
pip install pymongo
pip install bson
## Usage
```python
from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
# Add personal information into tha database
add_personal_info()
# Get the all personal information database
get_personal_info()
# Get the  peronal information by ID
get_personal_info_by_id(id)
# Add corona information into tha database
add_corona()
# Get the all corona information database
get_corona()
# Get the  corona information by ID
get_corona_by_id(id)
