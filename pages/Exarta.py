import streamlit as st
import streamlit.components.v1 as components
import time
from functions import  all_data_for_stats, exarta_values_for_insights


st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

st.markdown(
    """
    <style>
      [data-testid="stSidebar"] {
        background-color: #272B34;
    }

  .st-emotion-cache-cxju6m {
    position: relative;
    top: 0px;
    background-color: #272B34;
    z-index: 999991;
    min-width: 244px;
    max-width: 337.5px;
    transform: none;
    transition: transform 300ms, min-width 300ms, max-width 300ms;
}
  svg[viewBox="0 0 24 24"] > path[d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12l4.58-4.59z"] {
        fill: white !important;
    }

    /* Select the right-pointing arrow SVG (sidebar closed) */
    svg[viewBox="0 0 24 24"] > path[d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6-6-6z"] {
        fill: transparent !important;
    }



    .st-emotion-cache-6tkfeg {
    color: white;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    display: table-cell;
}

    st-emotion-cache-onk2zl eczjsme18 {
    position: relative;
    user-select: auto;
    width: 176px;
    height: auto;
    box-sizing: border-box;
    flex-shrink: 0;
}


    .st-emotion-cache-onk2zl {
    position: relative;
    top: 0px;
    background-color: #272B34;
    z-index: 999991;
    min-width: 244px;
    max-width: 288px;
    transform: none;
    transition: transform 300ms, min-width 300ms, max-width 300ms;
}

    .st-emotion-cache-1f3w014 {
    vertical-align: middle;
    overflow: hidden;
    color: inherit;
    fill: currentcolor;
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    font-size: 1.5rem;
    width: 30px;
    height: 67px;
    flex-shrink: 0;
}


.st-emotion-cache-ocqkz7 {
    margin-left: 8px;
    margin-right: 116px;
    display: 10;
    /* -webkit-box-flex: 1; */
    /* flex-grow: 1; */
    /* -webkit-box-align: stretch; */
    /* align-items: stretch; */
    gap: 15px;
    flex-direction: row;
    flex-wrap: nowrap;
}

    .st-emotion-cache-1vt4y43 {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 2.5rem;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    user-select: none;
    background-color: #272B34;
    border: 1px solid rgba(49, 51, 63, 0.2);
}

    ._container_51w34_1,
    ._profileContainer_51w34_53 {
        display: none;
        visibility: hidden;
    }
  
   
   header {visibility: hidden;}       
   footer {visibility: hidden;}         
   .stApp > header {display: none;}   

    
    
    /* Ensure all content aligns properly in the dark background */
    .stApp {
        background-color: #191B21;
        color: white;
    }

     @media (max-width: 768px) {

         [data-testid="stIFrame"] {
    margin-top: -80px !important;
    border: 0 !important;
    overflow: hidden;
}
.st-emotion-cache-19u4bdk {
    position: fixed;
    top: 3.25rem;
    left: 2.5rem;
    z-index: 2;
    display: flex;
    -webkit-box-pack: center;
    justify-content: center;
    -webkit-box-align: start;
    align-items: start;
    transition: left 300ms;
}
     

    }
    </style>
    """,
    unsafe_allow_html=True
)


df_all_data = all_data_for_stats()

exarta_youtube, exarta_x, exarta_facebook, exarta_linkedin, exarta_instagram = exarta_values_for_insights(df_all_data)



