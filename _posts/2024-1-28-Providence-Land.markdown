---
layout: post
title:  "Providence's tax income and land ownership"
date:   2024-1-28 13:17:35 -0800
categories: jekyll update
---

For my most recent project I did a study of Providence, Rhode Island! This was an interesting challenge for me because I typically work with data sets pertaining to places or things that I have personal prior knowledge of, but going into this I knew almost nothing about Providence. This meant that I didn't know where the economic centers of the city were or who the biggest land owners would be, which was kind of nice because I wasn't expecting anything in particular and I could really learn through the numbers.

For this project I was able to combine two different data sets about Providence, one of them was the 'Property Tax Roll', containing Property Tax information on every property in the entire city while the other was the Parcel boundaries which had geographic information. I was able to combine these data sets because they shared a Tax ID column and this let me make some interesting maps! 

The city of Providence has right around 44,000 individual land parcels all paying tax (or not) separately. The entity that owned the most property was actually 361 different units in the same building at 1000 Providence Street owned by 'Athena Providence Place'. There was a fascinating court case pertaining to the property tax of this building you can read about [here](https://law.justia.com/cases/rhode-island/supreme-court/2021/19-247.html)!

The image below shows every property, plotted by the amount of tax assessed on their property and the amount of tax actually paid. 

!['assessed property tax '](/images/Providence/Assessed%20Property%20Value%20vs%20Paid%20Tax.png){:class="img-responsive"}

The next chart displays the same data, but distilled one more time. Now you can see the Assessed land value on the X axis and the percent of tax paid when compared to the assessed land value. We can see that Providence has three distinct tax brackets and on top of that has flexibility within the brackets.

!['assessed property tax vs paid tax percent'](/images/Providence/Assessed%20Property%20Value%20vs%20Paid%20Tax%20Percent.png){:class="img-responsive"}

Now lets take that data and map it! Below you can see that the residential areas seem to pay less when compared to their assessed value whereas properties in the business zones and along the water pay more. This must be due to Providence or Rhode Island tax rates for the land.

!['Tax paid as a percent of assessed property value '](/images/Providence/Realized%20Tax%20Percentage%20map.png){:class="img-responsive"}

Now we can compare the map above, which looks at the tax paid as a percent of the assessed value with the map below, which looks at the tax paid per square foot. There are some clear similarities in the geographical patterns here.

!['Tax Paid by SQFT'](/images/Providence/Assessed%20Property%20Value%20by%20SQFT.png){:class="img-responsive"}

Now lets take a look at the ownership by state! The large majority (over 90%) of the properties in the data set are owned by residents of Rhode Island. Take a look at the distribution below.

!['Parcel ownership by state.'](/images/Providence/All%20Properties%20By%20State.png){:class="img-responsive"}

Enjoy similar data on an interactive map! I chose to exclude all properties owned by RI residents for legibility's sake. The colors of the map below represent the owner's state but you can hover over the parcels to get other information about the land. 

<br>
<div class="video-container">
    <iframe src="/images/Providence/Out_of_state_ownership.html" height="415" width="700" allowfullscreen="" frameborder="0">
    </iframe>
</div>
<br>


Thanks for taking the time to read all this! Thanks to the City of Providence for providing the wonderful data, see the [parcel data here](https://data.providenceri.gov/Neighborhoods/Providence-Parcel-Boundaries-2017/78bu-i8at) and the [tax data here](https://data.providenceri.gov/dataset/2023-Property-Tax-Roll/fd8d-n74v/about_data). See the code that I wrote to make this project [here](https://github.com/amschechter/amschechter.github.io/blob/main/DataScience/Shape%20Projects/Providence_Property_Tax.ipynb).