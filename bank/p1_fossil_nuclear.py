"""Energy resources: fossil fuels and nuclear power - features, impacts and new technologies (spec 3.3.3, 3.3.4.1).  Genn pp. 183-196."""
from gen.model import Q, P, Table, Chart, Essay

T = "fossil-nuclear"

QUESTIONS = [
    Q("FN-01", T, "3.3.4.1", "187-188",
      intro="Figure 1 shows the percentage of the oil in a reservoir that can be recovered using different recovery techniques.",
      figures=[Chart("bar", "Recovery technique", "Cumulative oil recovered / %", {"Recovered": [("Primary", 20), ("Primary + secondary", 40), ("Primary + secondary + tertiary", 60)]}, y_min=0, y_max=100)],
      parts=[
          P("Describe how primary oil recovery works and explain why it recovers only about 20% of the oil.", 2,
            ms=["Natural pressure of gas above the oil (or dissolved in it) or water beneath forces oil up the production well; pump-jacks ('nodding donkeys') increase flow",
                "Pressure falls as oil is removed so the remaining oil no longer flows to the well"]),
          P("Describe secondary recovery and explain how it can be linked to carbon capture and storage.", 2,
            ms=["Water or natural gas is pumped down an injection well to maintain the pressure and flow of oil (recovery to about 40%)", "Captured CO2 can be pumped down instead, increasing oil recovery while storing the CO2 underground"]),
          P("Describe <b>three</b> tertiary (enhanced) recovery techniques.", 3, items=3,
            ms=["Steam injection (from combustion or solar parabolic concentrators) to heat the oil and reduce its viscosity", "Controlled underground combustion to heat the oil",
                "Detergents / solvents to reduce surface tension so oil flows more easily", "Bacteria that partially digest heavy oil into lighter oils and produce CO2 to maintain pressure"]),
          P("Explain <b>three</b> advantages of directional drilling.", 3,
            ms=["Many wells can be drilled from a single platform, reducing land take / number of rigs", "Deposits under locations where rigs cannot be placed (urban areas, sensitive habitats) can be reached",
                "Drilling can follow softer strata (quicker) and target multiple small reservoirs up to 10 km away, increasing total recovery"]),
      ]),

    Q("FN-02", T, "3.3.4.1", "184, 189-190",
      parts=[
          P("Explain why oil and gas trapped in shale cannot be extracted by conventional drilling and describe how hydraulic fracturing (fracking) allows extraction.", 3,
            ms=["Shale has very low permeability so the 'tight' oil / gas cannot flow through the rock to a well",
                "Fluid is pumped down at high pressure to open fissures in the shale along which oil / gas can flow to the recovery well", "Sand grains (to hold fissures open) and solvents are pumped in to increase the recovery rate"]),
          P("Describe <b>four</b> environmental concerns about fracking and suggest how they may be reduced.", 5,
            ms=["Natural gas may enter aquifer water", "Injected chemicals may reach aquifers or the surface; toxic metals in the rock may be mobilised",
                "Large volumes of water needed", "Earth tremors as fracking releases natural tensions in the crust (though not tremors that could not occur naturally)",
                "Reduced by: collection, treatment and re-use of waste water; well casing standards; restricting sites away from aquifers / sensitive areas; monitoring"]),
          P("Explain why tar sands and oil shales are not included in most estimates of oil reserves despite containing more oil than conventional crude oil.", 2,
            ms=["Extraction is expensive and energy-intensive (quarrying and hot water treatment, steam / solvent / combustion in-situ; heating shale to release oil) so it is not economically viable at current prices",
                "Reserves only include what is economically exploitable now; high environmental impacts (land take, water, CO2) also limit exploitation"]),
      ]),

    Q("FN-03", T, "3.3.4.1", "187, 190",
      parts=[
          P("Describe coal gasification and coal liquefaction and explain how each increases the usefulness of coal.", 4,
            ms=["Gasification: coal (including deposits too deep to mine) is burnt underground under controlled conditions to produce fuel gases (hydrogen, carbon monoxide, methane)",
                "Allows deep coal to be exploited and gas can be piped / used in gas turbines or for hydrogen with CCS", "Liquefaction: coal is converted to liquid hydrocarbons directly with solvents or via gasification and chemical conversion",
                "Provides liquid fuels for vehicles / aircraft that solid coal cannot supply"]),
          P("Describe what methane hydrate is and where it is found.", 2,
            ms=["A solid, ice-like crystalline structure in which methane is trapped within water ice", "Found at low temperatures (polar regions / permafrost) or high pressure in ocean sediments around continental margins"]),
          P("Describe <b>two</b> proposed methods of extracting methane from hydrate deposits and explain <b>two</b> environmental risks.", 4,
            ms=["Water heating: hot water pumped into sediments melts the hydrate releasing methane", "Depressurisation: drilling reduces pressure so methane dissociates from the crystals",
                "CO2 injection: CO2 bonds more strongly to the ice and displaces methane (could double as CCS)",
                "Risks: methane not collected escapes to the atmosphere - powerful greenhouse gas / positive feedback; seabed ecology poorly understood; sediment instability / landslides"]),
      ]),

    Q("FN-04", T, "3.3.4.1", "191-193",
      intro="Table 1 compares a 1000 MW coal-fired power station with a 1000 MW nuclear power station.",
      figures=[Table(["Feature", "Coal-fired", "Nuclear (uranium)"], [["Fuel used per year", "3.5 million tonnes", "30 tonnes"], ["CO_2 emitted per kWh / g", "900", "12 (mostly fuel processing and construction)"], ["Construction cost / &pound; billion", "2", "20"], ["Fuel cost per kWh / pence", "3.0", "0.5"], ["Typical response to changes in demand", "Hours", "Slow (days)"]])],
      parts=[
          P("Explain how nuclear fission releases energy in a reactor.", 3,
            ms=["Nuclei of large atoms (uranium-235, plutonium-239) split when hit by a neutron", "A small amount of mass is converted to a large amount of energy (E = mc^2) and more neutrons are released, causing a chain reaction (controlled by control rods / moderator)",
                "The heat boils water to steam which drives turbines and generators"]),
          P("Use Table 1 to explain why nuclear power is used for base-load electricity but not for meeting peaks in demand.", 2,
            ms=["Output changes slowly (days) so it cannot follow rapid fluctuations in demand", "Very high construction cost but low fuel cost means it is most economic running continuously at full output"]),
          P("Use Table 1 to explain why nuclear power stations can be built where coal-fired stations could not.", 2,
            ms=["Only 30 t of fuel a year (very high energy density) so no need for railways / ports to deliver millions of tonnes of coal", "Still need condenser cooling water (coast / large lake) and a stable site"]),
          P("Explain why the CO<sub>2</sub> emissions of nuclear power are not zero.", 1, ms=["Uranium must be mined, purified, concentrated and processed into fuel using (fossil) energy; reactor construction and decommissioning have embodied energy"]),
          P("Give <b>two</b> reasons why the true cost of nuclear electricity is uncertain.", 2, items=2,
            ms=["No commercial reactor has been fully decommissioned so costs are unknown and often exceed estimates", "Large projects often overrun original cost estimates", "Long-term waste disposal costs uncertain", "State subsidies may hide costs"]),
      ]),

    Q("FN-05", T, "3.3.4.1", "192-194",
      parts=[
          P("Describe <b>three</b> factors that have restricted the growth of nuclear power.", 3, items=3,
            ms=["Public opposition following accidents (Three Mile Island 1979, Chernobyl 1986, Fukushima 2011)", "Very complex, expensive technology needing an advanced industrial infrastructure",
                "Concerns about links between civil nuclear materials and weapons / terrorism", "Uncertainty over permanent disposal of radioactive waste", "Uncertain decommissioning costs"]),
          P("Explain how a plutonium 'breeder' reactor can produce more fissile fuel than it uses.", 3,
            ms=["Only 0.7% of natural uranium is fissile U-235; the remaining 99.3% is non-fissile U-238 (a 'fertile' fuel)",
                "Neutron bombardment in the reactor converts U-238 to fissile plutonium-239 (via beta decays)", "So much more energy is harnessed from the mined uranium; fast reactors need no moderator but are complex and costly"]),
          P("Give <b>two</b> advantages and <b>two</b> disadvantages of thorium reactors compared with uranium reactors.", 4, labels=["Advantages", "Disadvantages"],
            ms=["Advantages: thorium is three times more abundant; much less radioactive waste with shorter half-lives; harder to make weapons material; no fuel enrichment needed",
                "Disadvantages: thorium-232 is not fissile so must be bred into uranium-233 (slow breeding rate); U-233 is an alpha emitter so very hazardous to handle; less developed technology with high development costs"]),
      ]),

    Q("FN-06", T, "3.3.4.1", "195-196",
      parts=[
          P("Explain the difference between nuclear fission and nuclear fusion.", 2,
            ms=["Fission: splitting the nuclei of large atoms (U-235, Pu-239) when hit by neutrons", "Fusion: joining the nuclei of small atoms (deuterium and tritium - isotopes of hydrogen) to form helium, releasing a neutron and energy - the energy source of stars"]),
          P("State the sources of the two fuels used in fusion research.", 2, items=2, ms=["Deuterium (hydrogen-2) extracted from (sea)water", "Tritium (hydrogen-3) produced by neutron bombardment of lithium (a lithium blanket around the reactor)"]),
          P("Explain why very high temperatures, a vacuum and a magnetic field are needed in a toroidal (torus) fusion reactor.", 3,
            ms=["Very high temperature turns hydrogen into a plasma (electrons stripped away) and gives nuclei enough kinetic energy to overcome the repulsion between positive nuclei and collide",
                "Vacuum so the plasma is not cooled by air", "Magnetic field holds the plasma centrally so it does not touch the container walls and cool"]),
          P("Give <b>two</b> potential advantages of fusion over fission and one reason why it is not yet a commercial energy source.", 3,
            ms=["Fuel (deuterium / lithium) is abundant / effectively unlimited", "Much less radioactive waste (no long-lived fission products); no chain reaction / meltdown risk; no weapons material",
                "Not yet achieved sustained net energy output: reactors (JET) use more energy than they release; ITER aims for 500 MW out from 50 MW in; laser fusion also experimental; commercial viability decades away"]),
      ]),

    Q("FN-07", T, "3.3.3-3.3.4.1", "183-196",
      parts=[
          P("Evaluate the extent to which new technologies could allow fossil fuels and nuclear fission to continue to supply a large proportion of the world's energy sustainably.", 9, level=True,
            ms=["Fossil fuel technologies: secondary / tertiary recovery raising recovery from 20% to 60%; directional drilling and subsea wells; ROVs; fracking for tight oil and gas; tar sands / oil shales; coal gasification / liquefaction; enhanced gas recovery; methane hydrates; CCS (pre / post combustion, storage)",
                "Limits: still finite (discoveries declining since the 1980s); rising energy and financial cost of unconventional sources; environmental impacts (aquifers, water use, tremors, land take, habitat damage); CO2 and other pollution; CCS unproven at scale and impractical for vehicles",
                "Nuclear: new uranium extraction (polymer adsorption from seawater, phosphate mining, coal ash); molten salt reactors; plutonium breeder and thorium reactors increasing fuel use many-fold; fusion as a long-term prospect",
                "Limits: cost overruns, decommissioning, waste, public opposition, proliferation, embodied energy of low-grade uranium; fusion not commercial",
                "Sustainability criteria: maintaining supply without unacceptable environmental, economic or social impact; comparison with renewables and energy conservation; energy gap argument",
                "Judgement: technologies can extend supplies and reduce some impacts but cannot make non-renewables sustainable indefinitely; role as transition / base-load alongside renewables"]),
          P("State the approximate percentage of natural gas in a reservoir that can be recovered using its own pressure.", 1, ms=["80-90%"]),
      ]),
]

ESSAYS = []
