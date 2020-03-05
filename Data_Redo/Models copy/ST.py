import sys
import pandas as pd
import altair as alt

if sys.version_info[0] < 3:
    reload(sys) # noqa: F821 pylint:disable=undefined-variable
    sys.setdefaultencoding("utf-8")

@st.cache
def get_cr_data():
    df = pd.read_csv("finished_df.csv")
    return df.set_index("Ticker")

try:
    df = get_cr_data()
except urllib.error.URLError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )
    # return "Error"

companies = st.multiselect(
    "Choose Tickers", list(df.index), ["AAL", "VZ"]
)
if not companies:
    st.error("Please select at least one Ticker.")
    return "Please select at least one TIcker"

data = df.loc[companies]
# data /= 1000000.0
df.loc[test_df["Ticker"] == data]
st.write("Bond Information", data.sort_index())

data = data.T.reset_index()
data = pd.melt(data, id_vars=["index"]).rename(
    columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
)
chart = (
    alt.Chart(data)
    .mark_area(opacity=0.3)
    .encode(
        x="year:T",
        y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
        color="Region:N",
    )
)
st.altair_chart(chart, use_container_width=True)