#-----------------------------------------------------------------

import pandas as pd
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
from db import db_conn
import plotly.graph_objects as go
import numpy as np
new_db_conn = db_conn()

@st.cache_data(ttl=3600 * 1) 
def all_data_for_stats():
    
    df_sheet0 = new_db_conn.read(worksheet="Sheet0")  
    df_sheet1 = new_db_conn.read(worksheet="Sheet1")  
    df_sheet2 = new_db_conn.read(worksheet="Sheet2")  
    all_data = pd.concat([df_sheet0, df_sheet1, df_sheet2], ignore_index=True)
    all_data.replace('NA', pd.NA, inplace=True)
    all_data.fillna(0, inplace=True)

    return all_data


@st.cache_data(ttl=3600 * 1) 
def df_for_comp():

    df_for_com = new_db_conn.read(worksheet="comparisons", ttl=5)
    df_for_com.replace('NA', pd.NA, inplace=True)
    df_for_com.fillna(0, inplace=True)
    return df_for_com


 

all_data = all_data_for_stats()

all_data['Date'] = pd.to_datetime(all_data['Date'], format='%m/%d/%Y')


def zeniva_values_for_insights(data):
    zeniva_data = data[(data["Product"] == "zeniva") & (data["Platform"])]
    max_date = zeniva_data['Date'].max()
    
    latest_zeniva_data = zeniva_data[zeniva_data['Date'] == max_date]
    pivoted_data = latest_zeniva_data.pivot(index=['Date', 'Product', 'Platform'], columns='Matrix', values='Values').reset_index()
    zeniva_youtube = pivoted_data[pivoted_data["Platform"] == "youtube"]
    zeniva_x = pivoted_data[pivoted_data["Platform"] == "x"]
    zeniva_tiktok = pivoted_data[pivoted_data["Platform"] == "tiktok"]
    zeniva_linkedin = pivoted_data[pivoted_data["Platform"] == "linkedin"]
    zeniva_instagram = pivoted_data[pivoted_data["Platform"] == "instagram"]
    zeniva_facebook = pivoted_data[pivoted_data["Platform"] == "facebook"]
    return (
        zeniva_youtube[["total_followers", "today_followers", "yesterday_followers"]],
        zeniva_x[["total_followers", "today_followers", "yesterday_followers"]],
        zeniva_tiktok[["total_followers", "today_followers", "yesterday_followers"]],
        zeniva_linkedin[["total_followers", "today_followers", "yesterday_followers"]],
        zeniva_instagram[["total_followers", "today_followers", "yesterday_followers"]],
        zeniva_facebook[["total_followers", "today_followers", "yesterday_followers"]],
    )


def exarta_values_for_insights(data):
    exarta_data = data[(data["Product"] == "Exarta") & (data["Platform"])]
    max_date = exarta_data['Date'].max()
    
    latest_exarta_data = exarta_data[exarta_data['Date'] == max_date]
    pivoted_data = latest_exarta_data.pivot(index=['Date', 'Product', 'Platform'], columns='Matrix', values='Values').reset_index()
    exarta_youtube = pivoted_data[pivoted_data["Platform"] == "youtube"]
    exarta_x = pivoted_data[pivoted_data["Platform"] == "x"]
    exarta_facebook = pivoted_data[pivoted_data["Platform"] == "facebook"]
    exarta_linkedin = pivoted_data[pivoted_data["Platform"] == "linkedin"]
    exarta_instagram = pivoted_data[pivoted_data["Platform"] == "instagram"]
    return (
        exarta_youtube[["total_followers", "today_followers", "yesterday_followers"]],
        exarta_x[["total_followers", "today_followers", "yesterday_followers"]],
        exarta_facebook[["total_followers", "today_followers", "yesterday_followers"]],
        exarta_linkedin[["total_followers", "today_followers", "yesterday_followers"]],
        exarta_instagram[["total_followers", "today_followers", "yesterday_followers"]],
    )



def odyssey_values_for_insights(data):
    odyssey_data = data[(data["Product"] == "Odyssey") & (data["Platform"])]
    max_date = odyssey_data['Date'].max()
    
    latest_odyssey_data  = odyssey_data[odyssey_data['Date']== max_date]
    pivoted_data = latest_odyssey_data.pivot(index=['Date', 'Product', 'Platform'], columns='Matrix', values='Values').reset_index()
    odyssey_youtube = pivoted_data[pivoted_data["Platform"] == "youtube"]
    odyssey_tiktok = pivoted_data[pivoted_data["Platform"] == "tiktok"]
    odyssey_instagram = pivoted_data[pivoted_data["Platform"] == "instagram"]
    odyssey_facebook = pivoted_data[pivoted_data["Platform"] == "facebook"]
    return (
        odyssey_youtube[["total_followers", "today_followers", "yesterday_followers"]],
        odyssey_tiktok[["total_followers", "today_followers", "yesterday_followers"]],
        odyssey_instagram[["total_followers", "today_followers", "yesterday_followers"]],
        odyssey_facebook[["total_followers", "today_followers", "yesterday_followers"]],
    )



