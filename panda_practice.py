import matplotlib.pyplot as plt
import pandas as pd
from prophet import Prophet


# fetch weather between 1870-2010
def fetch_weather():
    url = "https://www.data.jma.go.jp/stats/etrn/view/monthly_s3.php?prec_no=44&block_no=47662"
    dfs = pd.read_html(url)
    df = dfs[0].dropna()
    plt.scatter(df["年"], df["1月"])
    plt.show()


def expect_weather_in_100_years():
    url = "https://www.data.jma.go.jp/stats/etrn/view/monthly_s3.php?prec_no=44&block_no=47662"
    dfs = pd.read_html(url)
    df = dfs[0].dropna()
    data = pd.DataFrame()
    data["y"] = df["1月"]
    data["ds"] = df[["年"]].apply(lambda x: "{}".format(x[0]), axis=1) + "-01-01"
    model = Prophet(daily_seasonality=True, weekly_seasonality=True, yearly_seasonality=True)
    model.fit(data)

    future_data = model.make_future_dataframe(periods=100, freq="y")
    forecast_data = model.predict(future_data)
    model.plot(forecast_data)
    model.plot_components(forecast_data)
    plt.show()


if __name__ == '__main__':
    # fetch_weather()
    expect_weather_in_100_years()
