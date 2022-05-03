# 常量
_CURRENT_YEAR = 2022
_CHOSEN_BUILT_AREA_MIN = 40
_CHOSEN_BUILT_AREA_MAX = 60
# 权重
_ARCH_AREA_WEIGHT = 0.2
_FLOOR_WEIGHT = 0.2
_HAS_ELEVATOR_WEIGHT = 0.2
_BUILT_YEAR_WEIGHT = 0.2
_COMMUNITY_INDEX_WEIGHT = 0.2


# 计算自如房源综合得分
def calculate_synthesis(arch_area_text, floor_text, has_elevator_text, built_year_text, community_index_text):
    # 清洗数据源
    # 建筑面积
    if not is_number(arch_area_text):
        temp_list = list(filter(lambda ch: ch in '0123456789.', arch_area_text))
        arch_area_text = ''.join(temp_list)
    arch_area = float(arch_area_text)

    # 所属楼层
    current_floor = int(floor_text.split('/')[0])

    # 总楼层
    total_floor = int(floor_text.split('/')[1])

    # 有无电梯
    if has_elevator_text == '有':
        has_elevator = True
    else:
        has_elevator = False

    # 建造年份
    if not is_number(built_year_text):
        temp_list = filter(lambda ch: ch in '0123456789', built_year_text)
        built_year_text = ''.join(temp_list)
    built_year = int(built_year_text)

    # 自如小区指数
    community_index = float(community_index_text)

    # print('%s %s %s %s %s %s' %(arch_area, current_floor, total_floor, has_elevator, built_year, community_index))

    # 建筑面积得分
    arch_area_score = (arch_area - _CHOSEN_BUILT_AREA_MIN) / (_CHOSEN_BUILT_AREA_MAX - _CHOSEN_BUILT_AREA_MIN) * 100

    # 楼层得分
    floor_score = 60
    if total_floor > 7:
        floor_score += 20
        if current_floor == 1:
            floor_score -= 20
    else:
        if current_floor == 1:
            floor_score -= 60
        elif current_floor == total_floor:
            floor_score -= 40

    # 有无电梯得分
    if has_elevator:
        has_elevator_score = 100
    else:
        has_elevator_score = 50

    # 建造年份得分
    if (_CURRENT_YEAR - built_year) > 20:
        built_year_score = 40
    elif (_CURRENT_YEAR - built_year) > 15:
        built_year_score = 50
    elif (_CURRENT_YEAR - built_year) > 10:
        built_year_score = 60
    elif (_CURRENT_YEAR - built_year) > 5:
        built_year_score = 80
    else:
        built_year_score = 100

    # 自如小区指数得分
    community_index_score = community_index * 10

    # 计算加权平均综合得分
    synthesis = arch_area_score * _ARCH_AREA_WEIGHT \
                + floor_score * _FLOOR_WEIGHT \
                + has_elevator_score * _HAS_ELEVATOR_WEIGHT \
                + built_year_score * _BUILT_YEAR_WEIGHT \
                + community_index_score * _COMMUNITY_INDEX_WEIGHT

    return synthesis


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 测试脚本
if __name__ == '__main__':
    print(calculate_synthesis('45㎡', '2/6', '无', '1994年建成', '5.6'))
