import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats


def data_distribution(df):
    #set font size
    sns.set(font_scale=1.5)

    fig, ax = plt.subplots(figsize=(20, 8))
    sns.histplot(data=df, x='mean_temp')
    plt.xlabel('Mean Temp for Next 14 days')
    plt.title('Distribution of our Target Variable');
    
def region_viz(df):
    fig, ax = plt.subplots(1, 2, figsize=(20, 8))

    fig.suptitle('Is there a relationship between climate region and the mean temperature?')
    
    sns.countplot(x='region', data=df, ax=ax[0])
    ax[0].set_title('Distribution of Regions')

    sns.barplot(x='region', y='mean_temp', data=df, ax=ax[1])
    rate = df['mean_temp'].mean()
    ax[1].set_title('Mean temp across regions')
    ax[1].axhline(rate,  label = f'Average Temp Across All Regions {rate:.2f}', linestyle='dotted', color='black')
    ax[1].legend()
    plt.show()

def region_stats_test(df):
    dry = df[df.region_bins == 'Dry']
    temp = df[df.region_bins == 'Temperate']
    cont = df[df.region_bins == 'Continental']
    
    corr, p = stats.kruskal(dry.mean_temp, temp.mean_temp, cont.mean_temp)
    
    print(f'p-value: {p}')
    

def elevation_bin_viz(df):
    fig, ax = plt.subplots(1, 2, figsize=(20, 8))

    fig.suptitle('Is there a relationship between elevation_range and the mean temperature?')
    
    sns.countplot(x='elevation_range', data=df, ax=ax[0])
    ax[0].set_title('Distribution of Elevation')

    sns.barplot(x='elevation_range', y='mean_temp', data=df, ax=ax[1])
    rate = df['mean_temp'].mean()
    ax[1].set_title('Mean temp across elevation bins')
    ax[1].axhline(rate,  label = f'Average Temp Across All Elevations {rate:.2f}', linestyle='dotted', color='black')
    ax[1].legend()
    plt.show()
    
    
def elevation_bin_kruskal_test(df):
    bl = df[df.elevation_range == 'bottom_low']
    tl = df[df.elevation_range == 'top_low']
    mid = df[df.elevation_range == 'mid']
    h = df[df.elevation_range == 'high']

    corr, p = stats.kruskal(bl.mean_temp, tl.mean_temp, mid.mean_temp, h.mean_temp)
    
    print(f'p-value: {p}')


def elevation_bin_dist_viz(df):
    bl = df[df.elevation_range == 'bottom_low']
    tl = df[df.elevation_range == 'top_low']
    mid = df[df.elevation_range == 'mid']
    h = df[df.elevation_range == 'high']
    
    fig, ax = plt.subplots(1, 4, figsize=(20, 8))

    fig.suptitle('Distribution of Observations by Elevation Bin')

    sns.histplot(x='mean_temp', data= bl, ax=ax[0])
    ax[0].set_title('Bottom Low')
    ax[0].set_ylim(0,2000)
    ax[0].set_xlim(-20,40)
    ax[0].set_ylabel('')

    sns.histplot(x='mean_temp', data= tl, ax=ax[1])
    ax[1].set_title('Top Low')
    ax[1].set_ylim(0,2000)
    ax[1].set_xlim(-20,40)
    ax[1].set_ylabel('')

    sns.histplot(x='mean_temp', data= mid, ax=ax[2])
    ax[2].set_title('Mid')
    ax[2].set_ylim(0,2000)
    ax[2].set_xlim(-20,40)
    ax[2].set_ylabel('')

    sns.histplot(x='mean_temp', data= h, ax=ax[3])
    ax[3].set_title('High')
    ax[3].set_ylim(0,2000)
    ax[3].set_xlim(-20,40)
    ax[3].set_ylabel('')

    plt.show()
    
    
def precipitation_viz(df):
    fig, ax = plt.subplots(1, 2, figsize=(20, 8))

    sns.histplot(data=df, x ='precip', ax=ax[0])
    ax[0].set_title('Distribution of Precipitation')

    sns.regplot(x='mean_temp', y='precip', data=df, line_kws={'color': 'red'}, ax=ax[1])
    ax[1].set_title('Is there a correlation between mean temp and precipitation?')
    rate = df['precip'].mean()
    ax[1].axhline(rate,  label = f'Overall Mean Precipitation: {rate:.2f}', linestyle='dotted', color='black')
    ax[1].legend()
    plt.show()
    
def precip_spearmanr_test(df):
    corr, p = stats.spearmanr(df['precip'], df['mean_temp'])
    print(f'p-value: {p}')

    
def potential_evap_viz(df):
    fig, ax = plt.subplots(1, 2, figsize=(20, 8))

    sns.histplot(data=df, x ='potential_evap', ax=ax[0])
    ax[0].set_title('Distribution of Potential Evaporation')

    sns.regplot(x='mean_temp', y='potential_evap', data=df, line_kws={'color': 'red'}, ax=ax[1])
    ax[1].set_title('Is there a correlation between mean temp and potential evaporation?')
    rate = df['potential_evap'].mean()
    ax[1].axhline(rate,  label = f'Overall Mean Potential Evaporation: {rate:.2f}', linestyle='dotted', color='black')
    ax[1].legend()
    ax[1].set_ylim(-50,1200)
    plt.show()
    
def potential_evap_spearmanr_test(df):
    corr, p = stats.spearmanr(df['potential_evap'], df['mean_temp'])
    print(f'p-value: {p}')
    
def geopotential_viz(df):
    rows = df.sample(frac =.01)
    
    fig, ax = plt.subplots(2, 2, figsize=(20, 20))

    fig.suptitle('Is there a correlation between mean temp and geopotential pressure at different heights?')

    sns.scatterplot(x='height_10_mb', y='mean_temp', hue='region_bins', data= rows, ax=ax[0][0])
    ax[0][0].set_title('At 10 Milibars')
    ax[0][0].legend()

    sns.scatterplot(x='height_100_mb', y='mean_temp', hue='region_bins', data= rows, ax=ax[0][1])
    ax[0][1].set_title('At 100 Milibars')
    ax[0][1].legend()

    sns.scatterplot(x='height_500_mb', y='mean_temp', hue='region_bins', data= rows, ax=ax[1][0])
    ax[1][0].set_title('At 500 Milibars')
    ax[1][0].legend()

    sns.scatterplot(x='height_850_mb', y='mean_temp', hue='region_bins', data= rows, ax=ax[1][1])
    ax[1][1].set_title('At 850 Milibars')
    ax[1][1].legend()

    plt.show()