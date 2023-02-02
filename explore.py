import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats

region_order = ['BSh',
 'BSk',
 'BWh',
 'BWk',
 'Cfa',
 'Cfb',
 'Csa',
 'Csb',
 'Dfa',
 'Dfb',
 'Dfc',
 'Dsb',
 'Dsc',
 'Dwa',
 'Dwb']

region_palette = {'BSh':'#c88817',
 'Cfa':'#007701',
 'BSk':'#cca955',
 'BWk':'#f7f867',
 'BWh':'#fdcc02',
 'Csa':'#97f909',
 'Csb':'#144a28',
 'Cfb':'#085807',
 'Dfb':'#820084',
 'Dsc':'#b9bbb8',
 'Dfc':'#c807c8',
 'Dfa':'#540055',
 'Dsb':'#888888',
 'Dwa':'#6729b8',
 'Dwb':'#b66bf6'}


def data_distribution(df):
    #set font size
    sns.set(font_scale=1.5)

    fig, ax = plt.subplots(figsize=(20, 8))
    sns.histplot(data=df, x='mean_temp')
    plt.xlabel('Mean Temp for Next 14 days')
    plt.title('Distribution of our Target Variable');
    
def region_viz(df):
    #set font size
    sns.set(font_scale=1.5)

    fig, ax = plt.subplots(1, 2, figsize=(20, 8))

    sns.countplot(x='region', data=df, ax=ax[0], palette=region_palette, order=region_order)
    ax[0].set_title('Distribution of Regions')
    ax[0].set_xlabel('Köppen-Geiger climate classifications')

    sns.barplot(x='region', y='mean_temp', data=df, ax=ax[1], palette=region_palette, order=region_order)
    rate = df['mean_temp'].mean()
    ax[1].set_title('Average Temperature by Region')
    ax[1].axhline(rate,  label = f'Average temp across all regions {rate:.2f}°C', linestyle='dotted', color='black')
    ax[1].set_xlabel('Köppen-Geiger climate classifications')
    ax[1].set_ylabel('Temperature(°C)')
    ax[1].legend()
    plt.show()
    

def elevation_bin_viz(df):
    fig, ax = plt.subplots(1, 1, figsize=(20, 10))

    sns.barplot(x='elevation_range', y='mean_temp', data=df, palette='Blues')
    rate = df['mean_temp'].mean()
    ax.set_title('Is there a relationship between elevation range and temperature?')
    ax.axhline(rate,  label = f'Average Temp Across All Elevations {rate:.2f}°C', linestyle='dotted', color='black')
    ax.set_xticklabels(['Bottom Low\n0-500','Top Low\n560-900','Mid\n1000-1700','High\n1800-3100'])
    ax.set_xlabel('')
    ax.set_ylabel('Temperature (°C)')
    ax.legend()
    plt.show()
    
    
def elevation_bin_kruskal_test(df):
    bl = df[df.elevation_range == 'bottom_low']
    tl = df[df.elevation_range == 'top_low']
    mid = df[df.elevation_range == 'mid']
    h = df[df.elevation_range == 'high']

    corr, p = stats.kruskal(bl.mean_temp, tl.mean_temp, mid.mean_temp, h.mean_temp)
    
    print(f'p-value: {p}')


def elevation_bin_dist_viz(df):
    sns.set_style('white')
    bl = df[df.elevation_range == 'bottom_low']
    tl = df[df.elevation_range == 'top_low']
    mid = df[df.elevation_range == 'mid']
    h = df[df.elevation_range == 'high']

    fig, ax = plt.subplots(1, 4, figsize=(20, 8))

    fig.suptitle('Distribution of Observations by Elevation Bin')

    sns.histplot(x='mean_temp', data= bl, ax=ax[0], color='#d4e1ee')
    ax[0].set_title('Bottom Low')
    ax[0].set_ylim(0,2000)
    ax[0].set_xlim(-20,40)
    ax[0].set_ylabel('')
    ax[0].set_xlabel('Temperature (°C)')

    sns.histplot(x='mean_temp', data= tl, ax=ax[1], color = '#9dc2d5')
    ax[1].set_title('Top Low')
    ax[1].set_ylim(0,2000)
    ax[1].set_xlim(-20,40)
    ax[1].set_ylabel('')
    ax[1].set_xlabel('Temperature (°C)')

    sns.histplot(x='mean_temp', data= mid, ax=ax[2], color='#5a94b9')
    ax[2].set_title('Mid')
    ax[2].set_ylim(0,2000)
    ax[2].set_xlim(-20,40)
    ax[2].set_ylabel('')
    ax[2].set_xlabel('Temperature (°C)')

    sns.histplot(x='mean_temp', data= h, ax=ax[3], color='#296399')
    ax[3].set_title('High')
    ax[3].set_ylim(0,2000)
    ax[3].set_xlim(-20,40)
    ax[3].set_ylabel('')
    ax[3].set_xlabel('Temperature (°C)')

    plt.show()
    
    
