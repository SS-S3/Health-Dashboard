import matplotlib.pyplot as plt
import seaborn as sns

class StravaDataVisualizer:
    @staticmethod
    def plot_activity_distance(df):
        
        #Create a bar plot of activity distances
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x='name', y='distance', data=df)
        plt.title('Recent Activity Distances')
        plt.xlabel('Activity Name')
        plt.ylabel('Distance (km)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('activity_distances.png')
        plt.close()

    @staticmethod
    def plot_activity_types(df):
        
        #Create a pie chart of activity types
        
        activity_counts = df['type'].value_counts()
        plt.figure(figsize=(8, 8))
        plt.pie(activity_counts, labels=activity_counts.index, autopct='%1.1f%%')
        plt.title('Activity Types')
        plt.axis('equal')
        plt.savefig('activity_types.png')
        plt.close()