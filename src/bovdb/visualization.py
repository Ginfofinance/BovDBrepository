"""
Visualization functions for BovDB stock quotes and intraday data.
"""

from typing import Optional
import pandas as pd


def plot_candlestick(
    df: pd.DataFrame,
    ticker_name: str = "ASSET",
    with_factor: bool = False,
    save_path: Optional[str] = None,
    show: bool = True,
) -> None:
    """
    Renders a standard daily Candlestick chart using mplfinance.

    Args:
        df: DataFrame containing date, open, high, low, close, and optionally factor/volume.
        ticker_name: Name/ticker code for chart title.
        with_factor: Boolean indicating if factor adjustment was applied.
        save_path: Optional file path to save output (e.g. .pdf or .png).
        show: If True, calls plt.show().
    """
    try:
        import mplfinance as mpf
        import matplotlib.pyplot as plt
    except ImportError:
        raise ImportError(
            "mplfinance and matplotlib are required for plot_candlestick. "
            "Please install them via: pip install mplfinance matplotlib"
        )

    plot_df = df.copy()

    if "date" in plot_df.columns:
        plot_df["date"] = pd.to_datetime(plot_df["date"])
        plot_df.set_index("date", inplace=True)

    if with_factor and "factor" in plot_df.columns:
        plot_df["open"] = plot_df["open"] / plot_df["factor"]
        plot_df["high"] = plot_df["high"] / plot_df["factor"]
        plot_df["low"] = plot_df["low"] / plot_df["factor"]
        plot_df["close"] = plot_df["close"] / plot_df["factor"]

    # Format columns for mplfinance (Open, High, Low, Close, Volume)
    ohlc_cols = {c: c.capitalize() for c in ["open", "high", "low", "close", "volume"] if c in plot_df.columns}
    plot_df.rename(columns=ohlc_cols, inplace=True)

    factor_label = "with factor" if with_factor else "without factor"
    title = f"{ticker_name} Daily Candlesticks ({factor_label})"

    style = mpf.make_mpf_style(
        base_mpf_style="classic",
        marketcolors=mpf.make_marketcolors(up="g", down="r", inherit=True)
    )

    kwargs = {
        "type": "candle",
        "style": style,
        "title": title,
        "ylabel": "Price (R$)",
        "figsize": (10, 6),
    }

    if "Volume" in plot_df.columns and plot_df["Volume"].sum() > 0:
        kwargs["volume"] = True
        kwargs["ylabel_lower"] = "Volume"

    if save_path:
        kwargs["savefig"] = save_path

    mpf.plot(plot_df, **kwargs)
    if show and not save_path:
        plt.show()


def plot_intraday_5min(
    df: pd.DataFrame,
    day: Optional[str] = None,
    ticker_name: str = "ASSET",
    save_html: Optional[str] = None,
    show: bool = True,
):
    """
    Renders an interactive 5-minute intraday candlestick chart using Plotly.

    Args:
        df: DataFrame containing date, time (or datetime), open, high, low, close, volume.
        day: Optional date filter ('YYYY-MM-DD').
        ticker_name: Name of asset for title.
        save_html: Optional path to export HTML chart.
        show: If True, calls fig.show().
    """
    try:
        import plotly.graph_objects as go
    except ImportError:
        raise ImportError(
            "plotly is required for plot_intraday_5min. "
            "Please install it via: pip install plotly"
        )

    plot_df = df.copy()

    if day and "date" in plot_df.columns:
        plot_df = plot_df[plot_df["date"] == day].copy()

    if plot_df.empty:
        raise ValueError(f"No intraday data available for day: {day}")

    if "datetime" not in plot_df.columns and "date" in plot_df.columns and "time" in plot_df.columns:
        plot_df["datetime"] = pd.to_datetime(plot_df["date"] + " " + plot_df["time"])

    fig = go.Figure(data=[
        go.Candlestick(
            x=plot_df["datetime"],
            open=plot_df["open"],
            high=plot_df["high"],
            low=plot_df["low"],
            close=plot_df["close"],
            name="OHLC"
        )
    ])

    title_text = f"5-Minute Candlestick Chart: {ticker_name}" + (f" ({day})" if day else "")
    fig.update_layout(
        title=title_text,
        xaxis_title="Time",
        yaxis_title="Price (R$)",
        xaxis_rangeslider_visible=False,
        template="plotly_white"
    )

    if save_html:
        fig.write_html(save_html)

    if show:
        fig.show()

    return fig


def plot_annual_stats(
    df: pd.DataFrame,
    ticker_name: str = "VALE3",
    start_year: int = 1995,
    end_year: int = 2024,
    save_path: Optional[str] = None,
    show: bool = True,
) -> None:
    """
    Calculates and plots annual average prices and standard deviation with and without factor.

    Args:
        df: Daily price DataFrame with date, close, factor columns.
        ticker_name: Name of ticker for title.
        start_year: Beginning year of analysis.
        end_year: Ending year of analysis.
        save_path: Optional path to save PDF/PNG figure.
        show: If True, displays the plot.
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        raise ImportError(
            "matplotlib is required for plot_annual_stats. "
            "Please install it via: pip install matplotlib"
        )

    data = df.copy()
    data["date"] = pd.to_datetime(data["date"])
    data["year"] = data["date"].dt.year

    data = data[(data["year"] >= start_year) & (data["year"] <= end_year)].copy()
    data["close_adj"] = data["close"] / data["factor"]

    grouped = data.groupby("year").agg(
        avg_raw=("close", "mean"),
        std_raw=("close", "std"),
        avg_adj=("close_adj", "mean"),
        std_adj=("close_adj", "std"),
    ).reset_index()

    years = grouped["year"].tolist()
    width = 0.35

    plt.rcParams["figure.figsize"] = (16, 6)
    fig, ax = plt.subplots()

    pos1 = [y - width / 2 for y in years]
    pos2 = [y + width / 2 for y in years]

    ax.bar(pos1, grouped["avg_raw"], width, yerr=grouped["std_raw"],
           align="center", ecolor="black", capsize=4, label="without Factor", color="#1f77b4")
    ax.bar(pos2, grouped["avg_adj"], width, yerr=grouped["std_adj"],
           align="center", ecolor="black", capsize=4, label="with Factor", color="#ff7f0e")

    ax.set_xlabel("Year", fontsize=14)
    ax.set_ylabel("Average Price (R$)", fontsize=14)
    ax.set_title(f"{ticker_name} Annual Mean & Std Dev ({start_year} - {end_year})", fontsize=16, fontstyle="italic")
    ax.set_xticks(years)
    plt.xticks(rotation=45, size=11)
    plt.yticks(size=11)
    ax.legend(fontsize=12, frameon=True)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, format="pdf" if save_path.endswith(".pdf") else "png")

    if show and not save_path:
        plt.show()
