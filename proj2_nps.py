#################################
##### Name: Andre Ray 
##### Uniqname: dreray
#################################

from bs4 import BeautifulSoup
import requests
import json
import secrets # file that contains your API key

BASE_URL ='https://www.nps.gov/'
response = requests.get(BASE_URL)
soup = BeautifulSoup(response.text, 'html.parser')

#print(soup)

states = soup.find('ul', class_= 'dropdown-menu SearchBar-keywordSearch').find_all('li')



parks_url = BASE_URL+'/yell'
response2 = requests.get(parks_url)
soup2 = BeautifulSoup(response2.text, 'html.parser')


parks = soup2.find('div', class_ = "Hero-titleContainer clearfix").find('a')
park_name = parks.text.strip()
print(park_name)


category = soup2.find('div', class_ = "Hero-designationContainer").find('span')
park_category = category.text.strip()

print(park_category)












'''

<div class="col-sm-12">
<div class="Hero-titleContainer clearfix">
<a href="/yell/" class="Hero-title " id="anch_10">Yellowstone</a>
<div class="Hero-designationContainer">
<span class="Hero-designation">National Park</span>
<span class="Hero-location">ID, MT, WY</span>
</div>
</div>
</div>

<div class="Hero-titleContainer clearfix">
<a href="/isro/" class="Hero-title " id="anch_10">Isle Royale</a>
<div class="Hero-designationContainer">
<span class="Hero-designation">National Park</span>
<span class="Hero-location">Michigan</span>
</div>
</div>

'''




'''
<ul class="dropdown-menu SearchBar-keywordSearch" role="menu" style="max-height: 300px; overflow-y: auto; overflow-x: hidden;">
<li><a href="/state/al/index.htm" id="anch_10">Alabama</a></li><li><a href="/state/ak/index.htm" id="anch_11">Alaska</a></li><li><a href="/state/as/index.htm" id="anch_12">American Samoa</a></li><li><a href="/state/az/index.htm" id="anch_13">Arizona</a></li><li><a href="/state/ar/index.htm" id="anch_14">Arkansas</a></li><li><a href="/state/ca/index.htm" id="anch_15">California</a></li><li><a href="/state/co/index.htm" id="anch_16">Colorado</a></li><li><a href="/state/ct/index.htm" id="anch_17">Connecticut</a></li><li><a href="/state/de/index.htm" id="anch_18">Delaware</a></li><li><a href="/state/dc/index.htm" id="anch_19">District of Columbia</a></li><li><a href="/state/fl/index.htm" id="anch_20">Florida</a></li><li><a href="/state/ga/index.htm" id="anch_21">Georgia</a></li><li><a href="/state/gu/index.htm" id="anch_22">Guam</a></li><li><a href="/state/hi/index.htm" id="anch_23">Hawaii</a></li><li><a href="/state/id/index.htm" id="anch_24">Idaho</a></li><li><a href="/state/il/index.htm" id="anch_25">Illinois</a></li><li><a href="/state/in/index.htm" id="anch_26">Indiana</a></li><li><a href="/state/ia/index.htm" id="anch_27">Iowa</a></li><li><a href="/state/ks/index.htm" id="anch_28">Kansas</a></li><li><a href="/state/ky/index.htm" id="anch_29">Kentucky</a></li><li><a href="/state/la/index.htm" id="anch_30">Louisiana</a></li><li><a href="/state/me/index.htm" id="anch_31">Maine</a></li><li><a href="/state/md/index.htm" id="anch_32">Maryland</a></li><li><a href="/state/ma/index.htm" id="anch_33">Massachusetts</a></li><li><a href="/state/mi/index.htm" id="anch_34">Michigan</a></li><li><a href="/state/mn/index.htm" id="anch_35">Minnesota</a></li><li><a href="/state/ms/index.htm" id="anch_36">Mississippi</a></li><li><a href="/state/mo/index.htm" id="anch_37">Missouri</a></li><li><a href="/state/mt/index.htm" id="anch_38">Montana</a></li><li><a href="/state/ne/index.htm" id="anch_39">Nebraska</a></li><li><a href="/state/nv/index.htm" id="anch_40">Nevada</a></li><li><a href="/state/nh/index.htm" id="anch_41">New Hampshire</a></li><li><a href="/state/nj/index.htm" id="anch_42">New Jersey</a></li><li><a href="/state/nm/index.htm" id="anch_43">New Mexico</a></li><li><a href="/state/ny/index.htm" id="anch_44">New York</a></li><li><a href="/state/nc/index.htm" id="anch_45">North Carolina</a></li><li><a href="/state/nd/index.htm" id="anch_46">North Dakota</a></li><li><a href="/state/mp/index.htm" id="anch_47">Northern Mariana Islands</a></li><li><a href="/state/oh/index.htm" id="anch_48">Ohio</a></li><li><a href="/state/ok/index.htm" id="anch_49">Oklahoma</a></li><li><a href="/state/or/index.htm" id="anch_50">Oregon</a></li><li><a href="/state/pa/index.htm" id="anch_51">Pennsylvania</a></li><li><a href="/state/pr/index.htm" id="anch_52">Puerto Rico</a></li><li><a href="/state/ri/index.htm" id="anch_53">Rhode Island</a></li><li><a href="/state/sc/index.htm" id="anch_54">South Carolina</a></li><li><a href="/state/sd/index.htm" id="anch_55">South Dakota</a></li><li><a href="/state/tn/index.htm" id="anch_56">Tennessee</a></li><li><a href="/state/tx/index.htm" id="anch_57">Texas</a></li><li><a href="/state/ut/index.htm" id="anch_58">Utah</a></li><li><a href="/state/vt/index.htm" id="anch_59">Vermont</a></li><li><a href="/state/vi/index.htm" id="anch_60">Virgin Islands</a></li><li><a href="/state/va/index.htm" id="anch_61">Virginia</a></li><li><a href="/state/wa/index.htm" id="anch_62">Washington</a></li><li><a href="/state/wv/index.htm" id="anch_63">West Virginia</a></li><li><a href="/state/wi/index.htm" id="anch_64">Wisconsin</a></li><li><a href="/state/wy/index.htm" id="anch_65">Wyoming</a></li>
</ul>

'''

