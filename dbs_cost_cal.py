#coding:utf-8
# DBS 费用计算
# 合同折扣
DISCOUNT_FEE = 0.6
# 备份计划规格
backup_plan_specifications = {
    'micro': {
        'storage_unit': 'GB',
        'backup_100gb_cost_time': '20hour',
        'free_storage': 40,
        'basic_cost_per_mon': 30,
        'over_free_storage_cost_per_gb': 0.75,
        },
    'small': {
        'storage_unit': 'GB',
        'backup_100gb_cost_time': '5hour',
        'free_storage': 400,
        'basic_cost_per_mon': 140,
        'over_free_storage_cost_per_gb': 0.35,
        },
    'medium': {
        'storage_unit': 'GB',
        'backup_100gb_cost_time': '2.5hour',
        'free_storage': 800,
        'basic_cost_per_mon': 224,
        'over_free_storage_cost_per_gb': 0.25,
        },
    'large': {
        'storage_unit': 'GB',
        'backup_100gb_cost_time': '1.5hour',
        'free_storage': 1600,
        'basic_cost_per_mon': 359,
        'over_free_storage_cost_per_gb': 0.15,
        },
    'xlarge': {
        'storage_unit': 'GB',
        'backup_100gb_cost_time': '1hour',
        'free_storage': 10000000000,
        'basic_cost_per_mon': 900,
        'over_free_storage_cost_per_gb': 0,
        },
    }

# 费用计算公式
# 例如，A公司的数据库大小为150 GB，计划进行4次/月的全量备份，预计当月总备份量为600 GB（150 GB * 4）。A公司可以购买以下三种规格（以中国内地地域价格计算）：
#    micro（入门型）的费用 = 30元 + （600 GB - 40 GB）* 0.75元/GB = 450元
#    small（低配型）的费用 = 140元 + （600 GB - 400 GB）* 0.35元/GB = 210元
#    medium（中配型）的费用 = 224元（实际产生的数据量小于免费额度，无需额外收费）

current_backup_plan_specification = 'small'
plan_total_storage = 1232.01

for backup_plan_specification, backup_plan_specification_info  in backup_plan_specifications.items():
    basic_cost_per_mon = backup_plan_specification_info['basic_cost_per_mon']
    free_storage = backup_plan_specification_info['free_storage']
    over_free_storage_cost_per_gb = backup_plan_specification_info['over_free_storage_cost_per_gb']
    backup_100gb_cost_time = backup_plan_specification_info['backup_100gb_cost_time']

    if backup_plan_specification == 'xlarge':
        cost = basic_cost_per_mon * DISCOUNT_FEE
    else:
        cost = (basic_cost_per_mon + (plan_total_storage - free_storage) * over_free_storage_cost_per_gb) * DISCOUNT_FEE
    cost = round(cost, 2)

    if current_backup_plan_specification == backup_plan_specification:
        print(f"当前规格,{current_backup_plan_specification}：{cost}")
    else:
        print(f"{backup_plan_specification}：{cost}")





# 同样的数据量，用不同的备份计划规格，费用是怎样的