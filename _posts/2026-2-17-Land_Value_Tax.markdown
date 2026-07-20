---
layout: post
title:  "A look at Property Tax Assessment"
date:   2026-2-16 13:17:35 -0800
categories: jekyll update
thumbnail: '/images/Georgism_Study/Seattle_land_val_from_the_north.png'
---

##### *Update #2! I got the chance to publish different version of this article in theUrbanist! Check it out <a href="https://www.theurbanist.org/op-ed-the-case-for-shifting-to-a-land-value-tax/" target="_blank">here</a>.*

##### *I made a version of the maps in this post where you can adjust the data shown! Check it out <a href="https://property-tax-interactive.streamlit.app/" target="_blank">here</a>.*

### How do we charge tax?

Property tax plays a critical role in how Seattle functions. In 2025 property tax represented over [22% of Seattle's entire revenue stream](https://www.seattle.gov/economic-and-revenue-forecasts/forecasts), accounting for the City's largest income category. Property Tax brings in more than Seattle's other significant income sources of Sales tax, B&O tax, and Utility Tax. Here in the state of Washington it is especially critical due to our lack of state income tax.

I believe that our method of assessing property tax is antiquated and unnecessarily discourages development. Current practice in King County, in addition to the entire United States, (? I believe???) is to assess property values by combining the value of the land with the value of the ‘improvements’, unceremoniously adding them together, and then charging that years tax based on the sum. The improvements on the land - meaning the value of any and all structures on that land - are often assessed at dramatically higher values than the land itself.


Here in Seattle we are blessed with being located on an isthmus! We are bound by water to the east and west and are thus unable to sprawl. This situation means that we have to look inward to accommodate our seemingly insatiable growth demand. Using data from 2025, the city of Seattle has $156,763,537,497 ($156 Billion) worth of appraised land value and a remarkably similar $159,457,751,625 ($159 Billion) worth of appraised improved value. Note that not all of the properties included in those numbers are taxed because they are public properties or exempt for some other reason. The value of taxable land in the city is $126,251,307,057 and taxable improvements are $137,720,958,907. For the rest of this piece I will be referring to the total appraised value, both taxable and non-taxable. 


Our property tax system by nature discourages development. When a property owner builds on their land - their tax bill jumps. Often dramatically. The most extreme case in terms of raw improvements is [Onni South Lake Union](https://blue.kingcounty.com/Assessor/eRealProperty/Dashboard.aspx?ParcelNbr=2693100068) located on Denny/Boren in South Lake Union. This building occupies a lot of 55,000 square feet, or 1.26 acres. The improvements on the lot were assessed at a hefty $714,577,100 in 2022 while the lot itself was valued at $49,531,500, meaning the improvements are over 14 times the value of the land. With a total Seattle tax rate of $9.19418 per $1,000 of property value, the owner of the lot pays $7,025,352 in tax, $6,569,950 of which is derived from the improvement values. There are approximately 827 units in the tower meaning tenants pay over $700 per month per unit in property tax, about 95% of which is derived from the assessed improvements. 

### Taking this to the rest of the city

The numbers pertaining to Onni SLU and many other office and residential buildings in the most valuable parts of the city are indeed enormous, but that is actually not what my gripe is really about. Nearly all of the parcels with the highest amounts of assessed improvements are located in the most desirable parts of the city where people will pay top dollar to be. I believe that our tax code should continue to tax those parcels at extremely high rates, not because their structures are so impressive, but because the land is so valuable.

The effects of the current property tax system are also extremely significant in more residential parts of Seattle. Here is a small display showing the median values of some property types.

This table shows that there is a disparity in how different land use types take advantage of their space.

| Property Type | Median **Land** Value | Median **Improved** Value | Occurrences of this building type in Seattle |
| All Seattle Property | $ 477,000 | $ 422,000 | 178,565 |
| Single Family Homes | $ 497,000 | $419,000 | 130,011 |
| Townhouses | $249,000 | $450,000 | 22,360 |
| Gas Stations | $2,273,150 | $415,650 | 96 |

### Maps!


Take a look at a couple of maps I made comparing the Appraised Land Value and the Appraised Improvement value. The maps displayed here group every parcel in the city into hexagons, and adds together the land value and improvement value respectively that are captured in that hexagon. 

This map showing the appraised land value by hexagons throughout the city displays that the highest land values are where you would expect. Land located in Downtown, South Lake Union and the U-District is taxed at a higher rate than other land around the city.

#### Appraised Land Value aggregated spatially

<iframe src="/images/Georgism_Study/Land_val_hex_viz_500_v2.html" height="555" width="700" allowfullscreen="" frameborder="0"> </iframe>
*This is an interactive map. Use your scroll wheel to zoom in/out and Ctrl + Drag to change the view angle*


But now take a look at this map showing the improved upon value of that same land. The disparities seen in the improvement maps are dramatically larger than the disparity between land values across the city. I believe that this is a symptom of our tax code. Why would a developer make an extravagant building for any purpose on less valuable land when the valuation will be nearly entirely based upon the improvements?

#### Appraised Improvement Value aggregated spatially

<iframe src="/images/Georgism_Study/Improved_val_hex_viz_500_v2.html" height="555" width="700" allowfullscreen="" frameborder="0"> </iframe>


Does this distribution of valuation in buildings vs. land seem natural? Does it makes sense that the land across the city is valued in a relatively even fashion with gentle peaks and valleys, whereas the investments made in our built structures are so incredibly concentrated in small areas of our city? The Office of Planning and Community Development has been using the city comprehensive plan to designate 'neighborhood centers' across the city in an effort to encourage development. I posit that an altered property tax code, one that would not charge extremely high improvement taxes on structures built on relatively low-value land, could do a lot to help develop those types of areas. 


### Gas Stations and the like

A huge beneficiary of the current system are businesses who operate with underdeveloped land. Nobody looks at a gas station and thinks ‘what an amazing victory of architecture!’. The King County assessor agrees. Gas stations pay an average of $0.23 cents in improved value for every $1 of land value. For context Single Family homes, which account for about 70% of our parcels pay on average slightly more in improved value than land value, $1.03 dollars of imp val for every $1 of land value (this number is different than what the table above says because of the mean vs median gap. The highest value homes push up the mean improvement number shown here.), while Townhomes, the second most common parcel type, pay an average of $1.86 in improvement value tax for every dollar of land value tax. Apartments pay an even higher ratio at $2.14 in improved value for every $1 of land val. These discrepancies, which extend to other non-maximizing land uses such as commercial parking (13 cents per dollar), Big Box Retail (8 cents per dollar), fast food restaurants (6 cents per dollar) all pay far less in taxes than they should just because they operate with less than amazing buildings. We are discouraging land use types we need more of, such as apartments and dense lots in Single Family neighborhoods while encouraging businesses to not maximize their land usage.

### Vacant lots

This one may seem self evident but I would also like to mention vacant lots. Throughout the city there are quite a few vacant lots. Specifically there are 889 Vacant Single Family, 253 Vacant Multi-Family, 246 Vacant Commercial and 216 Vacant Industrial lots. These lots naturally have extremely low Improvement to Land Value ratios, and although some of them have valid reasons for being vacant, many of them sit empty because it is the cheapest and easiest thing to do. If we had a system where a vacant lot had to pay the same in property tax as the identical lot nextdoor with a house on it, chances are there would be significantly less vacancy. Our current code enables vacancy in a city that needs the opposite.

### The MFTE

It would be disingenuous of me to not mention the [MultiFamily Tax Exemption](https://www.seattle.gov/housing/housing-developers/multifamily-tax-exemption). This is a program by the city of Seattle done to counteract this exact dynamic. Property developers can (and frequently do) apply for the MFTE to get a property tax exemption in exchange for providing a certain percentage of rent-restricted properties. This is a good program that makes development in our city easier. 

But there are a few factors holding back the MFTE. 
* Developers still have to apply, get approved and designate a certain amount of units to make less profit on.
* Because it is an 'exemption', it will always be an exception to the rule and not a culture change.
* It does not help a family that wants to build an DADU in the backyard, Does not punish a business who is taking poor advantage of their land, and does not help a small time developer who would want to make a [multiplex](https://www.theurbanist.org/2025/10/03/seattle-council-sets-the-stage-for-a-potential-multiplex-boom/) on their land.


### What we can do about it

Tax Law is notoriously difficult to change and I am no legal scholar or politician. So take this with a grain of salt.

I propose slowly, over time, increasing the 'weight' of the land value and decreasing the 'weight' of the improvement value. What I mean is that next year we could assess properties as we normally do, but when it comes time to do that final sum to add together the land value with the improved value, the assessors office could multiply the land value by 1.02, and multiply the improved value by 0.98. And then the next year change those numbers to 1.04 and 0.96 respectively and keep it going, so that in 50 years we are charging only tax on the land.


### In Conclusion

I know that this is a serious topic and that there are many considerations that I have either not covered in this article or have not considered myself. If you are reading this and have thoughts I would love to hear them. Please reach out at aaron.m.schechter@gmail.com

Thanks to King County for the [Data](https://data.kingcounty.gov/Property-Assessments/Real-Property-Tax-Receivables/dkna-i698/data_preview), and if you would like to see my code for this project you can find it [here](https://github.com/amschechter/Georgism_Study).

Thanks for reading. Let me know what you think.
