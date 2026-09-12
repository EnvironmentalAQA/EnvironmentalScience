"""Energy resources: energy conservation - transport, buildings, industry (spec 3.3.4.2).  Genn pp. 225-235."""
from gen.model import Q, P, Table, Chart, Essay

T = "energy-conservation"

QUESTIONS = [
    Q("ECON-01", T, "3.3.4.2.1", "225-228",
      intro="Table 1 shows the energy used per passenger-kilometre by different forms of transport when carrying a typical load.",
      figures=[Table(["Mode of transport", "Typical occupancy", "Energy use / MJ per passenger-km"], [["Car (petrol, 1 occupant)", "1", "2.9"], ["Car (petrol, 4 occupants)", "4", "0.7"], ["Bus (diesel)", "25", "0.6"], ["Electric train", "200", "0.3"], ["Bicycle", "1", "0.06"], ["Short-haul aircraft", "120", "2.4"]])],
      parts=[
          P("Calculate the percentage reduction in energy per passenger-km achieved by carrying four people in a car instead of one.", 1, calc=True, unit="%", ms=["(2.9 - 0.7) / 2.9 x 100 = 75.9% (accept 76%)"]),
          P("Explain why bulk transport (buses, trains) uses less energy per passenger-km than cars.", 2,
            ms=["Although the larger vehicle uses more energy in total, it carries many more people / a larger load", "So the energy per passenger (or per tonne of goods) is lower; steel wheels on rails also have low rolling resistance"]),
          P("Suggest <b>three</b> reasons why people continue to use cars despite the energy advantages of public transport.", 3, items=3,
            ms=["Flexibility of routes / destinations and door-to-door convenience", "Time / speed and reliability where public transport is infrequent", "Low fuel tax / cheap fuel", "Carrying goods; comfort; status"]),
          P("Explain how integrated transport systems and Active Traffic Management reduce energy use.", 4,
            ms=["Integrated systems (park and ride, bicycles on trains, linked timetables) make it convenient to use the most efficient mode for each part of a journey",
                "So more journeys shift from cars to bulk transport / cycling", "ATM / smart motorways use variable speed limits to prevent congestion and keep traffic flowing freely",
                "Vehicles avoid stop-start driving and run nearer their optimum speed (about 56 mph), reducing fuel wasted in acceleration and idling"]),
      ]),

    Q("ECON-02", T, "3.3.4.2.1", "225-227",
      parts=[
          P("Explain how each of the following features of vehicle design reduces energy use.", 6,
            labels=["Aerodynamics", "Reduced mass", "Regenerative braking (KERS)"],
            ms=["Aerodynamic shapes / fairings reduce friction with the air (air resistance) so less energy is needed to propel the vehicle, especially at speed; hydrodynamics for ships",
                "Reduced mass (plastics, carbon-fibre composites, high-strength steel alloys, aluminium engine blocks, lighter batteries and magnets, rounded shapes) means less energy to accelerate and less rolling resistance, so lower fuel consumption",
                "Conventional friction brakes convert kinetic energy to waste heat; regenerative braking uses a generator to convert it to electricity stored in a battery (or returned to the rail grid) which then propels the vehicle, so less fuel is needed to accelerate again"]),
          P("Explain why solid steel wheels on rails lose less energy than pneumatic tyres on roads.", 2,
            ms=["Pneumatic tyres deform as they rotate; the continual change in shape and air movement inside generates frictional heat (more if under-inflated)", "Steel wheels do not deform so rolling resistance is very low"]),
          P("Describe <b>two</b> ways combustion efficiency in an internal combustion engine can be improved.", 2, items=2,
            ms=["More valves per cylinder to remove exhaust gases fully so they do not mix with fresh fuel", "Better temperature control (thermostatic fan)", "Electronic ignition control / regular servicing to keep spark timing correct", "Turbochargers supplying more oxygen"]),
      ]),

    Q("ECON-03", T, "3.3.4.2.1", "227-228",
      parts=[
          P("Explain what is meant by the <b>embodied energy</b> of a vehicle and how it can be reduced.", 3,
            ms=["The energy used to extract raw materials, manufacture the components and assemble the vehicle (for a typical car about 1.5 years of its fuel use)",
                "Reduced by using recycled materials (eg recycled aluminium needs 1/20 of the energy of new)", "Lighter designs using less material; longer vehicle life spreading the embodied energy"]),
          P("Describe <b>four</b> principles of designing vehicles for end of life.", 4, items=4,
            ms=["Use of recyclable materials wherever possible", "Easy identification of components and their composition (code stamps)", "Easy dismantling and separation of components / materials",
                "Reusable components for new vehicles", "Compostable materials for parts that cannot be recycled"]),
          P("Explain why there is an optimum speed for fuel efficiency in a car.", 2,
            ms=["At low speed a large proportion of the energy just runs the engine rather than moving the car", "At high speed energy is wasted overcoming air resistance (which rises with the square of speed); optimum for many cars about 56 mph"]),
          P("Give <b>one</b> way driver behaviour or vehicle systems can reduce fuel use in congested traffic.", 1, ms=["Automatic stop / start systems cutting the engine when stationary; smooth driving in higher gears avoiding sudden braking / acceleration"]),
      ]),

    Q("ECON-04", T, "3.3.4.2.2", "228-231",
      intro="Table 1 shows the rate of heat loss through 1 m<sup>2</sup> of different glazing systems for a 1 &deg;C temperature difference (U-value).",
      figures=[Table(["Glazing", "Heat loss / W m^-2 K^-1"], [["Single glazing", "5.8"], ["Double glazing, air filled", "2.8"], ["Double glazing, argon filled, low-e glass", "1.6"], ["Triple glazing, krypton filled, low-e glass", "0.8"], ["Double glazing, vacuum (0.2 mm gap)", "0.74"]])],
      parts=[
          P("A house has 20 m<sup>2</sup> of single glazing. The average temperature difference between inside and outside over the heating season is 12 &deg;C. Calculate the reduction in the rate of heat loss if the windows are replaced with argon-filled low-e double glazing.", 3, calc=True, unit="W",
            ms=["Single: 5.8 x 20 x 12 = 1392 W", "Argon: 1.6 x 20 x 12 = 384 W", "Reduction = 1008 W (accept 1010)"]),
          P("Explain why the gap between the panes should be as large as possible but not too large.", 2,
            ms=["A wider gap of trapped gas reduces conduction because gas is a poor conductor", "If the gap is too wide convection currents start in the gas, carrying heat across; the optimum depends on the gas and window size"]),
          P("Explain how low-emissivity glass and inert gas filling each reduce heat loss.", 2,
            ms=["Low-e coating reflects long-wavelength infrared back into the room, reducing radiation losses", "Argon / krypton / xenon have lower thermal conductivity than air so less conduction across the gap"]),
          P("Explain why vacuum double glazing has a very narrow gap and where it is used.", 2,
            ms=["Panes must be held apart by small spacers which cannot be long, so the gap is only about 0.2 mm", "Used where there is not room for thick gas-filled multiple glazing (eg historic buildings)"]),
          P("State <b>one</b> reason why insulation thickness has an optimum value.", 1, ms=["Each extra layer saves less energy (diminishing returns) while cost rises, so beyond the optimum the cost of insulation exceeds the value of energy saved"]),
      ]),

    Q("ECON-05", T, "3.3.4.2.2", "228-232",
      parts=[
          P("Explain how each of the following building design features reduces energy use.", 6,
            labels=["Orientation", "Low surface area : volume ratio", "Earth sheltering"],
            ms=["Orientation: south-facing windows (northern hemisphere) maximise passive solar gains; rooms needing warmth on the sunny side; fewer / smaller windows on the north side where losses are greatest; solar screens / brise soleil prevent summer overheating",
                "Low SA:V (compact shapes, terraced / joined buildings, fewer storeys of small footprint) means less external surface per unit volume through which heat is lost",
                "Earth sheltering: the ground is warmer than winter air and shields the building from wind, so conduction and wind-chill losses are reduced"]),
          P("Compare the embodied energy of concrete with alternative building materials.", 2,
            ms=["Cement manufacture (heating limestone) is very energy intensive so concrete has high embodied energy", "Limecrete has about half the embodied energy of concrete; rammed earth, straw bales and lime mortar are lower still"]),
          P("Describe how a heat exchanger allows a building to be ventilated with minimal heat loss.", 2,
            ms=["Warm stale air leaving and cold fresh air entering pass through the exchanger in opposite directions (counter-current) separated by thin conducting pipes / plates with a large surface area", "Heat transfers from the outgoing to the incoming air so fresh air enters already warmed"]),
      ]),

    Q("ECON-06", T, "3.3.4.2.2", "232-233",
      parts=[
          P("Explain how occupancy sensors and programmable thermostats reduce energy waste.", 2,
            ms=["Occupancy sensors detect infrared / movement and switch lights or appliances off when no one is in the room", "Programmable thermostats set different temperatures for different rooms and times so unused rooms / periods are not heated"]),
          P("Explain why LED lights use much less electricity than the filament and CFL lamps they replaced, and give <b>two</b> other examples of low-energy appliance design.", 3,
            ms=["LEDs convert a much larger proportion of electricity to light rather than heat", "Washing machines with cold / low-temperature cycles and fast spins (less drying); dishwashers using less water so less heating; cookers with double / triple glazed doors; fridges with linear compressors; LED screens using half the power of plasma; germanium transistors"]),
          P("Describe <b>three</b> changes in human behaviour that reduce domestic energy use.", 3, items=3,
            ms=["Turning off lights / appliances rather than standby", "Turning thermostats and radiator valves down / off in unused rooms", "Only heating the water needed (kettle)", "Showering instead of bathing; eco-cycles", "Choosing smaller vehicles / less travel"]),
          P("Explain why heating water on demand saves energy compared with storing hot water.", 2,
            ms=["Stored hot water loses heat continuously through the tank walls and pipes", "Heating as needed (or just before) avoids these standing losses; if storage is needed the tank should be well insulated"]),
      ]),

    Q("ECON-07", T, "3.3.4.2.3", "233-235",
      intro="Figure 1 compares the energy flows in a conventional gas-fired power station and a combined heat and power (CHP) station, each supplied with 100 units of fuel energy.",
      figures=[Table(["", "Conventional power station", "CHP station"], [["Electricity output / units", "40", "35"], ["Useful heat supplied to buildings / units", "0", "45"], ["Waste heat lost / units", "60", "20"]], caption="Figure 1")],
      parts=[
          P("Calculate the overall efficiency of each station.", 2, calc=True, unit="%", ms=["Conventional: 40 / 100 = 40%", "CHP: (35 + 45) / 100 = 80%"]),
          P("Explain why the electrical efficiency of a CHP station is often deliberately kept below 40%.", 2,
            ms=["Extracting less energy as electricity leaves the cooling / condenser water at a higher temperature", "Hotter water is more useful for district heating of homes, fish farms, greenhouses"]),
          P("Explain why CHP stations must be located close to the users of the heat.", 1, ms=["Hot water loses heat and needs pumping energy over distance; heat cannot be transported as far as electricity"]),
          P("Explain how each of the following features of an industrial heat exchanger increases its efficiency.", 3, labels=["Long narrow copper pipes", "Counter-current flow", "Reduced flow rate"],
            ms=["Long narrow pipes give a large surface area and copper is a good thermal conductor so heat transfers quickly", "Hot and cold fluids flowing in opposite directions maintain a temperature gradient along the whole length so more heat is transferred",
                "Slower flow allows more time for heat to transfer"]),
          P("Explain why a single large spherical tank loses less heat than several small cubic tanks holding the same total volume of hot fluid.", 2,
            ms=["One large tank has a lower surface area : volume ratio than many small ones", "A sphere has the smallest surface area for any volume; less surface means less heat loss (with insulation of low thermal conductivity)"]),
      ]),

    Q("ECON-08", T, "3.3.4.2.3", "234-235",
      parts=[
          P("Explain how integrated manufacture saves energy in the iron and steel industry.", 2,
            ms=["Molten iron from the blast furnace is converted directly to steel on the same site", "So it does not cool and need re-melting; transport energy between sites is also avoided; waste heat from one process used by another (eg Kalundborg)"]),
          P("Explain why recycling is not always energy efficient.", 2,
            ms=["Collecting and processing small dispersed quantities can use more energy in transport than is saved", "Mass production and large-scale mining have economies of scale; some materials (glass) take more energy to make than plastic but can be refilled many times"]),
          P("Explain how each of the following manages electricity infrastructure to conserve energy.", 4, labels=["High-voltage grid", "ICT management of supply and demand"],
            ms=["Transmitting at high voltage means low current so less energy is lost as heat in the cables (loss proportional to current squared); overhead cables cheaper than underground which need cooling",
                "ICT / smart grids co-ordinate real-time data on demand and supply from many sources, switching generation, storage (pumped storage, batteries) and flexible loads so surplus is not wasted and inefficient peaking plants are avoided"]),
          P("Give <b>two</b> locational factors affecting where new generating infrastructure is built.", 2, items=2,
            ms=["Proximity to the grid / demand to reduce transmission losses and cable costs", "Access to cooling water for thermal stations", "Resource availability (wind, tidal range, fuel deliveries)", "Land availability and planning / public acceptance; stable geology"]),
      ]),
]

ESSAYS = [
    Essay("ESS-P1-CONSERVE", 1,
          "Discuss the extent to which energy conservation technologies could reduce the need for new energy supplies in a developed country.",
          "3.3.4.2, 3.3.1", "170-174, 225-235",
          ["Scale of the problem: how energy is used (transport, buildings, industry, water); links between affluence and per capita use",
           "Transport: bulk / integrated transport, ATM, vehicle design (aerodynamics, mass, tyres, KERS, combustion efficiency), low embodied energy, design for end of life, driver behaviour, electric vehicles",
           "Buildings: orientation and passive solar, SA:V, thermal mass, low embodied energy materials, earth sheltering, glazing (low-e, inert gas, vacuum), insulation optimum, heat exchangers, automatic ventilation, occupancy sensors, thermostats, low-energy appliances, behaviour",
           "Industry: heat recovery and exchangers, insulation and high-volume storage, CHP, integrated manufacture, recycling and mass reduction, high-voltage grid, peak shaving, ICT management",
           "Limits: rebound effect, cost and payback, existing building stock, embodied energy of replacements, behaviour",
           "Evaluation with quantitative examples; comparison with the cost of new supply; conclusion that conservation is the cheapest first step but cannot alone meet demand growth"]),
]
