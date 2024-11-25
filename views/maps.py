import streamlit as st
import folium
from folium import plugins

# Set page title and layout
st.set_page_config(page_title="Apartments in Georgia", layout="wide")

# Title of the Streamlit app
st.title("Nearby Apartments in Georgia, USA")

# Description of the app
st.write("""
    Below is a map centered on Georgia, USA, with markers representing nearby apartment listings.
    Each marker provides a link to more details about the apartment, including pictures, rent, and contact information.
""")

# Create a folium map centered around Georgia, USA
georgia_coordinates = [33.6407, -83.4427]  # Coordinates for the center of Georgia

# Create a Folium map object
m = folium.Map(location=georgia_coordinates, zoom_start=7)  # Adjust zoom level as necessary

# Apartment data
apartments = [
    {
        "name": "District at Parkview",
        "coordinates": [33.8184, -84.1381],  # Location: Stone Mountain, GA
        "image": "https://photos.zillowstatic.com/fp/1a2b3c4d5e6f7g8h9i0j.jpg",
        "url": "https://www.zillow.com/b/district-at-parkview-stone-mountain-ga-5Xj8b2/",
        "description": "1-3 bedroom apartments with modern amenities in Stone Mountain."
    },
    {
        "name": "Georgia Green",
        "coordinates": [33.9519, -83.3576],  # Location: Athens, GA
        "image": "https://photos.zillowstatic.com/fp/2b3c4d5e6f7g8h9i0j1k.jpg",
        "url": "https://www.zillow.com/b/georgia-green-athens-ga-5Xj8b3/",
        "description": "2-bedroom units near the University of Georgia."
    },
    {
        "name": "The Ellis Apartments",
        "coordinates": [33.8101, -84.2386],  # Location: Clarkston, GA
        "image": "https://photos.zillowstatic.com/fp/3c4d5e6f7g8h9i0j1k2l.jpg",
        "url": "https://www.apartments.com/the-ellis-apartments-clarkston-ga/",
        "description": "1-4 bedroom apartments with fitness center and pool."
    },
    {
        "name": "Prose LaGrange",
        "coordinates": [33.0362, -85.0319],  # Location: LaGrange, GA
        "image": "https://photos.zillowstatic.com/fp/4d5e6f7g8h9i0j1k2l3m.jpg",
        "url": "https://www.apartments.com/prose-lagrange-lagrange-ga/",
        "description": "1-2 bedroom units with modern finishes and amenities."
    },
]

# Add markers for each apartment
for apartment in apartments:
    folium.Marker(
        location=apartment["coordinates"],
        popup=folium.Popup(f'<strong>{apartment["name"]}</strong><br>{apartment["description"]}<br><a href="{apartment["url"]}" target="_blank">View Details</a>', max_width=300),
        icon=folium.Icon(color="blue", icon="home")
    ).add_to(m)

# Save the map as an HTML file
map_path = "georgia_apartments_map.html"
m.save(map_path)

# Display the map in Streamlit
st.write("### Map of Apartments in Georgia")
st.components.v1.html(open(map_path, 'r').read(), height=600)

# Display apartment listings as a side panel
st.write("### Nearby Apartments:")
for apartment in apartments:
    st.write(f"**{apartment['name']}**")
    st.write(f"Location: {apartment['coordinates'][0]}, {apartment['coordinates'][1]}")
    st.write(f"Description: {apartment['description']}")
    st.write(f"[View More Details]({apartment['url']})")
    st.image(apartment["image"], caption=apartment['name'], use_column_width=True)
    st.markdown("---")
