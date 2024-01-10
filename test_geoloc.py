import folium


coords = (45.91,6.15)
mapIUT = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=15)
coords = [45.91954,6.154727]
folium.Marker(location=coords, popup = "IUT Annecy").add_to(mapIUT)
mapIUT.save(outfile='mapIUT.html')
print("Traitement terminé")