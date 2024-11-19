import streamlit as st
import streamlit.components.v1 as components
import time
from functions import zeniva_overview, odyssey_overview, df_for_comp
import pandas as pd


st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

hideTopBar = True

# Inject custom CSS to target the entire page background
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #272B34;
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
    margin-top: -38px;
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

df_for_comparisons = df_for_comp()
 
today_paid_installs_for_zin, todays_free_installs_zin, lifetime_installs_zin, today_paid_uninstalls_zin, today_free_uninstalls_zin, lifetime_uninstalls_zin= zeniva_overview(df_for_comparisons)

todays_forge_installs_for_odyssey, todays_free_installs_for_odyssey, lifetime_installs_for_odyssey, todays_forge_uninstalls_for_odyssey, today_free_uninstalls_for_odyssey, lifetime_uninstalls_for_odyssey = odyssey_overview(df_for_comparisons) 

html_code = f"""
    <style>

     @media (min-width: 1024px) {{
    .header {{
        background-color: #20232A;
        padding: 20px;
        text-align: center;
        color: white;
    }}
    .main-container {{
    display: grid;
    grid-template-columns: repeat(3,1fr);
     gap: 20px;
 
}}

 .exartaLogo {{
  padding-left: 178px;
        width: 50px;
        height: 50px;
}}
.menulogo {{
          width: 30px;
    height: 24px;
}}

 .header-link {{
        margin-right: 20px;
        padding-right: 100px;
        color: #F0F0F0;
        font-family: 'Roboto', sans-serif;
        font-size: 25px;
        font-style: normal;
        font-weight: 300;
        line-height: normal;
        text-decoration: none;
    }}
    
    /* Additional link hover styles can be added if necessary */
    .header-link:hover {{
        text-decoration: underline;
    }}

     .heading {{
        text-align: left;
        color: white;
        font-family: 'Roboto', sans-serif;
        font-size: 30px;
        font-style: normal;
        font-weight: 600;
        line-height: normal;
    }}

    .mobileHeading{{
        display: none;
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
 
.image-containert {{
    position: absolute;
    top: 10px; /* Adjust as needed */
    left: 11px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}
 
.image-containert img {{
    width: 100px; /* Adjust as needed */
    height: 50px;
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
            margin-top: 100px;
        }}
        .metric-row {{
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
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
 
 
        .progress-container {{
    width: 100%; /* Full width relative to the parent container */
    max-width: 1800px; /* Maximum width to ensure it doesn't exceed 1800px */
    height: 10px;
    background-color: #323743; /* Background color of the entire container */
    border-radius: 0px; /* No rounding for the container edges */
    overflow: hidden; /* Ensures that the progress bar stays within the container */
    margin: 0 auto; /* Center the progress container */
}}
 
.progress-bar {{
    width: 0; /* Initial width of the progress bar */
    height: 100%; /* Full height of the container */
    background: #495161; /* Progress bar color */
    border-radius: 5px;
    animation: grow 60s linear forwards; /* Animation: grow over 10 seconds */
}}
 
@keyframes grow {{
    from {{
        width: 0;
    }}
    to {{
        width: 100%; /* Grow to full width */
    }}
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
     }}

 @media (max-width: 768px)  {{
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
    padding: 20px;
    box-sizing: border-box; /* Ensure padding does not increase height */
}}

.exartaLogo {{
                  padding-left: 75%;
        width: 44px;
        height: 23px;
}}

 .header-link {{
            display: none;
        }}

        .mobileHeading {{
        text-align: left;
        color: white;
        font-family: 'Roboto', sans-serif;
        font-size: 20px;
        font-style: normal;
        font-weight: 600;
        line-height: normal;
    }}

    .heading {{
        display:none;
    }}

 }}

    </style>
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
    
     <div class="progress-container">
    <div class="progress-bar"></div>
</div>

   <h2 class="heading">Social Media</h2>
    <h2 class="mobileHeading">Overview</h2> 

</div>
"""
 
