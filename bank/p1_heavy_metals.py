"""Pollution: heavy metals - lead, mercury (also cadmium, tin, iron) (spec 3.4.3.2.11).  Genn pp. 275-279."""
from gen.model import Q, P, Table, Chart, Essay

T = "heavy-metals"

QUESTIONS = [
    Q("HM-01", T, "3.4.3.2.11", "275-276",
      intro="Figure 1 shows the mean concentration of lead in the blood of children in a large city between 1976 and 2000, and the year in which lead additives in petrol began to be phased out.",
      figures=[Chart("line", "Year", "Blood lead / &micro;g dl^-1", {"Mean blood lead": [(1976, 15.0), (1980, 12.5), (1984, 9.0), (1988, 6.0), (1992, 4.0), (1996, 3.0), (2000, 2.2)]}, y_min=0)],
      parts=[
          P("Calculate the percentage decrease in mean blood lead between 1976 and 2000.", 2, calc=True, unit="%", ms=["(15.0 - 2.2) / 15.0 x 100", "= 85.3% (accept 85%)"]),
          P("Explain why tetraethyl lead was added to petrol and why this caused a public health threat.", 3,
            ms=["Added as an anti-knock agent to smooth combustion and reduce engine wear",
                "Lead particulates were released in exhaust gases into the air of cities and inhaled / deposited on soil and food",
                "Lead is a neurotoxin that bioaccumulates; chronic exposure damages the nervous system / brain development in children"]),
          P("Suggest <b>two</b> reasons, other than petrol additives, why blood lead concentrations continued to fall after 1990.", 2, items=2,
            ms=["Replacement of lead water pipes / lead solder with copper / tin-based solder; phosphoric acid dosing of water supplies forming insoluble lead phosphate",
                "Phasing out of lead-based paint / safer paint removal", "Lead-free electrical solder", "Restrictions on lead fishing weights / shotgun pellets", "Industrial emission controls"]),
          P("Explain how adding small amounts of phosphoric acid to a water supply reduces lead in drinking water.", 2,
            ms=["Reacts with the lead in old pipes to form an insoluble layer of lead phosphate on the inside of the pipe", "This prevents lead dissolving into the water"]),
          P("Explain why discarded lead fishing weights and shotgun pellets can poison waterfowl.", 1,
            ms=["Swans / ducks swallow them (mistaking them for snails / grit) and the lead is absorbed, causing lead poisoning"]),
      ]),

    Q("HM-02", T, "3.4.3.2.11", "276-277",
      intro="In the 1950s a chemical factory at Minamata, Japan, discharged inorganic mercury compounds into a shallow bay. Thousands of local people who ate fish and shellfish from the bay suffered severe neurological damage and many babies were born with birth abnormalities.",
      parts=[
          P("Explain how the low-toxicity inorganic mercury discharged into the bay came to cause such severe poisoning.", 4,
            ms=["Inorganic mercury settled into anaerobic sediments where anaerobic microbes converted it to organic (methyl) mercury",
                "Methyl mercury is liposoluble so it is absorbed easily and stored in fat / passes through cell membranes",
                "It bioaccumulated in fish and shellfish and biomagnified along the food chain to reach much higher concentrations than in the water",
                "Local people ate large amounts of fish (critical group) so received toxic doses"]),
          P("Explain why methyl mercury caused both neurological damage in adults and birth abnormalities.", 3,
            ms=["Liposoluble so it crosses the blood-brain barrier into the brain, inhibiting enzymes / nerve function (neurotoxin)",
                "It crosses the placenta and harms the developing unborn baby", "Mercury is a teratogen, preventing normal gene expression / development"]),
          P("Compare the toxicity of the three chemical forms of mercury.", 3,
            ms=["Elemental (liquid) mercury: not easily absorbed through skin or gut, though vapour is absorbed in the lungs",
                "Inorganic compounds (eg mercury oxide): moderately well absorbed in the gut",
                "Organic compounds (eg methyl mercury): easily absorbed through skin, gut and lungs; liposoluble so most toxic and bioaccumulates"]),
      ]),

    Q("HM-03", T, "3.4.3.2.11", "275-278",
      parts=[
          P("Give <b>three</b> sources of mercury pollution.", 3, items=3,
            ms=["Disposal of items containing mercury: batteries, thermometers, fluorescent lights", "Chemical plants producing chlorine using mercury electrodes", "Combustion of coal", "Gold mining (amalgamation)"]),
          P("Describe <b>three</b> methods used to control mercury pollution.", 3, items=3,
            ms=["Replacement of mercury thermometers with alcohol / electronic thermometers (discontinued uses)", "Removal from effluents by reverse osmosis / activated carbon filters / ion exchange filters",
                "Disposal / storage of wastes at high pH to reduce solubility", "Encapsulation of mercury-containing hazardous waste in cement"]),
          P("Explain why heavy metal wastes are stored under alkaline conditions.", 2,
            ms=["Most heavy metals are more soluble at low pH / less soluble at high pH", "So at high pH they remain insoluble / immobile and cannot be leached into water or absorbed by organisms"]),
          P("State what is meant by synergism and give an example involving a heavy metal.", 2,
            ms=["The effects of two pollutants interact to produce a different (greater) effect than either alone", "Cadmium and zinc; ozone and sulfur dioxide"]),
      ]),

    Q("HM-04", T, "3.4.3.2.11", "275-279",
      intro="Table 1 shows the concentration of cadmium in rice and in the kidneys of people living in two villages in Japan. Village A is downstream of a zinc mine.",
      figures=[Table(["Village", "Cadmium in rice / mg kg^-1", "Cadmium in kidney of residents / mg kg^-1", "Cases of bone disease (itai-itai) per 1000 people"],
                     [["A (downstream of mine)", "1.2", "180", "34"], ["B (control)", "0.05", "22", "0"]])],
      parts=[
          P("Calculate how many times more concentrated cadmium is in the kidneys of village A residents than in their rice.", 1, calc=True, unit="times", ms=["180 / 1.2 = 150"]),
          P("Explain why cadmium and zinc pollution often occur together.", 1, ms=["Cadmium and zinc occur together in the same ores so mine drainage / smelting releases both"]),
          P("Use Table 1 and your knowledge of the properties of cadmium to explain the high rate of bone disease in village A.", 4,
            ms=["Mine drainage water contaminated irrigation water / paddy soil so rice absorbed cadmium (1.2 vs 0.05 mg kg^-1)",
                "Cadmium is liposoluble / not excreted so it bioaccumulates in the body (kidneys) with chronic exposure to small doses over years",
                "Cadmium causes kidney failure and bone decalcification / skeletal collapse (itai-itai disease)",
                "Rice is the staple food so residents receive a large dose; village B has no exposure and no disease (correlation supports causation)"]),
          P("Suggest <b>two</b> ways cadmium pollution from the mine could be controlled.", 2, items=2,
            ms=["Collect mine drainage water and neutralise / raise pH with lime so cadmium precipitates and stays insoluble", "Cover / cap spoil heaps to prevent leaching and dust",
                "Recycle nickel-cadmium batteries / hazardous waste landfill", "Phytoremediation of contaminated paddy soils"]),
          P("Cadmium is used in cadmium-telluride photovoltaic panels. Suggest why this new use may cause pollution in the future.", 2,
            ms=["Manufacture may release cadmium in effluents / dust", "Panels have a limited life; disposal of old panels (landfill, incineration of pigments) could release cadmium unless recycled"]),
      ]),

    Q("HM-05", T, "3.4.3.2.11", "275-279",
      parts=[
          P("Which of the following is the main reason that lead-based paint is a greater risk to children than to adults? Tick one box.", 1,
            mcq=["Children inhale more lead vapour", "Children pick up dust / flakes and suck their fingers", "Lead is more soluble in children's blood", "Children spend more time near roads"],
            ms=["B"]),
          P("Explain how tri-butyl tin (TBT) in anti-fouling paint caused pollution even though only small amounts dissolved into the sea.", 3,
            ms=["TBT is highly toxic to marine molluscs / crustaceans and an endocrine disruptor altering growth and reproduction of oysters / whelks even at very low concentrations",
                "It bioaccumulated in shellfish and could pass to humans eating them", "It was assumed dilution would make it harmless (illustrates the need for the precautionary principle); now prohibited and replaced by copper"]),
          P("Iron is not toxic, yet iron-rich drainage from mine spoil heaps kills fish. Explain why, and describe how it is controlled.", 3,
            ms=["In the low-oxygen conditions of the spoil heap iron is in its soluble reduced form and is leached into the river",
                "In the river it is oxidised to insoluble iron oxide (orange sediment); the oxidation uses dissolved oxygen so the river is deoxygenated, killing aerobic organisms",
                "Control: drainage water is passed over mesh screens where the iron oxidises and is deposited before the water reaches the river; the solid iron is removed periodically"]),
          P("Give <b>two</b> uses of lead that continue because they do not cause significant lead release into the environment.", 2, items=2,
            ms=["Lead-acid car batteries (recycled)", "Lead flashing on roofs / windows", "Radiation shielding"]),
          P("Explain why heavy metals are described as neurotoxins.", 1, ms=["They inhibit enzyme function, especially the enzymes of the nervous system / nerve cells"]),
      ]),
]

ESSAYS = []
