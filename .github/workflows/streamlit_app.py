import pandas as pd
from google.colab import files
uploaded = files.upload()
for filename in uploaded.keys():
    df = pd.read_csv(filename)  # Load the CSV file
    print(f"Loaded {filename} into DataFrame.")
  print(df.head(50))
pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
%%writefile app.py
! wget -q -o - ipv4.icanhazip.com
!apt-get install nodejs
!npm install -g localtunnel@2.0.2
! streamlit run app.py & npx localtunnel --port 8501
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.title("Exploring Tourism and Accommodation Trends in Selected Lebanese Towns")
Tourism_Index_COLUMN = 'Tourism Index'
Number_of_Hotels_COLUMN = 'Total_number_of_hotels'
data_csv='551015b5649368dd2612f795c2a9c2d8_20240902_115953.csv'
@st.cache_data  
def load_data(nrows):
  data = pd.read_csv(data_csv, nrows=nrows)
  #lowercase = lambda x: str(x).lower()
  #data.rename(lowercase, axis='columns', inplace=True)
  #data[Tourism_Index_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
  return data

data_load_state = st.text('Loading data...')
data = load_data(50)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
  st.subheader('Raw data')
  st.write(data)

st.markdown("In this interactive dashboard, we explore two important aspects of tourism in Lebanon.")
st.markdown("Tourism Index:The Tourism Index measures a town's attractiveness to tourists, considering factors like attractions, culture, and infrastructure. A higher score indicates a greater ability to attract visitors, boosting economic activity and hospitality growth.")
st.markdown("Number of Hotels:The number of hotels in a town reflects its accommodation capacity. Towns with more hotels are better positioned to welcome tourists, highlighting their dependence on tourism for economic purposes.")
st.subheader('Number of hotels By Town')
Hotels_to_filter = st.slider('Tourism Index', 0, 4, 0)
filtered_data = data[Tourism_Index_COLUMN ][data[Number_of_Hotels_COLUMN] == Hotels_to_filter]
chart_data = pd.DataFrame(
    {
        "Town": data['Town'],
        "Hotels": data[Number_of_Hotels_COLUMN][data[Number_of_Hotels_COLUMN]==Hotels_to_filter]
  
    }
)
#hist_values = np.histogram(filtered_data, bins=5, range=(0,5))[0]
st.bar_chart(chart_data, x= 'Town', y= 'Hotels')

pie_data = pd.DataFrame(
    { 
        "Town": data['Town'],
        "Tourism_Index": data[Tourism_Index_COLUMN],
        "Hotels_Index": data[Number_of_Hotels_COLUMN][data[Number_of_Hotels_COLUMN]==Hotels_to_filter]
  
    }
)


Index = st.selectbox('Index', ['Tourism_Index', 'Hotels_Index'])
fig=px.pie(pie_data,values=Index,names='Town',height=300,width=200,title=f"{Index}")
st.plotly_chart(fig, use_container_width=True)
