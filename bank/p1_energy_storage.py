"""Energy resources: secondary fuels, fluctuations in supply and demand, energy storage (spec 3.3.4.1).  Genn pp. 217-224."""
from gen.model import Q, P, Table, Chart, Essay

T = "energy-storage"

QUESTIONS = [
    Q("EST-01", T, "3.3.4.1", "221-222",
      intro="Figure 1 shows the demand for electricity in the UK over a 24-hour period on a weekday in winter.",
      figures=[Chart("line", "Time / hours", "Demand / GW", {"Demand": [(0, 30), (2, 26), (4, 25), (6, 30), (8, 40), (10, 42), (12, 41), (14, 40), (16, 44), (18, 50), (20, 46), (22, 38), (24, 31)]}, y_min=0)],
      parts=[
          P("Describe the pattern of demand shown in Figure 1.", 2,
            ms=["Lowest overnight (about 25 GW at 04:00), rising steeply from 06:00 to about 40 GW by 08:00", "Fairly steady through the day then a peak of about 50 GW at 18:00 (evening) before falling overnight"]),
          P("Explain the causes of the fluctuations shown in Figure 1 and give <b>two</b> other causes of fluctuations in electricity demand.", 4,
            ms=["24-hour day / night cycle: people asleep overnight; morning rise as heating, lighting, cooking, industry and offices start", "Evening peak: lighting, cooking, heating as people return home; short-term 'TV pickup' at programme breaks / mealtimes",
                "Other causes: seasonal (winter heating / lighting, summer air conditioning); weather-related (cold snaps); weekday / weekend differences in industrial use"]),
          P("Explain why base-load power stations (nuclear, large coal) produce a surplus of electricity at night.", 2,
            ms=["They generate 24 hours a day because it is uneconomic / slow to turn them off and on, and output changes slowly", "Demand falls faster at night than output can be reduced, so the surplus must be stored or is lost as heat from cables"]),
          P("Give <b>two</b> causes of fluctuations in energy <b>supply</b>.", 2, items=2,
            ms=["Intermittent renewable resources: wind, solar, tidal", "Bulk delivery of transported fuels (oil tankers, coal trains, biofuel harvests)", "Breakdowns / maintenance of power stations"]),
      ]),

    Q("EST-02", T, "3.3.4.1", "222",
      intro="A pumped-storage HEP station has an upper reservoir 500 m above its turbines. It can hold 7 million m<sup>3</sup> of water. The density of water is 1000 kg m<sup>-3</sup> and g = 9.8 N kg<sup>-1</sup>.",
      parts=[
          P("Describe how pumped-storage HEP is used for peak shaving.", 3,
            ms=["At times of low demand / surplus supply (night, windy periods) surplus electricity pumps water from the lower to the upper reservoir, storing it as gravitational potential energy",
                "At peaks in demand water flows down through the turbines generating electricity", "Can go from standby to full power in under 15 seconds so it meets sudden peaks (TV pickup) that fossil / nuclear stations cannot follow"]),
          P("Calculate the maximum gravitational potential energy stored when the upper reservoir is full. Give your answer in standard form.", 3, calc=True, unit="J",
            ms=["Mass = 7 x 10^6 x 1000 = 7 x 10^9 kg", "PE = m g h = 7 x 10^9 x 9.8 x 500", "= 3.43 x 10^13 J (accept 3.4 x 10^13)"]),
          P("The station returns 75% of the electricity used for pumping. Explain why the process is still worthwhile despite this loss.", 2,
            ms=["The electricity used for pumping is surplus that would otherwise be wasted / lost as heat, or cheap off-peak electricity", "It avoids building rapid-response low-efficiency peaking plants (open-cycle gas turbines) and allows intermittent renewables to be used"]),
          P("Give <b>two</b> locational requirements of a pumped-storage station.", 2, items=2,
            ms=["Two water bodies / sites with a large height difference close together (mountainous)", "Impermeable, stable rock", "Close to the grid / demand", "Adequate water supply"]),
      ]),

    Q("EST-03", T, "3.3.4.1", "219-221",
      parts=[
          P("Explain how hydrogen can be used to store energy from intermittent renewable resources, and describe <b>two</b> ways the stored energy can be released.", 4,
            ms=["Surplus electricity (eg windy nights) electrolyses water to produce hydrogen which is stored", "Hydrogen has a high energy density so it can be transported / stored for long periods",
                "Released by combustion for heat, industrial processes or steam turbines; or by fuel cells combining hydrogen and oxygen electrochemically to produce electricity and water", "Can also be used as a vehicle fuel or converted to methane / ammonia"]),
          P("Compare <b>three</b> methods of storing hydrogen, giving a disadvantage of each.", 3,
            ms=["Compressed gas (up to 700 times normal volume) - energy to run the compressor, strong tanks", "Liquefied at very low temperature - energy for refrigeration and compression",
                "Adsorbed on a metal matrix (metal hydride) at low pressure - tanks larger and heavier than a petrol tank storing the same energy", "Conversion to ammonia - some energy needed but less than the alternatives"]),
          P("Explain how a fuel cell differs from a rechargeable battery.", 2,
            ms=["Both convert chemical energy to electricity electrochemically, but a battery stores a fixed amount of chemicals which are reformed by recharging",
                "A fuel cell keeps producing electricity as long as fresh fuel (hydrogen / alcohol) and oxidant are supplied"]),
          P("Explain what is meant by the 'hydrogen economy'.", 1,
            ms=["Using hydrogen made from surplus renewable electricity as the main store and carrier of energy, released when demand exceeds supply or intermittent sources fail, for heating, vehicles and electricity"]),
      ]),

    Q("EST-04", T, "3.3.4.1", "223-224",
      intro="Table 1 shows features of three rechargeable battery types.",
      figures=[Table(["Battery type", "Energy density / Wh kg^-1", "Charge-discharge cycles", "Storage efficiency / %", "Cost per kWh / &pound;", "Safety issues"], [["Lead-acid", "35", "500", "80", "100", "Toxic lead, acid"], ["Nickel-cadmium", "50", "1500", "75", "250", "Toxic cadmium"], ["Lithium-ion", "200", "2000", "92", "150", "Fire risk"]])],
      parts=[
          P("Use Table 1 to explain why lithium-ion batteries are used in electric vehicles but lead-acid batteries are still used for stationary storage in some off-grid solar systems.", 4,
            ms=["Vehicles: high energy density (200 Wh kg^-1) minimises battery mass so range is greater; many cycles and high efficiency",
                "Stationary storage: mass is unimportant so the low energy density of lead-acid does not matter; lowest cost per kWh; well-established, recyclable",
                "Lead-acid drawbacks: fewer cycles and lower efficiency; lithium fire risk needs management", "Nickel-cadmium largely replaced because of cadmium toxicity and cost"]),
          P("Give <b>two</b> other factors that affect the viability of a rechargeable battery.", 2, items=2, ms=["Recharging speed", "Self-discharge during non-use", "Availability of raw materials (lithium, cobalt)", "Recyclability / disposal"]),
          P("Describe how Vehicle-to-Grid (V2G) systems could reduce the need for peaking power stations.", 2,
            ms=["Parked electric vehicles plugged into the grid form a very large distributed battery", "At peaks a small proportion of their stored energy is fed back to the grid; surplus grid energy recharges them - avoiding costly, low-efficiency open-cycle gas turbines"]),
          P("Explain how Power-to-Gas (P2G) systems use existing infrastructure.", 2,
            ms=["Surplus electricity electrolyses water to hydrogen, which can be converted to methane", "Methane is fed into the existing natural gas pipe network and storage, so no new distribution system is needed"]),
      ]),

    Q("EST-05", T, "3.3.4.1", "222-224",
      parts=[
          P("Explain why compressed air energy storage with heat recovery can achieve over 90% efficiency.", 2,
            ms=["Surplus energy drives a pump compressing air stored in underground caverns (salt mines); releasing it drives machinery / turbines", "Compression produces a lot of heat; storing this heat (hot oil / molten salt) and returning it when the air expands recovers energy that would otherwise be lost"]),
          P("Explain why large-volume hot water stores lose heat more slowly per unit of stored energy than small ones.", 2,
            ms=["As volume increases the surface area : volume ratio decreases", "Heat is lost through the surface so there is less surface per unit of stored heat; very large stores can carry summer solar heat into winter (inter-seasonal storage)"]),
          P("Explain why molten salt rather than water is used to store heat from CSP plants.", 2,
            ms=["Potassium nitrate has a much higher boiling point so it stores heat at up to 550 &deg;C without pressurisation", "Water could only reach such temperatures under high pressure, increasing costs; high temperature needed to raise steam for turbines"]),
          P("Explain how high thermal mass building materials reduce energy use.", 2,
            ms=["Materials with high specific heat capacity (concrete, water) warm and cool slowly", "They absorb heat in hot weather reducing overheating / air conditioning, and release it as the weather cools, delaying the need for heating"]),
          P("Describe <b>one</b> other energy storage technology.", 2,
            ms=["Flywheels: rotating mass stores kinetic energy for short-term smoothing / generation", "Supercapacitors: electrochemical capacitors with 10-100 times the energy density of conventional capacitors; possible future large-scale electricity storage", "Thermal storage in molten salt / high-volume tanks; hydrogen / P2G; batteries"]),
      ]),

    Q("EST-06", T, "3.3.4.1", "217-224",
      parts=[
          P("Explain why the development of energy storage technologies is essential if renewable energy resources are to provide most of a country's electricity.", 9, level=True,
            ms=["Renewables are intermittent (solar at night, calm days, slack tides) and some unpredictable; demand fluctuates daily, weekly, seasonally and short-term; supply and demand rarely match",
                "Without storage, surplus is wasted and shortages must be met by fossil-fuel peaking plants; large-scale electricity storage not yet possible directly so energy must be converted",
                "Pumped-storage HEP: proven, rapid response, peak shaving, but limited sites", "Batteries: lithium-ion for grid and vehicles; factors affecting viability; V2G",
                "Hydrogen: electrolysis, storage methods, fuel cells, hydrogen economy, P2G into the gas grid; high energy density enables vehicle use", "Compressed air with heat recovery; thermal storage (molten salt for CSP, high-volume stores, thermal mass); flywheels; supercapacitors",
                "Grid management / ICT and diversity of resources (wind + solar + tidal + biofuel) reduce but do not remove the need for storage; energy conservation reduces peaks",
                "Evaluation of efficiency losses, costs, resource limits (lithium), and which technologies suit short-term vs inter-seasonal storage; judgement"]),
          P("State what is meant by <b>peak shaving</b>.", 1, ms=["Storing surplus energy at times of low demand / high supply to meet later peaks in demand, so peak generating capacity can be reduced"]),
      ]),
]

ESSAYS = []
