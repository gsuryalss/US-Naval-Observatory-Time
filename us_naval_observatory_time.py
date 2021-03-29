import urllib.request as ur
# import bs4
import re


# US Naval Observatory Master Clock Time
class UsNavalTime:
    def __init__(self):
        self.noaa_url = 'http://tycho.usno.navy.mil/cgi-bin/timer.pl'
        self.page_content = self.get_resp()

    # get the response from us navy military time page
    def get_resp(self):
        resp = ur.urlopen(self.noaa_url).read().decode('utf-8')
        return resp

    # Universal Time
    def universal_time(self):
        univ_pattern = re.compile(r"<BR>(.*?)\s+Univ", re.I)
        univ_time = univ_pattern.findall(self.page_content)
        return univ_time[0]

    # Eastern Time
    def eastern_time(self):
        east_pattern = re.compile(r"<BR>(.*?)\s+East", re.I)
        east_time = east_pattern.findall(self.page_content)
        return east_time[0]

    # Central Time
    def central_time(self):
        cent_pattern = re.compile(r"<BR>(.*?)\s+Cent", re.I)
        cent_time = cent_pattern.findall(self.page_content)
        return cent_time[0]

    # Mountain Time
    def mountain_time(self):
        moun_pattern = re.compile(r"<BR>(.*?)\s+Moun", re.I)
        moun_time = moun_pattern.findall(self.page_content)
        return moun_time[0]

    # Pacific Time
    def pacific_time(self):
        paci_pattern = re.compile(r"<BR>(.*?)\s+Paci", re.I)
        paci_time = paci_pattern.findall(self.page_content)
        return paci_time[0]

    # Alaska Time
    def alaska_time(self):
        alas_pattern = re.compile(r"<BR>(.*?)\s+Alas", re.I)
        alas_time = alas_pattern.findall(self.page_content)
        return alas_time[0]

    # Hawaii-Aleutian Time
    def hawaii_aleutian_time(self):
        hawa_pattern = re.compile(r"<BR>(.*?)\s+Hawa", re.I)
        hawa_time = hawa_pattern.findall(self.page_content)
        return hawa_time[0]

    def print_time(self):
        print("\n\t\tUS Naval Observatory Master Clock Time\t\t\n")
        print("\tUniversal Time:\t\t-", self.universal_time())
        print("\tEastern Time:\t\t-", self.eastern_time())
        print("\tCentral Time:\t\t-", self.central_time())
        print("\tMountain Time:\t\t-", self.mountain_time())
        print("\tPacific Time:\t\t-", self.pacific_time())
        print("\tAlaska Time:\t\t-", self.alaska_time())
        print("\tHawaii-Aleutian Time: -", self.hawaii_aleutian_time())


noaa_time = UsNavalTime()
noaa_time.print_time()

# US Naval Observatory Master Clock Time
# noaa_url = 'http://tycho.usno.navy.mil/cgi-bin/timer.pl'
# resp = ur.urlopen(noaa_url).read().decode('utf-8')
# # print(bs4.BeautifulSoup(resp, 'html.parser').prettify())
# print(resp)
#
# # Universal Time
# univ_pattern = re.compile(r"<BR>(.*?)\s+Univ", re.I)
# univ_time = univ_pattern.findall(resp)
# print("Universal Time:\t\t-", univ_time[0])
#
# # Eastern Time
# east_pattern = re.compile(r"<BR>(.*?)\s+East", re.I)
# east_time = east_pattern.findall(resp)
# print("Eastern Time:\t\t-", east_time[0])
#
# # Central Time
# cent_pattern = re.compile(r"<BR>(.*?)\s+Cent", re.I)
# cent_time = cent_pattern.findall(resp)
# print("Central Time:\t\t-", cent_time[0])
#
# # Mountain Time
# moun_pattern = re.compile(r"<BR>(.*?)\s+Moun", re.I)
# mount_time = moun_pattern.findall(resp)
# print("Mountain Time:\t\t-", mount_time[0])
#
# # Pacific Time
# paci_pattern = re.compile(r"<BR>(.*?)\s+Paci", re.I)
# paci_time = paci_pattern.findall(resp)
# print("Pacific Time:\t\t-", paci_time[0])
#
# # Alaska Time
# alas_pattern = re.compile(r"<BR>(.*?)\s+Alas", re.I)
# alas_time = alas_pattern.findall(resp)
# print("Alaska Time:\t\t-", alas_time[0])
#
# # Hawaii-Aleutian Time
# hawa_pattern = re.compile(r"<BR>(.*?)\s+Hawa", re.I)
# hawa_time = hawa_pattern.findall(resp)
# print("Hawaii-Aleutian Time: -", hawa_time[0])