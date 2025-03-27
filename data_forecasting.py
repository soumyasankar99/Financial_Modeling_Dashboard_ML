from statsmodels.tsa.arima.model import ARIMA
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def arima_forecasting(df, st):
    st.subheader("🔮 ARIMA Forecasting")
    model = ARIMA(df['Revenue'], order=(5,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=12)
    future_dates = pd.date_range(start=df.index[-1], periods=13, freq='M')[1:]

    fig, ax = plt.subplots()
    ax.plot(df.index, df['Revenue'], label='Historical')
    ax.plot(future_dates, forecast, color='red', label='Forecast')
    ax.set_title("ARIMA - Revenue Forecast")
    ax.legend()
    st.pyplot(fig)

def lstm_forecasting(df, st):
    st.subheader("🧠 LSTM Forecasting")

    scaler = MinMaxScaler()
    df_lstm = scaler.fit_transform(df[['Revenue']])
    seq_len = 12
    X, y = [], []

    for i in range(len(df_lstm) - seq_len):
        X.append(df_lstm[i:i+seq_len])
        y.append(df_lstm[i+seq_len])

    X, y = np.array(X), np.array(y)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(seq_len, 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=20, verbose=0)

    input_seq = df_lstm[-seq_len:].reshape((1, seq_len, 1))
    forecast_scaled = []

    for _ in range(12):
        pred = model.predict(input_seq, verbose=0)[0][0]
        forecast_scaled.append(pred)
        input_seq = np.append(input_seq[:, 1:, :], [[[pred]]], axis=1)

    forecast = scaler.inverse_transform(np.array(forecast_scaled).reshape(-1, 1))
    future_dates = pd.date_range(start=df.index[-1], periods=13, freq='M')[1:]

    fig, ax = plt.subplots()
    ax.plot(df.index, df['Revenue'], label='Historical')
    ax.plot(future_dates, forecast, label='LSTM Forecast', color='green')
    ax.set_title("LSTM - Revenue Forecast")
    ax.legend()
    st.pyplot(fig)
