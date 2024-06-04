import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    csv = pd.read_csv('adult.data.csv', delimiter=',')
    df = pd.DataFrame(csv)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_from_df = df['race']
    race_count = race_from_df.value_counts()

    # What is the average age of men?
    men_from_df = df[df['sex'] == 'Male']
    men_ages = men_from_df['age']
    average_age_men_sum = men_ages.sum()
    average_age_men = average_age_men_sum // len(men_ages)

    # What is the percentage of people who have a Bachelor's degree?
    those_with_bachelors = df[df['education'] == 'Bachelors']
    those_with_bachelors_count = len(those_with_bachelors)
    total_education_count = len(df['education'])
    percentage_bachelors = (those_with_bachelors_count / total_education_count) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # percentage with salary >50K

    filtered_higher_ed_df = df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))]
    filtered_higher_ed_rich_df = df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')]
    filtered_lower_ed_rich_df = df[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')]
    higher_education = (len(filtered_higher_ed_df) / total_education_count) * 100
    lower_education = 100 - higher_education
    higher_education_rich = (len(filtered_higher_ed_rich_df) / total_education_count) * 100
    lower_education_rich = (len(filtered_lower_ed_rich_df) / total_education_count) * 100

    # Remove later
    earn_over_fiftykdf = df[df['salary'] == '>50K']
    earn_under_fiftykdf = df[df['salary'] == '<=50K']
    percentage_over = (len(earn_over_fiftykdf) / total_education_count) * 100
    percentage_under = (len(earn_under_fiftykdf) / total_education_count) * 100
    print(percentage_over)
    print(percentage_under)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    least_hours_worked_per_week_df = df['hours-per-week']
    min_work_hours = min(least_hours_worked_per_week_df)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = least_hours_worked_per_week_df[df['hours-per-week'] == '1']
    num_min_workers_over_fiftyk = num_min_workers[df['salary'] == '>50K']
    if len(num_min_workers) > 0:
        rich_percentage = (len(num_min_workers_over_fiftyk) / len(num_min_workers)) * 100
    else:
        rich_percentage = 0

    country_salary_counts = df.groupby(['native-country', 'salary']).size().unstack(fill_value=0)
    # Calculate the total number of earners for each country
    country_totals = country_salary_counts.sum(axis=1)
    # Calculate the percentage of earners over 50K for each country
    country_percentages = (country_salary_counts['>50K'] / country_totals) * 100
    # Find the country with the highest percentage of earners over 50K
    highest_percentage_country = country_percentages.idxmax()
    highest_percentage_value = country_percentages.max()

    highest_earning_country = highest_percentage_country
    highest_earning_country_percentage = highest_percentage_value

    # Identify the most popular occupation for those who earn >50K in India.

    # Filter the DataFrame for rows where 'native-country' is 'India' and 'salary' is over 50K
    india_high_earners_df = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    # Count the occurrences of each occupation for high earners in India
    occupation_counts = india_high_earners_df['occupation'].value_counts()
    # Find the most popular occupation
    most_popular_occupation = occupation_counts.idxmax()
    top_IN_occupation = most_popular_occupation

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()
