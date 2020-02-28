# gender_age

Usage:
python gender_age.py data_src\aligned

The face image in the data_src\aligned folder,
Women who are between 16 and 29 years old,
Move to data_src\aligned\match folder.

Uses Face++ API.
Register on the Face++ website (free) and issue api_key and api_secret.
Create an .apikey file in the workspace folder.

.apikey file contents

         {
         "api_key": "**** (issued api_key)",
         "api_secret": "**** (issued api_secret)"
         }

Place gender_age.py in the workspace folder.

how to use
python gender_age.py data_src\aligned