'''
<div class="SearchBar-keywordSearch input-group input-group-lg open" role="group">
<button type="button" class="SearchBar-keywordSearch input-group input-group-lg btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
By State... <span class="caret"></span>
</button>
<!--populate state links here in this list-->
<ul class="dropdown-menu SearchBar-keywordSearch" role="menu" style="max-height: 300px; overflow-y: auto; overflow-x: hidden;">
<li><a href="/state/al/index.htm" id="anch_10">Alabama</a></li><li><a href="/state/ak/index.htm" id="anch_11">Alaska</a></li><li><a href="/state/as/index.htm" id="anch_12">American Samoa</a></li><li><a href="/state/az/index.htm" id="anch_13">Arizona</a></li><li><a href="/state/ar/index.htm" id="anch_14">Arkansas</a></li><li><a href="/state/ca/index.htm" id="anch_15">California</a></li><li><a href="/state/co/index.htm" id="anch_16">Colorado</a></li><li><a href="/state/ct/index.htm" id="anch_17">Connecticut</a></li><li><a href="/state/de/index.htm" id="anch_18">Delaware</a></li><li><a href="/state/dc/index.htm" id="anch_19">District of Columbia</a></li><li><a href="/state/fl/index.htm" id="anch_20">Florida</a></li><li><a href="/state/ga/index.htm" id="anch_21">Georgia</a></li><li><a href="/state/gu/index.htm" id="anch_22">Guam</a></li><li><a href="/state/hi/index.htm" id="anch_23">Hawaii</a></li><li><a href="/state/id/index.htm" id="anch_24">Idaho</a></li><li><a href="/state/il/index.htm" id="anch_25">Illinois</a></li><li><a href="/state/in/index.htm" id="anch_26">Indiana</a></li><li><a href="/state/ia/index.htm" id="anch_27">Iowa</a></li><li><a href="/state/ks/index.htm" id="anch_28">Kansas</a></li><li><a href="/state/ky/index.htm" id="anch_29">Kentucky</a></li><li><a href="/state/la/index.htm" id="anch_30">Louisiana</a></li><li><a href="/state/me/index.htm" id="anch_31">Maine</a></li><li><a href="/state/md/index.htm" id="anch_32">Maryland</a></li><li><a href="/state/ma/index.htm" id="anch_33">Massachusetts</a></li><li><a href="/state/mi/index.htm" id="anch_34">Michigan</a></li><li><a href="/state/mn/index.htm" id="anch_35">Minnesota</a></li><li><a href="/state/ms/index.htm" id="anch_36">Mississippi</a></li><li><a href="/state/mo/index.htm" id="anch_37">Missouri</a></li><li><a href="/state/mt/index.htm" id="anch_38">Montana</a></li><li><a href="/state/ne/index.htm" id="anch_39">Nebraska</a></li><li><a href="/state/nv/index.htm" id="anch_40">Nevada</a></li><li><a href="/state/nh/index.htm" id="anch_41">New Hampshire</a></li><li><a href="/state/nj/index.htm" id="anch_42">New Jersey</a></li><li><a href="/state/nm/index.htm" id="anch_43">New Mexico</a></li><li><a href="/state/ny/index.htm" id="anch_44">New York</a></li><li><a href="/state/nc/index.htm" id="anch_45">North Carolina</a></li><li><a href="/state/nd/index.htm" id="anch_46">North Dakota</a></li><li><a href="/state/mp/index.htm" id="anch_47">Northern Mariana Islands</a></li><li><a href="/state/oh/index.htm" id="anch_48">Ohio</a></li><li><a href="/state/ok/index.htm" id="anch_49">Oklahoma</a></li><li><a href="/state/or/index.htm" id="anch_50">Oregon</a></li><li><a href="/state/pa/index.htm" id="anch_51">Pennsylvania</a></li><li><a href="/state/pr/index.htm" id="anch_52">Puerto Rico</a></li><li><a href="/state/ri/index.htm" id="anch_53">Rhode Island</a></li><li><a href="/state/sc/index.htm" id="anch_54">South Carolina</a></li><li><a href="/state/sd/index.htm" id="anch_55">South Dakota</a></li><li><a href="/state/tn/index.htm" id="anch_56">Tennessee</a></li><li><a href="/state/tx/index.htm" id="anch_57">Texas</a></li><li><a href="/state/ut/index.htm" id="anch_58">Utah</a></li><li><a href="/state/vt/index.htm" id="anch_59">Vermont</a></li><li><a href="/state/vi/index.htm" id="anch_60">Virgin Islands</a></li><li><a href="/state/va/index.htm" id="anch_61">Virginia</a></li><li><a href="/state/wa/index.htm" id="anch_62">Washington</a></li><li><a href="/state/wv/index.htm" id="anch_63">West Virginia</a></li><li><a href="/state/wi/index.htm" id="anch_64">Wisconsin</a></li><li><a href="/state/wy/index.htm" id="anch_65">Wyoming</a></li>
</ul>
</div>
'''

