Lectures
========

Download pdf &amp; mp4 from course page


Dependencies:
  BeatifulSoup
  Selenium
    
Assume profile already contains log-in info & aut0-download for pdf & mp4
In firefox, Tools -> Options -> Applications set to save file automatically
Args:
1. Class name
    When you enter class page, it will be after "coursera.org"
    E.g. For "https://class.coursera.org/datasci-001/class/index", class name is "datasci-001"
2. Profile location
    In Windows, click Start, type "%APPDATA%\Mozilla\Firefox\Profiles" and profile is in folder with "default" in name
    E.g. "C:\\Users\\rajd\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\r8gk2ms5.default"
    Notice, the double slashes
3. Download location
    Any folder, but again make sure to have double slashes and proper formatting
    E.g. "C:\\Users\\rajd\\Downloads\\Lectures"
