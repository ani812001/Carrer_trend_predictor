import pandas as pd
import os
import random
from datetime import datetime, timedelta

# Paths
RAW_PATH = "data/raw/jobs.csv"

# Sample data generators
titles = ["Data Scientist", "Software Engineer", "Product Manager", "UX Designer", "DevOps Engineer"]
companies = ["TechCorp", "InnovateX", "DataWorks", "Appify", "CloudNet"]
locations = ["New York, NY", "San Francisco, CA", "Austin, TX", "Seattle, WA", "Chicago, IL"]
salary_ranges = ["$80k-$100k", "$100k-$120k", "$120k-$150k", "$150k-$180k", "$60k-$80k"]

# Generate 50 fake job records
data = []
for _ in range(50):
    title = random.choice(titles)
    company = random.choice(companies)
    location = random.choice(locations)
    salary = random.choice(salary_ranges)
    days_ago = random.randint(0, 60)
    posted_date = (datetime.today() - timedelta(days=days_ago)).strftime("%Y-%m-%d")
    
    data.append([title, company, location, salary, posted_date])

# Create DataFrame
df = pd.DataFrame(data, columns=["title", "company", "location", "salary", "posted_date"])

# Ensure directory exists
os.makedirs(os.path.dirname(RAW_PATH), exist_ok=True)

# Save to CSV
df.to_csv(RAW_PATH, index=False)

RAW_PATH
