### import libraries
import pandas as pd
import streamlit as st
import joblib

#######################################################################################################################################
### Create a title
st.title("THIS IS MY COOL APP")
st.sidebar.subheader("Usage Filters")
round_trip_select = st.sidebar.checkbox("Round Trips Only")
# Press R in the app to refresh after changing the code and saving here


# #######################################################################################################################################
# ### DATA LOADING

# ### A. define function to load data

# @st.cache_data
# def load_data(round_trip_select):
#     df = pd.read_csv("NYC_bikes_small.csv")
#     df = df.rename(columns={"Start Station Latitude":"LAT",
#                             "Start Station Longitude":"LON"})
#     df["Start Time"] = pd.to_datetime(df["Start Time"])
#     if round_trip_select:
#         filter = df["Start Station ID"] == df["End Station ID"]
    
#         df = df.loc[filter,:]
#     return df


# ### B. Load first 50K rows into a df variable
# data = load_data(round_trip_select)


# ### C. Display the dataframe in the app
# st.dataframe(data)
# st.write("Total Trips Shown {}".format(data.shape[0]))




# #######################################################################################################################################
# ### STATION MAP

# st.subheader("NYC Station Map")
# st.map(data)




# #######################################################################################################################################
# ### DATA ANALYSIS & VISUALIZATION

# ### B. Add filter on side bar after initial bar chart constructed
# # filter for round trips





# ### A. Add a bar chart of usage per hour

# hourly_usage = data["Start Time"].dt.hour.value_counts()

# st.bar_chart(hourly_usage)


# #######################################################################################################################################
# ### MODEL INFERENCE

# # A. Load the model using joblib
# model = joblib.load('sentiment_pipeline.pkl')


# # B. Set up input field

# text = st.text_input('Enter your review text below', 'Best. Restaurant. Ever.')

# # C. Use the model to predict sentiment & write result
# prediction = model.predict({text})


# # C. Use the model to predict sentiment & write result
# if prediction == 1:
#     st.write('We predict that this is a positive review!')
# else:
#     st.write('We predict that this is a negative review!')