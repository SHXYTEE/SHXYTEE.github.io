import base64
import os

img_dir = r'C:\Users\Spect\Repos\magnolia\ext\yews-github\yix\img'

# Load all images into a dict
images = {}
for f in sorted(os.listdir(img_dir)):
    if f.endswith('.jpg'):
        path = os.path.join(img_dir, f)
        with open(path, 'rb') as file:
            b64 = base64.b64encode(file.read()).decode('utf-8')
            images[f] = f'data:image/jpeg;base64,{b64}'

# Map Blake artwork references to available images
blake_map = {
    'The Ancient of Days': 'Urizen.jpg',
    'Newton': 'Urizen.jpg',
    'Christ Raising Jairus\'s Daughter': '_The Man Sweeping the Interpreter_s Parlour__ from Bunyan_s Pilgrim_s progress.jpg',
    'The Circle of the Lustful': 'The Circle of the Lustful_ Paolo and Francesca_ Inferno_ canto V.jpg',
    'Europe a Prophecy': 'The Canterbury Pilgrims.jpg',
    'Jerusalem': 'The Day of Judgment.jpg',
    'The Great Red Dragon and the Woman Clothed with the Sun': 'Nude Figure of a Man with Flaming Torch.jpg',
    'The Good and Evil Angels': 'Figure Seen from the Back_ with Outstretched Arm.jpg',
    'Jacob\'s Ladder': 'Menalcas Watching Women Dance_ from The Pastorals of Virgil.jpg',
    'The Vision of the Last Judgment': 'The Day of Judgment.jpg',
    'Albion Rose': 'A Rolling Stone is Ever Bare of Moss_ from The Pastorals of Virgil.jpg',
    'The Sun at His Eastern Gate': 'Sabrina_s Silvery Flood_ from The Pastorals of Virgil.jpg',
    'The Whirlwind': 'One Cycle of Hell.jpg',
    'Glad Day': 'A Rolling Stone is Ever Bare of Moss_ from The Pastorals of Virgil.jpg',
    'Pity': '_The Man Sweeping the Interpreter_s Parlour__ from Bunyan_s Pilgrim_s progress.jpg',
    'The Ghost of a Flea': 'Nude Figure Reaching Down Between Rocks.jpg',
    'Satan Exulting Over Eve': 'Medea Killing Her Children.jpg',
    'Nebuchadnezzar': 'Blasted Tree and Flattened Crops_ from The Pastorals of Virgil.jpg',
    'The House of Death': 'Death on a White Horse.jpg',
    'The Number of the Beast Is 666': 'The Circle of the Thieves_ Agnolo Brunelleschi Attacked by a Six-Footed Serpent_ Inferno_ canto XXV.jpg',
    'Elohim Creating Adam': 'Figure Seen from the Back_ with Outstretched Arm.jpg',
}

def get_img_tag(blake_ref):
    """Get the appropriate image tag for a Blake artwork reference."""
    clean_title = blake_ref.replace('Blake, Wm. ', '').strip()
    # Remove year if present (format: "Title. Year.")
    if clean_title.endswith('.'):
        clean_title = clean_title[:-1]
    # Split on last period to remove year
    if '.' in clean_title:
        # Check if the part after last dot is a 4-digit year
        parts = clean_title.rsplit('.', 1)
        if len(parts) == 2 and parts[1].strip().isdigit():
            clean_title = parts[0].strip()
    img_file = blake_map.get(clean_title)
    if img_file and img_file in images:
        return f'<img src="{images[img_file]}" style="max-width:100%;height:auto;margin:1rem 0;">'
    return ''

# Generate img tags for all Blake references
img_1 = get_img_tag('Blake, Wm. The Ancient of Days. 1794.')
img_2 = get_img_tag('Blake, Wm. Newton. 1795.')
img_3 = get_img_tag('Blake, Wm. Christ Raising Jairus\'s Daughter. 1799.')

