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
    city = input('please select one city from chicago, new york city, washington : ').lower()
    while city not in (CITY_DATA.keys()):
        print ('please select valid city name ')
        city = input('please select one city from chicago, new york city, washington : ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    inputs = input ('would you filter by specific month or day or all ? ').lower()
    months = ['january','february','march','april','may','june']
    month = input ('select month from the first half of the year ').lower()
    if inputs == 'month':
        
        while month not in months :
            print ('please select a valid month name')
            month = input ('select month from the first half of the year ').lower()
    else :
        inputs == "all"
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    day = input('select day ').lower()
    if inputs == 'day':
        
        while day not in days:
            print("please enter a valid day name")
            day = input('select day ').lower()
    else :
        inputs == 'all'


    print('-'*40)
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
    #load data of the city
    df = pd.read_csv(CITY_DATA[city])
    #convert the column of start hour to date time 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #create month column from start hour column
    df['month'] = (df['Start Time'].dt.month_name()).str.lower()
    #create day of weak column from start hour column
    df['day_of_week'] = (df['Start Time'].dt.day_name()).str.lower()
    #filter by month
    if month != 'all' :
        
        df=df[df['month'] == month]
    #filter by day
    if day != 'all' :
        df= df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df['month'].mode()[0]
    print('the most common month is :{}'.format(month))

    # TO DO: display the most common day of week
    day = df['day_of_week'].mode()[0]
    print ('the most common day is :{}'.format(day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour = df['hour'].mode()[0]
    print ('the most common hour is : {}'.format(hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('the most common start station is : {}'.format(start_station))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('the most common end station is : {}'.format(end_station))


    # TO DO: display most frequent combination of start station and end station trip
    from_to_trip = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    print('the most frequent trip is : {}'.format(from_to_trip.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print ('total travel time in seconds is {} and in hours is {} '.format(total_travel_time, total_travel_time/3600))

    # TO DO: display mean travel time
    average_travel_time=df['Trip Duration'].mean()
    print ('average travel time in seconds is {} and in hours is {} '.format(average_travel_time, average_travel_time/3600))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df :
        print('the count of gender is {}'.format(df['Gender'].value_counts()))


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year'  in df :
       
        earliest_year=int(df['Birth Year'].min())
        print('\n earliest year is {}.'.format(earliest_year))
        recent_year = int(df['Birth Year'].max())
        print('\n most recent year is {}'.format(recent_year))
        common_year=int(df['Birth Year'].mode()[0])
        print('\n most common year is {} '.format(common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_date(df) :

    """ ask user if he want to display five rows and continue in asking 
    until you stop . """
    i = 0
    answer = input('would you like to display the first five rows of data ? ')
    
    while True:
        
        if answer == 'yes' :
            
            print(df.iloc[i:i+5])
            answer = input('would you like to display the next five rows of data ? ')
            i += 5
        elif answer == 'no' :
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_date(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
