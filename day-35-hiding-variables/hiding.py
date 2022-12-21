import os

api_key = "13453iubi72843i21u43"

"""Exporting information so its hidden:
Open terminal in the wd
type: "export API_KEY=13453iubi72843i21u43"
type: "env" so you know it works
import os
use method below to get hold of the info
"""

my_hidden_api = os.environ.get("API_KEY")
