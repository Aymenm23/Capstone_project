# Capstone_project
This is my capstone for the duration of the bootcamp at BrainStation.

# Capstone Project Breakdown:

# Title: Harvesting Hope: Revolutionizing Farming Practices for Sustainable Crop Yield Growth

# Objective:

- Use machine-learning and precision agriculture to predict if there is a correlation between soil composition and climate factors when predicting crop yield.


# Datasets:
- World Hunger Index
- Country Agricultural Land 
- Country Crop Production
- Country Population Statistics
- Vegetation Health Index
- Vegetation Condition Index
- Crop Recommendation Datasets (Which crop suits what kind of environment and production stats)

# Goal: 
Use precision agriculture to assess how production of vegetation in an informed manner can affect the crop yield.

# Features:
- Soil Composition
    - N - ratio of Nitrogen content in soil
    - Ph - ph value of the soil
    - OM - organic matter in soil

- Climate
    - Humidity
    - Rainfall in mm
    - Average temp

- Country Index (Data engineered in SQL)
    - Area Harvested
    - Country crop/harvest yield based on 175 top crop/produce
    - ASI - Agricultural Stress Index
    - VHI - Vegetation health index

# Preprocessing Steps
First I obtained my dataset from the FAO where it broke down the data by continent. I shifted my focus onto two countries of similar size on relatively opposite sides of the GHI scale, this is how I settled on Yemen and Thailand. 

I then made all of my necessary transformations on SQL, the transformations include:
- Converting the years into one column
- Removing all flag columns
- Breaking up the element columns into 3 (Production, Yield, Area Harvested)
- Concatenated climate data, soil data, VHI and ASI to the table by utilizing excel to format and SQL to join.
- Converted all NAN's to 0
- Removed all duplicates
- Removed all blanks (none)

# Modeling
Using the three most common regression methods I inputed my data after preforming all necessary preliminary steps (set Xy, split test/train, and instantiate). I then made predictions and evaluated based on Mean Absolute Error and R2.



