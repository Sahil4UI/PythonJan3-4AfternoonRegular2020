Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list-mutable - create,remove,update,add
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    list-mutable - create,remove,update,add
NameError: name 'mutable' is not defined
>>> list1 = []
>>> list1 = [1,23,]
>>> list1
[1, 23]
>>> tup = ()#immutable
>>> tup = (1,2,3,4)
>>> tup[0]
1
>>> tup[1]
2
>>> tup[2]
3
>>> tup[-1]
4
>>> tup[::-1]
(4, 3, 2, 1)
>>> tup
(1, 2, 3, 4)
>>> help(tup)
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Built-in subclasses:
 |      asyncgen_hooks
 |      UnraisableHookArgs
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> #list comprehension
>>> x =[]
>>> for i in range(1,11):
	x.append(i)

>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x = [i for i in range(1,11)]
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> #tuple comprehension
>>> x = (i for i in range(1,11))
>>> type(x)
<class 'generator'>
>>> list(x)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x
<generator object <genexpr> at 0x0000027A841A1890>
>>> x = [1,2,3]
>>> x[0]=12
>>> x
[12, 2, 3]
>>> x = (1,2,3)
>>> x[0]=12
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    x[0]=12
TypeError: 'tuple' object does not support item assignment
>>> #dictionary
>>> #dictionary - key and value - pair
>>> k = {'id':101,"name":"Lokesh"}
>>> #k = {key1:value1 , key2:value2,key3:value3}
>>> k[0]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    k[0]
KeyError: 0
>>> k
{'id': 101, 'name': 'Lokesh'}
>>> k['id']
101
>>> k['name']
'Lokesh'
>>> k
{'id': 101, 'name': 'Lokesh'}
>>> k.keys()
dict_keys(['id', 'name'])
>>> k.values()
dict_values([101, 'Lokesh'])
>>> k.items()
dict_items([('id', 101), ('name', 'Lokesh')])
>>> k = {}
>>> k['rollNo'] = 45
>>> k
{'rollNo': 45}
>>> k['Name'] = 'Yash'
>>> k
{'rollNo': 45, 'Name': 'Yash'}
>>> k['address'] = 'njf'
>>> k
{'rollNo': 45, 'Name': 'Yash', 'address': 'njf'}
>>> k['rollNo']=1
>>> k
{'rollNo': 1, 'Name': 'Yash', 'address': 'njf'}
>>> k['Name']="Mohit"
>>> k
{'rollNo': 1, 'Name': 'Mohit', 'address': 'njf'}
>>> k['ph_no']=987654321
>>> k
{'rollNo': 1, 'Name': 'Mohit', 'address': 'njf', 'ph_no': 987654321}
>>> k['parents_name'] = 'Yogesh'
>>> k
{'rollNo': 1, 'Name': 'Mohit', 'address': 'njf', 'ph_no': 987654321, 'parents_name': 'Yogesh'}
>>> k.pop('ph_no')
987654321
>>> k
{'rollNo': 1, 'Name': 'Mohit', 'address': 'njf', 'parents_name': 'Yogesh'}
>>> k.popitem()
('parents_name', 'Yogesh')
>>> k
{'rollNo': 1, 'Name': 'Mohit', 'address': 'njf'}
>>> k.popitem()
('address', 'njf')
>>> k
{'rollNo': 1, 'Name': 'Mohit'}
>>> k.clear()
>>> k
{}
>>> path = "https://www.flipkart.com/asus-rog-phone-3-black-128-gb/p/itmf8623d755871d?pid=MOBFUXPBV3TFMPAH&lid=LSTMOBFUXPBV3TFMPAH63D3RA&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&fm=SEARCH&iid=58292af9-3659-4e69-915c-c39ac6c17840.MOBFUXPBV3TFMPAH.SEARCH&ppt=sp&ppn=sp&ssid=8zn1iuxbxs0000001611829908878&qH=1f568d0b548915af"
>>> import urllib.request as url
>>> import bs4
>>> res=url.urlopen(path)
>>> res
<http.client.HTTPResponse object at 0x0000027A848E1640>
>>> data = bs4.BeautifulSoup(res,'lxml')
>>> li = data.findAll('li',class_='_21lJbe')
>>> li
[<li class="_21lJbe">Handset, Adapter (30W), USB Type-C to Type C Cable, Ejector Pin (SIM Tray Needle), Aero Case, AJ Dongle, Documentation (User Guide, Warranty Card)</li>, <li class="_21lJbe">ZS661KS-6A039IN</li>, <li class="_21lJbe">ROG Phone 3</li>, <li class="_21lJbe">Black</li>, <li class="_21lJbe">Smartphones</li>, <li class="_21lJbe">Dual Sim</li>, <li class="_21lJbe">No</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Stereo Speaker, Quad Mic, Dirac Sound Enhancement</li>, <li class="_21lJbe">Head: 0.736 W/kg, Body: 1.497 W/kg</li>, <li class="_21lJbe">16.74 cm (6.59 inch)</li>, <li class="_21lJbe">2340 x 1080 Pixels</li>, <li class="_21lJbe">Full HD+</li>, <li class="_21lJbe">Qualcomm Adreno 650</li>, <li class="_21lJbe">Full HD+ AMOLED HDR Display</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Android 10</li>, <li class="_21lJbe">Qualcomm Snapdragon 865+ (SM8250)</li>, <li class="_21lJbe">Octa Core</li>, <li class="_21lJbe">3.1 GHz</li>, <li class="_21lJbe">2G GSM: 850/900/1800/1900, 3G HSDPA: 850/900/1700/1800/1900/2100, 4G FDD LTE: B1(2100), B2(1900), B3(1800), B4(1700/2100), B5(850), B7(2600), B8(900), B20(800), B28(700), 4G TDD-LTE: B34(2000), B38(2600), B39(1900), B40(2300), B41(2500), 5G: n41/77/78/79</li>, <li class="_21lJbe">128 GB</li>, <li class="_21lJbe">12 GB</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">64MP + 13MP + 5MP</li>, <li class="_21lJbe">64MP + 13MP + 5MP Rear Camera Setup, 64MP (Sony IMX686) Wide Camera, 13MP Ultrawide Camera, 5MP Macro Camera, Pro Video Mode, 8K, 4K HDR, HyperSteady Video (Uses Wide Angle Camera for Stabilization)</li>, <li class="_21lJbe">No</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">24MP Front Camera</li>, <li class="_21lJbe">24MP Front Camera, Aperture: F/2.0 (High Resolution Camera)</li>, <li class="_21lJbe">Rear LED Flash | Front Screen Flash</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Primary Camera</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">5G, 4G, 3G, 2G</li>, <li class="_21lJbe">5G, 4G LTE, WCDMA, GSM</li>, <li class="_21lJbe">5G, 4G, 3G, Wi-Fi</li>, <li class="_21lJbe">Google Chrome</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">v5.1</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">802.11a/b/g/n/ac/ax (Wi-Fi 6)</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">No</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">USB Type C</li>, <li class="_21lJbe">Google Maps</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Capacitive</li>, <li class="_21lJbe">Nano</li>, <li class="_21lJbe">No</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">Gyroscope, E-compass, Proximity Sensor, Ambient Light Sensor, Hall Sensor, In-display Fingerprint, Accelerator, Gyro (Support ARCore), Ultrasonic Sensor</li>, <li class="_21lJbe">USF 3.1 Storage, Supports aptX and aptX HD, Navigation: GPS (L1+L5), GLONASS (G1), BDS (B1), Galileo (E1+E5a), QZSS (L1+L5), 2x2 MIMO Support, Wi-Fi Direct</li>, <li class="_21lJbe">A-GPS, GLONSS, BEIDOU, GALILEO, QZSS</li>, <li class="_21lJbe">No</li>, <li class="_21lJbe">Yes</li>, <li class="_21lJbe">6000 mAh</li>, <li class="_21lJbe">78 mm</li>, <li class="_21lJbe">171 mm</li>, <li class="_21lJbe">9.85 mm</li>, <li class="_21lJbe">240 g</li>, <li class="_21lJbe">Brand Warranty of 1 Year Available for Mobile and 6 Months for Accessories</li>, <li class="_21lJbe">1 Year</li>]
>>> for i in li:
	print(i.text)

