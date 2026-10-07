TAYSEER: WHERE THE NEXT SAR 40M SHOULD GO
SDAIA Academy - SDA-DSC-112 Data Visualization & Storytelling - Capstone Project

Team: Naif Alnasser, Muaied Alsharef
SDAIA Academy on GitHub: https://github.com/SDAIAAcademy


BIG IDEA
--------
Tayseer has passed 65% digital adoption nationally, but 8 regions holding half
its users are still below target. Concentrating the SAR 40M on the four furthest
behind (Najran, Northern Borders, Al-Baha and Jazan) closes 84% of the
remaining gap and is the fastest route to every region reaching 65%.

OUR ASK
-------
Approve SAR 36M for Najran, Northern Borders, Al-Baha and Jazan, split by the
size of each region's gap, plus a SAR 4M reserve released at a 6-month
checkpoint.


WHAT WE DID
-----------
The capstone question: where should the next SAR 40 million go to lift lagging
regions toward the 65% digital-adoption target?

1. Built the evidence in Tableau.
   An interactive dashboard of Tayseer digital adoption from the course
   dataset (monthly, by region, service category and channel, Jan 2022 to
   Dec 2025).

2. Checked the national picture.
   National adoption reached 66.2% in Dec 2025, up 2.9 points in a year. It
   first crossed 65% in Aug 2025.

3. Found the regional gap.
   8 of 13 regions are still below 65%, and they hold 52% of users.

4. Sized the gap per region.
   For each below-target region we calculated how many users would need to
   move to digital for it to reach 65%, and how long it needs at its current
   pace (Dec 2024 to Dec 2025). Four regions hold 84% of the remaining gap
   and need 7 to 19 months on their own. The other four are within 0.7
   points of 65% and should cross it within about 3 months.

5. Compared three ways to spend SAR 40M.
   Spread it evenly across the 8 regions, target the gap, or run one
   national campaign. Each option was scored on how much money reaches the
   regions that hold the gap.

6. Recommended Option B and set a checkpoint.
   At month 6, each funded region should have closed at least half its gap.
   The SAR 4M reserve then goes to any near-miss region still below 65%.

7. Told it as a 7-slide executive story.
   BLUF/Ask, Situation, Complication, Evidence, Options, Recommendation, and
   Ask + Next step, delivered in 7 minutes.


THE DASHBOARD
-------------
Live dashboard (Tableau Public):
https://public.tableau.com/app/profile/naif.alnasser/viz/TayseerDigitalAdoption/TayseerDigitalAdoption

Sheets:
  KPI                          National digital adoption for the latest month
                               (Dec 2025): 66.2%
  Regional Adoption            Adoption by region, sorted lowest to highest,
                               with a 65% target reference line. Regions are
                               colored Below Target (red) or On/Above Target
                               (gray).
  Tayseer - Digital Adoption   The dashboard: KPI on top, regional bar chart
                               below, a Region filter (multiple-values
                               dropdown, default All) and the color legend.
  National Trend               Monthly national adoption, Jan 2022 to Dec 2025,
                               with the 65% target line (54.1% to 66.2%).
  Target Gaps                  Each below-target region's share of the
                               remaining gap to 65% (Dec 2025): Najran 31%,
                               Northern Borders 20%, Al-Baha 17%, Jazan 16%.
  Tayseer - Evidence           Second dashboard: National Trend above
                               Target Gaps.

Evidence dashboard:
https://public.tableau.com/app/profile/naif.alnasser/viz/TayseerDigitalAdoption/TayseerEvidence

Calculated fields:
  Digital Adoption % = SUM([Digital Adoption Pct] / 100 * [Unique Users])
                       / SUM([Unique Users]) * 100
  Target Status      = IF [Digital Adoption %] < 65 THEN "Below Target"
                       ELSE "On/Above Target" END
  Users to Reach 65  = IF [Digital Adoption %] < 65 THEN
                       (65 - [Digital Adoption %]) / 100 * SUM([Unique Users]) END
  Share of Remaining Gap % = [Users to Reach 65]
                       / WINDOW_SUM([Users to Reach 65]) * 100

Adoption is weighted by unique users, so large regions count more than small
ones.


