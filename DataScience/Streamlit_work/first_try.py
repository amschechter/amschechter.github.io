### OK. I am trying some different stuff here.
### I am moving from Jupyter Notebooks to a traditional python file.
### I'm doing this to grow my world but also to try to use streamlit. 
### Steamlit does technically have a jupyter extension but that seems like more trouble than worth. Good luck to me.

import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np
import h3pandas


def main():
    austin_airbnb_df = pd.read_csv('C:/Users/aaron/Code/Data/austin_airbnb_listings.csv')

    #neighborhood = st.selectbox(label="Austin Neighborhood", options=austin_airbnb_df['neighbourhood'].tolist())

    min_price = austin_airbnb_df['price'].min()
    max_price = austin_airbnb_df['price'].max()

    print (min_price)
    print (max_price)

    st.subheader('Filters')

    price_slider = st.slider(label = "AirBnB price", min_value=min_price, max_value=max_price, value=(min_price, max_price))

    print (price_slider[0])
    print (price_slider[1])


    filtered_frame = austin_airbnb_df[(austin_airbnb_df['price'] >= price_slider[0]) & 
                                      (austin_airbnb_df['price'] <= price_slider[1])]


    st.subheader(price_slider[0])
    st.subheader(price_slider[1])

    st.subheader("Airbnbs")
    st.dataframe(filtered_frame)

    
    st.map(data=filtered_frame, size=3)

main()

#if __name__ == "__main__":
 #   main()