img_4 = get_img_tag('Blake, Wm. The Circle of the Lustful. 1827.')
img_5 = get_img_tag('Blake, Wm. Europe a Prophecy. 1794.')
img_6 = get_img_tag('Blake, Wm. Newton. 1795.')  # Meloni uses Newton again
img_7 = get_img_tag('Blake, Wm. Jerusalem. 1804.')

img_8 = get_img_tag('Blake, Wm. The Great Red Dragon and the Woman Clothed with the Sun. 1805.')

img_9 = get_img_tag('Blake, Wm. The Good and Evil Angels. 1795.')
img_10 = get_img_tag('Blake, Wm. Jerusalem. 1804.')
img_11 = get_img_tag('Blake, Wm. Jacob\'s Ladder. 1805.')

img_12 = get_img_tag('Blake, Wm. The Vision of the Last Judgment. 1808.')
img_13 = get_img_tag('Blake, Wm. Albion Rose. 1794.')
img_14 = get_img_tag('Blake, Wm. The Sun at His Eastern Gate. 1805.')
img_15 = get_img_tag('Blake, Wm. The Whirlwind. 1820.')
img_16 = get_img_tag('Blake, Wm. Glad Day. 1794.')
img_17 = get_img_tag('Blake, Wm. Elohim Creating Adam. 1795.')
img_18 = get_img_tag('Blake, Wm. The Great Red Dragon and the Woman Clothed with the Sun. 1805.')
img_19 = get_img_tag('Blake, Wm. Pity. 1795.')
img_20 = get_img_tag('Blake, Wm. The Ghost of a Flea. 1819.')

# Generate yews-batch-1.toml
post1 = f'''title = "YEWS Batch #1"
date = "2026-06-20"

body = """
<b>5:28 AM</b>

‍

<b>Israel-Hezbollah Ceasefire Renewed Amid Iran Talks</b>

‍

<b>Blake, Wm. The Ancient of Days. 1794.</b>

{img_1}

‍

Israel and Hezbollah agreed to renew their truce after clashes threatened U.S.-Iran negotiations in Switzerland. The ceasefire follows deadly strikes, with both sides warning against violations.

U.S. envoy Steve Witkoff heads to talks as Lebanon reports ruined homes and civilian impacts. Officials hope the pause stabilizes the region for broader peace efforts.

"This fragile truce is a step, but vigilance is required," said a U.S. official.

Source

‍

<b>Trump Unveils Qatari-Gifted Air Force One</b>

‍

<b>Blake, Wm. Newton. 1795.</b>

{img_2}

‍

President Trump showcased a luxury Boeing 747 donated by Qatar as the new Air Force One, calling it the world's most advanced presidential aircraft.

The plane, valued at hundreds of millions, features top-tier modifications. It arrives amid broader foreign policy moves including Iran deal talks.

"Finest in the world," Trump stated during the unveiling.

Source

‍

<b>Obama Presidential Center Opens on Juneteenth</b>

‍

<b>Blake, Wm. Christ Raising Jairus's Daughter. 1799.</b>

{img_3}

‍

Barack and Michelle Obama surprised visitors at the newly opened presidential center in Chicago, coinciding with Juneteenth celebrations.

The center highlights their legacy and public service. It drew crowds on the holiday marking emancipation.

"This is a place for history and hope," said attendees reflecting on its significance.

Source
"""

viewMBC = """

"""'''

with open(r'C:\Users\Spect\Repos\magnolia\ext\yews-github\yix\posts\yews-batch-1.toml', 'w', encoding='utf-8') as f:
    f.write(post1)