class NationalSite:
    '''a national site

    Instance Attributes
    -------------------
    category: string
        the category of a national site (e.g. 'National Park', '')
        some sites have blank category.
    
    name: string
        the name of a national site (e.g. 'Isle Royale')

    address: string
        the city and state of a national site (e.g. 'Houghton, MI')

    zipcode: string
        the zip-code of a national site (e.g. '49931', '82190-0168')

    phone: string
        the phone of a national site (e.g. '(616) 319-7906', '307-344-7381')
    '''
    def __init__(self, category="", name="", address = "", zipcode="", phone=""):

        self.category = category
        self.name = name
        self.address = address
        self.zipcode = zipcode
        self.phone = phone

    def info(self):
        return f"{self.name}({self.category}):{address}{self.zip}"



def build_state_url_dict():
    ''' Make a dictionary that maps state name to state page url from "https://www.nps.gov"

    Parameters
    ----------
    None

    Returns
    -------
    dict
        key is a state name and value is the url
        e.g. {'michigan':'https://www.nps.gov/state/mi/index.htm', ...}
    '''
    state_dict = {}

    for state in states:
        state_name = state.text.lower().strip()
        state_url = state.find('a')['href']
        state_link = BASE_URL + state_url
        state_dict[state_name] = state_link

    #print(state_dict)
    return state_dict




def get_site_instance(site_url):
    '''Make an instances from a national site URL.
    
    Parameters
    ----------
    site_url: string
        The URL for a national site page in nps.gov
    
    Returns
    -------
    instance
        a national site instance
    '''
    parks_url = BASE_URL+'/isro'
    response2 = requests.get(parks_url)
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    parks = soup2.find('div', class_ = "Hero-titleContainer clearfix").find('a')
    park_name = parks.text.strip()
    print(park_name)


def get_sites_for_state(state_url):
    '''Make a list of national site instances from a state URL.
    
    Parameters
    ----------
    state_url: string
        The URL for a state page in nps.gov
    
    Returns
    -------
    list
        a list of national site instances
    '''
    pass


def get_nearby_places(site_object):
    '''Obtain API data from MapQuest API.
    
    Parameters
    ----------
    site_object: object
        an instance of a national site
    
    Returns
    -------
    dict
        a converted API return from MapQuest API
    '''
    pass
    

if __name__ == "__main__":
    pass