def plot_histograms(product_name, platform_name):
    # Load and preprocess the data
    df = all_data
    df = df[(df['Product'] == product_name)]
    
    # Define metrics for each platform
    platform_metrics = {
        'youtube': ['clicks', 'views', 'daily_spend'],
        'meta': ['clicks', 'reach', 'daily_spend'],
        'shopify': ['clicks', 'daily_spend', 'impressions'], 
        'ppc': ['clicks', 'daily_spend', 'impressions'],
    }

    # Check if platform is recognized and select metrics
    if platform_name in platform_metrics:
        selected_metrics = platform_metrics[platform_name]
    else:
        st.error(f"Platform {platform_name} not recognised.")
        return

    # Filter data by platform
    df_platform = df[df['Platform'] == platform_name]

    # Convert 'Date' column to datetime format
    df_platform['Date'] = pd.to_datetime(df_platform['Date'], format='%m/%d/%Y')

    # Ensure platform has data
    if df_platform.empty:
        st.error(f"No data available for platform {platform_name}.")
        return

    # Filter metrics and summarize values
    df_filtered = df_platform[df_platform['Matrix'].isin(selected_metrics)]
    summary_df = df_filtered.groupby(['Date', 'Matrix'])['Values'].sum().reset_index()
    
    # Pivot to make 'Date' rows and 'Matrix' columns
    summary_pivot = summary_df.pivot(index='Date', columns='Matrix', values='Values').fillna(0)
    summary_pivot.reset_index(inplace=True)

    # Color mapping for metrics
    color_discrete_map = {
        'clicks': '#BC679C',
        'views': '#F68C5B',
        'daily_spend': '#A6B174',
        'reach': '#F68C5B',
        'impressions': '#F68C5B'
    }
    
    # Label mapping for metrics
    label_map = {
        'clicks': 'Clicks',
        'views': 'Views',
        'daily_spend': 'Daily Spend',
        'reach': 'Reach',
        'impressions': 'Impressions'
    }

    # Reshape for plotting
    summary_melted = summary_pivot.melt(id_vars='Date', var_name='Metric', value_name='Value')
    yt_value = summary_melted.loc[summary_melted['Metric'] == 'views', 'Value']