# Generate yews-batch-2.toml
post2 = f'''title = "YEWS Batch #2"
date = "2026-06-20"

body = """
<b>5:30 AM</b>

‍

<b>UK Train Crash Kills One, Injures Dozens</b>

‍

<b>Blake, Wm. The Circle of the Lustful. 1827.</b>

{img_4}

‍

Two passenger trains collided north of London near Bedford, killing at least one person and injuring dozens more. British police and rail authorities are investigating the cause of the crash.

Emergency services responded swiftly to the scene as passengers were evacuated. The incident disrupted services in the region.

"This is a tragic event," officials stated amid ongoing inquiries.

Source

‍

<b>Ukraine Launches Major Drone Strike on Moscow</b>

‍

<b>Blake, Wm. Europe a Prophecy. 1794.</b>

{img_5}

‍

Ukraine carried out its largest drone attack on Moscow yet, igniting a key oil refinery and disrupting flights across the capital. Thick smoke billowed over the city.

The assault targeted Russian energy infrastructure as the war continues. Russia claimed defensive measures while facing renewed scrutiny.

"These strikes demonstrate our determination," Ukrainian officials affirmed.

Source

‍

<b>Meloni Denies Trump's G7 Photo Claim</b>

‍

<b>Blake, Wm. Newton. 1795.</b>

{img_6}

‍

Italian Prime Minister Giorgia Meloni rejected Donald Trump's assertion that she begged for a photo at the G7 summit, calling the story fabricated. Italy's foreign minister canceled a planned U.S. visit.

The exchange underscores strains in U.S.-European ties. Meloni said she was stunned by the remarks.

"This is not ally behavior," an Italian source noted.

Source

‍

<b>Burnham Victory Sets Stage for UK Leadership Challenge</b>

‍

<b>Blake, Wm. Jerusalem. 1804.</b>

{img_7}

‍

Andy Burnham's strong win in a UK by-election positions him as a serious contender to challenge Prime Minister Keir Starmer. Starmer pledged to fight any leadership bid.

The result highlights deepening divisions within Labour amid national challenges. Burnham's profile rises significantly.

"Renewal and real leadership are needed," supporters declared.

Source
"""

viewMBC = """

"""'''

with open(r'C:\Users\Spect\Repos\magnolia\ext\yews-github\yix\posts\yews-batch-2.toml', 'w', encoding='utf-8') as f:
    f.write(post2)

# Generate yews-batch-3.toml
post3 = f'''title = "YEWS Batch #3"
date = "2026-06-20"

body = """
<b>5:31 AM</b>

‍

<b>Woman Killed in Dominican Hotel Fire</b>

‍

<b>Blake, Wm. The Great Red Dragon and the Woman Clothed with the Sun. 1805.</b>

{img_8}

‍

A woman died and nearly 1,700 tourists were evacuated after a large fire at a beach resort hotel in Bayahibe, Dominican Republic.

Italian tourist Francesca Valentino, 46, was killed at the Viva Wyndham Dominicus Beach Hotel. Authorities are investigating the cause.

"This tragedy has devastated families and the local community," said emergency officials.

Source
"""

viewMBC = """

"""'''

with open(r'C:\Users\Spect\Repos\magnolia\ext\yews-github\yix\posts\yews-batch-3.toml', 'w', encoding='utf-8') as f:
    f.write(post3)

