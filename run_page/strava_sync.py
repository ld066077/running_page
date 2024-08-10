import argparse
import json

from config import JSON_FILE, SQL_FILE, get_activity_title  # 导入获取活动标题的函数
from generator import Generator

# for only run type, we use the same logic as garmin_sync
def run_strava_sync(client_id, client_secret, refresh_token, only_run=False):
    generator = Generator(SQL_FILE)
    generator.set_strava_config(client_id, client_secret, refresh_token)
    generator.only_run = only_run
    generator.sync(False)

    activities_list = generator.load()

    # 更新活动标题
    for activity in activities_list:
        activity['name'] = get_activity_title(activity)

    with open(JSON_FILE, "w") as f:
        json.dump(activities_list, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("client_id", help="strava client id")
    parser.add_argument("client_secret", help="strava client secret")
    parser.add_argument("refresh_token", help="strava refresh token")
    parser.add_argument(
        "--only-run",
        dest="only_run",
        action="store_true",
        help="if is only for running",
    )
    options = parser.parse_args()
    run_strava_sync(
        options.client_id,
        options.client_secret,
        options.refresh_token,
        only_run=options.only_run,
    )