Exarta_html_code = f"""
    <style>
     .header {{
        background-color: #20232A;
        padding: 20px;
        text-align: center;
        color: white;
    }}
    .main-container {{
   
    display: flex;
    flex-direction: column;
    gap: 20px;
    height: 100vh; /* Full height of the viewport */
    padding: 0px;
    box-sizing: border-box; /* Ensure padding does not increase height */
}}

.exartaLogo {{
          padding-left: 80%;
        width: 50px;
        height: 50px;
}}

.menulogo {{
          width: 30px;
    height: 24px;
}}

 .header-link {{
            display: none;
        }}

       .heading{{
       text-align: left;
        color: white;
        font-family: 'Roboto', sans-serif;
        font-size: 20px;
        font-style: normal;
        font-weight: 600;
        line-height: normal;
       }} 

 
.main-card {{
    background-color: #272B34;
    height: 260px;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    color: white;
    position: relative;
}} 

.image-container {{
    position: absolute;
    top: 20px; /* Adjust as needed */
    left: 20px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}

.image-container img {{
    width: 100px; /* Adjust as needed */
    height: auto;
}}


.image-containerx {{
    position: absolute;
    top: 23px; /* Adjust as needed */
    left: 20px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}

.image-containerx img {{
    width: 35px; /* Adjust as needed */
    height: 32px;
}}
    .card {{
        background-color: #343844;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        height: 170px;
    }}
    .paid-installs {{
        background-color: #A6B174;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }}
    .today-installs {{
        background-color: #F68C5B;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }}
    .today-paid-users {{
        background-color: #BC679C;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }}
    .row {{
        display: flex;
        justify-content: space-between;
    }}
    .column {{
        flex: 1;
        margin: 0 10px;
    }}
    .number-text {{
        color: #F0F0F0;
        font-family: Roboto;
        font-size: 48px;
        font-style: normal;
        font-weight: 800;
        line-height: normal;
    }}
    .card-text {{
        color: #F0F0F0;
        font-family: Roboto;
        font-size: 26.172px;
        font-style: normal;
        font-weight: 600;
        line-height: normal;
    }}
    .graph-container {{
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    .metric-container {{
            margin-top: 70px;
        }}
        .metric-row {{
            display: flex;
            justify-content: space-between;

            padding: 6px 0;
        }}
        .metric-row p {{
            margin: 0;
        }}
        .metric-line {{
            border-bottom: 1px solid rgba(209, 209, 209, 0.1); /* Correct property for creating a line */
            margin: 10px 0;
        }}
        .metric-left {{
            color: #F0F0F0;
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
            font-style: normal;
            font-weight: 300;
            line-height: normal;
            text-align: left;
        }}
        .metric-right {{
            color: white;
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
            font-style: normal;
            font-weight: 500;
            line-height: normal;
            text-align: right;
        }}
           
 
@keyframes grow {{
    from {{
        width: 0;
    }}
    to {{
        width: 100%; /* Grow to full width */
    }}
}}

 .image-containery {{
    position: absolute;
    top: 11px; /* Adjust as needed */
    left: 8px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}
 
.image-containery img {{
    width: 120px; /* Adjust as needed */
    height: 45px;
}}

.image-containeri {{
    position: absolute;
    top: 20px; /* Adjust as needed */
    left: 20px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}

.image-containeri img {{
    width: 105px; /* Adjust as needed */
    height: 37px;
}}

    </style>

        <head>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
        </head>


   
  <div class="header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
                      <img class="menulogo" src="https://i.ibb.co/G2zRtNb/Frame.png" alt="logo">
                        <img class="exartaLogo" src="https://i.ibb.co/0jT4xCS/Logo-2-1.png" alt="logo">
            <div> 
              <a href="#overview" class="header-link">Overview</a>
            <a href="#zeniva" class="header-link">Zeniva</a>
            <a href="#odyssey" class="header-link">Odyssey</a>
            <a href="#exarta" class="header-link">Exarta</a>
    
            </div>
        </div>
    </div>

</div>
    <h2 class="heading">Social Media</h2>
    <div class="main-container">
    <div class="main-card">
        <div class="image-containery">
            <img src="https://i.ibb.co/dc9nPSD/0109e9eb56d423e70f5960980428bd58.png" alt="logo">
        </div>
    <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower </p>
        <p class="metric-right">{int(exarta_youtube['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(exarta_youtube['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(exarta_youtube['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-containerx">
            <img src="https://i.ibb.co/F3NHfk7/9e4a770de98237a79973f9654303f292.png" alt="logo">
        </div>
<div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower </p>
        <p class="metric-right">{int(exarta_x['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(exarta_x['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(exarta_x['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-container">
            <img src="https://i.ibb.co/8dLDtzM/image-11.png" alt="logo">
        </div>
        <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower </p>
        <p class="metric-right">{int(exarta_facebook['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(exarta_facebook['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(exarta_facebook['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-container">
            <img src="https://i.ibb.co/YNMG5vr/1524028dffda5c43327cb4b962333b48.png" alt="logo">
        </div>
        <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower </p>
        <p class="metric-right">{int(exarta_linkedin['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(exarta_linkedin['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(exarta_linkedin['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-containeri">
            <img src="https://i.ibb.co/XFh4Bvy/insta.png" alt="logo">
        </div>
        <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower </p>
        <p class="metric-right">{int(exarta_instagram['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(exarta_instagram['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(exarta_instagram['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    
    </div>


</div>
"""
components.html(Exarta_html_code, height=1000, scrolling=True)
# time.sleep(60)
# st.switch_page("./main.py")