def precipitation_viz(df):
    fig, ax = plt.subplots(1, 1, figsize=(20, 8))

    #sns.histplot(data=df, x ='precip', ax=ax[0])
    #ax[0].set_title('Distribution of Precipitation')

    sns.regplot(x='mean_temp', y='precip', data=df, line_kws={'color': 'red'})
    ax.set_title('Is there a correlation between temperature and precipitation?')
    rate = df['precip'].mean()
    ax.axhline(rate,  label = f'Overall Mean Precipitation: {rate:.2f}mm', linestyle='dotted', color='black')
    ax.set_ylabel('Precipitation (mm)')
    ax.set_xlabel('Temperature (°C)')
    ax.legend()
    plt.show()
    
def precip_spearmanr_test(df):
    corr, p = stats.spearmanr(df['precip'], df['mean_temp'])
    print(f'p-value: {p}')

    
def potential_evap_viz(df):
    fig, ax = plt.subplots(1, 1, figsize=(20, 8))

    #sns.histplot(data=df, x ='potential_evap', ax=ax[0])
    #ax[0].set_title('Distribution of Potential Evaporation')

    sns.regplot(x='mean_temp', y='potential_evap', data=df, line_kws={'color': 'red'})
    ax.set_title('Is there a correlation between temperature and potential evaporation?')
    rate = df['potential_evap'].mean()
    ax.axhline(rate,  label = f'Overall Mean Potential Evaporation: {rate:.2f}mL', linestyle='dotted', color='black')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Potential Evaporation (mL)')
    ax.legend()
    ax.set_ylim(-50,1200)
    plt.show()
    
def potential_evap_spearmanr_test(df):
    corr, p = stats.spearmanr(df['potential_evap'], df['mean_temp'])
    print(f'p-value: {p}')
    
def geopotential_viz(df):
    fig, ax = plt.subplots(2, 2, figsize=(20, 20))

    fig.suptitle('Is there a correlation between temperature and geopotential pressure at different heights?')

    sns.regplot(x='height_10_mb', y='mean_temp',  data= df, ax=ax[0][0],line_kws={'color': 'red'})
    ax[0][0].set_title('At 10 Milibars')
    ax[0][0].set_xlabel('Meters above mean sea level')
    ax[0][0].set_ylabel('Temperature (°C)')

    sns.regplot(x='height_100_mb', y='mean_temp',  data= df, ax=ax[0][1],line_kws={'color': 'red'})
    ax[0][1].set_title('At 100 Milibars')
    ax[0][1].set_xlabel('Meters above mean sea level')
    ax[0][1].set_ylabel('Temperature (°C)')

    sns.regplot(x='height_500_mb', y='mean_temp',  data= df, ax=ax[1][0],line_kws={'color': 'red'})
    ax[1][0].set_title('At 500 Milibars')
    ax[1][0].set_xlabel('Meters above mean sea level')
    ax[1][0].set_ylabel('Temperature (°C)')

    sns.regplot(x='height_850_mb', y='mean_temp',  data= df, ax=ax[1][1],line_kws={'color': 'red'})
    ax[1][1].set_title('At 850 Milibars')
    ax[1][1].set_xlabel('Meters above mean sea level')
    ax[1][1].set_ylabel('Temperature (°C)')


    plt.show()