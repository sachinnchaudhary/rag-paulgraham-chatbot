from bs4 import BeautifulSoup
import json
import requests
import os
#the website for scraping data.
url = "https://www.paulgraham.com/reddits.html"

#creating function for looping to scrape essays.
def scrape_essays(url):
     response = requests.get(url)
     essays_dt = response.content

     soup = BeautifulSoup(essays_dt, "html.parser")

     essay_content = soup.find('font', {'face': 'verdana', 'size': '2'})

     essay_tokens = essay_content.get_text(separator="\n\n",strip=True)

     return essay_tokens


#to dump the scraped data into the json file.

def adding_json(json_file_path, essay_title, essay_tokens):

          with open(json_file_path, "r", encoding="utf-8") as file:
                essays = json.load(file)


          essays[essay_title] = essay_tokens

          with open(json_file_path, "w", encoding="utf-8") as file:
                json.dump(essays, file, indent=4, ensure_ascii=False)



json_file_path = os.path.join("....your os path......")

essay_url = [{"you can use your own url too...."}]

#essay urls to scrape the data

essay_url = [
     {"url":"https://www.paulgraham.com/reddits.html", "title": "The Reddits"},
     {"url":"https://www.paulgraham.com/google.html", "title":"How To Start Google"},
     {"url":"https://www.paulgraham.com/best.html", "title":"The Best Essay"},
     {"url":"https://www.paulgraham.com/superlinear.html", "title":"Superlinear Returns"},
     {"url":"https://www.paulgraham.com/greatwork.html", "title":"How To Do Great Work"},
     {"url":"https://www.paulgraham.com/getideas.html", "title":"How To Get New Ideas"},
     {"url":"https://www.paulgraham.com/read.html", "title":"The Need To Read"},
     {"url":"https://www.paulgraham.com/want.html", "title":"What you(want to) Want"},
     {"url":"https://www.paulgraham.com/alien.html", "title":"Alien Truth"},
     {"url":"https://www.paulgraham.com/users.html", "title":"What I've Learned From Users"},
     {"url":"https://www.paulgraham.com/heresy.html", "title":"Heresy"},
     {"url":"https://www.paulgraham.com/words.html", "title":"Putting Ideas Into The Word"},
     {"url":"https://www.paulgraham.com/goodtaste.html", "title":"Is There Such Thing As Good Taste"},
     {"url":"https://www.paulgraham.com/smart.html", "title":"Beyond Smart"},
     {"url":"https://www.paulgraham.com/weird.html", "title":"Weird Languages"},
     {"url":"https://www.paulgraham.com/hwh.html", "title":"How To Work Hard"},
     {"url":"https://www.paulgraham.com/own.html", "title":"A Project Of One's Own"},
     {"url":"https://www.paulgraham.com/fn.html", "title":"Fierce Nerds"},
     {"url":"https://www.paulgraham.com/nft.html", "title":"An Nft That Saves Life"},
     {"url":"https://www.paulgraham.com/real.html", "title":"The Real Reason To End Death Penalty"},
     {"url":"https://www.paulgraham.com/richnow.html", "title":"How People Get Rich Now"},
     {"url":"https://www.paulgraham.com/simply.html", "title":"Write Simply"},
     {"url":"https://www.paulgraham.com/donate.html", "title":"Donate Unrestricted"},
     {"url":"https://www.paulgraham.com/worked.html", "title":"What I Worked On"},
     {"url":"https://www.paulgraham.com/earnest.html", "title":"Earnestness"},
     {"url":"https://www.paulgraham.com/ace.html", "title":"Billionaires Build"},
     {"url":"https://www.paulgraham.com/airbnbs.html", "title":"The Airbnbs"},
     {"url":"https://www.paulgraham.com/think.html", "title":"How To Think For Yourself"},
     {"url":"https://www.paulgraham.com/early.html", "title":"Early Work"},
     {"url":"https://www.paulgraham.com/wtax.html", "title":"Modeling a Wealth Tax"},
     {"url":"https://www.paulgraham.com/conformism.html", "title":"The Four Quadrants of Conformism"},
     {"url":"https://www.paulgraham.com/orth.html", "title":"Orthodox Privilege"},
     {"url":"https://www.paulgraham.com/cred.html", "title":"Coronavirus and Credibility"},
     {"url":"https://www.paulgraham.com/useful.html", "title":"How to Write Usefully"},
     {"url":"https://www.paulgraham.com/noob.html", "title":"Being a Noob"},
     {"url":"https://www.paulgraham.com/fh.html", "title":"Haters"},
     {"url":"https://www.paulgraham.com/mod.html", "title":"The Two Kinds of Moderate"},
     {"url":"https://www.paulgraham.com/fp.html", "title":"Fashionable Problems"},
     {"url":"https://www.paulgraham.com/kids.html", "title":"Having Kids"},
     {"url":"https://www.paulgraham.com/lesson.html", "title":"The Lesson to Unlearn"},
     {"url":"https://www.paulgraham.com/nov.html", "title":"Novelty and Heresy"},
     {"url":"https://www.paulgraham.com/genius.html", "title":"The Bus Ticket Theory of Genius"},
     {"url":"https://www.paulgraham.com/sun.html", "title":"General and Surprising"},
     {"url":"https://www.paulgraham.com/pow.html", "title":"Charisma / Power"},
     {"url":"https://www.paulgraham.com/disc.html", "title":"The Risk of Discovery"},
     {"url":"https://www.paulgraham.com/pgh.html", "title":"How to Make Pittsburgh a Startup Hub"},
     {"url":"https://www.paulgraham.com/vb.html", "title":"Life is Short"},
     {"url":"https://www.paulgraham.com/ineq.html", "title":"Economic Inequality"},
     {"url":"https://www.paulgraham.com/re.html", "title":"The Refragmentation"},
     {"url":"https://www.paulgraham.com/jessica.html", "title":"Jessica Livingston"},
     {"url":"https://www.paulgraham.com/bias.html", "title":"A Way to Detect Bias"},
     {"url":"https://www.paulgraham.com/talk.html", "title":"Write Like You Talk"},
     {"url":"https://www.paulgraham.com/aord.html", "title":"Default Alive or Default Dead?"},
     {"url":"https://www.paulgraham.com/safe.html", "title":"Why It's Safe for Founders to Be Nice"},
     {"url":"https://www.paulgraham.com/name.html", "title":"Change Your Name"},
     {"url":"https://www.paulgraham.com/altair.html", "title":"What Microsoft Is this the Altair Basic of?"},
     {"url":"https://www.paulgraham.com/ronco.html", "title":"The Ronco Principle"},
     {"url":"https://www.paulgraham.com/work.html", "title":"What Doesn't Seem Like Work?"},
     {"url":"https://www.paulgraham.com/corpdev.html", "title":"Don't Talk to Corp Dev"},
     {"url":"https://www.paulgraham.com/95.html", "title":"Let the Other 95% of Great Programmers In"},
     {"url":"https://www.paulgraham.com/ecw.html", "title":"How to Be an Expert in a Changing World"},
     {"url":"https://www.paulgraham.com/know.html", "title":"How You Know"},
     {"url":"https://www.paulgraham.com/pinch.html", "title":"The Fatal Pinch"},
     {"url":"https://www.paulgraham.com/mean.html", "title":"Mean People Fail"},
     {"url":"https://www.paulgraham.com/before.html", "title":"Before the Startup"},
     {"url":"https://www.paulgraham.com/fr.html", "title":"How to Raise Money"},
     {"url":"https://www.paulgraham.com/herd.html", "title":"Investor Herd Dynamics"},
     {"url":"https://www.paulgraham.com/convince.html", "title":"How to Convince Investors"},
     {"url":"https://www.paulgraham.com/ds.html", "title":"Do Things that Don't Scale"},
     {"url":"https://www.paulgraham.com/invtrend.html", "title":"Startup Investing Trends"},
     {"url":"https://www.paulgraham.com/startupideas.html", "title":"How to Get Startup Ideas"},
     {"url":"https://www.paulgraham.com/hw.html", "title":"The Hardware Renaissance"},
     {"url":"https://www.paulgraham.com/growth.html", "title":"Startup = Growth"},
     {"url":"https://www.paulgraham.com/swan.html", "title":"Black Swan Farming"},
     {"url":"https://www.paulgraham.com/todo.html", "title":"The Top of My Todo List"},
     {"url":"https://www.paulgraham.com/speak.html", "title":"Writing and Speaking"},
     {"url":"https://www.paulgraham.com/ycstart.html", "title":"How Y Combinator Started"},
     {"url":"https://www.paulgraham.com/property.html", "title":"Defining Property"},
     {"url":"https://www.paulgraham.com/ambitious.html", "title":"Frighteningly Ambitious Startup Ideas"},
     {"url":"https://www.paulgraham.com/word.html", "title":"A Word to the Resourceful"},
     {"url":"https://www.paulgraham.com/schlep.html", "title":"Schlep Blindness"},
     {"url":"https://www.paulgraham.com/vw.html", "title":"Snapshot: Viaweb, June 1998"},
     {"url":"https://www.paulgraham.com/hubs.html", "title":"Why Startup Hubs Work"},
     {"url":"https://www.paulgraham.com/patentpledge.html", "title":"The Patent Pledge"},
     {"url":"https://www.paulgraham.com/airbnb.html", "title":"Subject: Airbnb"},
     {"url":"https://www.paulgraham.com/control.html", "title":"Founder Control"},
     {"url":"https://www.paulgraham.com/tablets.html", "title":"Tablets"},
     {"url":"https://www.paulgraham.com/founders.html", "title":"What We Look for in Founders"},
     {"url":"https://www.paulgraham.com/superangels.html", "title":"The New Funding Landscape"},
     {"url":"https://www.paulgraham.com/seesv.html", "title":"Where to See Silicon Valley"},
     {"url":"https://www.paulgraham.com/hiresfund.html", "title":"High Resolution Fundraising"},
     {"url":"https://www.paulgraham.com/yahoo.html", "title":"What Happened to Yahoo"},
     {"url":"https://www.paulgraham.com/future.html", "title":"The Future of Startup Funding "},
     {"url":"https://www.paulgraham.com/addiction.html", "title":"The Acceleration of Addictiveness"},
     {"url":"https://www.paulgraham.com/top.html", "title":"The Top Idea in Your Mind "},
     {"url":"https://www.paulgraham.com/selfindulgence.html", "title":"How to Lose Time and Money "},
     {"url":"https://www.paulgraham.com/organic.html", "title":"Organic Startup Ideas"},
     {"url":"https://www.paulgraham.com/apple.html", "title":"Apple's Mistake"},
     {"url":"https://www.paulgraham.com/really.html", "title":"What Startups Are Really Like"},
     {"url":"https://www.paulgraham.com/discover.html", "title":"Persuade xor Discover "},
     {"url":"https://www.paulgraham.com/publishing.html", "title":"Post-Medium Publishing"},
     {"url":"https://www.paulgraham.com/nthings.html", "title":"The List of N Things"},
     {"url":"https://www.paulgraham.com/determination.html", "title":"The Anatomy of Determination "},
     {"url":"https://www.paulgraham.com/kate.html", "title":"What Kate Saw in Silicon Valley "},
     {"url":"https://www.paulgraham.com/segway.html", "title":"The Trouble with the Segway"},
     {"url":"https://www.paulgraham.com/ramenprofitable.html", "title":"Ramen Profitable"},
     {"url":"https://www.paulgraham.com/makersschedule.html", "title":"Maker's Schedule, Manager's Schedule "},
     {"url":"https://www.paulgraham.com/revolution.html", "title":"A Local Revolution?"},
     {"url":"https://www.paulgraham.com/twitter.html", "title":"Why Twitter is a Big Deal"},
     {"url":"https://www.paulgraham.com/foundervisa.html", "title":"The Founder Visa"},
     {"url":"https://www.paulgraham.com/5founders.html", "title":"Five Founders"},
     {"url":"https://www.paulgraham.com/relres.html", "title":"Relentlessly Resourceful"},
     {"url":"https://www.paulgraham.com/angelinvesting.html", "title":"How to Be an Angel Investor"},
     {"url":"https://www.paulgraham.com/convergence.html", "title":"Why TV Lost"},
     {"url":"https://www.paulgraham.com/maybe.html", "title":"Can You Buy a Silicon Valley? Maybe."},
     {"url":"https://www.paulgraham.com/hackernews.html", "title":"What I've Learned from Hacker News"},
     {"url":"https://www.paulgraham.com/13sentences.html", "title":"Startups in 13 Sentences"},
     {"url":"https://www.paulgraham.com/identity.html", "title":"Keep Your Identity Small"},
     {"url":"https://www.paulgraham.com/credentials.html", "title":"After Credentials"},
     {"url":"https://www.paulgraham.com/divergence.html", "title":"Could VC be a Casualty of the Recession?"},
     {"url":"https://www.paulgraham.com/highres.html", "title":"The High-Res Society"},
     {"url":"https://www.paulgraham.com/artistsship.html", "title":'The Other Half of "Artists Ship"'},
     {"url":"https://www.paulgraham.com/badeconomy.html", "title":"Why to Start a Startup in a Bad Economy"},
     {"url":"https://www.paulgraham.com/fundraising.html", "title":"A Fundraising Survival Guide"},
     {"url":"https://www.paulgraham.com/prcmc.html", "title":"The Pooled-Risk Company Management Company"},
     {"url":"https://www.paulgraham.com/cities.html", "title":"Cities and Ambition"},
     {"url":"https://www.paulgraham.com/distraction.html", "title":"Disconnecting Distraction"},
     {"url":"https://www.paulgraham.com/lies.html", "title":"Lies We Tell Kids"},
     {"url":"https://www.paulgraham.com/good.html", "title":"Be Good"},
     {"url":"https://www.paulgraham.com/googles.html", "title":"Why There Aren't More Googles"},
     {"url":"https://www.paulgraham.com/heroes.html", "title":"Some Heroes"},
     {"url":"https://www.paulgraham.com/disagree.html", "title":"How to Disagree"},
     {"url":"https://www.paulgraham.com/boss.html", "title":"You Weren't Meant to Have a Boss"},
     {"url":"https://www.paulgraham.com/ycombinator.html", "title":"A New Venture Animal"},
     {"url":"https://www.paulgraham.com/trolls.html", "title":"Trolls"},
     {"url":"https://www.paulgraham.com/newthings.html", "title":"Six Principles for Making New Things"},
     {"url":"https://www.paulgraham.com/startuphubs.html", "title":"Why to Move to a Startup Hub"},
     {"url":"https://www.paulgraham.com/webstartups.html", "title":"The Future of Web Startups"},
     {"url":"https://www.paulgraham.com/philosophy.html", "title":"How to Do Philosophy"},
     {"url":"https://www.paulgraham.com/colleges.html", "title":"News from the Front"},
     {"url":"https://www.paulgraham.com/die.html", "title":"How Not to Die"},
     {"url":"https://www.paulgraham.com/head.html", "title":"Holding a Program in One's Head"},
     {"url":"https://www.paulgraham.com/stuff.html", "title":"Stuff"},
     {"url":"https://www.paulgraham.com/equity.html", "title":"The Equity Equation"},
     {"url":"https://www.paulgraham.com/unions.html", "title":"An Alternative Theory of Unions"},
     {"url":"https://www.paulgraham.com/guidetoinvestors.html", "title":"The Hacker's Guide to Investors"},
     {"url":"https://www.paulgraham.com/judgement.html", "title":"Two Kinds of Judgement"},
     {"url":"https://www.paulgraham.com/microsoft.html", "title":"Microsoft is Dead"},
     {"url":"https://www.paulgraham.com/notnot.html", "title":"Why to Not Not Start a Startup"},
     {"url":"https://www.paulgraham.com/wisdom.html", "title":"Is It Worth Being Wise?"},
     {"url":"https://www.paulgraham.com/foundersatwork.html", "title":"Learning from Founders"},
     {"url":"https://www.paulgraham.com/goodart.html", "title":"How Art Can Be Good"},
     {"url":"https://www.paulgraham.com/startupmistakes.html", "title":"The 18 Mistakes That Kill Startups"},
     {"url":"https://www.paulgraham.com/mit.html", "title":"A Student's Guide to Startups"},
     {"url":"https://www.paulgraham.com/investors.html", "title":"How to Present to Investors"},
     {"url":"https://www.paulgraham.com/copy.html", "title":"Copy What You Like"},
     {"url":"https://www.paulgraham.com/island.html", "title":"The Island Test"},
     {"url":"https://www.paulgraham.com/marginal.html", "title":"The Power of the Marginal"},
     {"url":"https://www.paulgraham.com/america.html", "title":"Why Startups Condense in America"},
     {"url":"https://www.paulgraham.com/siliconvalley.html", "title":"How to Be Silicon Valley"},
     {"url":"https://www.paulgraham.com/startuplessons.html", "title":"The Hardest Lessons for Startups to Learn"},
     {"url":"https://www.paulgraham.com/randomness.html", "title":"See Randomness"},
     {"url":"https://www.paulgraham.com/softwarepatents.html", "title":"Are Software Patents Evil?"},
     {"url":"https://www.paulgraham.com/6631327.html", "title":"6,631,372"},
     {"url":"https://www.paulgraham.com/whyyc.html", "title":"Why YC"},
     {"url":"https://www.paulgraham.com/love.html", "title":"How to Do What You Love"},
     {"url":"https://www.paulgraham.com/procrastination.html", "title":"Good and Bad Procrastination"},
     {"url":"https://www.paulgraham.com/web20.html", "title":"Web 2.0"},
     {"url":"https://www.paulgraham.com/startupfunding.html", "title":"How to Fund a Startup"},
     {"url":"https://www.paulgraham.com/vcsqueeze.html", "title":"The Venture Capital Squeeze"},
     {"url":"https://www.paulgraham.com/ideas.html", "title":"Ideas for Startups"},
     {"url":"https://www.paulgraham.com/sfp.html", "title":"What I Did this Summer"},
     {"url":"https://www.paulgraham.com/inequality.html", "title":"Inequality and Risk"},
     {"url":"https://www.paulgraham.com/ladder.html", "title":"After the Ladder"},
     {"url":"https://www.paulgraham.com/opensource.html", "title":"What Business Can Learn from Open Source"},
     {"url":"https://www.paulgraham.com/hiring.html", "title":"Hiring is Obsolete"},
     {"url":"https://www.paulgraham.com/submarine.html", "title":"The Submarine"},
     {"url":"https://www.paulgraham.com/bronze.html", "title":"Why Smart People Have Bad Ideas"},
     {"url":"https://www.paulgraham.com/mac.html", "title":"Return of the Mac"},
     {"url":"https://www.paulgraham.com/writing44.html", "title":"Writing, Briefly"},
     {"url":"https://www.paulgraham.com/college.html", "title":"Undergraduation"},
     {"url":"https://www.paulgraham.com/venturecapital.html", "title":"A Unified Theory of VC Suckage"},
     {"url":"https://www.paulgraham.com/start.html", "title":"How to Start a Startup"},
     {"url":"https://www.paulgraham.com/hs.html", "title":"What You'll Wish You'd Known"},
     {"url":"https://www.paulgraham.com/usa.html", "title":"Made in USA"},
     {"url":"https://www.paulgraham.com/charisma.html", "title":"It's Charisma, Stupid"},
     {"url":"https://www.paulgraham.com/polls.html", "title":"Bradley's Ghost"},
     {"url":"https://www.paulgraham.com/laundry.html", "title":"A Version 1.0"},
     {"url":"https://www.paulgraham.com/bubble.html", "title":"What the Bubble Got Right"},
     {"url":"https://www.paulgraham.com/essay.html", "title":"The Age of the Essay"},
     {"url":"https://www.paulgraham.com/pypar.html", "title":"The Python Paradox"},
     {"url":"https://www.paulgraham.com/gh.html", "title":"Great Hackers"},
     {"url":"https://www.paulgraham.com/gap.html", "title":"Mind the Gap"},
     {"url":"https://www.paulgraham.com/wealth.html", "title":"How to Make Wealth"},
     {"url":"https://www.paulgraham.com/gba.html", "title":'The Word "Hacker"'},
     {"url":"https://www.paulgraham.com/say.html", "title":"What You Can't Say"},
     {"url":"https://www.paulgraham.com/ffb.html", "title":"Filters that Fight Back"},
     {"url":"https://www.paulgraham.com/hp.html", "title":"Hackers and Painters"},
     {"url":"https://www.paulgraham.com/iflisp.html", "title":"If Lisp is So Great"},
     {"url":"https://www.paulgraham.com/hundred.html", "title":"The Hundred-Year Language"},
     {"url":"https://www.paulgraham.com/nerds.html", "title":"Why Nerds are Unpopular"},
     {"url":"https://www.paulgraham.com/better.html", "title":"Better Bayesian Filtering"},
     {"url":"https://www.paulgraham.com/desres.html", "title":"Design and Research"},
     {"url":"https://www.paulgraham.com/spam.html", "title":"A Plan for Spam"},
     {"url":"https://www.paulgraham.com/icad.html", "title":"Revenge of the Nerds"},
     {"url":"https://www.paulgraham.com/power.html", "title":"Succinctness is Power"},
     {"url":"https://www.paulgraham.com/fix.html", "title":"What Languages Fix"},
     {"url":"https://www.paulgraham.com/taste.html", "title":"Taste for Makers"},
     {"url":"https://www.paulgraham.com/noop.html", "title":"Why Arc Isn't Especially Object-Oriented"},
     {"url":"https://www.paulgraham.com/diff.html", "title":"What Made Lisp Different"},
     {"url":"https://www.paulgraham.com/road.html", "title":"The Other Road Ahead"},
     {"url":"https://www.paulgraham.com/rootsoflisp.html", "title":"The Roots of Lisp"},
     {"url":"https://www.paulgraham.com/langdes.html", "title":"Five Questions about Language Design"},
     {"url":"https://www.paulgraham.com/popular.html", "title":"Being Popular"},
     {"url":"https://www.paulgraham.com/javacover.html", "title":"Java's Cover"},
     {"url":"https://www.paulgraham.com/avg.html", "title":"Beating the Averages"},
     {"url":"https://www.paulgraham.com/lwba.html", "title":"Programming Bottom-Up"},
     {"url":"https://www.paulgraham.com/progbot.html", "title":"Programming Bottom-Up"},
     {"url":"https://www.paulgraham.com/prop62.html", "title":"his Year We Can End the Death Penalty in California"},
]


#to add the scraped data in json format in file.

for essay in essay_url:
    url = essay["url"]
    title = essay["title"]
    essay_text = scrape_essays(url)
    if essay_text:
        adding_json(json_file_path, title, essay_text)
        print(f"Essay '{title}' added to {json_file_path}")