components.html(html_code, height=140)
st.markdown(
    """
    <style>
    .button {
    margin-top: 11px;
    font-size: 16px;
    padding: 5px 31px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    color: #272B34;
    margin: 5px;
}

    /* Default button style */
    .default-button {
        background-color: #F68C5B;
        color: black;
    }

    /* Active button style for the current page */
    .active-button {
    background-color: #F68C5B;
    color: white;
    border-radius: 8px;
    height: 36px;
   width: 109px;
    margin-top: 2px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

    .button:hover {
        opacity: 0.9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if 'current_page' not in st.session_state:
    st.session_state.current_page = "Zeniva_Overview"

# Function to navigate to the other page
def navigate_to(page):
    st.session_state.current_page = page
    st.experimental_rerun()

# Page Header


# Create two buttons side by side in a single row
col1, col2 = st.columns(2)

# Button to navigate to the second page
with col1:
    if st.session_state.current_page == "Odyssey_Overview":
        button_style = "active-button"
    else:
        button_style = "default-button"
    if st.button("Odyssey3D", key="navigate_to_second"):
        st.switch_page("pages/Odyssey_Overview.py")
        
# Button for "Social Media"
with col2:
    if st.session_state.current_page == "Zeniva_Overview":
        button_style = "active-button"
    else:
        button_style = "default-button"
    
    # Render the button with the appropriate style
    st.markdown(f'<button class="button {button_style}">Zeniva</button>', unsafe_allow_html=True)

st.markdown("---")

html_code = f"""
    <style>     

@media (max-width: 768px) {{ 
  
.zeniva-card {{
    background-color: transparent;
    border-radius: 10px;
    text-align: center;
    color: white;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
            margin-top: 22px;
}}

.odyssey-card {{
   display: none;
}}
 
 
.image-container {{
    display: none;
}}
 
.image-containerx {{
    position: absolute;
    top: 20px; /* Adjust as needed */
    left: 20px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}
 
.image-containerx img {{
    width: 100px; /* Adjust as needed */
    height: 29px;
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
   
   
     .graph-container {{
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
 
    .metric-container {{
            margin-top: 100px;
        }}
        .metric-row {{
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
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
 
 
.firstrowcards {{
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-bottom: 4px
}}
 
.secondrowcards {{
         display: flex;
        gap: 10px;
        margin-top: 5px;
        flex-direction: column;
}}
 
.card {{
    background-color: #444B57;
     height: 70px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        border-radius: 5px;
        padding: 10px;
}}
.card1 {{
          background-color: #A6B174;
        height: 70px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        border-radius: 5px;
        padding: 10px;
}}
.card2 {{
          background-color:#F68C5B; 
        height: 70px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        border-radius: 5px;
        padding: 10px;
}}
.card3 {{
           background-color:#BC679C  ;
        height: 70px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        border-radius: 5px;
        padding: 10px;
}}
 
 
.card-number {{
           font-size: 45px;
        font-weight: 900;
        color: white;
        margin-top: 35px;
        margin-bottom: 0px;
        margin-top: 1px;
    
}}
 
.card-text {{
 
font-family: Roboto;
        font-size: 13px;
        /* font-style: normal; */
        /* font-weight: 600; */
        line-height: normal;
        margin-top: 0px;
}}
 
.progress-container {{
  display: flex;
}}
 
@keyframes grow {{
    from {{
        width: 0;
    }}
    to {{
        width: 100%; /* Grow to full width */
    }}
}}
 }}

 
  

    </style>
 
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
        </head>
 
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
        </head>
 

     <div class="main-container">
    <div class="zeniva-card">
        <div class="image-container">
            <img src="https://i.ibb.co/3WLkjzJ/7bdf715624ed952d97ee1983147bfc6e.png" alt="logo">
        </div>
 
         <div class="firstrowcards">
         <div class="card1">
        <p class="card-number">{int(today_paid_installs_for_zin)}</p>
        <p class="card-text">Today's Paid Installs</p>
    </div>
    <div class="card2">
        <p class="card-number">{int(todays_free_installs_zin)}</p>
        <p class="card-text">Today's Free Installs</p>
    </div>
    <div class="card3">
        <p class="card-number">{int(lifetime_installs_zin)}</p>
        <p class="card-text">Total Installs</p>
    </div>
    </div>
  <div class="secondrowcards">
    <div class="card">
        <p class="card-number">{int(today_paid_uninstalls_zin)}</p>
        <p class="card-text">Today's Paid Uninstalls</p>
    </div>
    <div class="card">
        <p class="card-number">{int(today_free_uninstalls_zin)}</p>
        <p class="card-text">Today's Free Uninstalls</p>
    </div>
    <div class="card">
        <p class="card-number">{int(lifetime_uninstalls_zin)}</p>
        <p class="card-text">Total Uninstalls</p>
    </div>
</div>
   
    </div>
    <div class="odyssey-card">
        <div class="image-containerx">
            <img src="https://i.ibb.co/sqWcC9d/becbd639884fea2ce7449a6c2aabe320.png" alt="logo">
        </div>
 
 <div class="firstrowcards">
        <div class="card1">
        <p class="card-number">{int(todays_forge_installs_for_odyssey)}</p>
        <p class="card-text">Today's Forge Installs</p>
    </div>
    <div class="card2">
        <p class="card-number">{int(todays_free_installs_for_odyssey)}</p>
        <p class="card-text">Today's Free Installs</p>
    </div>
    <div class="card3">
        <p class="card-number">{int(lifetime_installs_for_odyssey)}</p>
        <p class="card-text">Total Installs</p>
    </div>
    </div>
     <div class="secondrowcards">
    <div class="card">
        <p class="card-number">{int(todays_forge_uninstalls_for_odyssey)}</p>
        <p class="card-text">Today's Forge Uninstalls</p>
    </div>
    <div class="card">
        <p class="card-number">{int(today_free_uninstalls_for_odyssey)}</p>
        <p class="card-text">Today's Free Uninstalls</p>
    </div>
    <div class="card">
        <p class="card-number">{int(lifetime_uninstalls_for_odyssey)}</p>
        <p class="card-text">Total Uninstalls</p>
    </div>
</div>
</div>


</div>
"""
 

components.html(html_code, height=610)
# time.sleep(60)
# st.switch_page("pages/Zeniva_Social_Media.py")