# Generate openai-ai-batch.toml
post4 = f'''title = "OpenAI AI News Batch"
date = "2026-06-20"

body = """
<b>5:32 AM</b>

‍

<b>OpenAI Hires Gemini Co-Lead</b>

‍

<b>Blake, Wm. The Ancient of Days. 1794.</b>

{img_1}

‍

OpenAI has recruited Noam Shazeer, one of the leaders behind Google's Gemini models, in a high-profile talent move in the AI race.

Shazeer helped shape some of Google's most advanced AI systems. His departure highlights escalating competition for top researchers as companies race to build larger and more capable models. "The AI talent war is accelerating," one industry analyst said.

Source

‍

<b>SoftBank Launches OpenAI Cyber Defense Tool</b>

‍

<b>Blake, Wm. The Good and Evil Angels. 1795.</b>

{img_9}

‍

SoftBank unveiled a cybersecurity product built on OpenAI technology and aimed at protecting critical infrastructure in Japan.

The service is designed to identify vulnerabilities and speed security updates. SoftBank founder Masayoshi Son described AI as a tool for national resilience as cyber threats become more sophisticated.

Source

‍

<b>Europe Pushes for AI Independence</b>

‍

<b>Blake, Wm. Jerusalem. 1804.</b>

{img_10}

‍

European leaders are discussing new funding mechanisms to strengthen domestic AI development and reduce reliance on foreign platforms.

Executives and policymakers argue that Europe needs greater computing power, investment, and research capacity to remain competitive in the global AI economy.

Source

‍

<b>Von der Leyen Calls for AI Cooperation</b>

‍

<b>Blake, Wm. Jacob's Ladder. 1805.</b>

{img_11}

‍

European Commission President Ursula von der Leyen said it is in the mutual interest of the United States and Europe to share access to trusted AI systems.

She compared AI governance to aviation safety, arguing that advanced technologies require common standards and international trust.

Source
"""

viewMBC = """

"""'''

with open(r'C:\Users\Spect\Repos\magnolia\ext\yews-github\yix\posts\openai-ai-batch.toml', 'w', encoding='utf-8') as f:
    f.write(post4)

# Generate spacex-airforce-batch.toml
post5 = f'''title = "SpaceX AirForce One Batch"
date = "2026-06-20"

body = """
<b>5:33 AM</b>

‍

<b>Trump Debuts Qatar-Gifted Air Force One</b>

‍

<b>Blake, Wm. Newton. 1795.</b>

{img_2}

‍

President Trump unveiled a modified Boeing 747 gifted by Qatar, introducing it as a temporary Air Force One while delayed replacements remain years away.

The aircraft underwent extensive security and communications upgrades before joining the presidential fleet. Critics questioned the ethics of accepting a foreign gift valued at hundreds of millions of dollars.

Trump called it "the world's most luxurious plane." Supporters described it as a practical solution to Boeing's delays.

Source

‍

<b>SpaceX Faces New Starship Review</b>

‍

<b>Blake, Wm. The Ancient of Days. 1794.</b>

{img_1}

‍

Federal regulators ordered SpaceX to investigate a Starship booster failure following the company's latest test flight. The review comes as Starship remains central to future Moon and Mars missions.

Despite the booster mishap, the mission achieved several planned objectives, including payload deployment and a controlled splashdown.

The FAA said corrective actions must be approved before additional flights proceed.

Source

‍

<b>Starship Remains SpaceX's Biggest Bet</b>

‍

<b>Blake, Wm. The Great Red Dragon and the Woman Clothed with the Sun. 1805.</b>

{img_8}

‍

Investors continue to focus on Starship as the centerpiece of SpaceX's long-term ambitions following the company's public debut.

The rocket is designed to become the world's first fully reusable orbital launch system. Success could dramatically reduce launch costs and expand lunar and Martian exploration.

Analysts describe Starship as the project most likely to determine whether SpaceX's valuation can keep rising.

Source

‍

<b>Stablecoin Rules Reshape Crypto Industry</b>

‍

<b>Blake, Wm. Elohim Creating Adam. 1795.</b>

{img_17}

‍

The GENIUS Act continues to reshape the U.S. digital asset market, establishing federal standards for dollar-backed stablecoins.

The law requires reserves, oversight, and disclosure standards intended to increase confidence in digital dollars. Supporters argue the framework brings long-awaited regulatory clarity.

Industry leaders say clearer rules could accelerate mainstream adoption of blockchain-based payments.

Source

‍

<b>Digital Dollars Gain Washington Support</b>

‍

<b>Blake, Wm. The House of Death. 1805.</b>

{img_20}

‍

Federal policymakers continue implementing stablecoin legislation passed last year, marking one of the most significant crypto reforms in U.S. history.

The law requires stablecoins to be backed by highly liquid assets and subjects issuers to regulatory supervision.

Supporters say the framework strengthens trust. Critics warn rapid growth could introduce new financial risks.

Source
"""

viewMBC = """

"""'''

