"""Revision notes: Energy resources (spec 3.3).  Genn pp. 170-235."""

NOTES = {
# =====================================================================
"energy-features": {
    "summary": "Energy use rises with affluence and changes with industry, climate and technology. Each resource has a profile of features - renewability, energy density, intermittency, location, storage, transport, technology, impacts, politics and economics - that decides what it is good for and how sustainable it is. Fossil fuels dominate today; the transition must begin before depletion forces it.",
    "sections": [
        ("The importance of energy and factors affecting use", "170-174",
         "<ul><li><b>Per capita energy consumption</b> rises with <b>affluence</b>: more appliances, cars, travel, heating and cooling, and the embodied energy of consumer goods. Energy use per person differs by more than 100 times between the richest and poorest countries.</li>"
         "<li><b>Relative cost of energy</b> shapes demand: cheap energy is used less carefully.</li><li><b>Type of industry:</b> heavy industry (steel, aluminium, cement) uses far more than light manufacturing or services.</li>"
         "<li><b>Climate:</b> heating in cold countries, air conditioning in hot ones.</li><li><b>Social and environmental awareness</b> and <b>how energy is used</b> (efficiency of buildings, transport choices).</li>"
         "<li><b>Changes in energy use:</b> historic shift from wood to coal to oil and gas, now towards electricity, renewables and gas; growth concentrated in developing economies.</li></ul>"),
        ("Features of energy resources", "175-179",
         "<table class=\"nt\"><tr><th>Feature</th><th>Meaning and examples</th></tr>"
         "<tr><td>Renewable / non-renewable</td><td>Replaced as used (solar, wind, HEP, biofuels) or not (fossil fuels, uranium)</td></tr>"
         "<tr><td>Depletable / non-depletable</td><td>Renewables can still be depleted by over-use (over-cut biofuel forests, over-abstracted geothermal heat); solar and wind cannot</td></tr>"
         "<tr><td>Abundance</td><td>Total resource available, eg huge solar and wind resources vs limited HEP sites</td></tr>"
         "<tr><td>Locational constraints</td><td>Where the resource can be harnessed: wind speed, tidal range, rainfall and relief for HEP, geothermal heat flow, coal seams; power stations also need cooling water, land, grid access</td></tr>"
         "<tr><td>Intermittency</td><td>Availability varies over time - solar at night, wind on calm days, tidal at slack water</td></tr>"
         "<tr><td>Predictability</td><td>Tides are exactly predictable; wind and sunshine only approximately</td></tr>"
         "<tr><td>Energy density</td><td>Energy per unit mass or volume - very high for uranium and fossil fuels, low for wind, solar and biomass so large collectors are needed</td></tr>"
         "<tr><td>Need for energy conversions</td><td>Most resources must be converted (heat to electricity, light to electricity) and each conversion loses energy</td></tr>"
         "<tr><td>Applicability to uses</td><td>Electricity vs heat vs transport fuel; liquid fuels dominate transport because of energy density and storage</td></tr>"
         "<tr><td>Ease of storage</td><td>Coal, oil and gas store easily; electricity does not; heat can be stored in thermal masses</td></tr>"
         "<tr><td>Ease of transport</td><td>Pipelines, tankers, grid; biomass is bulky; hydrogen is difficult</td></tr>"
         "<tr><td>Environmental impacts</td><td>Before use (extraction, embodied energy of equipment) and as a consequence of use (pollution, habitat damage, depletion)</td></tr>"
         "<tr><td>Technological development</td><td>Mature (fossil fuels, HEP) vs developing (wave, fusion); cost falls as technology matures</td></tr>"
         "<tr><td>Political and economic influences</td><td>Subsidies, guaranteed prices, planning, energy security, concentration of oil in the Middle East, external costs not in the price</td></tr></table>"),
        ("Sustainability of energy resources", "180-182",
         "<p><b>Resource depletion:</b> non-renewables run down; new discoveries of conventional oil have declined since the 1980s. <b>Economic sustainability:</b> rising extraction costs, price volatility, need for investment. <b>Environmental impacts:</b> climate change, acid rain, smoke, habitat loss, radioactive waste. <b>Future energy supplies:</b> a diverse mix matched to uses, energy conservation to reduce demand, storage and grid development, and starting the transition before depletion - because building new infrastructure takes decades.</p>"),
    ],
    "diagrams": [
        {"type": "chart", "title": "Energy density of selected resources (MJ per kg, approximate)", "kind": "bar", "x_label": "", "y_label": "MJ kg-1",
         "series": {"Energy density": [("Wood", 15), ("Coal", 25), ("Oil", 42), ("Natural gas", 50), ("Hydrogen", 120)]}, "y_min": 0, "y_max": 130,
         "caption": "Illustrative values (Genn pp. 177, 183). Uranium is millions of MJ per kg - off the scale; wind and solar have no fuel mass at all, which is why collectors must be large."},
    ],
    "numbers": ["Energy use per person varies more than 100-fold between countries", "Conventional oil discoveries have declined since the 1980s"],
    "exam": ["Complete a table of resource features (tick boxes: renewable, intermittent, high energy density...) - specimen Q1.", "Interpret electricity generation mix data (Pakistan, June 2023 Q5; UK 1990-2020, June 2024 Q2).",
             "Explain why a feature (energy density, intermittency, location) limits a resource's use.", "Essays: properties of energy resources and reducing impacts (June 2023); factors affecting choice of resources (June 2024); new technologies (specimen)."],
},
# =====================================================================
"fossil-nuclear": {
    "summary": "Fossil fuels are chemical energy stores of high energy density but finite, polluting and politically concentrated; new technologies extend supplies at rising cost. Nuclear fission offers very high energy density and low-carbon base load but faces cost, waste and public opposition; breeder and thorium reactors and fusion could extend it far into the future.",
    "sections": [
        ("Features of fossil fuels", "183-184",
         "<p>Coal, oil and natural gas are <b>chemical energy</b> from ancient biomass; <b>high energy density</b>, easily stored and transported, usable for heat, electricity and transport with mature technology. But they are <b>finite</b>: the available resource depends on price, technology and whether extraction causes unacceptable pollution; oil is concentrated politically (Middle East) causing <b>international trade problems</b>; prices are volatile.</p>"),
        ("Extraction and its impacts", "185-186",
         "<ul><li><b>Coal:</b> open-cast (overburden removal, land take, dust, noise) or deep mining (subsidence, spoil heaps, methane, acid mine drainage).</li>"
         "<li><b>Oil and gas:</b> drilling on land and offshore; pipelines fragment habitats; spills; flaring; subsidence; produced water.</li></ul>"),
        ("New technologies: coal", "187",
         "<p><b>Coal gasification</b> (reacting coal with steam and oxygen to make syngas, cleaner burning, can be done underground in unminable seams) and <b>coal liquefaction</b> (converting coal to liquid fuels) extend coal's uses but are energy-intensive.</p>"),
        ("New technologies: oil", "187-189",
         "<ul><li><b>Primary recovery</b> uses natural pressure - about 20% of the oil; <b>secondary recovery</b> injects water or gas to maintain pressure; <b>tertiary (enhanced) recovery</b> pumps down steam to thin heavy oil, detergents or solvents to reduce surface tension, CO<sub>2</sub>, or bacteria that partly digest heavy oil - together raising recovery to about 60%.</li>"
         "<li><b>Directional drilling</b> reaches many deposits from one platform; <b>subsea wells</b> and ROVs open deep water.</li>"
         "<li><b>Fracking</b> (hydraulic fracturing): water, sand and chemicals pumped at high pressure open shale releasing tight oil and gas. Concerns: contamination of aquifers, huge water use, disposal of flow-back fluid, small earth tremors, methane leaks, land take, extended fossil-fuel dependence.</li>"
         "<li><b>Tar sands and oil shales:</b> mined or heated in place to extract bitumen - high energy input, land and water impacts (Alberta).</li></ul>"),
        ("New technologies: gas and CCS", "190",
         "<p><b>Enhanced gas recovery</b>; <b>methane hydrates</b> (methane frozen in seabed sediments - vast resource, risky to exploit); <b>carbon capture and storage</b> - CO<sub>2</sub> captured from flue gases, compressed and pumped into depleted fields or saline aquifers; reduces emissions but costs energy and is unproven at scale.</p>"),
        ("Nuclear fission", "191-194",
         "<p>Splitting uranium-235 (or plutonium-239) nuclei with neutrons releases heat that raises steam for turbines; the chain reaction is controlled with moderators and control rods. <b>Features:</b> extremely high energy density (few fuel deliveries), reliable base load, low CO<sub>2</sub>; but uranium is finite and low-grade ores need much energy to process; <b>technology</b> is complex; <b>political</b> difficulties (proliferation, siting); <b>economic</b> issues (huge capital cost, overruns, decommissioning, long-lived waste); public opposition after Chernobyl and Fukushima. <b>Uranium extraction:</b> open-cast, underground, in-situ leaching; new sources - phosphate mining by-product, coal ash, polymer adsorption from seawater. <b>New reactor designs:</b> small modular reactors, molten-salt reactors (safer, can use thorium), <b>plutonium fast breeder reactors</b> that make more fuel than they use from U-238, and <b>thorium reactors</b> - thorium is more abundant than uranium and produces less long-lived waste.</p>"),
        ("Nuclear fusion", "195-196",
         "<p>Fusing deuterium (from seawater) and tritium (bred from lithium) at very high temperatures in a magnetically confined plasma (tokamak) releases enormous energy with little long-lived waste and no chain reaction risk. Still experimental (ITER); not expected to be commercial for decades.</p>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Oil recovery stages", "nodes": [("p", "Primary: natural\npressure ~20%", 0, 0), ("s", "Secondary: water /\ngas injection", 1, 0), ("t", "Tertiary: steam, solvents,\nCO2, bacteria -> ~60%", 2, 0), ("u", "Unconventional: fracking,\ntar sands, oil shale", 3, 0)],
         "kinds": {"u": "warn"}, "edges": [("p", "s"), ("s", "t"), ("t", "u")], "caption": "Each stage costs more energy and money per barrel and has greater environmental impact (Genn pp. 187-189)."},
    ],
    "numbers": ["Primary recovery ~20% of oil in place; tertiary recovery raises it to ~60%", "Thorium more abundant than uranium; breeder reactors multiply usable fuel", "Fusion fuel: deuterium (seawater) + tritium (from lithium)"],
    "exam": ["Explain how plutonium and thorium reactors release energy; compare isotope half-lives and health risks (June 2022 Q2).", "Uranium ore grade vs energy to extract (Nov 2020 Q3, 15 marks).",
             "Fracking: process and concerns; CCS process.", "9-mark: can new technologies keep fossil fuels and nuclear supplying energy sustainably? Essay on energy technologies (specimen)."],
},
# =====================================================================
"renewables": {
    "summary": "Renewable resources - solar, HEP, wind, wave, tidal, biofuels, geothermal - are inexhaustible but mostly intermittent, low in energy density and tied to particular locations. New technologies keep improving how they are harnessed and reducing their impacts; their contribution depends on storage and a diverse mix.",
    "sections": [
        ("General features of renewables", "196-198",
         "<p><b>Intermittency and predictability</b> (tides predictable; wind, wave and sun less so); <b>low energy density</b> so large collectors; <b>application</b> mostly to electricity, less to heat and transport (biofuels the exception); <b>geographical constraints</b>; <b>environmental impacts</b> mainly from equipment manufacture and land use; <b>technological development</b> uneven (HEP mature, wave immature); <b>economic issues</b> - high capital, low running costs, falling prices, subsidies.</p>"),
        ("Solar power", "199-203",
         "<p><b>Problems:</b> intermittent (day/night, seasons), unreliable (cloud), low energy density, changing angle of incidence. <b>Location:</b> best in sunny deserts; concentrating systems need cloudless skies; high latitudes have long summer days but weak winters. <b>Harnessing:</b> <b>photothermal panels</b> heat water (evacuated tubes minimise losses; thermal stores keep heat); <b>passive solar architecture</b> (south-facing glazing, atria, brise soleil, light tubes); <b>heat pumps</b> move low-grade heat from ground or air using a compressor and expansion valve, delivering up to four times the energy used; <b>photovoltaic cells</b> release electrons when photons are absorbed - efficiencies vary with cost; solar farms and rooftops. <b>Impacts:</b> toxic wastes in manufacture (silicon tetrachloride, cadmium), water for cleaning, land use. <b>New technologies:</b> multijunction cells, anti-reflective moth-eye surfaces (smooth cells reflect 30%), concentrating solar power with molten-salt storage to 550 &deg;C, PV-thermal hybrids, transparent PV, heliostats, self-cleaning surfaces.</p>"),
        ("Hydroelectric power", "203-205",
         "<p>Gravitational potential energy of rain on high ground. <b>Site requirements:</b> large catchment, high evenly distributed rainfall, low turbidity, impermeable bedrock, low seismic activity, narrow exit to a large basin, few land-use conflicts, near the grid. <b>Impacts on flow regime:</b> reduced floods and sediment downstream, changed temperature and oxygen, barriers to fish, drowned habitats and settlements, methane from vegetation, evaporation. <b>Types:</b> large dams (Three Gorges), run-of-river, <b>micro-hydro</b> for isolated communities, low-head and helical turbines; pumped storage (see energy storage).</p>"),
        ("Wind power", "206-209",
         "<p><b>Aerogenerators</b> absorb kinetic energy; output rises with the cube of wind speed and with rotor area, so bigger and taller turbines and steady sites (offshore, hills, coasts) are favoured. <b>Horizontal-axis (HAWT)</b> most common; <b>vertical-axis (VAWT)</b> accept wind from any direction, are quieter and can be closer together but less efficient. <b>Locational constraints:</b> wind speed and reliability, land availability, distance to grid, shallow seas for offshore. <b>Impacts:</b> visual, noise, bird and bat strikes, shadow flicker, habitat disturbance during construction, embodied energy - offset within months. <b>New technologies:</b> direct-drive generators, larger offshore turbines, floating platforms, wind lens designs, airborne turbines.</p>"),
        ("Wave power", "210-211",
         "<p>Waves carry kinetic energy greatest where fetch and wind are large - the UK Atlantic coast. Devices: oscillating water columns, floating attenuators (Pelamis), point absorbers, overtopping devices. Constraints: storm survival, corrosion, distance to grid, conflicts with shipping and fishing; technology still immature.</p>"),
        ("Biofuels", "212-213",
         "<p>Wood, charcoal, energy crops (miscanthus, willow coppice), crop residues, <b>biodiesel</b> from oil crops, <b>bioethanol</b> from sugar and starch, <b>biogas</b> from anaerobic digestion of wastes, landfill gas. <b>Advantages:</b> renewable, storable, can replace liquid transport fuels, use wastes, carbon-neutral in principle. <b>Disadvantages:</b> low energy density, competition with food for land and water, habitat loss (palm oil), fertiliser and energy inputs may exceed the benefit, smoke. <b>New:</b> second-generation fuels from cellulose, algae.</p>"),
        ("Geothermal power", "213-214",
         "<p>Heat from the Earth's interior: high-temperature schemes generate electricity where hot rocks are near the surface (Iceland, New Zealand); low-temperature schemes and ground-source heat pumps work almost anywhere. Impacts: release of dissolved gases (H<sub>2</sub>S, CO<sub>2</sub>), subsidence, induced tremors; heat can be depleted locally. <b>New:</b> hot dry rock (enhanced geothermal) fracturing deep granite and circulating water.</p>"),
        ("Tidal power", "214-217",
         "<p>Predictable, driven by the Moon's gravity. <b>Barrages</b> across estuaries with large tidal range (Severn, Rance) - large output but very high cost, loss of inter-tidal habitat, changed sedimentation, shipping obstruction; <b>tidal lagoons</b> (Swansea Bay proposal) and <b>in-stream turbines</b> in fast currents (Pentland Firth) have lower impacts. Constraints: few suitable sites; output follows the tidal cycle, so still intermittent though predictable.</p>"),
        ("Secondary fuels", "217-221",
         "<p>Electricity and hydrogen are <b>secondary fuels</b> made from primary resources. Electricity is generated from kinetic energy (turbines), light (PV) or chemical energy (fuel cells) and transported by grid. <b>Hydrogen</b> made by electrolysis (or from natural gas) can be stored as compressed gas, liquid or in metal hydrides and used in fuel cells or engines - the 'hydrogen economy' - but storage and conversion losses are large.</p>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Ground-source heat pump", "nodes": [("g", "Ground / air:\nlow-grade heat", 0, 0), ("ev", "Evaporator: refrigerant\nboils, absorbing heat", 1, 0), ("comp", "Compressor: pressure up,\ngas condenses -> heat out", 2, 0), ("h", "Building heated\n(up to 4x energy input)", 3, 0), ("ex", "Expansion valve:\npressure drops, liquid boils", 2, 1)],
         "kinds": {"h": "hi"}, "edges": [("g", "ev"), ("ev", "comp"), ("comp", "h"), ("comp", "ex"), ("ex", "ev")], "caption": "Genn pp. 200-201. The change of state of the refrigerant moves heat from a cold source to a warm building."},
        {"type": "chart", "title": "Wind turbine power output rises steeply with wind speed", "kind": "line", "x_label": "Wind velocity / m s-1", "y_label": "Power / kW",
         "series": {"Output": [(3, 5), (5, 60), (7, 170), (9, 380), (11, 700), (13, 1100), (14, 1300), (16, 1300), (20, 1300)]}, "y_min": 0, "y_max": 1500,
         "caption": "Power rises with the cube of wind speed until the rated output is reached, then is capped (Genn pp. 206-207; specimen Q4)."},
    ],
    "numbers": ["Heat pumps deliver up to 4x the energy used to run them", "Smooth PV cells reflect ~30% of light; CSP molten salt stored at 550 &deg;C", "Wind power proportional to (wind speed)<sup>3</sup>"],
    "exam": ["Explain problematic properties of solar / wind and how new technologies address them (June 2024 Q2 VAWTs; Nov 2020 Q5 wind lens; Nov 2021 Q8 solar PV).", "Use a power-output graph to estimate changes (specimen Q4).",
             "Energy density of biofuels and why low-density elephant grass is still grown (June 2022 Q4).", "Wave energy devices (June 2022 Q6, MCQ).", "9-mark: potential of renewables in the UK; solar technologies; essay on new technologies and energy impacts."],
},
# =====================================================================
"energy-storage": {
    "summary": "Supply and demand fluctuate on every timescale and renewables are intermittent, so energy must be stored in another form - pumped water, batteries, hydrogen, compressed air, heat, flywheels - and the grid managed intelligently. Storage is the key to renewables providing most of a country's electricity.",
    "sections": [
        ("Fluctuations in supply and demand", "221-222",
         "<p><b>Supply</b> fluctuates because renewables are intermittent (solar daily and seasonal, wind unpredictable, tidal on a lunar cycle) and because power stations need maintenance. <b>Demand</b> fluctuates <b>seasonally</b> (winter heating and lighting), over <b>24 hours</b> (morning and evening peaks, night trough) and in <b>short-term surges</b> (advertising breaks, kettles). Base load is met by nuclear and large fossil plants that cannot change output quickly; peaks by gas turbines, HEP and storage.</p>"),
        ("Pumped-storage HEP", "222",
         "<p>Surplus (cheap night-time or windy) electricity pumps water from a lower to an upper reservoir; at peak demand it flows back through turbines (Dinorwig can reach full output in seconds). Proven, efficient (about 70-80% round trip), long-lived; but needs suitable mountain sites and floods land.</p>"),
        ("Chemical energy: batteries and hydrogen", "220-221, 223",
         "<p><b>Rechargeable batteries</b> (lithium-ion, flow batteries) now store grid electricity and power vehicles; <b>viability</b> depends on energy density, cost, lifetime (charge cycles), charging speed, safety, and scarce materials (lithium, cobalt); <b>vehicle-to-grid</b> lets parked cars act as distributed storage. <b>Hydrogen:</b> made by <b>electrolysis</b> with surplus electricity, stored compressed, liquefied or in hydrides, and converted back in <b>fuel cells</b> (hydrogen + oxygen &rarr; electricity + water) or injected into the gas grid (<b>power-to-gas</b>); high energy density per kg suits vehicles and seasonal storage, but each conversion loses energy and storage is difficult.</p>"),
        ("Other storage technologies", "223-224",
         "<ul><li><b>Compressed air</b> pumped into caverns, with heat recovery to raise efficiency.</li><li><b>Thermal storage:</b> molten salt at concentrating solar plants, hot-water tanks, high-volume stores for district heating, thermal mass in buildings, ice storage for cooling.</li>"
         "<li><b>Flywheels</b> and <b>supercapacitors</b> for very short-term smoothing.</li><li><b>Gravity storage</b> (raising weights) and liquid-air storage under development.</li></ul>"),
        ("Managing the mismatch without storage", "235",
         "<p>A <b>diverse mix</b> (wind + solar + tidal + biofuel) smooths supply; <b>high-voltage grid links</b> and interconnectors move power between regions; <b>IT / smart-grid management</b> shifts demand (smart meters, time-of-use tariffs, controlled charging); <b>energy conservation</b> reduces peaks. These reduce but do not remove the need for storage, and seasonal storage remains the hardest problem.</p>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Pumped-storage HEP", "nodes": [("sur", "Surplus electricity\n(night / windy)", 0, 0), ("pump", "Pump water to\nupper reservoir", 1, 0), ("up", "Upper reservoir:\ngravitational PE", 2, 0), ("turb", "Water flows down\nthrough turbines", 2, 1), ("peak", "Electricity at\npeak demand", 1, 1)],
         "kinds": {"sur": "hi", "peak": "hi"}, "edges": [("sur", "pump"), ("pump", "up"), ("up", "turb"), ("turb", "peak")], "caption": "Genn p. 222. Round-trip efficiency about 70-80%; response time seconds."},
        {"type": "chart", "title": "UK electricity demand over 24 hours (illustrative)", "kind": "line", "x_label": "Hour", "y_label": "Demand / GW",
         "series": {"Demand": [(0, 26), (3, 23), (6, 27), (8, 35), (12, 36), (16, 38), (18, 42), (20, 38), (23, 29)]}, "y_min": 0, "y_max": 50,
         "caption": "Night trough, morning rise, evening peak - the shape behind June 2023 Q6 (Genn p. 222)."},
    ],
    "numbers": ["Pumped storage round-trip efficiency ~70-80%; Dinorwig reaches full output in seconds", "Fuel cell: hydrogen + oxygen -> electricity + water"],
    "exam": ["Interpret a 24-hour supply/demand graph and suggest advantages of nuclear (base load) and pumped storage (June 2023 Q6).", "Explain hydrogen fuel cells and energy conversions (Nov 2020 Q6).",
             "Name and describe storage technologies (June 2024 Q2).", "9-mark: why storage is essential for a renewable-based grid; evaluate technologies for short-term vs seasonal storage."],
},
# =====================================================================
"energy-conservation": {
    "summary": "Using less energy for the same service is the cheapest and cleanest 'resource'. Transport, buildings and industry each have design, technology and behavioural options, and the electricity system itself can waste less through CHP, grid management and peak shaving.",
    "sections": [
        ("Transport", "225-228",
         "<ul><li><b>Bulk transport</b> (ships, trains, pipelines) uses far less energy per tonne-km than lorries or aircraft; mode choice also depends on speed, flexibility, cost and infrastructure.</li>"
         "<li><b>Vehicle design:</b> aerodynamics (lower drag), lighter materials (aluminium, composites, high-strength steel), low rolling-resistance tyres, smaller efficient engines, hybrid and electric drives, <b>regenerative braking / KERS</b> storing braking energy, stop-start systems, <b>fuel combustion efficiency</b> (direct injection, turbocharging, lean burn), design for end of life (recyclable, low <b>embodied energy</b>).</li>"
         "<li><b>Mode of vehicle use:</b> car sharing, public transport, cycling, walking, avoiding congestion, driving style, speed limits, home working, planning that reduces the need to travel.</li></ul>"),
        ("Buildings", "228-233",
         "<ul><li><b>Orientation</b> and passive solar gain; <b>building surface area</b> (compact shapes, terraces lose less heat); <b>high thermal mass</b> materials store heat and even out temperatures; <b>low embodied energy</b> materials (timber, recycled); <b>earth-sheltered</b> buildings.</li>"
         "<li><b>Insulation:</b> loft, cavity and solid-wall insulation, double / triple glazing, draught-proofing; <b>U-values</b> measure heat loss (lower is better); improved materials (aerogels, vacuum panels).</li>"
         "<li><b>Ventilation with heat recovery</b> (warm outgoing air heats incoming air); automatic ventilation; <b>occupancy sensors</b> and <b>programmable thermostats</b>; efficient water heating and appliances (heat pump water heaters, fridge waste heat); LED lighting uses a fraction of the electricity of filament bulbs.</li>"
         "<li><b>Human behaviour:</b> lower thermostat settings, closing curtains, switching off - often the largest saving and the hardest to achieve.</li></ul>"),
        ("Industry", "233-234",
         "<ul><li><b>Heat recovery</b> from furnaces and processes; <b>combined heat and power (CHP)</b> using the waste heat of electricity generation for heating (efficiency from about 35% to over 80%); <b>district heating</b> with high-volume heat stores.</li>"
         "<li><b>Integrated manufacture</b> so heat from one process feeds the next; <b>recycling</b> (recycled aluminium and steel need a fraction of primary energy); <b>mass reduction</b> - lighter products need less material and transport energy; more efficient motors, drives and lighting.</li></ul>"),
        ("Electricity infrastructure", "235",
         "<p><b>Peak shaving</b> with pumped-storage HEP and demand management avoids building extra power stations; the <b>high-voltage grid</b> reduces transmission losses; <b>IT management</b> (smart grids, smart meters, dynamic pricing) matches supply to demand and integrates renewables.</p>"),
    ],
    "diagrams": [
        {"type": "chart", "title": "Insulation thickness vs heat loss: diminishing returns", "kind": "line", "x_label": "Fibreglass thickness / mm", "y_label": "U-value / W m-2 K-1",
         "series": {"U-value": [(0, 2.3), (50, 0.7), (100, 0.4), (150, 0.28), (200, 0.22), (270, 0.16), (300, 0.15)]}, "y_min": 0, "y_max": 2.5,
         "caption": "The first 100 mm gives most of the benefit (Genn pp. 229-230; June 2022 Q5). Lower U-value = less heat loss."},
    ],
    "numbers": ["CHP raises overall efficiency from ~35% to over 80%", "LED lamps use a small fraction of a filament bulb's electricity", "Recycled aluminium needs ~5% of primary energy"],
    "exam": ["Interpret U-value / insulation data and explain diminishing returns (June 2022 Q5).", "Explain how named vehicle or building design features reduce energy use (6 marks, 2 each).",
             "Explain CHP, regenerative braking, heat recovery, smart grids.", "Essay: extent to which energy conservation reduces environmental impacts (Nov 2021)."],
},
}
