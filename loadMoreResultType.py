from enum import Enum, unique

@unique
class load_more_result_type(Enum):
    more_result_loading = 1  # 正在加载更多内容，请稍候
    more_has_loaded = 2  # 新内容已成功加载。向下滚动即可查看更多内容。
    no_more = 3  # 看来您已经看完了所有内容
    cannot_load_more = 4  # 无法加载更多内容，点击即可重试
