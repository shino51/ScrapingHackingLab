import matplotlib.pyplot as plt
import pandas as pd


# fetch weather between 1870-2010
def fetch_weather():
    url = "https://www.data.jma.go.jp/stats/etrn/view/monthly_s3.php?prec_no=44&block_no=47662"
    dfs = pd.read_html(url)
    df = dfs[0].dropna()
    plt.scatter(df["年"], df["1月"])
    plt.show()


if __name__ == '__main__':
    fetch_weather()
