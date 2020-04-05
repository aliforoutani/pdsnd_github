#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=['chicago','new york city','washington']
months=['all','january','february','march','april','may','june']
days=['all','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


# In[2]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
            city=input("Please choose your city 'new york city','chicago','washindton': ").lower()
            month_day=input('Would you like to filter by day, month, both or none? ')
            if month_day=='both':
                month=input("Please enter name of the month,'january, february, march, april, may, june': ").lower()
                day=input('Please enter the name of the day of the week: ').title()
            elif month_day=='month':
                month=input("Please enter name of the month,'january, february, march, april, may, june': ").lower()
                day='all'
            elif month_day=='day':
                day=input('Please enter the name of the day of the week: ').lower().title()
                month='all'
            else:
                month='all'
                day='all'
            if city not in cities:
                print('Invalid city name please try again!')
            elif month not in months:
                print('Invalid month name please try again!')
            elif day not in days:
                print('Invalid day name please try again!')
            else:
                break
                
    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


# In[3]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    if month!='all':
        month=months.index(month)
        df=df[df['month']==month]
    if day!='all':
        df=df[df['day_of_week']==day]
    df['hour']=df['Start Time'].dt.hour

    return df


# In[4]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month=months[df['month'].mode()[0]].title()
    print("\nMost common month of travel: {}".format(most_common_month))
    
    # display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print("\nMost common day of travel: {}".format(most_common_day))
    
    # display the most common start hour
    most_common_hour=df['hour'].mode()[0]
    print("\nMost common hour of travel: {}".format(most_common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[5]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print("\nMost commonly used start station: {}".format(most_common_start_station))
    
    # display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print("\nMost commonly used end station: {}".format(most_common_end_station))

    # display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+" to "+df['End Station']
    most_combination=df['combination'].mode()[0]
    print("\nMost frequent combination of start station and end station trip is: {} ".format(most_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('\nTotal time of the travel is : {} seconds'.format(total_travel_time))

    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('\nMean time of the travel is : {} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user=df['User Type'].value_counts()
    print('\nNumber of different user types are:\n{}'.format(counts_of_user))
    
    # Display counts of gender
    if 'Gender' not in df.columns:
        print('\nData not available')
    else:
        counts_of_gender=df['Gender'].value_counts()
        print('\nNumber of different genders are:\n{}'.format(counts_of_gender))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print('\nData not available')
    else:
        earliest_birthday=df['Birth Year'].min()
        print('\nThe earliest year of birth is: {}'.format(earliest_birthday))
        
        most_recent=df[df['Start Time']==df['Start Time'].min()]['Birth Year'].min()
        print('\nThe most recent year of birth: {}'.format(most_recent))
        
        most_common_birthday=df['Birth Year'].mode()[0]
        print('\nThe most common year of birth is: {}'.format(most_common_birthday))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[23]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

    data_table=input('\nWould you like to see the raw data? Enter yes or no.')
    if data_table.lower() =='yes':
        while True:
            print(df.head())
            more_data=input('\nWould you like to see more? Enter yes or no.\n')
            if more_data.lower() !='yes':
                break
            df=df.drop(df.head().index,axis=0)
            
            
        


# In[22]:


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:




