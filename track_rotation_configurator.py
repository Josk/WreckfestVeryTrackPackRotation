import csv
from typing import TextIO
from xml.dom import minidom


def main():

    track_rotation_output = "track_rotation.txt"
    user_tracks = "user_track_rotation.csv"

    populate_user_defined_tracks(user_tracks, track_rotation_output)


def populate_user_defined_tracks(user_tracks, track_rotation_output):
    output_file: TextIO = open(track_rotation_output, 'w')
    output_file.write("")

    with open(user_tracks) as tracks_csv_file:
        tracks_csv_reader = csv.reader(tracks_csv_file, delimiter=',')
        line_count = 0
        root = minidom.Document()
        xml = root.createElement('Tracks')
        root.appendChild(xml)

        for event in tracks_csv_reader:
            if line_count > 0:
                location = event[0].strip(" \n").lower()
                track_name = event[1].strip(" \n").lower()
                track_file_name = event[2].lower()
                race_type = event[3].strip(" \n").lower()
                laps = event[4].strip(" \n")
                minutes = event[5].strip(" \n")
                num_teams = event[6].strip(" \n")
                elimination_interval = event[7].strip(" \n")

                if race_type == "racing":
                    race_type = "racing"
                elif race_type == "derby":
                    race_type = "derby"
                else:
                    line_count = line_count + 1
                    print("ERROR: race_type " + race_type + "  LineNum: " + str(line_count))
                    continue

                race_num = str(line_count-1)
                output_file.write("# Race " + race_num + "\n")
                output_file.write("# Location: " + location + "\n")
                output_file.write("# Track Name: " + track_name + "\n")
                output_file.write("el_add=" + track_file_name + "\n")
                output_file.write("el_gamemode=" + race_type + "\n")
                output_file.write("el_num_teams=" + num_teams + "\n")
                output_file.write("el_laps=" + laps + "\n")
                output_file.write("el_elimination_interval=0" + "\n")
                output_file.write("el_car_reset_disabled=0" + "\n")
                output_file.write("el_wrong_way_limiter_disabled=1" + "\n")
                output_file.write("#el_car_class_restriction=a" + "\n")
                output_file.write("el_car_restriction=" + "\n")
                output_file.write("el_weather=random" + "\n")
                output_file.write("\n")

                trackXML = root.createElement("Track")
                trackXML.setAttribute('Direction','Clockwise')

                trackIsModXML = root.createElement("IsMod")
                trackIsModValue = root.createTextNode("true")
                trackIsModXML.appendChild(trackIsModValue)
                trackXML.appendChild(trackIsModXML)

                trackFileNameXML = root.createElement("Name")
                trackFileNameValue = root.createTextNode(track_file_name)
                trackFileNameXML.appendChild(trackFileNameValue)
                trackXML.appendChild(trackFileNameXML)

                trackNameXML = root.createElement("DisplayName")
                trackNameValue = root.createTextNode(track_name)
                trackNameXML.appendChild(trackNameValue)
                trackXML.appendChild(trackNameXML)

                imageXML = root.createElement("ImageFileName")
                trackXML.appendChild(imageXML)
                layoutXML = root.createElement("LayoutFileName")
                trackXML.appendChild(layoutXML)
                weathersXML = root.createElement("Weathers")
                trackXML.appendChild(weathersXML)

                lengthXML = root.createElement("Length")
                lengthValue = root.createTextNode("0")
                lengthXML.appendChild(lengthValue)
                trackXML.appendChild(lengthXML)

                areaXML = root.createElement("Area")
                areaValue = root.createTextNode("0")
                areaXML.appendChild(areaValue)
                trackXML.appendChild(areaXML)

                gametypeXML = root.createElement("GameType")
                gametypenameXML = root.createElement("Name")
                gametypenameValue = root.createTextNode(race_type)
                gametypenameXML.appendChild(gametypenameValue)
                gametypeXML.appendChild(gametypenameXML)
                trackXML.appendChild(gametypeXML)


                xml.appendChild(trackXML)

            line_count = line_count + 1
    output_file.close()
    with open('ModTracks.xml','w') as f:
        f.write(root.toprettyxml())

    print(root.toprettyxml())
    return


main()