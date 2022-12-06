########## Run this code in your terminal to have it hosted on your browser!  In Terminal: 'streamlit run 04_streamlit_code.py' ##########
########## Also hosted live @ https://usa-food-insecurity.herokuapp.com// ##########

## Code for embedding into in tableau from https://towardsdatascience.com/embedding-tableau-in-streamlit-a9ce290b932b
## Base code from streamlit lesson

# Steamlit imports
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_icon='📖',
    initial_sidebar_state = 'expanded'
)

page = st.sidebar.selectbox(
    'Page',
    ('Feeding America Visualized', 'Predicting Food Insecurity', 'Food Insecurity Indicators')
)

if page == 'Feeding America Visualized':
    st.title('Feeding America Visualized')
    st.write('''
This website and applet are a representation of our group's data exploration into food insecurity in America. The group was Ira Seidman, Alec Edgecliffe-Johnson, Ryan McDonald, and Andrew Roberts for a project in our General Assembly data science bootcamp. In this and subsequent pages we portray food insecurity and several related socioeconomic variables at county and state levels for the USA. We also explain the features that have the largest predictive power in our machine learning models (the code for which can be found on the project's [GitHub](https://github.com/iraseidman/USA_Food_Insecurity_Analysis)).
    ''')

    st.write('''
In the final page of this web app we display our timeseries forecasts for food insecurity until 2026 which was developed with the univariate Prophet tool and multivariate VAR models, the code for both can be found on GitHub.
    ''')

    st.subheader('Food Insecurity by County in the USA (2019)')
    st.write('''
Below is a map of food insecurity in the US. We can observe greater food insecurity in southern counties, parts of Appalachia, and counties in close proximity to Native American reservations (zoom out for Alaska and Hawaii for all maps).
    ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616862765912' style='position: relative'><noscript><a href='#'><img alt='FI Dash ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica_16167866065860&#47;FIDash&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='FoodInsecurityInAmerica_16167866065860&#47;FIDash' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica_16167866065860&#47;FIDash&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div> <script type='text/javascript'>

var divElement = document.getElementById('viz1616862765912');
var vizElement = divElement.getElementsByTagName('object')[0]; 
vizElement.style.width='90%';
vizElement.style.height='587px';
var scriptElement = document.createElement('script');
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
vizElement.parentNode.insertBefore(scriptElement, vizElement); </script>"""
        components.html(html_temp, height = 600, width = 900)
        
    if __name__ == "__main__":
        main()

    st.subheader('Percent Below Poverty Line by County (2019)')
    st.write('''
Below is a map of percent below the poverty line by county in the USA. Similar trends can be observed as in the above food insecurity map. However, areas of extreme proverty appear less widespread than food insecure.''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616957234900' style='position: relative'><noscript><a href='#'><img alt='Pov Dash ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica_16167866065860&#47;PovDash&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='FoodInsecurityInAmerica_16167866065860&#47;PovDash' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica_16167866065860&#47;PovDash&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div> <script type='text/javascript'>

var divElement = document.getElementById('viz1616957234900');
var vizElement = divElement.getElementsByTagName('object')[0]; 
vizElement.style.width='90%';
vizElement.style.height='587px';
var scriptElement = document.createElement('script');
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
vizElement.parentNode.insertBefore(scriptElement, vizElement); </script>"""
        components.html(html_temp, height = 600, width = 900)

    if __name__ == "__main__":
        main()

    st.subheader('Food Insecurity Against Various Factors (General Rate and Child Rate - 2019)')
    st.write('''
Below are plots of food insecurity rate by county in the USA. These scatter plots indicate the general food insecurity rates (in blue) and child food insecurity rates (in orange). The plots show a trend of child based food insecurity increasing at a faster rate than that of general food insecurity.  The data shows children are most at higher risk than adults for the majority of factors included in our data, most notably percent uninsured, percent minority, percent in poverty, and percent rural (shown below).''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616889772153' style='position: relative'><noscript><a href='#'><img alt='Food Insecurity Rate (general and children) Against Various Factors ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurtiyvsVariousFactors&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='FoodInsecurtiyvsVariousFactors&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurtiyvsVariousFactors&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div> <script type='text/javascript'>
        
var divElement = document.getElementById('viz1616889772153');
var vizElement = divElement.getElementsByTagName('object')[0]
vizElement.style.width='90%';
vizElement.style.height='587px';
var scriptElement = document.createElement('script');
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
vizElement.parentNode.insertBefore(scriptElement, vizElement); </script>"""
        
        components.html(html_temp, height = 600, width = 900)

    if __name__ == "__main__":
        main()

elif page == 'Predicting Food Insecurity':
    st.title('Predicting Food Insecurity')
    st.subheader('Socioeconomic Predictors for Food Insecurity')
    st.write('''
Our production machine learning model, which employed over 50 features and captured 93.5% of the variability of the data, shows that with all else held equal a one-unit increase in each of these features would result in an increase in food insecurity of the amount indicated in the table below.''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616866672368' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;LR&#47;LRFeatureCoef&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='LRFeatureCoef&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;LR&#47;LRFeatureCoef&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div> <script type='text/javascript'>

var divElement = document.getElementById('viz1616866672368');
var vizElement = divElement.getElementsByTagName('object')[0];
vizElement.style.width='90%';
vizElement.style.height='587px';
var scriptElement = document.createElement('script');
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
vizElement.parentNode.insertBefore(scriptElement, vizElement); </script>"""
        components.html(html_temp, height = 600, width = 900)
        
    if __name__ == "__main__":
        main()

elif page == 'Food Insecurity Indicators':
    st.title('Food Insecurity Indicators')
    st.subheader('Socioeconomic Factors Associated with Food Insecurity')
    st.write('''
A variety of factors contribute to food insecurity in a given community. Factors such as income, employment, access to healthcare, and education are just a few factors that affect one's access to food. The below visualizations depict food insecurity vs. formal education for each state in the overlying map with median household income depicted in the bar graph underneath.
    ''')
        
    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616974092017' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;State_Based_FI_Rate&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='State_Based_FI_Rate&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;State_Based_FI_Rate&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div> <script type='text/javascript'>
        
var divElement = document.getElementById('viz1616974092017');
var vizElement = divElement.getElementsByTagName('object')[0];
vizElement.style.width='90%';vizElement.style.height='587px';
var scriptElement = document.createElement('script');
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement); </script>"""
        components.html(html_temp, height = 600, width = 900)
        
    if __name__ == "__main__":
        main()