import json
from datetime import datetime

class SimpleLeaderboard:
    def __init__(self, file_path='leaderboard.json'):
        self.file_path = file_path
        self.records = self.load_records()

    def load_records(self):
        try:
            with open(self.file_path, 'r') as file:
                records = json.load(file)
            return records
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'Error loading leaderboard: {e}')
            print('Leaderboard will be initialized with empty records.')
            return []

    def save_records(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.records, file, indent=4)

    def add_record(self, user, score):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_record = {'user': user, 'score': score, 'time': timestamp}
        self.records.append(new_record)
        self.records = sorted(self.records, key=lambda x: x['score'], reverse=True)
        self.save_records()

    def fetch_records(self, n):
        return self.records[:n]


if __name__ == '__main__':

    # Example usage
    leaderboard = SimpleLeaderboard()

    # Add records
    leaderboard.add_record('Player1', 150)
    leaderboard.add_record('Player2', 200)
    leaderboard.add_record('Player3', 180)

    # Get top N records from the leaderboard
    top_records = leaderboard.fetch_records(n = 3)

    # Print leaderboard with headers
    print("User".ljust(15), "Score".ljust(10), "Time".ljust(20))
    print("-" * 45)
    for record in top_records:
        print(record['user'].ljust(15), str(record['score']).ljust(10), record['time'].ljust(20))
