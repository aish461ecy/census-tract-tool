
import streamlit as st
import pandas as pd
import requests
import io

st.set_page_config(page_title="Census Tract GEOID Lookup Tool", layout="centered")

st.title("Census Tract GEOID Lookup Tool")
st.write("Upload a CSV with columns named **lat** and **lon**. This tool returns a new CSV with **2020 Census Tract GEOIDs** added using the U.S. Census Geocoder API.")

def get_tract(lat, lon):
    url = "https://geocoding.geo.census.gov/geocoder/geographies/coordinates"
    params = {
        "x": lon,
        "y": lat,
        "benchmark": "Public_AR_Census2020",
        "vintage": "Census2020_Census2020",
        "format": "json"
    }
    try:
        r = requests.get(url, params=params, timeout=5)
        data = r.json()
        tracts = data["result"]["geographies"]["Census Tracts"]
        if len(tracts) > 0:
            return tracts[0]["GEOID"]
    except:
        return None
    return None

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if not {"lat", "lon"}.issubset(df.columns):
        st.error("CSV must contain 'lat' and 'lon' columns.")
    else:
        if st.button("Process"):
            st.info("Processing... Please wait.")

            df["tract_geoid"] = df.apply(
                lambda row: get_tract(row["lat"], row["lon"]), axis=1
            )

            output = io.BytesIO()
            df.to_csv(output, index=False)
            output.seek(0)

            out_name = uploaded_file.name.replace(".csv", "_with_tracts.csv")

            st.download_button(
                label="Download CSV with Tract GEOIDs",
                data=output,
                file_name=out_name,
                mime="text/csv"
            )

            st.success("Done! Click the button above to download your results.")
