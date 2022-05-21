# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

# conversion = {"M": 1000000,
#              "B": 1000000000}

def update_damages(values):
    num_damages = []
    
    for item in values:
        if 'M' in item:
            num_damages.append(float(item.strip('M'))*1000000)
        elif 'B' in item:
            num_damages.append(float(item.strip('B'))*1000000000)
        else:
            num_damages.append(item)
    
    return num_damages
    
numeric_damages = update_damages(damages)
print(numeric_damages)

# write your construct hurricane dictionary function here:

def hurricane_dict(*lst):
    data_set = []
    
    for i in range(len(lst[0])):
        data_set.append({"Name": lst[0][i],
        "Month": lst[1][i],
        "Year": lst[2][i],
        "Max Sustained Winds": lst[3][i],
        "Areas Affected": lst[4][i],
        "Damage": lst[5][i],
        "Death": lst[6][i]
        })
    
    hurricane_data = {lst[0][i]: data_set[i] for i in range(len(lst[0]))}
    
    return hurricane_data
    
hurricane_database = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, numeric_damages, deaths)
print(hurricane_database)

# write your construct hurricane by year dictionary function here:

def by_year(data):
    hurricane_by_year = {}
    
    for hurricane in data.values():
        year = hurricane.get('Year')
        if year not in hurricane_by_year.keys():
            hurricane_by_year.update({year: [hurricane]})
        if year in hurricane_by_year.keys():
            hurricane_by_year[year].append(hurricane)
    
    return hurricane_by_year

hurricane_data_by_year = by_year(hurricane_database)
print(hurricane_data_by_year)

# write your count affected areas function here:

def area_count(areas):
    counted_areas = {}
    
    for area_set in areas:
        for area in area_set:
            if area not in counted_areas.keys():
                counted_areas[area] = 1
            if area in counted_areas.keys():
                counted_areas[area] += 1
    
    return counted_areas

most_affected_areas = area_count(areas_affected)
print(most_affected_areas)

# write your find most affected area function here:

def most_affected(area_dict):
    greatest_count = 0
    area_affected = ""
    
    for area, count in area_dict.items():
        if count > greatest_count:
            greatest_count = count
        if area_dict.get(area) == greatest_count:
            area_affected = area
            
    most_affected_area = "{AREA} is the area most affected by hurricanes, being hit {COUNT} times.".format(AREA=area_affected, COUNT=str(greatest_count))
            
    return most_affected_area

worst_hit = most_affected(most_affected_areas)
print(worst_hit)

# write your greatest number of deaths function here:

def greatest_deaths(hurr_dict):
    max_death = 0
    max_name = ""
    
    for info in hurr_dict.values():
        if info['Death'] > max_death:
            max_death = info['Death']
            max_name = info['Name']
    
    most_deaths = "The most deadly hurricane was {NAME} responsible for {DEATH} deaths".format(NAME=max_name, DEATH=max_death)
    return most_deaths
    
deadliest_hurricane = greatest_deaths(hurricane_database)
print(deadliest_hurricane)

# write your catgeorize by mortality function here:

def mortality_cat(hurr_dict):
    # mortality_scale = {0: 0,
    #               1: 100,
    #               2: 500,
    #               3: 1000,
    #               4: 10000}
    
    mortality_dict = {0: [], 1: [], 2: [], 3: [], 4: []}
    
    for info in hurr_dict.values():
        if info['Death'] >= 10000:
            mortality_dict[4].append(info)
        elif info['Death'] >= 1000:
            mortality_dict[3].append(info)
        elif info['Death'] >= 500:
            mortality_dict[2].append(info)
        elif info['Death'] >= 100:
            mortality_dict[1].append(info)
        else:
            mortality_dict[0].append(info)
    
    return mortality_dict

mortality_rating = mortality_cat(hurricane_database)
print(mortality_rating)

# write your greatest damage function here:

def greatest_damage(hurr_dict):
    max_damage = 0
    max_hurr = ""
    
    for info in hurr_dict.values():
        if info['Damage'] == 'Damages not recorded':
            continue
        if info['Damage'] > max_damage:
            max_damage = info['Damage']
            max_hurr = info['Name']
    
    most_damage = "Hurrican {NAME} had the greatest damage cost at {COST}".format(NAME=max_hurr, COST=max_damage)
    return most_damage

biggest_financial_impact = greatest_damage(hurricane_database)
print(biggest_financial_impact)

# write your catgeorize by damage function here:

def damage_cat(hurr_dict):
    # damage_scale = {0: 0,
    #             1: 100000000,
    #             2: 1000000000,
    #             3: 10000000000,
    #             4: 50000000000}
    
    damage_dict = {0: [], 1: [], 2: [], 3: [], 4: []}
    
    for info in hurr_dict.values():
        if type(info['Damage']) == type(''):
            continue
        if info['Damage'] >= 50000000000:
            damage_dict[4].append(info)
        elif info['Damage'] >= 10000000000:
            damage_dict[3].append(info)
        elif info['Damage'] >= 1000000000:
            damage_dict[2].append(info)
        elif info['Damage'] >= 100000000:
            damage_dict[1].append(info)
        else:
            damage_dict[0].append(info)
    
    return damage_dict

damage_rating = damage_cat(hurricane_database)
print(damage_rating)