with open(r'C:\Users\Spect\Repos\magnolia\ext\yews-github\yix\posts\spacex-airforce-batch.toml', 'w', encoding='utf-8') as f:
    f.write(post5)

# Generate ai-market-batch.toml
post6 = f'''title = "AI Market Batch"
date = "2026-06-20"

body = """
<b>5:34 AM</b>

‍

<b>OpenAI Spending Revealed Ahead of IPO</b>

‍

<b>Blake, Wm. The Vision of the Last Judgment. 1808.</b>

{img_12}

‍

Reports indicate OpenAI spent billions expanding research, infrastructure, and operations as it prepares for a potential public offering.

The company continues to prioritize growth and computing capacity while investors watch for signs of long-term profitability.

Source

‍

<b>OpenAI Eyes Public Markets</b>

‍

<b>Blake, Wm. Albion Rose. 1794.</b>

{img_13}

‍

OpenAI has confidentially filed for a U.S. IPO that could value the company near $1 trillion.

The move would mark a major shift for the ChatGPT maker, which has become one of the most influential technology companies of the decade.

Source

‍

<b>SpaceX IPO Reshapes Wall Street</b>

‍

<b>Blake, Wm. The Sun at His Eastern Gate. 1805.</b>

{img_14}

‍

SpaceX's public debut has become one of the largest market events in recent history.

The listing pushed the company into the ranks of the world's most valuable businesses and intensified investor enthusiasm for space technology.

Source

‍

<b>Musk's 'Elon Premium' Faces Test</b>

‍

<b>Blake, Wm. The Whirlwind. 1820.</b>

{img_15}

‍

Investors are examining whether SpaceX can sustain the premium valuations associated with Elon Musk's ventures.

Analysts say expectations remain high as public markets evaluate future growth in launch services, satellites, and AI-related businesses.

Source

‍

<b>Retail Investors Rush Into SpaceX</b>

‍

<b>Blake, Wm. Glad Day. 1794.</b>

{img_16}

‍

Retail traders poured into SpaceX shares following the company's market debut.

The IPO attracted unusually strong interest from individual investors, reviving debates over whether excitement can outpace fundamentals.

Source

‍

<b>AI Stocks Continue Market Rally</b>

‍

<b>Blake, Wm. Elohim Creating Adam. 1795.</b>

{img_17}

‍

Artificial intelligence remains one of the dominant forces driving investor sentiment worldwide.

Analysts point to rising demand for computing infrastructure, software, and advanced models as capital continues flowing into the sector.

Source

‍

<b>Anthropic Pursues Massive Financing</b>

‍

<b>Blake, Wm. The Great Red Dragon and the Woman Clothed with the Sun. 1805.</b>

{img_8}

‍

Anthropic is reportedly working on a financing package worth tens of billions of dollars to expand AI infrastructure.

The funds would support large-scale computing resources and next-generation model development.

Source

‍

<b>AI Infrastructure Race Intensifies</b>

‍

<b>Blake, Wm. Pity. 1795.</b>

{img_19}

‍

Technology companies continue investing heavily in chips, data centers, and cloud capacity to support advanced AI systems.

The infrastructure race has become as important as the software itself.

Source

‍

<b>Small AI Models Gain Attention</b>

‍

<b>Blake, Wm. The Ghost of a Flea. 1819.</b>

{img_20}

‍

New research suggests smaller AI systems may soon handle many tasks currently reserved for massive models.

Supporters argue compact models could lower costs and expand access while reducing dependence on giant data centers.

Source
"""

viewMBC = """

"""'''

with open(r'C:\Users\Spect\Repos\magnolia\ext\yews-github\yix\posts\ai-market-batch.toml', 'w', encoding='utf-8') as f:
    f.write(post6)

print("All post files updated with embedded Blake images")
print(f"Sample img tag: {img_1[:80]}...")