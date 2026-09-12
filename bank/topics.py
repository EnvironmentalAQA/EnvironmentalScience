"""Topic tree for the site, mirroring the AQA 7447 specification.

Each subtopic: (slug, name, spec refs, Genn printed pages)
Paper 1 = Physical environment + Energy + Pollution + Research methods
Paper 2 = Living environment + Biological resources + Sustainability + Research methods
"""

PAPERS = {
    1: {
        "name": "Paper 1",
        "assessed": "The physical environment, Energy resources, Pollution, Research methods",
        "code": "7447/1",
        "topics": [
            {
                "slug": "physical", "name": "The physical environment", "spec": "3.2",
                "subtopics": [
                    ("atm-energy", "The atmosphere: energy processes (UV, IR, visible light)", "3.2.1.1", "86-89"),
                    ("climate-change", "Global climate change", "3.2.1.2", "89-107"),
                    ("ozone", "Ozone depletion", "3.2.1.3", "108-113"),
                    ("hydro-cycle", "The hydrosphere: hydrological cycle & unsustainable exploitation", "3.2.2.1-3.2.2.3", "114-121"),
                    ("hydro-management", "Water treatment, conservation & new sources", "3.2.2.4-3.2.2.5", "122-127"),
                    ("minerals", "Mineral resources (the lithosphere)", "3.2.3", "130-147"),
                    ("biogeochem", "Biogeochemical cycles: carbon, nitrogen, phosphorus", "3.2.4", "148-157"),
                    ("soils", "Soils: fertility, erosion & management", "3.2.5", "158-169"),
                ],
            },
            {
                "slug": "energy", "name": "Energy resources", "spec": "3.3",
                "subtopics": [
                    ("energy-features", "Importance & features of energy resources", "3.3.1-3.3.2", "170-182"),
                    ("fossil-nuclear", "Fossil fuels & nuclear power: sustainability and new technologies", "3.3.3, 3.3.4.1", "183-196"),
                    ("renewables", "Renewable energy technologies", "3.3.4.1", "196-217"),
                    ("energy-storage", "Fluctuations in supply/demand & energy storage", "3.3.4.1", "217-224"),
                    ("energy-conservation", "Energy conservation: transport, buildings, industry", "3.3.4.2", "225-235"),
                ],
            },
            {
                "slug": "pollution", "name": "Pollution", "spec": "3.4",
                "subtopics": [
                    ("pollutant-properties", "Properties of pollutants & environmental factors", "3.4.1-3.4.2", "236-242"),
                    ("pollution-control", "Principles of pollution control (CPA, CGM, new technologies)", "3.4.3.1, 3.4.3.3", "243-245, 303-304"),
                    ("air-pollution", "Atmospheric pollution: smoke, acid rain, NOx, hydrocarbons, CO, smogs", "3.4.3.2.1-3.4.3.2.5", "245-254"),
                    ("water-pollution", "Thermal & oil pollution", "3.4.3.2.6-3.4.3.2.7", "254-262"),
                    ("pesticides", "Pesticides", "3.4.3.2.8", "262-266"),
                    ("nutrient-pollution", "Nutrient pollution, sewage treatment & acid mine drainage", "3.4.3.2.9-3.4.3.2.10", "266-275"),
                    ("heavy-metals", "Heavy metals: lead, mercury", "3.4.3.2.11", "275-279"),
                    ("solid-waste", "Solid wastes", "3.4.3.2.12", "279-285"),
                    ("noise", "Noise pollution", "3.4.3.2.13", "286-295"),
                    ("radiation", "Ionising radiation", "3.4.3.2.14", "295-304"),
                ],
            },
            {
                "slug": "research", "name": "Research methods", "spec": "3.7",
                "subtopics": [
                    ("methodology", "Scientific methodologies & sampling design", "3.7.1", "390-393"),
                    ("sampling", "Sampling techniques & measuring abiotic factors", "3.7.2.1-3.7.2.2", "394-419"),
                    ("stats", "Specialist techniques & statistical analysis", "3.7.2.3", "402-407, 420-423"),
                ],
            },
        ],
    },
    2: {
        "name": "Paper 2",
        "assessed": "The living environment, Biological resources, Sustainability, Research methods",
        "code": "7447/2",
        "topics": [
            {
                "slug": "living", "name": "The living environment", "spec": "3.1",
                "subtopics": [
                    ("life-conditions", "Conditions for life on Earth", "3.1.1", "5-9"),
                    ("biodiversity-value", "Importance of biodiversity: resources & ecosystem services", "3.1.2.1", "10-19"),
                    ("human-impacts", "How humans influence biodiversity", "3.1.2.2", "20-25"),
                    ("conservation-priorities", "Conservation priorities, legislation & protocols", "3.1.2.3.1-3.1.2.3.2", "26-39"),
                    ("cbr-habitat", "Captive breeding, habitat creation & management", "3.1.2.3.3-3.1.2.3.4", "32-49"),
                    ("habitats", "Habitat case studies: woodland, rainforest, reefs, islands, mangroves, Antarctica", "3.1.2.3.4", "50-71"),
                    ("eco-monitoring", "Ecological monitoring & new technologies", "3.1.2.3.5-3.1.2.3.6", "402-407"),
                    ("life-processes", "Adaptation, terminology, succession & population control", "3.1.3", "72-85"),
                ],
            },
            {
                "slug": "bioresources", "name": "Biological resources", "spec": "3.5",
                "subtopics": [
                    ("agroecosystems", "Agroecosystems: abiotic & biotic factors", "3.5.1.1", "306-320"),
                    ("food-species", "Manipulation of food species & agricultural energetics", "3.5.1.2", "321-327"),
                    ("agri-impacts", "Impacts of agriculture, social/political factors & sustainable agriculture", "3.5.1.3-3.5.1.5", "328-337"),
                    ("fishing", "Marine productivity & fishing", "3.5.2.1-3.5.2.2", "338-351"),
                    ("aquaculture", "Aquaculture", "3.5.2.3", "352-359"),
                    ("forests", "Forest resources & deforestation", "3.5.3", "360-369"),
                ],
            },
            {
                "slug": "sustainability", "name": "Sustainability", "spec": "3.6",
                "subtopics": [
                    ("dynamic-equilibria", "Dynamic equilibria, feedback & tipping points", "3.6.1", "370-372"),
                    ("natural-systems", "Energy & material cycles: natural vs human systems", "3.6.2-3.6.3", "373-374"),
                    ("circular-economy", "The circular economy, biocapacity & ecological footprints", "3.6.4", "374-389"),
                ],
            },
            {
                "slug": "research", "name": "Research methods", "spec": "3.7",
                "subtopics": [
                    ("methodology", "Scientific methodologies & sampling design", "3.7.1", "390-393"),
                    ("sampling", "Sampling techniques & measuring abiotic factors", "3.7.2.1-3.7.2.2", "394-419"),
                    ("stats", "Specialist techniques & statistical analysis", "3.7.2.3", "402-407, 420-423"),
                ],
            },
        ],
    },
}


def subtopic_index():
    """slug -> dict(name, spec, pages, papers, topic)"""
    idx = {}
    for pno, paper in PAPERS.items():
        for t in paper["topics"]:
            for slug, name, spec, pages in t["subtopics"]:
                d = idx.setdefault(slug, {"slug": slug, "name": name, "spec": spec, "pages": pages,
                                          "papers": [], "topic": t["name"], "topic_slug": t["slug"]})
                if pno not in d["papers"]:
                    d["papers"].append(pno)
    return idx


BOOK = "R. Genn, Environmental Science A level AQA (Insight & Perspective, 2018)"