# Apply logarithmic transformation to values
    if platform_name == 'youtube':
        summary_melted.loc[summary_melted['Metric'] == 'views', 'Value'] = np.log(summary_melted.loc[summary_melted['Metric'] == 'views', 'Value'])
        summary_melted.loc[summary_melted['Metric'] == 'daily_spend', 'Value'] = np.log(summary_melted.loc[summary_melted['Metric'] == 'daily_spend', 'Value'])
        summary_melted.loc[summary_melted['Metric'] == 'clicks', 'Value'] = np.log(summary_melted.loc[summary_melted['Metric'] == 'clicks', 'Value'])
        

    if platform_name == 'meta':
        summary_melted.loc[summary_melted['Metric'] == 'reach', 'Value'] = np.log(summary_melted.loc[summary_melted['Metric'] == 'reach', 'Value'])
        summary_melted.loc[summary_melted['Metric'] == 'daily_spend', 'Value'] = np.log(summary_melted.loc[summary_melted['Metric'] == 'daily_spend', 'Value'])
        summary_melted.loc[summary_melted['Metric'] == 'clicks', 'Value'] = np.log(summary_melted.loc[summary_melted['Metric'] == 'clicks', 'Value'])

    if platform_name in ['shopify', 'ppc']:
        summary_melted.loc[summary_melted['Metric'] == 'daily_spend', 'Value'] = np.log(summary_melted.loc[summary_melted['Metric'] == 'daily_spend', 'Value'])
        summary_melted.loc[summary_melted['Metric'] == 'impressions', 'Value'] = np.log(summary_melted.loc[summary_melted['Metric'] == 'impressions', 'Value'])
        summary_melted.loc[summary_melted['Metric'] == 'clicks', 'Value'] = np.log(summary_melted.loc[summary_melted['Metric'] == 'clicks', 'Value'])


    # Plot histogram
    fig = px.histogram(
        summary_melted, 
        x='Date', 
        y='Value', 
        color='Metric', 
        barmode='group', 
        height=300,
        width=800,
        color_discrete_map=color_discrete_map,
    )
    

    # # Set bar labels and positions
    # for trace in fig.data:
    #     trace.text = trace.y  
    #     trace.textposition = 'outside'  # Set text position for all traces
    #     trace.textfont.size = 14  # Set font size for all traces
    for trace in fig.data:
        # Match each trace by the metric name and set text from summary_df
        metric = trace.name
        text_values = summary_df[summary_df['Matrix'] == metric]['Values'].astype(str)
        # Make sure to align the lengths
        if len(trace.y) == len(text_values):
            trace.text = text_values  # Set text as values from summary_df
            print(type(text_values))
        
        trace.textposition = 'outside'  # Set text position for all traces
        trace.textfont.size = 20  # Set font size for all traces        


    # Set y-axis range
    max_value = summary_melted['Value'].max()
    fig.update_yaxes(range=[0, max_value * 1.2])

    # Update trace names based on label_map
    fig.for_each_trace(lambda trace: trace.update(
        name=label_map.get(trace.name, trace.name),
        showlegend=True
    ))
    
    # Customize x-axis date formatting
    unique_dates = df_platform['Date'].dt.to_period('D').astype('str').unique()
    formatted_dates = [pd.to_datetime(date).strftime('%d %B') for date in unique_dates]

    fig.update_layout(
        xaxis=dict(
            tickvals=pd.to_datetime(unique_dates).to_pydatetime(),
            ticktext=formatted_dates,
            ticklabelposition="outside",
            title_standoff=10,
            ticks="outside",
            tickfont=dict(size=14),
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        bargap=0.4,
        bargroupgap=0.3,
   yaxis=dict(
        showgrid=False,  # Enable horizontal grid lines
        zeroline=False,
        showticklabels=False,
        gridcolor='rgba(255,255,255,0.1)',  # Set grid line color to a very translucent white
        gridwidth=1,  # Set the width of grid lines
    ),
    xaxis_title=None,
    yaxis_title=None,
)

    # Border and opacity settings
    fig.update_traces(marker=dict(
        line=dict(width=5, color='rgba(0,0,0,0)'),
        opacity=0.9
    ))

    # Legend settings
    fig.update_layout(
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": -0.5,
            "xanchor": "center",
            "x": 0.5,
            "font": {"color": "white", "size": 15},
        },
        legend_title_text="",
    )

    # Convert figure to HTML and return
    fig_html = fig.to_html(include_plotlyjs='cdn')
    return fig_html



def zeniva_overview(df):

    today_paid_installs = df[(df['Product'] == 'Zeniva') & (df['Matrix'] == 'today_paid_installs')]['Values'].values[0]
    todays_free_installs = df[(df['Product'] == 'Zeniva') & (df['Matrix'] == 'todays_free_installs')]['Values'].values[0] 
    lifetime_installs = df[(df['Product'] == 'Zeniva') & (df['Matrix'] == 'lifetime_installs')]['Values'].values[0] 
    today_paid_uninstalls = df[(df['Product'] == 'Zeniva') & (df['Matrix'] == 'today_paid_installs')]['Values'].values[0] 
    today_free_uninstalls = df[(df['Product'] == 'Zeniva') & (df['Matrix'] == 'today_free_uninstalls')]['Values'].values[0] 
    lifetime_uninstalls = df[(df['Product'] == 'Zeniva') & (df['Matrix'] == 'lifetime_uninstalls')]['Values'].values[0] 

    return today_paid_installs, todays_free_installs, lifetime_installs, today_paid_uninstalls, today_free_uninstalls, lifetime_uninstalls 




# Odyessey comparison overview part
def odyssey_overview(df):
    todays_forge_installs = df[(df['Product'] == 'odyssey') & (df['Matrix'] == 'todays_forge_installs')]['Values'].values[0] 
    todays_free_installs = df[(df['Product'] == 'odyssey') & (df['Matrix'] == 'todays_free_installs')]['Values'].values[0] 
    lifetime_installs = df[(df['Product'] == 'odyssey') & (df['Matrix'] == 'lifetime_installs')]['Values'].values[0] 
    todays_forge_uninstalls= df[(df['Product'] == 'odyssey') & (df['Matrix'] == 'todays_forge_uninstalls')]['Values'].values[0] 
    today_free_uninstalls = df[(df['Product'] == 'odyssey') & (df['Matrix'] == 'today_free_uninstalls')]['Values'].values[0] 
    lifetime_uninstalls = df[(df['Product'] == 'odyssey') & (df['Matrix'] == 'lifetime_uninstalls')]['Values'].values[0] 

    return todays_forge_installs, todays_free_installs, lifetime_installs, todays_forge_uninstalls, today_free_uninstalls, lifetime_uninstalls
