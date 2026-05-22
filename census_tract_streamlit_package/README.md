
# Census Tract GEOID Lookup Tool

This web tool accepts a CSV file with `lat` and `lon` columns and returns a
new CSV with the corresponding **2020 Census Tract GEOIDs**, using the U.S. Census Geocoder API.

## How to Use
1. Upload a CSV with columns:
   - lat
   - lon
2. Click **Process**
3. Download the resulting `<name>_with_tracts.csv`

## Streamlit Cloud Deployment
1. Create a GitHub repo with:
   - app.py
   - requirements.txt
   - README.md
2. Go to: https://streamlit.io/cloud
3. Click **Deploy App**
4. Choose your repo and `app.py`
5. Deploy

Your app will be available at a shareable URL like:
`https://yourname.streamlit.app`
