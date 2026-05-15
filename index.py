python
import pandas as pd
import plotly.express as px
from fbprophet import Prophet

# Load SAIDI data
data = pd.read_csv('SAIDI.csv')
data['Date'] = pd.to_datetime(data['Year'], format='%Y')
data = data.rename(columns={"SAIDI": "y", "Date": "ds"})

# Create a time series plot
fig = px.line(data, x='ds', y='y', title='SAIDI Over Time', labels={"ds": "Year", "y": "SAIDI (minutes)"})
fig.show()

# Predict future SAIDI values using Facebook Prophet
model = Prophet()
model.fit(data)

future = model.make_future_dataframe(periods=3, freq='Y')
forecast = model.predict(future)

# Plot the forecast
fig_forecast = model.plot(forecast)
fig_forecast.show()

# Save forecast to CSV
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv('SAIDI_forecast.csv', index=False)
