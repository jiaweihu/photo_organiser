from geopy.geocoders import Nominatim
from exif_parser import Exif_Parser

class Photo_Info:
    def __init__(self, photoName): 
        self.loc = Nominatim(user_agent="GetLoc")
        self.exifParser = Exif_Parser(photoName)

    def convert_to_degress(self, value):
        """
        Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
        :param value:
        :type value: exifread.utils.Ratio
        :rtype: float
        """
        d = float(value[0][0]) / float(value[0][1])
        m = float(value[1][0]) / float(value[1][1])
        s = float(value[2][0]) / float(value[2][1])

        return d + (m / 60.0) + (s / 3600.0)
    
    def get_exif_location(self):
        """
        Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)
        """
        lat = None
        lon = None

        gps_latitude, gps_latitude_ref, gps_longitude, gps_longitude_ref = self.exifParser.get_GpsData()

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = self.convert_to_degress(gps_latitude)
            if gps_latitude_ref.decode("utf-8") != 'N':
                lat = 0 - lat

            lon = self.convert_to_degress(gps_longitude)
            if gps_longitude_ref.decode("utf-8") != 'E':
                lon = 0 - lon

        return lat, lon

    def getPhotoAddress(self):
        gpslat, gpslon = self.get_exif_location()
        resultStr = "photo"
        if gpslat and gpslon:
            locname = self.loc.reverse(str(gpslat) + ", " + str(gpslon))
            address = locname.address
            x = address.split(",")
            resultStr = x[2].strip() + "-" + x[3].strip()
        return resultStr

    def getPhotoTime(self):
        date_time_str = self.exifParser.getTimeStamp()
        date_time_str= date_time_str.replace(" ", "-")
        date_time_str= date_time_str.replace(":", "-")
        return date_time_str


def main():
    photo_name = 'data\image\london.jpeg'
    photo_info = Photo_Info(photo_name)
    print(photo_info.getPhotoAddress())
    print(photo_info.getPhotoTime())

if __name__ == "__main__":
    main()
