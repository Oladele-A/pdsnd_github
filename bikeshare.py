import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please enter the city you want to explore. \n').lower()
    while city not in CITY_DATA:
        city = input('Please enter the city you want to explore.\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please enter a month of the year or all to get data for all months. \n').lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december','all']
    while month not in months:
        month = input('Please enter a valid month. \n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter a day of the week or all to get data for all days \n').lower()
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    while day not in days:
        day = input('Please enter a valid day you want to filter by.\n').lower()

    print('-'*40)
    print('done')
    return city, month, day


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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december','all']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    print('done')
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    m = df['month'].mode()[0]
    print(f'The most common month is: {m}')

    # TO DO: display the most common day of week
    d = df['day_of_week'].mode()[0]
    print('the most common day of week is:{}'.format(d))

    # TO DO: display the most common start hour
    h = df['hour'].mode()[0]
    print(f'the most common start hour is: {h}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('done')


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    st = df['Start Station'].mode()[0]
    print(f'most commonly used start station is: {st}')

    # TO DO: display most commonly used end station
    end = df['End Station'].mode()[0]
    print(f'most commonly used end station is: {end}')

    # TO DO: display most frequent combination of start station and end station trip
    combo = df['Start Station'] + ' --> ' + df['End Station']
    combo = combo.mode()[0]
    print(f'most frequent combination of start station and end station trip is: {combo}' )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('done')


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print(f'total travel time is: {total}sec')

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print(f'mean travel time is: {mean}sec')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('done')


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f'counts of the user types: \n {user_type}')

    # TO DO: Display counts of gender
    if 'Gender'in df.columns:
        gender = df['Gender'].value_counts()
        print(f'counts of the user gender: \n {gender}')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        early = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        print(f'earliest, most recent, and most common year of birth are : {early} , {recent} , {common}')
    else: print(' \n Chicago dataset does not have Gender nor Birth year data yet!.' )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('done')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        #Ask the user whether they would like to see the raw data
        enter = ['yes','no']
        user_input = input('Would you like to see more data? (Enter:Yes/No).\n')

        while user_input.lower() not in enter:
            user_input = input('Please Enter Yes or No:\n')
            user_input = user_input.lower()
        n = 0
        while True :
            if user_input.lower() == 'yes':
                print(df.iloc[n : n + 5])
                n += 5
                user_input = input('\nWould you like to see more data? (Type:Yes/No).\n')
                while user_input.lower() not in enter:
                    user_input = input('Please Enter Yes or No:\n')
                    user_input = user_input.lower()
            else:
                break

        restart = input('\nWould you like to restart? (Enter:Yes/No).\n')
        #check wheather the user is entering the valid entry or not
        while restart.lower() not in enter:
            restart = input('Please Enter Yes or No:\n')
            restart = restart.lower()
        if restart.lower() != 'yes':
            print('BYE!')
            break


if __name__ == "__main__":
	main()
