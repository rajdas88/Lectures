Lectures
========

Allows for automatic download of *pdf* and *mp4* from course page

Setup
=====
This code runs using Python 2.7 along with:
<ul>
<li>BeautifulSoup</li>
<li>Selenium</li>
</ul>

**Finnicky assumptions:** <br />
Assume profile already contains log-in information and auto-download for *pdf* and *mp4*.<br />
For more information, check http://support.mozilla.org/en-US/kb/change-firefox-behavior-when-open-file.<br />

To Run
======
There are 3 arguments:
<ol>
<li><b>Class name</b><br />
    When you enter the class page, it will be after "coursera.org".<br />
    <i>E.g. For "https://class.coursera.org/datasci-001/class/index", class name is "datasci-001"</i></li>
<li><b>Profile location</b><br />
    In Windows, click Start, type "%APPDATA%\Mozilla\Firefox\Profiles" and profile is in folder with "default" in name<br />
    <i>E.g. "C:\\Users\\rajd\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\r8gk2ms5.default"</i><br />
    <i>Notice, the double slashes for the escape sequence<i><br /></li>
<li><b>Download location</b><br />
    Any folder, but again make sure to have double slashes and proper formatting<br />
    <i>E.g. "C:\\Users\\rajd\\Downloads\\Lectures"<br /></i></li>
</ol>

<code>
python CourseraScraper.py datasci-001 C:\\Users\\rajd\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\r8gk2ms5.default C:\\Users\\rajd\\Downloads\\Lectures
</code>
