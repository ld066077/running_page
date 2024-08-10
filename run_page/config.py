import os
from collections import namedtuple
import yaml

# getting content root directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)

OUTPUT_DIR = os.path.join(parent, "activities")
GPX_FOLDER = os.path.join(parent, "GPX_OUT")
TCX_FOLDER = os.path.join(parent, "TCX_OUT")
FIT_FOLDER = os.path.join(parent, "FIT_OUT")
ENDOMONDO_FILE_DIR = os.path.join(parent, "Workouts")
FOLDER_DICT = {
    "gpx": GPX_FOLDER,
    "tcx": TCX_FOLDER,
    "fit": FIT_FOLDER,
}
SQL_FILE = os.path.join(parent, "run_page", "data.db")
JSON_FILE = os.path.join(parent, "src", "static", "activities.json")
SYNCED_FILE = os.path.join(parent, "imported.json")
SYNCED_ACTIVITY_FILE = os.path.join(parent, "synced_activity.json")

# TODO: Move into nike_sync NRC THINGS


BASE_TIMEZONE = "Asia/Shanghai"


start_point = namedtuple("start_point", "lat lon")
run_map = namedtuple("polyline", "summary_polyline")

try:
    with open("config.yaml") as f:
        _config = yaml.safe_load(f)
except:
    _config = {}


def config(*keys):
    def safeget(dct, *keys):
        for key in keys:
            try:
                dct = dct[key]
            except KeyError:
                return None
        return dct

    return safeget(_config, *keys)


# add more type here
STRAVA_GARMIN_TYPE_DICT = {
    "Hike": "hiking",
    "Run": "running",
    "EBikeRide": "cycling",
    "Walk": "walking",
    "Swim": "swimming",
}
# 新增函数：获取活动标题
def get_activity_title(activity):
    """
    获取活动标题，优先使用Strava标题，若不存在则使用默认标题
    :param activity: 活动字典对象，包含 Strava 标题和活动类型
    :return: 活动标题
    """
    # 检查Strava标题是否存在
    strava_title = activity.get('name')
    if strava_title:
        return strava_title
    
    # 如果Strava标题不存在，根据活动类型返回默认标题
    activity_type = activity.get('type')
    default_title = STRAVA_GARMIN_TYPE_DICT.get(activity_type, "Unknown Activity")
    
    return default_title