import pandas as pd

team_names = [
    "Strategic Synergy",
    "Market Mavericks",
    "Brand Innovators",
    "The Brain Trust",
    "Insight Architects",
    "Data Drivers",
    "Visionary Vanguard",
    "The Trend Setters",
    "Profit Prophets",
    "The Pivot Masters",
    "Brand Ambassadors",
    "Growth Gurus",
    "The Bottom Line Brigade",
    "Conversion Catalysts",
    "Revenue Architects",
    "Market Mechanics",
    "Agile Achievers",
    "The Value Builders",
    "Marketing Maestros",
    "The Demand Drivers",
    "Creative Catalysts",
    "The ROI Wranglers",
    "Sales Strategists",
    "The Profit Pros",
    "Revenue Rangers",
    "Efficiency Experts",
    "The Conversion Crew",
    "Solution Specialists",
    "Growth Geeks",
    "The Success Squad",
    "Branding Brigade",
    "The Data Analysts",
    "Idea Engineers",
    "The Competitive Edge",
    "Conversion Crushers",
    "Digital Dominators",
    "Market Magicians",
    "Profit Engineers",
    "Visionary Ventures",
    "Trend Transformers"
]

team_ids = [f"gruppe{i+1}" for i,_ in enumerate(team_names)]

desk = [f"Medstudentvurdering Del 1, gruppe {i+1}" for i,_  in enumerate(team_names)]


print(desk)

data = {"groupname" : team_names, "description": desk, "groupidnumber": team_ids}

dataframe = pd.DataFrame(data)

dataframe.to_csv("grupper.csv", sep=",", encoding="ISO-8859-1", index=False)

print(dataframe)
first_names = [
    "Liam", "Emma", "Noah", "Olivia", "Elijah", "Ava", "James", "Isabella", "William", "Sophia",
    "Benjamin", "Mia", "Lucas", "Charlotte", "Henry", "Amelia", "Alexander", "Harper", "Mason", "Evelyn",
    "Michael", "Abigail", "Ethan", "Emily", "Daniel", "Ella", "Jacob", "Elizabeth", "Logan", "Camila",
    "Jackson", "Luna", "Levi", "Sofia", "Sebastian", "Avery", "Mateo", "Mila", "Jack", "Aria",
    "Owen", "Scarlett", "Theodore", "Penelope", "Aiden", "Layla", "Samuel", "Chloe", "Joseph", "Victoria",
    "John", "Riley", "David", "Nora", "Wyatt", "Zoey", "Matthew", "Lily", "Luke", "Eleanor",
    "Asher", "Hannah", "Carter", "Lillian", "Julian", "Addison", "Grayson", "Aubrey", "Leo", "Ellie",
    "Jayden", "Stella", "Gabriel", "Natalie", "Isaac", "Zoe", "Lincoln", "Leah", "Anthony", "Hazel",
    "Hudson", "Violet", "Dylan", "Aurora", "Ezra", "Savannah", "Thomas", "Audrey", "Charles", "Brooklyn",
    "Christopher", "Bella", "Jaxon", "Claire", "Maverick", "Skylar", "Josiah", "Lucy", "Isaiah", "Paisley",
    "Andrew", "Everly", "Eli", "Anna"
]


last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
    "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
    "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
    "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
    "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez",
    "Powell", "Jenkins", "Perry", "Russell"
]

passwords = [f"TestP@assword123" for i in last_names]

emails = [f"testuser{i+1}@example.com" for i,_ in enumerate(last_names)]

usernames=[f"teststud{i+1}" for i,_ in enumerate(last_names)]


data_users = {"username": usernames, "firstname": first_names, "lastname": last_names, "email": emails, "password": passwords}

df_users = pd.DataFrame(data_users)
df_users.to_csv("brukere.csv", sep=",", encoding="ISO-8859-1", index=False)

for mail in emails:
   print(mail)



