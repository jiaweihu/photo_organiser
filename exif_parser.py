import piexif
from datetime import datetime

class Exif_Parser:
    def __init__(self, photoName):
        self.exif_dict = piexif.load(photoName)
    
    def listAllData(self):
        thumbnail = self.exif_dict.pop('thumbnail') # This can not be iterated
        for ifd in self.exif_dict:
            print(f'{ifd}:')
            for tag in self.exif_dict[ifd]:
                if tag is not None:
                    tag_name = piexif.TAGS[ifd][tag]["name"]
                    tag_value = self.exif_dict[ifd][tag]
                    # Avoid print a large value, just to be pretty
                    if isinstance(tag_value, bytes):
                        tag_value = tag_value[:10]
                    print(f'\t{tag_name:25}: {tag_value}')

    def get_ExifKeyValue(self, exifData, key):
            if key in exifData:
                return exifData[key]
            return None

    def get_GpsData(self):
        ifdgps = "GPS"
        gpspart = self.exif_dict[ifdgps]

        gps_latitude = self.get_ExifKeyValue(gpspart, 2)  # 'GPS GPSLatitude')
        gps_latitude_ref = self.get_ExifKeyValue(gpspart, 1)
        gps_longitude = self.get_ExifKeyValue(gpspart, 4)
        gps_longitude_ref = self.get_ExifKeyValue(gpspart, 3)

        return gps_latitude, gps_latitude_ref, gps_longitude, gps_longitude_ref

    def getTimeStamp(self):
        ifdExif = "Exif"
        exifpart = self.exif_dict[ifdExif]
        date_time_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        timeByte = self.get_ExifKeyValue(exifpart, 36868)
        if timeByte:
            date_time_str = exifpart[36868].decode("utf-8")
        return date_time_str

def main():
    photo_name = 'data\image\london.jpeg'
    exif_parser = Exif_Parser(photo_name)
    # exif_parser.listAllData()
    print(exif_parser.get_GpsData())
    print(exif_parser.getTimeStamp())

if __name__ == "__main__":
    main()

