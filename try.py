import pandas as pd

# Your data
news_data = {
    'headline': [
        'Flushing Financial seeks to raise $70 million to shore up capital as it unloads underwater bonds', 
        'Stocks making the biggest moves midday: Adobe, Warner Bros. Discovery and more', 
        'Trump says heâ\x80\x99s not going to make any market predictions in case thereâ\x80\x99s a â\x80\x98dipâ\x80\x99', 
        'Stocks making the biggest moves premarket: Uber, Celsius, Adobe, Chewy and more', 
        'CFPB announces rule limiting bank overdraft fees; trade group sues in response', 
        'Stocks making the biggest moves after hours: Adobe, Chewy and more', 
        'Stocks making biggest moves midday: Broadcom, GE Vernova, Stitch Fix and more', 
        'Hereâ\x80\x99s the inflation breakdown for November 2024 â\x80\x94 in one chart', 
        "Stocks making biggest moves premarket: GameStop, Macy's, GE Vernova and more", 
        'China ramps up Wall Street meetings as Trump inauguration looms', 
        'Stocks making the biggest moves after hours: General Motors, GE Vernova and more', 
        "If Trump adds tariffs, 'either way, there is a cost to consumers': economist", 
        'Stocks making the biggest moves midday: Alphabet, SiriusXM, Alaska Air and more', 
        'Stocks making biggest moves premarket: Oracle, Alaska Air, MongoDB and more', 
        'Stocks making the biggest moves after hours: Oracle, C3.ai and more', 
        'Amazon is bringing Intuit QuickBooks software to its millions of third-party sellers', 
        "'Low-hire, low-fire' The U.S. job market is stagnant right now, economists say", 
        'Stocks making the biggest moves midday: Hershey, Nvidia, Alibaba and more', 
        "Treasury may fine small businesses $10,000 or more if they don't file this new report", 
        "Stocks making the biggest moves premarket: Nvidia, Palantir, Reddit, Macy's and more", 
        "AI's growth is just getting started, BlackRock's thematic ETF head says", 
        "'This was preventableâ\x80\x99: Corporate world shudders after UnitedHeathcare CEO slaying", 
        'Stocks making biggest moves midday: Lululemon, DraftKings, Rubrik and more', 
        'CFPB sues Comerica Bank, alleging it failed to administer federal benefits program', 
        'Stocks making biggest moves premarket: AMC, Lululemon, Rubrik, Petco and more', 
        "UniCredit's Orcel could still sweeten his bid and take on a double M&A offensive", 
        'Stocks making the biggest moves after hours: Ulta Beauty, Lululemon and more', 
        'Stocks making the biggest moves midday: American Eagle, Verint Systems and more', 
        'Stocks making big moves premarket: American Eagle Outfitters, Five Below', 
        "Far from a bazooka, China's stimulus measures are just trickling through the economy", 
        'Stocks making the biggest moves after hours: American Eagle, Five Below and more', 
        'More employers add 401(k) plan match for workers paying student loans', 
        "Powell says he's not worried about the Fed losing its independence under Trump"
    ],
    'time': [
        'Thu, Dec 12th 2024', 'Thu, Dec 12th 2024', 'Thu, Dec 12th 2024', 'Thu, Dec 12th 2024', 'Thu, Dec 12th 2024', 
        'Wed, Dec 11th 2024', 'Wed, Dec 11th 2024', 'Wed, Dec 11th 2024', 'Wed, Dec 11th 2024', '3 hours ago', 
        'Tue, Dec 10th 2024', 'Tue, Dec 10th 2024', 'Tue, Dec 10th 2024', 'Tue, Dec 10th 2024', 'Mon, Dec 9th 2024', 
        'Mon, Dec 9th 2024', 'Mon, Dec 9th 2024', 'Mon, Dec 9th 2024', 'Mon, Dec 9th 2024', 'Mon, Dec 9th 2024', 
        'Sun, Dec 8th 2024', 'Sat, Dec 7th 2024', 'Fri, Dec 6th 2024', 'Fri, Dec 6th 2024', 'Fri, Dec 6th 2024', 
        'Fri, Dec 6th 2024', 'Fri, Dec 6th 2024', 'Thu, Dec 5th 2024', 'Thu, Dec 5th 2024', 'Thu, Dec 5th 2024', 
        'Wed, Dec 4th 2024', 'Wed, Dec 4th 2024', 'Wed, Dec 4th 2024'
    ],
}

# Create the DataFrame
df = pd.DataFrame(news_data)

# Display the first few rows of the DataFrame
print(df.head())
