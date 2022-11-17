from src.utils.loggers import get_logger

logger = get_logger("main.py")


def output_10_pairs(df, page):
    step = 10
    if (page * step) + step <= len(df):
        page = page * step
        for i in range(page, len(df), step):
            result = df.iloc[i: i + step].to_dict('records')
            return result
    else:
        result = "THERE ARE ONLY : {} TRANSLATIONS PLEASE ENTER PAGE NUMBER FROM {} to {} ONLY".format(len(df), 0, (
                round(len(df) / step) - 1))
        return result
