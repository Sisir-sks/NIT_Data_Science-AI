import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

#Importing all the necessary libraries:seaborn-visualization,streamlit-frontend
st.title("Seaborn Data Visualization App")
sns.set_theme(style='whitegrid')
#Setting the theme of the visualization
#loading the dataset- tips
tips=sns.load_dataset('tips')
st.write("This is a sample dataset of tips given by customers in a restaurant")

def display_plot(title,plot_func):
    st.subheader(title)
    fig,ax=plt.subplots(figsize=(8,6))
    plot_func(ax)
    st.pyplot(fig)
    plt.close(fig)
    #Function to display the plot

def line_plot(ax):
    sns.lineplot(data=tips,x='total_bill',y='tip',marker='o',hue='sex',ax=ax)

    ax.set_title('Line Plot of Total Bill vs Tip')

def scatter_plot(ax):
    sns.scatterplot(tips,x='total_bill',y='tip',hue='time',size='size',palette='deep',ax=ax)
    ax.set_title('Scatter Plot of Total Bill vs Tip')

def bar_plot(ax):
    sns.barplot(data=tips,x='day',y='total_bill',hue='sex',palette='muted',ax=ax)
    ax.set_title('Bar Plot of Total Bill vs Day')

def box_plot(ax):
    sns.boxplot(data=tips,x='smoker',y='total_bill',hue='sex',palette='rocket',ax=ax)
    ax.set_title('Box Plot of Total Bill vs Smoker')

def violin_plot(ax):
    sns.violinplot(data=tips,x='day',y='total_bill',hue='time',split=True,palette='magma',ax=ax)
    ax.set_title('Violin Plot of Total Bill vs Day')

def count_plot(ax):
    sns.countplot(data=tips,x='day',hue='smoker',palette='dark',ax=ax)
    ax.set_title('Count Plot of Day vs Smoker')

def reg_plot(ax):
    sns.regplot(data=tips,x='total_bill',y='tip',scatter_kws={'s':50},line_kws={'color':'red'},ax=ax)
    ax.set_title('Regression Plot of Total Bill vs Tip')

def hist_plot(ax):
    sns.histplot(data=tips,x='total_bill',bins=20,kde=True,color='blue',ax=ax)
    ax.set_title('Histogram of Total Bill')

def pair_plot(ax):
    sns.pairplot(data=tips,hue='sex',vars=["total_bill","tip","size"],palette='husl',ax=ax)
    ax.set_title('Pair Plot of Total Bill, Tip and Size')

def cat_plot(ax):
    sns.catplot(tips,x='day',y='tip',hue='sex',palette='bright',kind='point',ax=ax)
    ax.set_title('Categorical Plot of Day vs Tip')


def joint_plot(ax):
    sns.jointplot(data=tips,x='total_bill',y='tip',kind='scatter',hue='smoker',palette='coolwarm',ax=ax)
    ax.set_title('Joint Plot of Total Bill vs Tip')

def facetgrid_plot(ax):
    sns.FacetGrid(tips,col='time',row='smoker',margin_titles=True).map(sns.histplot,'total_bill',bins=10,kde=True,ax=ax)
    ax.set_title('Facet Grid Plot of Total Bill')

def strip_plot(ax):
    sns.stripplot(tips,x='day',y='tip',hue='sex',jitter=True,palette='Set2',ax=ax)
    ax.set_title('Strip Plot of Day vs Tip')

def kde_plot(ax):
    sns.kdeplot(tips,x='total_bill',hue='sex',fill=True,palette='tab10',ax=ax)
    ax.set_title('KDE Plot of Total Bill')
# defined all the functions

plot_map = {
    'Line Plot': line_plot,
    'Scatter Plot': scatter_plot,
    'Bar Plot': bar_plot,
    'Box Plot': box_plot,
    'Violin Plot': violin_plot,
    'Count Plot': count_plot,
    'Regression Plot': reg_plot,
    'Histogram': hist_plot,
    'Strip Plot': strip_plot,
    'KDE Plot': kde_plot
}
# defined a dictionary to map plot names to their respective functions
select_plot=st.selectbox("Select a plot type",list(plot_map.keys()))
display_plot(select_plot,plot_map[select_plot])