Handset, Adapter (30W), USB Type-C to Type C Cable, Ejector Pin (SIM Tray Needle), Aero Case, AJ Dongle, Documentation (User Guide, Warranty Card)
ZS661KS-6A039IN
ROG Phone 3
Black
Smartphones
Dual Sim
No
Yes
Yes
Yes
Stereo Speaker, Quad Mic, Dirac Sound Enhancement
Head: 0.736 W/kg, Body: 1.497 W/kg
16.74 cm (6.59 inch)
2340 x 1080 Pixels
Full HD+
Qualcomm Adreno 650
Full HD+ AMOLED HDR Display
Yes
Android 10
Qualcomm Snapdragon 865+ (SM8250)
Octa Core
3.1 GHz
2G GSM: 850/900/1800/1900, 3G HSDPA: 850/900/1700/1800/1900/2100, 4G FDD LTE: B1(2100), B2(1900), B3(1800), B4(1700/2100), B5(850), B7(2600), B8(900), B20(800), B28(700), 4G TDD-LTE: B34(2000), B38(2600), B39(1900), B40(2300), B41(2500), 5G: n41/77/78/79
128 GB
12 GB
Yes
Yes
64MP + 13MP + 5MP
64MP + 13MP + 5MP Rear Camera Setup, 64MP (Sony IMX686) Wide Camera, 13MP Ultrawide Camera, 5MP Macro Camera, Pro Video Mode, 8K, 4K HDR, HyperSteady Video (Uses Wide Angle Camera for Stabilization)
No
Yes
24MP Front Camera
24MP Front Camera, Aperture: F/2.0 (High Resolution Camera)
Rear LED Flash | Front Screen Flash
Yes
Yes
Yes
Yes
Primary Camera
Yes
Yes
Yes
5G, 4G, 3G, 2G
5G, 4G LTE, WCDMA, GSM
5G, 4G, 3G, Wi-Fi
Google Chrome
Yes
v5.1
Yes
802.11a/b/g/n/ac/ax (Wi-Fi 6)
Yes
Yes
Yes
No
Yes
USB Type C
Google Maps
Yes
Yes
Capacitive
Nano
No
Yes
Yes
Gyroscope, E-compass, Proximity Sensor, Ambient Light Sensor, Hall Sensor, In-display Fingerprint, Accelerator, Gyro (Support ARCore), Ultrasonic Sensor
USF 3.1 Storage, Supports aptX and aptX HD, Navigation: GPS (L1+L5), GLONASS (G1), BDS (B1), Galileo (E1+E5a), QZSS (L1+L5), 2x2 MIMO Support, Wi-Fi Direct
A-GPS, GLONSS, BEIDOU, GALILEO, QZSS
No
Yes
6000 mAh
78 mm
171 mm
9.85 mm
240 g
Brand Warranty of 1 Year Available for Mobile and 6 Months for Accessories
1 Year
>>> 
