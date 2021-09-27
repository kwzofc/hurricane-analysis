# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille',
         'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September',
          'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977,
         1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
                       175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], [
    'Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M',
           'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
          2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# write your update damages function here:


def updating_damages(damages):
    damages_value = []

    for damage in damages:
        if "M" in damage:
            damages_value.append(float(damage[:-1])*1000000)
        elif "B" in damage:
            damages_value.append(float(damage[:-1])*1000000000)
        else:
            damages_value.append('Damages not recorded')

    return damages_value


updating_damages = updating_damages(damages)

print("Update damages function\n")
print(updating_damages)
print("------------------------------\n")

# write your construct hurricane dictionary function here:


def create_record(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    table = {}

    for i in range(len(names)):
        if names[i] in table.keys():
            table[names[i]].update({
                'Name': names[i],
                'Month': months[i],
                'Year': years[i],
                'Max Sustained Wind': max_sustained_winds[i],
                'Areas Affected': areas_affected[i],
                'Damage': damages[i],
                'Death': deaths[i]
            })
        else:
            table[names[i]] = {
                'Name': names[i],
                'Month': months[i],
                'Year': years[i],
                'Max Sustained Wind': max_sustained_winds[i],
                'Areas Affected': areas_affected[i],
                'Damage': damages[i],
                'Death': deaths[i]
            }

    return table


hurricanes_record_by_name = create_record(
    names,
    months,
    years,
    max_sustained_winds,
    areas_affected,
    damages,
    deaths
)
print("Construct hurricane dictionary function\n")
print(hurricanes_record_by_name)
print("------------------------------\n")

# write your construct hurricane by year dictionary function here:


def create_record_by_year(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    table = {}

    for i in range(len(names)):
        if years[i] in table.keys():
            table[years[i]].append({
                'Name': names[i],
                'Month': months[i],
                'Year': years[i],
                'Max Sustained Wind': max_sustained_winds[i],
                'Areas Affected': areas_affected[i],
                'Damage': damages[i],
                'Death': deaths[i]
            })
        else:
            table[years[i]] = [{
                'Name': names[i],
                'Month': months[i],
                'Year': years[i],
                'Max Sustained Wind': max_sustained_winds[i],
                'Areas Affected': areas_affected[i],
                'Damage': damages[i],
                'Death': deaths[i]
            }]

    return table


hurricanes_record_by_year = create_record_by_year(
    names,
    months,
    years,
    max_sustained_winds,
    areas_affected,
    damages,
    deaths
)
print("Construct hurricane by year dictionary function\n")
print(f"{hurricanes_record_by_year[1932]}")
print("------------------------------\n")

# write your count affected areas function here:


def count_affected_area(records):
    count_affected_area = {}

    for record in records:
        count_affected_area[record] = len(records[record]['Areas Affected'])

    return count_affected_area


count_affected_area = count_affected_area(hurricanes_record_by_name)
print("Count affected areas function\n")
print(count_affected_area)
print("------------------------------\n")

# write your find most affected area function here:


def most_area_affected(records):
    area_affected_counts = {}

    for record in records.values():
        for area in record['Areas Affected']:
            if area in area_affected_counts.keys():
                area_affected_counts[area] += 1
            else:
                area_affected_counts[area] = 1

    return f"{max(area_affected_counts, key=area_affected_counts.get)}: {area_affected_counts[max(area_affected_counts, key=area_affected_counts.get)]}"


max_affected_areas = most_area_affected(hurricanes_record_by_name)
print("Find most affected area function\n")
print(max_affected_areas)
print("------------------------------\n")

# write your greatest number of deaths function here:


def deadliest_hurricane(records):
    deadliest_hurricane = {}

    for record in records.values():
        deadliest_hurricane[record['Name']] = record['Death']

    return f"{max(deadliest_hurricane, key=deadliest_hurricane.get)}: {deadliest_hurricane[max(deadliest_hurricane, key=deadliest_hurricane.get)]}"


deadliest_hurricane = deadliest_hurricane(hurricanes_record_by_name)
print("Greatest number of deaths function\n")
print(deadliest_hurricane)
print("------------------------------\n")

# write your categorize by mortality function here:


mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}


def rates_hurricanes_by_deaths(records, scales):
    rate_hurricanes = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }

    for record in records.values():
        if record['Death'] == scales[0]:
            rate_hurricanes[0].append(record)
        elif record['Death'] > scales[0] and record['Death'] <= scales[1]:
            rate_hurricanes[1].append(record)
        elif record['Death'] > scales[1] and record['Death'] <= scales[2]:
            rate_hurricanes[2].append(record)
        elif record['Death'] > scales[2] and record['Death'] <= scales[3]:
            rate_hurricanes[3].append(record)
        elif record['Death'] > scales[3] and record['Death'] <= scales[4]:
            rate_hurricanes[4].append(record)
        else:
            rate_hurricanes[5].append(record)

    return rate_hurricanes


rates_hurricanes_by_deaths = rates_hurricanes_by_deaths(
    hurricanes_record_by_name, mortality_scale)
print("Categorize by mortality function\n")
print(rates_hurricanes_by_deaths)
print("------------------------------\n")

# write your greatest damage function here:


def max_hurricane_damage(records, damages):
    hurricanes_damage = {}
    index = 0

    for record in records.values():
        if isinstance(damages[index], float):
            hurricanes_damage[record['Name']] = damages[index]
        index += 1

    return hurricanes_damage


max_hurricane_damage = max_hurricane_damage(
    hurricanes_record_by_name, updating_damages)
print("Greatest damage function\n")
print(
    f"\n{max(max_hurricane_damage, key=max_hurricane_damage.get)}: {max_hurricane_damage[max(max_hurricane_damage, key=max_hurricane_damage.get)]}")
print("------------------------------\n")

# write your categorize by damage function here:


damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000
                }


def rates_hurricanes_by_damage(records, damages, scales):
    rates_hurricanes_damage = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }
    index = 0

    for record in records.values():
        if damages[index] == scales[0] or not isinstance(damages[index], float):
            rates_hurricanes_damage[0].append(record)
        elif damages[index] > scales[0] and damages[index] <= scales[1]:
            rates_hurricanes_damage[1].append(record)
        elif damages[index] > scales[1] and damages[index] <= scales[2]:
            rates_hurricanes_damage[2].append(record)
        elif damages[index] > scales[2] and damages[index] <= scales[3]:
            rates_hurricanes_damage[3].append(record)
        elif damages[index] > scales[3] and damages[index] <= scales[4]:
            rates_hurricanes_damage[4].append(record)
        else:
            rates_hurricanes_damage[5].append(record)
        index += 1

    return rates_hurricanes_damage


damage_severity_rates = rates_hurricanes_by_damage(
    hurricanes_record_by_name,
    updating_damages,
    damage_scale
)
print("Categorize by damage function\n")
print(damage_severity_rates)
print("------------------------------\n")
