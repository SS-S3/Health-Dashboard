import os
from dotenv import load_dotenv
from strava_api_config import StravaAPIClient
from data_processor import StravaDataProcessor
from visualization_module import StravaDataVisualizer

def main():
    # Load Strava API Client
    strava_client = StravaAPIClient()

    # Authentication Flow (Note: This would typically be done through a web interface)
    print("To authenticate:")
    authorization_url, state = strava_client.get_authorization_url()
    print(f"1. Please visit this URL to authorize the application: {authorization_url}")
    print("2. After authorization, you'll be redirected with a code.")
    authorization_code = input("3. Enter the full redirect URL you received: ")

    # Exchange token
    token = strava_client.exchange_token(authorization_code)
    access_token = token['access_token']

    try:
        # Fetch activities
        activities = strava_client.get_athlete_activities(access_token)

        # Process activities
        activities_df = StravaDataProcessor.process_activities(activities)
        activity_summary = StravaDataProcessor.generate_activity_summary(activities_df)

        # Generate visualizations
        StravaDataVisualizer.plot_activity_distance(activities_df)
        StravaDataVisualizer.plot_activity_types(activities_df)

        # Display results
        print("\n--- Strava Activity Summary ---")
        for key, value in activity_summary.items():
            print(f"{key.replace('_', ' ').title()}: {value}")

        print("\nVisualizations saved: activity_distances.png, activity_types.png")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()