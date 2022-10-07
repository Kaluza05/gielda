import pandas as pd
import matplotlib.pyplot as plt
#import streamlit as st
my_url = 'https://www.bankier.pl/gielda/notowania/akcje?index=MWIG40'
def take_data(url):
    data = pd.read_html(url)[0]
    data.columns = [i.split(' ')[0] for i in data.columns]
    data = data[data['Walor'].notna()].reset_index(drop=True)
    data['Zmianaprocentowa'] = [float(str(i)[:-1].replace(',','.')) for i in data['Zmianaprocentowa']]
    data['Obrót'] = [int(i.replace('\xa0','')) for i in data['Obrót']]
    data['Liczbatransakcji'] = [int(float(str(i).replace('\xa0',''))) for i in data['Liczbatransakcji']]
    data = data[['Walor','Zmianaprocentowa','Obrót','Liczbatransakcji']]
    data = data.sort_values(by='Zmianaprocentowa',ascending=False).reset_index(drop=True)
    return data
akcje = take_data(my_url)
print(akcje)
akcje.plot(x='Walor',y= 'Zmianaprocentowa',kind = 'bar')
#st.plotly_chart(akcje)
plt.show()