KEY FINDINGS (DEC 2025)
-----------------------
Region            Adoption   Gap to 65%   Share of gap   Months to 65% at current pace
Najran            60.9%      4.1 pts      31%            ~19
Northern Borders  62.7%      2.3 pts      20%            ~11
Al-Baha           62.8%      2.2 pts      17%            ~7
Jazan             63.0%      2.0 pts      16%            ~8
Asir              64.4%      0.6 pts      7%             ~3
Tabuk             64.5%      0.5 pts      5%             ~2
Hail              64.7%      0.3 pts      2%             ~1
Al-Jouf           64.8%      0.2 pts      2%             <1

Qassim, Madinah, Eastern Province, Makkah and Riyadh are already at or above
65%.

"pts" = percentage points: the difference between two percentages. Najran at
60.9% is 4.1 points short of 65%.

Assisted channels (branch and call centre) still handle about 34% of
transactions in the priority regions. In 2025 an assisted transaction cost
SAR 23-24, compared with SAR 15-16 online, and satisfaction was lower
(CSAT 3.8 against 4.0-4.1 online). Complaints is the weakest service in the
below-target regions, at 58.8% digital. (Channel cost, CSAT and service
figures come from analysis/analyze.py, run on the same dataset.)

The full table is in analysis/regional_gap_dec2025.csv.


THE PRESENTATION
----------------
Tayseer_SAR40M_Capstone_Deck.pptx has 7 slides. Each slide has a takeaway
title, and the speaker notes give the script, timing and presenter.

  #  Slide                                                Presenter        Time
  1  BLUF / Ask: direct the SAR 40M to the four regions   Naif Alnasser    0:00-0:30
     holding 84% of the gap
  2  Situation: nationally, Tayseer passed 65% in         Naif Alnasser    0:30-1:15
     Aug 2025
  3  Complication: 8 of 13 regions (52% of users) are     Naif Alnasser    1:15-2:00
     still below 65%, shown on a regional map
  4  Evidence: Najran, Northern Borders, Al-Baha and      Naif Alnasser    2:00-4:00
     Jazan hold 84% of the remaining gap
  5  Options: three ways to spend SAR 40M, compared in    Muaied Alsharef  4:00-5:15
     one table
  6  Recommendation: SAR 36M split by gap + SAR 4M        Muaied Alsharef  5:15-6:15
     reserve
  7  Ask + next step: approve now, checkpoint at month    Muaied Alsharef  6:15-7:00
     6, target at month 12


TOOLS AND SOFTWARE
------------------
- Tableau Public (web authoring): dashboard, calculated fields, reference line,
  filters
- Python 3 (standard library): reproducible analysis of the gap, pace and
  channel costs (analysis/analyze.py)
- Microsoft PowerPoint: the executive presentation, with native charts, slide
  transitions and a map of Saudi Arabia's 13 regions colored by target status
- Git and GitHub: version control and submission

Map data: geoBoundaries (https://www.geoboundaries.org) Saudi Arabia ADM1, from
(c) OpenStreetMap contributors, licensed under the Open Database License
(ODbL) 1.0: https://opendatacommons.org/licenses/odbl/1-0/


REPRODUCE THE ANALYSIS
----------------------
The dataset (tayseer_services.csv) was provided by SDAIA Academy for the course
and is not included here.

  python analysis/analyze.py path/to/tayseer_services.csv

This prints the national summary and writes analysis/regional_gap_dec2025.csv.

Assumptions:
- "Current pace" means the Dec 2024 to Dec 2025 change continues in a straight
  line.
- "Gap" means the users who would need to move to digital for a region to
  reach 65% (gap in points x unique users).
- The dataset is synthetic course data.


REPOSITORY CONTENTS
-------------------
README.txt                           this file
Tayseer_SAR40M_Capstone_Deck.pptx    7-slide executive presentation
analysis/analyze.py                  reproduces every number in the deck
analysis/regional_gap_dec2025.csv    regional gap table (output of analyze.py)


TEAM
----
Naif Alnasser    (GitHub: Naif-aln)         Tableau dashboard, Situation,
                                            Complication and Evidence
Muaied Alsharef  (GitHub: MuaiedAlsharef)   Options, Recommendation and the Ask
