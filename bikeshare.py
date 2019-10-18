import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
Months = ['january', 'february', 'march', 'april', 'may', 'june','all']
Days = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday","all"]
def get_filters():###
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for Chicago, New York, or Washington? \n")
    while city.lower() not in CITY_DATA:
        print("You may have misspell the name or this city does not exist, please try again!", end='')
        city = input("invalid input of city. please try agian: ")
        if city.lower() in CITY_DATA:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input("Which month - January, February, March, April, May, or June or all?\n")
    while month.lower() not in Months:
        print("You may have misspell the name or this month does not exist, please try again!", end='')
        month = input("invalid input of month. please try agian: ")
        if month.lower() in Months:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input("Which day - sunday, monday, tuesday, wednesday, thursday, riday, or saturday or all?\n")
    while day.lower() not in Days:
        print("You may have misspell the name or this day does not exist, please try again!", end='')
        day = input("invalid input of Day. please try agian: ")
        if day.lower() in Days:
            break
    print('-'*60)
    return city.lower(), month.lower(), day.lower()

def load_data(city, month, day):###
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    if month == 'all' and day == 'all':
        df = df
    elif month != 'all' and day == 'all':
        month_index = Months.index(month)
        df = df.loc[pd.to_datetime(df['Start Time']).dt.month==month_index]
    elif month != 'all' and day != 'all':
        month_index = Months.index(month)
        day_index = Days.index(day) - 1
        df = df.loc[(pd.to_datetime(df['Start Time']).dt.month==month_index) & (pd.to_datetime(df['Start Time']).dt.dayofweek==day_index)]
    return df

def time_stats(df):
    while True:
        Show = input('\nWould you like to show about time stats yes or no.\n')
        if Show.lower() != 'yes':
            break
        else:
            """Displays statistics on the most frequent times of travel."""

            print('\nCalculating The Most Frequent Times of Travel...\n')
            start_time = time.time()
            #convert the Start Time column to datetime
            common_month = pd.to_datetime(df['Start Time']).dt.month
            most_common_month = common_month.mode()[0]
            print('\n Most common month of travel : ' + str(most_common_month))

            #To Do : display the most common day of week
            common_dayofweek = pd.to_datetime(df['Start Time']).dt.dayofweek
            most_common_dayofweek = common_dayofweek.mode()[0]
            print('\n Most common Day of travel : ' + str(most_common_dayofweek))

            #To Do : display the most common start hour
            common_hour = pd.to_datetime(df['Start Time']).dt.hour
            most_common_hour = common_hour.mode()[0]
            print('\n Most common Hour of travel : ' + str(most_common_hour))
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*60)
            break

def station_stats(df):
    while True:
        Show = input('\nWould you like to show about station stats yes or no.\n')
        if Show.lower() != 'yes':
            break
        else:
            """Displays statistics on the most popular stations and trip."""

            print('\nCalculating The Most Popular Stations and Trip...\n')
            start_time = time.time()

            # TO DO: display most commonly used start station
            most_common_start_station = (df['Start Station'].mode()[0])
            print('Most common start station:' + str(most_common_start_station))
            # TO DO: display most commonly used end station
            most_common_end_station = (df['End Station'].mode()[0])
            print('Most common End station:' + str(most_common_end_station))
            # TO DO: display most frequent combination of start station and end station trip
            common_combination_station = df['Start Station'] + df['End Station']
            most_common_combination_station = common_combination_station.mode()[0]
            print('Most common combination of Start and End station:' + str(most_common_combination_station))
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break

def trip_duration_stats(df):###
    while True:
        Show = input('\nWould you like to show about trip duration stats yes or no.\n')
        if Show.lower() != 'yes':
            break
        else:
            """Displays statistics on the total and average trip duration."""

            print('\nCalculating Trip Duration...\n')
            start_time = time.time()

            # TO DO: display total travel time
            Total_travel_time = (df['Trip Duration']).sum()
            print('Total Travel time: '+ str(Total_travel_time) + 's')
            # TO DO: display mean travel time
            Mean_travel_time = (df['Trip Duration']).mean()
            print('Mean Travel time: '+ str(Mean_travel_time) + 's')
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break

def user_stats(df): ###
    while True:
        Show = input('\nWould you like to show about user stats yes or no.\n')
        if Show.lower() != 'yes':
            break
        else:
            """Displays statistics on bikeshare users."""

            print('\nCalculating User Stats...\n')
            start_time = time.time()

            # TO DO: Display counts of user types
            count_of_user_type = (df['User Type'].value_counts())
            print('\ncount of each user type\n' + str(count_of_user_type))


            # TO DO: Display counts of gender
            if 'Gender' in df.columns:
                count_of_gender = (df['Gender'].value_counts())
                print('\ncount of gender of each user type\n' + str(count_of_gender))
            else:
                print('No gender for Selected file')
            # TO DO: Display earliest, most recent, and most common year of birth
            if 'Birth Year' in df.columns:
                earliest_birth_year = (df['Birth Year'].min())
                print('\nnoldest persons birth year: ' + str(earliest_birth_year))
                most_recent_birth_year = (df['Birth Year'].max())
                print('\nnyoungest persons birth year: ' + str(most_recent_birth_year))
                most_common_birth_year = (df['Birth Year'].min())
                print('\nnoldest persons birth year: ' + str(most_common_birth_year))
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break

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


if __name__ == "__main__":
	main()
