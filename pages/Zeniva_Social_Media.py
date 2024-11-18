import streamlit as st
import streamlit.components.v1 as components
import time
from functions import zeniva_values_for_insights, all_data_for_stats
from pages import Zeniva_Campaigns,Zeniva_Social_Media

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

# Inject custom CSS to target the entire page background
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color:#272B34;
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
    margin-right: 130px;
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

zeniva_youtube, zeniva_x, zeniva_tiktok, zeniva_linkedin, zeniva_instagram, zeniva_facebook = zeniva_values_for_insights(all_data_for_stats())

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
    padding-left: 100px;
    width: 100px;
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
    <h2 class="mobileHeading">Zeniva</h2> 

</div>
"""
 
components.html(html_code, height=140)
# st.markdown(
#     """
#     <style>

#     .st-emotion-cache-1vt4y43:active {
#     border-color: transparent;
#     color: white;
#     background-color: transparent;
# }

#     .button {
#     margin-top: 11px;
#     font-size: 16px;
#     padding: 9px 21px;
#     border-radius: 8px;
#     border: none;
#     cursor: pointer;
#     color: #272B34;
#     margin: 5px;
# }

#     /* Default button style */
#     .default-button {
#         background-color: #272B34;
#     }

#     /* Active button style for the current page */
#     .active-button {
#     border-radius: 8px;
#     height: 42px;
#     width: 129px;
#     margin-top: 0px;
#     background-color: #F68C5B;
#     margin-left: -19px;
#     box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
# }

    
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# if 'current_page' not in st.session_state:
#     st.session_state.current_page = "Zeniva_Social_Media"

# # Function to navigate to the other page
# def navigate_to(page):
#     st.session_state.current_page = page
#     st.experimental_rerun()

# # Page Header


# # Create two buttons side by side in a single row
# col1, col2 = st.columns(2)

# # Button to navigate to the second page
# with col1:
#     if st.session_state.current_page == "Zeniva_Campaigns":
#         button_style = "active-button"
#     else:
#         button_style = "default-button"
#     if st.button("Paid Campaigns", key="navigate_to_second"):
#         st.switch_page("pages/Zeniva_Campaigns.py")
        
# # Button for "Social Media"
# with col2:
#     if st.session_state.current_page == "Zeniva_Social_Media":
#         button_style = "active-button"
#     else:
#         button_style = "default-button"
    
#     # Render the button with the appropriate style
#     st.markdown(f'<button class="button {button_style}">Social Media</button>', unsafe_allow_html=True)

# st.markdown("---")

st.markdown(
    """
    <style>
    .button {
    margin-top: 11px;
    font-size: 16px;
    padding: 5px 21px;
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
    width: 150px;
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

# Initialize session state if not already set
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Zeniva_Campaigns"

# Function to navigate to the other page
def navigate_to(page):
    st.session_state.current_page = page
    st.experimental_rerun()

# Create two buttons side by side in a single row
col1, col2 = st.columns(2)

# Button for "Paid Campaigns" (Active on this page)
with col1:
    if st.session_state.current_page == "Zeniva_Campaigns":
        button_style = "active-button"
    else:
        button_style = "default-button"
    st.markdown(f'<button class="button {button_style}">Social Media</button>', unsafe_allow_html=True)

# Button for "Social Media" (Navigates to Zeniva_Social_Media)
with col2:
    if st.session_state.current_page == "Zeniva_Social_Media":
        button_style = "active-button"
    else:
        button_style = "default-button"
    if st.button("Paid campaigns", key="navigate_to_first"):
        st.switch_page("pages/Zeniva_Campaigns.py")

st.markdown("---")


html_code_metrics = f"""
    <style>

     @media (min-width: 1024px) {{
    
    .main-container {{
    display: grid;
    grid-template-columns: repeat(3,1fr);
     gap: 20px;
     margin-top: 50px;
 
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
                margin-top: -8px;
    }}
    .main-container {{
   
           display: flex;
        flex-direction: column;
        gap: 20px;
        height: 100vh;
        padding: 0px;
        box-sizing: border-box;
        margin-top: 25px;
}}

.exartaLogo {{
    padding-left: 5px;
    width: 50px;
    height: 50px;
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
    width: 100px; /* Adjust as needed */
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
 
 
        .progress-container {{
            display:none;
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


    </style>

    <div class="main-container">
    <div class="main-card">
        <div class="image-containery">
            <img src="https://i.ibb.co/dc9nPSD/0109e9eb56d423e70f5960980428bd58.png" alt="logo">
        </div>
       <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower </p>
        <p class="metric-right">{int(zeniva_youtube['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(zeniva_youtube['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(zeniva_youtube['total_followers'].iloc[0])}</p>
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
        <p class="metric-right">{int(zeniva_x['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(zeniva_x['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(zeniva_x['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
     <div class="main-card">
        <div class="image-containert">
            <img src="https://i.ibb.co/S0fVvSL/fc9958aff216c7090428e6fa1fa03889.png" alt="logo">
        </div>
        <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower </p>
        <p class="metric-right">{int(zeniva_tiktok['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(zeniva_tiktok['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(zeniva_tiktok['total_followers'].iloc[0])}</p>
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
        <p class="metric-right">{int(zeniva_linkedin['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(zeniva_linkedin['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(zeniva_linkedin['total_followers'].iloc[0])}</p>
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
        <p class="metric-right">{int(zeniva_instagram['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(zeniva_instagram['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(zeniva_instagram['total_followers'].iloc[0])}</p>
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
        <p class="metric-right">{int(zeniva_facebook['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(zeniva_facebook['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(zeniva_facebook['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
   
   
</div>
"""
 
components.html(html_code_metrics, height=900, scrolling=True)


