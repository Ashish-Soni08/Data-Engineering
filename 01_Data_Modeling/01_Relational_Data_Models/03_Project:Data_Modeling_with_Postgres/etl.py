import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    - Extracts the data from each song file in song_data for song_table and artist_table  
    - Transforms the data
    - Loads the right data into song_table and artist_table respectively
    
    Args:
        cur : connection(to the database) to get a cursor that will be used to execute queries.
        filepath (str): The location of the file to read
    
    Yields:
        Inserts data into the table
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_cols = ["song_id", "title", "artist_id", "year", "duration"]
    song_data = df[song_cols].values.tolist()
    song_data = [single_list for nested_list in song_data for single_list in nested_list]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_cols = ["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"]
    artist_data = df[artist_cols].values.tolist()
    artist_data = [single_list for nested_list in artist_data for single_list in nested_list]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    - Extracts the data from each log file in log_data  
    - Transforms the data
    - Loads the right data into time, users and songplays table respectively
    
    Args:
        cur : connection(to the database) to get a cursor that will be used to execute queries.
        filepath (str): The location of the file to read
    
    Yields:
        Inserts data into the table
    
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df.loc[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = df['ts']
    t = pd.to_datetime(t, unit='ms')
    
    # insert time data records
    time_data = [df['ts'], t.dt.day, t.dt.weekday, t.dt.month, t.dt.year, t.dt.weekofyear, t.dt.hour]
    column_labels = ['ts', 'day', 'day_of_week', 'month', 'year', 'week_of_year', 'hour']
    time_dict = dict(zip(column_labels, time_data))
    time_df = pd.DataFrame.from_dict(time_dict)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_cols = ['userId', 'firstName', 'lastName', 'gender', 'level']
    user_df = df[user_cols]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """ Process data 
    Args:
        cur : connection to get a cursor that will be used to execute queries.
        conn: connection to the database
        filepath (str): The location of the file to read
        func: function to use, to process the data
    
    Yields:
        Inserts data into the table
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='00_data/01_song_data', func=process_song_file)
    process_data(cur, conn, filepath='00_data/02_log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()