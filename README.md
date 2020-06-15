# CS 105 Final Project Phase 3 

## Project Synopsis: 
An analysis of the global wildfire trends with a focus on Australia, Brazil and the United States using Data Analysis and Machine Learning techniques. 

## Team Potato Members: 
###### Thi Nguyen, 862051496
###### Sydney Pun, 862053259
###### Heng Tan, 862155921


## Datasets Descriptions:
**Obtained through downloading:**
1. [Forest Fires in Brazil Dataset:](https://www.kaggle.com/gustavomodelli/forest-fires-in-brazil) This dataset provides an overview of the forest fires in Brazil over a period of 10 years.
2. [Forest Fires in Australia Dataset:](https://www.kaggle.com/carlosparadis/fires-from-space-australia-and-new-zeland) This dataset provides an overview of the Australian wildfires.
3. [1.88 Million US Wildfires:](https://www.kaggle.com/rtatman/188-million-us-wildfires) A dataset that contains 24 years of geo-referenced wildfire records that occurred in the U.S. from 1992 to 2015.
4. [NASA Fire Map:](https://firms.modaps.eosdis.nasa.gov/map/#z:7;c:-119.9,38.9;t:adv-points;d:2018-11-10..2018-11-30;l:firms_modis_a,fire_aqua_crc) An interactive web browser to browse the full archive of global active fire detections.
5. [Active Fire Data:](https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data) Downloadable active fire products in the form of KML, WMS, or text file formats that provide an overview of the history of active fires around the globe.

- Identifies and describes the dataset and problem at a high-level

**Data Obtained through Web Crawling:**
1. Twitter Dataset: A dataset containing a thousand Twitter posts using the Twitter search term forest fire acre.
2. NIFC Statistics: Crawling the National Interagency Fire Center's Statistics to analyze the annual wildfire reportings in the U.S.


## Phase 1 and 2 Contributions:

### Phase 1 Web Crawler Description: 
* Our Web Crawler crawls the National Interagency Fire Center's webpage to grab the annual wildfire reportings in the U.S. 
* Here is a link to the webpage for the statistics: https://www.nifc.gov/fireInfo/fireInfo_statistics.html

#### Twitter Scraper Description:
* Our Twitter Scraper scrapes the social media website Twitter.
* It searches for Twitter posts under the Twitter search term `forest fire acre`.
* It finds a thousand Twitter posts and then compiles them into a CSV file.

**Data Obtained through Web Crawling:**
1. Twitter Dataset: A dataset containing a thousand Twitter posts using the Twitter search term `forest fire acre`.
2. NIFC Statistics: Crawling the National Interagency Fire Center's Statistics to analyze the annual wildfire reportings in the U.S.

### Phase 2 Plan:
Because we wanted to prevent merge conflicts and we wanted to increase productivity, we have split the main three datasets that we have obtained amongst each member. This allows each member to have their own Jupyter notebook and thus perform data cleaning and EDA on their respective dataset. This prevents the issue of merge conflicts and of having all the team members constantly committing and pulling for updates on a single Jupyter notebook. 

#### Outline of Each Member's Responsibilities: 
###### Thi Nguyen: Cleaning and EDA on the Australia Dataset
###### Sydney Pun: Cleaning and EDA on the United States Dataset
###### Heng Tan: Cleaning and EDA on the Brazil Dataset


## Data Analysis Process Summary:

### Australia Dataset Analysis (Thi Nguyen):
* Set up the Model
* Fitted a Linear Regression Model
* Built a Model Using a Validation Set

### United States Dataset Analysis (Sydney Pun):
* Created a Heat Map
* Set up the Model
* Fitted a Linear Regression Model
* Build an Ashen Model to Predict Fire Acres

### Brazil Dataset Analysis (Heng Tan):
* Set up the Model
* Built a Model Using a Validation Set

### Results / Observations Obtained: 
* USA Results: Wildfires are primarily caused by lightening strikes. This illustrates the climate change issue. In addition, the average total acres burned down by wildfires is predicted to be 209,707.17121647 acres in 2020.


## How to Run Code:

### How to Run the Twitter Scraper:
* Install Python 3.7 or above because previous versions will likely not work.
* Install Selenium using the command `pip install -U selenium`
* Download the chromedriver from this link: https://chromedriver.chromium.org/downloads
* Save the chromedriver to the same path as the `twitter_scraper.py` script. 
* Open the file `twitter_scraper.py` and specify the path directory for your chromedriver
  * `driver = webdriver.Chrome(executable_path=r"C:\Chrome\chromedriver.exe")`
* Run `python twitter_scraper.py` and Tweet results will be printed into a CSV file. 

### How to Run the NIFC Crawler: 
* Install Python 3.7 or above
* Run `python nifc_table_crawler.py` and the NIFC stats will be printed into a CSV file. 

### How to Run Phase 2 and Phase 3:
* Download the files from the phase folders and run them on Jupyter Lab.
