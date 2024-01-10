#===============================================
# SAE 105: traitement de données
# Test pour afficher des villes sur une carte
# OpenstreetMap
#
#================================================

STATIONS = ['ABBEVILLE', 'AJACCIO', 'ALENCON', 'BALE-MULHOUSE',
            'BELLE ILE-LE TALUT', 'BORDEAUX-MERIGNAC', 'BOURGES',
            'BREST-GUIPAVAS', 'CAEN-CARPIQUET', 'CAP CEPET',
            'CLERMONT-FD', 'DIJON-LONGVIC', 'EMBRUN', 'GOURDON',
            'LE PUY-LOUDES', 'LILLE-LESQUIN', 'LIMOGES-BELLEGARDE',
            'LYON-ST EXUPERY', 'MARIGNANE', 'MILLAU', 'MONT-DE-MARSAN',
            'MONTELIMAR', 'MONTPELLIER', 'NANCY-OCHEY',
            'NANTES-BOUGUENAIS', 'NICE', 'ORLY', 'PERPIGNAN',
            "PLOUMANAC'H", 'POITIERS-BIARD', 'PTE DE CHASSIRON',
            'PTE DE LA HAGUE', 'REIMS-PRUNAY', 'RENNES-ST JACQUES',
            'ROUEN-BOOS', 'ST GIRONS', 'STRASBOURG-ENTZHEIM',
            'TARBES-OSSUN', 'TOULOUSE-BLAGNAC', 'TOURS', 'TROYES-BARBEREY']

LATS = [50.136, 41.918, 48.4455, 47.614333, 47.294333,
        44.830667, 47.059167, 48.444167, 49.18, 43.079333,
        45.786833, 47.267833, 44.565667, 44.745, 45.0745,
        50.57, 45.861167, 45.7265, 43.437667, 44.1185,
        43.909833, 44.581167, 43.577, 48.581, 47.15,
        43.648833, 48.716833, 42.737167, 48.825833,
        46.593833, 46.046833, 49.725167, 49.209667,
        48.068833, 49.383, 43.005333, 48.5495, 43.188,
        43.621, 47.4445, 48.324667]

LONGS = [1.834, 8.792667, 0.110167, 7.51, -3.218333, -0.691333,
         2.359833, -4.412, -0.456167, 5.940833, 3.149333, 5.088333,
         6.502333, 1.396667, 3.764, 3.0975, 1.175, 5.077833, 5.216,
         3.0195, -0.500167, 4.733, 3.963167, 5.959833, -1.608833,
         7.209, 2.384333, 2.872833, -3.473167, 0.314333, -1.4115,
         -1.939833, 4.155333, -1.734, 1.181667, 1.106833, 7.640333,
         0.0, 1.378833, 0.727333, 4.02]

TEMPS = [7.6, 13.5, 7.6, 6.8, 10.5, 11.5, 8.5, 9.7, 8.6, 11.8, 9.1,
         7.2, 5.7, 9.2, 6.0, 7.2, 7.6, 8.4, 12.0, 6.1, 11.6, 9.6, 11.7,
         6.5, 10.0, 11.7, 8.1, 12.6, 9.9, 9.1, 10.8, 9.5, 7.4, 9.0,
         7.1, 10.3, 6.7, 10.8, 10.6, 8.4, 8.1]

import folium, branca
coords = (46.539758, 2.430331)
map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=6)
for i in range(len(STATIONS)):
    folium.CircleMarker(
        location = (LATS[i], LONGS[i]),
        radius = TEMPS[i]*2,
        color = 'crimson',
        fill = True,
        fill_color = 'crimson'
    ).add_to(map)

map.save(outfile='map.html')

# Pour customizer les cercles avec des couleurs, .....
map1 = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=6)
cm = branca.colormap.LinearColormap(['blue', 'red'], vmin=min(TEMPS), vmax=max(TEMPS))
map1.add_child(cm) # add this colormap on the display

for lat, lng, size, color in zip(LATS, LONGS, TEMPS, TEMPS):
    folium.CircleMarker(
        location=[lat, lng],
        radius=size,
        color=cm(color),
        fill=True,
        fill_color=cm(color),
        fill_opacity=0.6
    ).add_to(map1)

map1.save(outfile='map1.html')
print("Traitement terminé")