import pandas as pd
import numpy as np

class StravaDataProcessor:
    @staticmethod
    def process_activities(activities):
       
        processed_activities = []
        for activity in activities:
            processed_activity = {
                'name': activity.get('name', 'Unnamed Activity'),
                'type': activity.get('type', 'Unknown'),
                'distance': round(activity.get('distance', 0) / 1000, 2),  # Convert to kilometers
                'moving_time': activity.get('moving_time', 0),
                'total_elevation_gain': round(activity.get('total_elevation_gain', 0), 2),
                'average_speed': round(activity.get('average_speed', 0) * 3.6, 2),  # Convert to km/h
                'max_speed': round(activity.get('max_speed', 0) * 3.6, 2),
                'calories': activity.get('calories', 0),
                'date': activity.get('start_date_local', '')
            }
            processed_activities.append(processed_activity)
        
        return pd.DataFrame(processed_activities)

    @staticmethod
    def generate_activity_summary(df):
        
        return {
            'total_activities': len(df),
            'total_distance': round(df['distance'].sum(), 2),
            'average_distance': round(df['distance'].mean(), 2),
            'total_calories_burned': round(df['calories'].sum(), 2),
            'most_frequent_activity': df['type'].mode()[0]
        }