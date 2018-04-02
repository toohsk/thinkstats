import survey

table = survey.Pregnancies()
table.ReadRecords()
print('妊娠レコードの総数:', len(table.records))

# Filter outcome value by 1, because live birth is given as 1
# From document there are 9148 cases of live birth
outcomes = [rec for rec in table.records if rec.outcome == 1]
print('出生児レコードの総数:', len(outcomes))

# Separeate lived birth child as first birth and after second.
first_birth = []
after_second = []
for rec in outcomes:
    if rec.birthord == 1:
        first_birth.append(rec)
    else:
        after_second.append(rec)
print('第一子のレコードの総数:', len(first_birth))
print('第二子以降のレコードの総数:', len(after_second))


# Compare gestation period between first birth and after second.
def mean_gestation_period(records):
    summary = 0

    for rec in records:
        summary += rec.prglength
    return summary / float(len(records))


mean_of_first = mean_gestation_period(first_birth)
mean_of_after_second = mean_gestation_period(after_second)\

print("第一子の妊娠期間の平均:", mean_of_first)
print("第二子以降の妊娠期間の平均:", mean_of_after_second)
print("妊娠期間の平均の差:", (mean_of_first - mean_of_after_second))
