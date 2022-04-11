

import pymongo

def addMetadataToCollection():
    mongo = pymongo.MongoClient("mongodb://lattice-100:27018/")
    db = mongo["sustaindb"]
    db["Metadata"].insert(
        {
            "collection" : "co_water_quality_rivers_and_streams", 
            "fieldMetadata": [
                                { "name" : "epoch_time", "type" : "DATE", "minDate" : -2191239000000, "maxDate" : 1709991300000 },
                                {
                                    "name": "Oxazepam glucuronide",
                                    "type": "NUMBER",
                                    "max": 90.2
                                },
                                {
                                    "name": "Mefenamic acid 3-hydroxy methyl",
                                    "type": "NUMBER",
                                    "max": 67.9
                                },
                                {
                                    "name": "Normorphine",
                                    "type": "NUMBER",
                                    "max": 101
                                },
                                {
                                    "name": "Lorazepam glucuronide",
                                    "type": "NUMBER",
                                    "max": 33.9
                                },
                                {
                                    "name": "Theobromine",
                                    "type": "NUMBER",
                                    "max": 52.5
                                },
                                {
                                    "name": "Dihydromorphine",
                                    "type": "NUMBER",
                                    "max": 79.2
                                },
                                {
                                    "name": "Norbuprenorphine",
                                    "type": "NUMBER",
                                    "max": 112
                                },
                                {
                                    "name": "7-Hydroxyquetiapine",
                                    "type": "NUMBER",
                                    "max": 108
                                },
                                {
                                    "name": "Gemfibrozil-D6",
                                    "type": "NUMBER",
                                    "max": 109
                                },
                                {
                                    "name": "Phenobarbital-D5",
                                    "type": "NUMBER",
                                    "max": 130
                                },
                                {
                                    "name": "Monensin",
                                    "type": "NUMBER",
                                    "max": 84.2
                                },
                                {
                                    "name": "Bromoxynil-13C6",
                                    "type": "NUMBER",
                                    "min": 79.9,
                                    "max": 107
                                },
                                {
                                    "name": "D9 (+/-)11-nor-9-carboxy-delta-THC",
                                    "type": "NUMBER",
                                    "max": 78.4
                                },
                                {
                                    "name": "Atrazine-d5 (ethyl-d5)",
                                    "type": "NUMBER",
                                    "min": 79.3,
                                    "max": 108
                                },
                                {
                                    "name": "Pentachlorophenol-13C6",
                                    "type": "NUMBER",
                                    "min": 42.4,
                                    "max": 92.8
                                },
                                {
                                    "name": "Piperidine, 1-(1-phenylcyclohexyl)-",
                                    "type": "NUMBER",
                                    "max": 95.6
                                },
                                {
                                    "name": "Nitrazepam",
                                    "type": "NUMBER",
                                    "max": 117
                                },
                                {
                                    "name": "2,2',4,4',5,5'-Hexachlorobiphenyl",
                                    "type": "NUMBER",
                                    "min": 1.45,
                                    "max": 1.45
                                },
                                {
                                    "name": "Benzene, 1,2,4-tribromo-5-(2,4-dibromophenoxy)-***retired***use BDE-099",
                                    "type": "NUMBER",
                                    "min": 3.28,
                                    "max": 3.28
                                },
                                {
                                    "name": "2,2',3,4,4',5'-Hexachlorobiphenyl",
                                    "type": "NUMBER",
                                    "min": 2.78,
                                    "max": 2.78
                                },
                                {
                                    "name": "2,2',4,4'-Tetrabromodiphenyl ether",
                                    "type": "NUMBER",
                                    "min": 3.89,
                                    "max": 3.89
                                },
                                {
                                    "name": "2,2',5,5'-Tetrachlorobiphenyl",
                                    "type": "NUMBER",
                                    "min": 0.47,
                                    "max": 0.47
                                },
                                {
                                    "name": "Chlordane",
                                    "type": "NUMBER",
                                    "min": 1.38,
                                    "max": 1.38
                                },
                                {
                                    "name": "3,3',4,4'-Tetrachlorobiphenyl",
                                    "type": "NUMBER",
                                    "min": 0.95,
                                    "max": 0.95
                                },
                                {
                                    "name": "Pyrene-d10",
                                    "type": "NUMBER",
                                    "min": 53.6,
                                    "max": 68.4
                                },
                                {
                                    "name": "2,2',3,4,4',5,5'-Heptachlorobiphenyl",
                                    "type": "NUMBER",
                                    "min": 0.58,
                                    "max": 0.58
                                },
                                {
                                    "name": "2,4,4'-Trichlorobiphenyl",
                                    "type": "NUMBER",
                                    "min": 4.43,
                                    "max": 4.43
                                },
                                {
                                    "name": "BDE-100",
                                    "type": "NUMBER",
                                    "min": 1.28,
                                    "max": 1.28
                                },
                                {
                                    "name": "2,2',4,5,5'-Pentachlorobiphenyl",
                                    "type": "NUMBER",
                                    "min": 1.19,
                                    "max": 1.19
                                },
                                {
                                    "name": "2,3',4,4',5-Pentachlorobiphenyl",
                                    "type": "NUMBER",
                                    "min": 1.46,
                                    "max": 1.46
                                },
                                {
                                    "name": "2-Nitro-M-Xylene",
                                    "type": "NUMBER",
                                    "min": 57.7,
                                    "max": 77.2
                                },
                                {
                                    "name": "m-Dichlorobenzene",
                                    "type": "NUMBER",
                                    "max": 0.003
                                },
                                {
                                    "name": "Dimethachlor ESA",
                                    "type": "NUMBER",
                                    "max": 96.6
                                },
                                {
                                    "name": "2,4-D-13C6",
                                    "type": "NUMBER",
                                    "min": 66.1,
                                    "max": 104
                                },
                                {
                                    "name": "Carbamazepine-d10",
                                    "type": "NUMBER",
                                    "max": 125
                                },
                                {
                                    "name": "Ibuprofen-13C3",
                                    "type": "NUMBER",
                                    "max": 131
                                },
                                {
                                    "name": "Tetrahydrocannabinol",
                                    "type": "NUMBER",
                                    "max": 118
                                },
                                {
                                    "name": "Cannabinol",
                                    "type": "NUMBER",
                                    "max": 85.8
                                },
                                {
                                    "name": "Clonazepam",
                                    "type": "NUMBER",
                                    "max": 120
                                },
                                {
                                    "name": "Chlordiazepoxide",
                                    "type": "NUMBER",
                                    "max": 113
                                },
                                {
                                    "name": "Butalbital",
                                    "type": "NUMBER",
                                    "max": 94.7
                                },
                                {
                                    "name": "Clobazam",
                                    "type": "NUMBER",
                                    "max": 110
                                },
                                {
                                    "name": "Dimerin",
                                    "type": "NUMBER",
                                    "max": 76.9
                                },
                                {
                                    "name": "Flunitrazepam",
                                    "type": "NUMBER",
                                    "max": 97
                                },
                                {
                                    "name": "Flurazepam",
                                    "type": "NUMBER",
                                    "max": 99.7
                                },
                                {
                                    "name": "Cannabidiol",
                                    "type": "NUMBER",
                                    "max": 102
                                },
                                {
                                    "name": "Mephobarbital",
                                    "type": "NUMBER",
                                    "max": 81.2
                                },
                                {
                                    "name": "Benzphetamine",
                                    "type": "NUMBER",
                                    "max": 143
                                },
                                {
                                    "name": "Allyl-sec-butyl-barbituric acid",
                                    "type": "NUMBER",
                                    "max": 93.7
                                },
                                {
                                    "name": "Pindolol",
                                    "type": "NUMBER",
                                    "max": 148
                                },
                                {
                                    "name": "Pentazocine",
                                    "type": "NUMBER",
                                    "max": 95.7
                                },
                                {
                                    "name": "Prazepam",
                                    "type": "NUMBER",
                                    "max": 113
                                },
                                {
                                    "name": "Seconal",
                                    "type": "NUMBER",
                                    "max": 137
                                },
                                {
                                    "name": "Fenbendazole",
                                    "type": "NUMBER",
                                    "max": 125
                                },
                                {
                                    "name": "Triazolam",
                                    "type": "NUMBER",
                                    "max": 146
                                },
                                {
                                    "name": "Velocity-discharge",
                                    "type": "NUMBER",
                                    "min": 0.03,
                                    "max": 77.3
                                },
                                {
                                    "name": "Brombuterol",
                                    "type": "NUMBER",
                                    "max": 116
                                },
                                {
                                    "name": "4(3H)-Quinazolinone, 2-methyl-3-(2-methylphenyl)-",
                                    "type": "NUMBER",
                                    "max": 99.3
                                },
                                {
                                    "name": "Secbutabarbital",
                                    "type": "NUMBER",
                                    "max": 149
                                },
                                {
                                    "name": "Thebaine",
                                    "type": "NUMBER",
                                    "max": 98.4
                                },
                                {
                                    "name": "Particle size, Sieve No_ 230, 250 mesh, (0_063mm)",
                                    "type": "NUMBER",
                                    "min": 81,
                                    "max": 97
                                },
                                {
                                    "name": "Hydrocarbons, petroleum",
                                    "type": "NUMBER",
                                    "max": 2
                                },
                                {
                                    "name": "Musk ketone",
                                    "type": "NUMBER",
                                    "max": 107
                                },
                                {
                                    "name": "Ethanone, 1-(2,3-dihydro-1,1,2,3,3,6-hexamethyl-1H-inden-5-yl)-",
                                    "type": "NUMBER",
                                    "max": 97.7
                                },
                                {
                                    "name": "Clopidogrel carboxylic acid",
                                    "type": "NUMBER",
                                    "max": 72.9
                                },
                                {
                                    "name": "Oxymorphone glucuronide",
                                    "type": "NUMBER",
                                    "max": 98.9
                                },
                                {
                                    "name": "Butylated hydroxyanisole",
                                    "type": "NUMBER",
                                    "max": 81.3
                                },
                                {
                                    "name": "Phenol-D6",
                                    "type": "NUMBER",
                                    "min": 33,
                                    "max": 111
                                },
                                {
                                    "name": "Ethanone, 1-[6-(1,1-dimethylethyl)-2,3-dihydro-1,1-dimethyl-1H-inden-4-yl]-",
                                    "type": "NUMBER",
                                    "max": 103
                                },
                                {
                                    "name": "Atorvastatin",
                                    "type": "NUMBER",
                                    "max": 83.5
                                },
                                {
                                    "name": "Oxidized Nifedipine",
                                    "type": "NUMBER",
                                    "max": 126
                                },
                                {
                                    "name": "Clenbuterol",
                                    "type": "NUMBER",
                                    "max": 118
                                },
                                {
                                    "name": "Cocaethylene",
                                    "type": "NUMBER",
                                    "max": 105
                                },
                                {
                                    "name": "Nifedipine",
                                    "type": "NUMBER",
                                    "max": 103
                                },
                                {
                                    "name": "Donepezil",
                                    "type": "NUMBER",
                                    "max": 132
                                },
                                {
                                    "name": "Salbutamol",
                                    "type": "NUMBER",
                                    "max": 166
                                },
                                {
                                    "name": "Levorphanol",
                                    "type": "NUMBER",
                                    "max": 94.4
                                },
                                {
                                    "name": "Uranium-234/235/238",
                                    "type": "NUMBER",
                                    "max": 0.304
                                },
                                {
                                    "name": "Ecgonine Methyl Ester",
                                    "type": "NUMBER",
                                    "max": 108
                                },
                                {
                                    "name": "Tetrachlorodibenzo-p-dioxin",
                                    "type": "NUMBER",
                                    "max": 0.8
                                },
                                {
                                    "name": "Total Dioxin TEQ, Bird",
                                    "type": "NUMBER",
                                    "max": 0.0078
                                },
                                {
                                    "name": "1,2,3,4,6,7,8,9-Octachlorodibenzo-p-dioxin",
                                    "type": "NUMBER",
                                    "max": 33
                                },
                                {
                                    "name": "Total Dioxin TEQ, Mammalian",
                                    "type": "NUMBER",
                                    "max": 0.056
                                },
                                {
                                    "name": "Tetrachlorodibenzofuran",
                                    "type": "NUMBER",
                                    "min": 1.1,
                                    "max": 9.9
                                },
                                {
                                    "name": "Secchi Reading Condition (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "Poor",
                                        "EXCELLENT",
                                        "MODERATE",
                                        "Excellent"
                                    ]
                                },
                                {
                                    "name": "Heptachlorodibenzo-p-dioxin",
                                    "type": "NUMBER",
                                    "min": 10,
                                    "max": 10
                                },
                                {
                                    "name": "Hexachlorodibenzofuran",
                                    "type": "NUMBER",
                                    "max": 2.9
                                },
                                {
                                    "name": "Pentachlorodibenzofuran",
                                    "type": "NUMBER",
                                    "max": 7.4
                                },
                                {
                                    "name": "Total Dioxin TEQ, Fish",
                                    "type": "NUMBER",
                                    "max": 0.0078
                                },
                                {
                                    "name": "Hexachlorodibenzo-p-dioxin",
                                    "type": "NUMBER",
                                    "min": 2.5,
                                    "max": 2.5
                                },
                                {
                                    "name": "Disopyramide",
                                    "type": "NUMBER",
                                    "max": 116
                                },
                                {
                                    "name": "Foramsulfuron",
                                    "type": "NUMBER",
                                    "max": 102
                                },
                                {
                                    "name": "Perylene-d12",
                                    "type": "NUMBER",
                                    "min": 0.04,
                                    "max": 62.5
                                },
                                {
                                    "name": "Nonylphenol",
                                    "type": "NUMBER",
                                    "max": 168
                                },
                                {
                                    "name": "Phenanthrene-d10",
                                    "type": "NUMBER",
                                    "min": 0.04,
                                    "max": 146
                                },
                                {
                                    "name": "Naphthalene-d8",
                                    "type": "NUMBER",
                                    "min": 0.04,
                                    "max": 0.04
                                },
                                {
                                    "name": "Acenaphthene-d10",
                                    "type": "NUMBER",
                                    "min": 0.04,
                                    "max": 146
                                },
                                {
                                    "name": "1,4-Dichlorobenzene-d4",
                                    "type": "NUMBER",
                                    "min": 0.04,
                                    "max": 0.04
                                },
                                {
                                    "name": "Terphenyl-d14",
                                    "type": "NUMBER",
                                    "min": 0.0253,
                                    "max": 0.0254
                                },
                                {
                                    "name": "Chlorophyll/Pheophytin ratio",
                                    "type": "NUMBER",
                                    "min": 1.03,
                                    "max": 1.75
                                },
                                {
                                    "name": "Inorganic nitrogen (NO2, NO3, & NH3)",
                                    "type": "NUMBER",
                                    "max": 2.3823521653
                                },
                                {
                                    "name": "MDA",
                                    "type": "NUMBER",
                                    "max": 117
                                },
                                {
                                    "name": "AB-PINACA 4-hydroxypentyl",
                                    "type": "NUMBER",
                                    "max": 86.5
                                },
                                {
                                    "name": "Volume, total",
                                    "type": "NUMBER",
                                    "max": 350
                                },
                                {
                                    "name": "Chrysene-d12",
                                    "type": "NUMBER",
                                    "min": 0.04,
                                    "max": 143
                                },
                                {
                                    "name": "MDEA",
                                    "type": "NUMBER",
                                    "max": 133
                                },
                                {
                                    "name": "Anion/cation ratio",
                                    "type": "NUMBER",
                                    "min": 0.483,
                                    "max": 15.1
                                },
                                {
                                    "name": "Nutrient-nitrogen",
                                    "type": "NUMBER",
                                    "max": 23.9
                                },
                                {
                                    "name": "Length, Total (Fish)",
                                    "type": "NUMBER",
                                    "min": 8,
                                    "max": 335
                                },
                                {
                                    "name": "RBP2, Low G, Channel Sinuosity (choice list)",
                                    "type": "NUMBER",
                                    "min": 17,
                                    "max": 17
                                },
                                {
                                    "name": "RBP2, Low G, Epifaunal Substrate/Available Cover (choice list)",
                                    "type": "NUMBER",
                                    "min": 16,
                                    "max": 16
                                },
                                {
                                    "name": "RBP2, Low G, Channel Alteration (choice list)",
                                    "type": "NUMBER",
                                    "min": 16,
                                    "max": 16
                                },
                                {
                                    "name": "RBP2, Low G, Riparian Vegetative Zone Width, Left Bank (choice list)",
                                    "type": "NUMBER",
                                    "min": 7,
                                    "max": 7
                                },
                                {
                                    "name": "RBP2, Low G, Pool Variability (choice list)",
                                    "type": "NUMBER",
                                    "min": 14,
                                    "max": 14
                                },
                                {
                                    "name": "RBP2, Low G, Vegetative Protection, Left Bank (choice list)",
                                    "type": "NUMBER",
                                    "min": 6,
                                    "max": 6
                                },
                                {
                                    "name": "RBP2, Low G, Pool Substrate Characterization (choice list)",
                                    "type": "NUMBER",
                                    "min": 14,
                                    "max": 14
                                },
                                {
                                    "name": "RBP2, Low G, Vegetative Protection, Right Bank (choice list)",
                                    "type": "NUMBER",
                                    "min": 6,
                                    "max": 6
                                },
                                {
                                    "name": "RBP2, Low G, Bank Stability, Right Bank (choice list)",
                                    "type": "NUMBER",
                                    "min": 5,
                                    "max": 5
                                },
                                {
                                    "name": "RBP2, Low G, Riparian Vegetative Zone Width, Right Bank (choice list)",
                                    "type": "NUMBER",
                                    "min": 7,
                                    "max": 7
                                },
                                {
                                    "name": "RBP2, Low G, Sediment Deposition (choice list)",
                                    "type": "NUMBER",
                                    "min": 15,
                                    "max": 15
                                },
                                {
                                    "name": "RBP2, Low G, Bank Stability, Left Bank (choice list)",
                                    "type": "NUMBER",
                                    "min": 5,
                                    "max": 5
                                },
                                {
                                    "name": "RBP2, Low G, Channel Flow Status (choice list)",
                                    "type": "NUMBER",
                                    "min": 12,
                                    "max": 12
                                },
                                {
                                    "name": "RBP2, High G, Embeddedness (choice list)",
                                    "type": "NUMBER",
                                    "min": 17,
                                    "max": 20
                                },
                                {
                                    "name": "RBP2, High G, Frequency of Riffles (or bends) (choice list)",
                                    "type": "NUMBER",
                                    "min": 19,
                                    "max": 20
                                },
                                {
                                    "name": "RBP2, High G, Velocity/Depth Regime (choice list)",
                                    "type": "NUMBER",
                                    "min": 17,
                                    "max": 19
                                },
                                {
                                    "name": "Organics volatile mix, unspecified",
                                    "type": "NUMBER",
                                    "max": 1.6
                                },
                                {
                                    "name": "Isopropalin",
                                    "type": "NUMBER",
                                    "min": 0.05,
                                    "max": 0.1
                                },
                                {
                                    "name": "Profluralin",
                                    "type": "NUMBER",
                                    "min": 0.05,
                                    "max": 0.1
                                },
                                {
                                    "name": "Oxadiazon",
                                    "type": "NUMBER",
                                    "min": 0.05,
                                    "max": 0.1
                                },
                                {
                                    "name": "Isatidine",
                                    "type": "NUMBER",
                                    "max": 85.5
                                },
                                {
                                    "name": "Retrorsine",
                                    "type": "NUMBER",
                                    "max": 103
                                },
                                {
                                    "name": "Discharge, Mine",
                                    "type": "NUMBER",
                                    "max": 0.331
                                },
                                {
                                    "name": "Senecionine N-oxide",
                                    "type": "NUMBER",
                                    "max": 84.7
                                },
                                {
                                    "name": "2,4-Dichlorophenylacetic acid",
                                    "type": "NUMBER",
                                    "min": 9.33,
                                    "max": 13.8
                                },
                                {
                                    "name": "Decachlorobiphenyl",
                                    "type": "NUMBER",
                                    "max": 0.8
                                },
                                {
                                    "name": "Octadecane, 1-chloro-",
                                    "type": "NUMBER",
                                    "min": 4.8,
                                    "max": 4.8
                                },
                                {
                                    "name": "Seneciphylline",
                                    "type": "NUMBER",
                                    "max": 113
                                },
                                {
                                    "name": "Monocrotaline",
                                    "type": "NUMBER",
                                    "max": 91.9
                                },
                                {
                                    "name": "Monocrotaline N-oxide",
                                    "type": "NUMBER",
                                    "max": 68.4
                                },
                                {
                                    "name": "Ritonavir",
                                    "type": "NUMBER",
                                    "max": 72.5
                                },
                                {
                                    "name": "Senecionine",
                                    "type": "NUMBER",
                                    "max": 104
                                },
                                {
                                    "name": "Octane, 1-chloro-",
                                    "type": "NUMBER",
                                    "min": 4.25,
                                    "max": 4.25
                                },
                                {
                                    "name": "Tetrachloro-m-xylene",
                                    "type": "NUMBER",
                                    "min": 0.432,
                                    "max": 0.562
                                },
                                {
                                    "name": "Seneciphylline N-oxide",
                                    "type": "NUMBER",
                                    "max": 99.6
                                },
                                {
                                    "name": "Discharge, River/Stream",
                                    "type": "NUMBER",
                                    "max": 114.592
                                },
                                {
                                    "name": "Methylfluorene",
                                    "type": "NUMBER",
                                    "max": 1978.52
                                },
                                {
                                    "name": "Anion deficit",
                                    "type": "NUMBER",
                                    "min": -200.56,
                                    "max": 120.1
                                },
                                {
                                    "name": "1,6,7-Trimethylnaphthalene",
                                    "type": "NUMBER",
                                    "max": 756.65
                                },
                                {
                                    "name": "Ionic strength",
                                    "type": "NUMBER",
                                    "max": 0.025
                                },
                                {
                                    "name": "C2-Chrysenes",
                                    "type": "NUMBER",
                                    "max": 388.23
                                },
                                {
                                    "name": "Methyldibenzothiophene",
                                    "type": "NUMBER",
                                    "max": 330.36
                                },
                                {
                                    "name": "C3-Fluorenes",
                                    "type": "NUMBER",
                                    "max": 3653.04
                                },
                                {
                                    "name": "C3-Chrysenes",
                                    "type": "NUMBER",
                                    "max": 39.79
                                },
                                {
                                    "name": "Biphenyl",
                                    "type": "NUMBER",
                                    "max": 150.88
                                },
                                {
                                    "name": "C4-Chrysenes",
                                    "type": "NUMBER",
                                    "max": 96.91
                                },
                                {
                                    "name": "C2-Fluorenes",
                                    "type": "NUMBER",
                                    "max": 2892.36
                                },
                                {
                                    "name": "C2-Dibenzothiophenes",
                                    "type": "NUMBER",
                                    "max": 664.34
                                },
                                {
                                    "name": "Water Column Habitat Type (%)",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "Sand/Substrate Habitat Type (%)",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "Hydrogen",
                                    "type": "NUMBER",
                                    "min": 0.002,
                                    "max": 0.074
                                },
                                {
                                    "name": "Methylchrysene",
                                    "type": "NUMBER",
                                    "max": 379.65
                                },
                                {
                                    "name": "C3-Dibenzothiophenes",
                                    "type": "NUMBER",
                                    "max": 746.3
                                },
                                {
                                    "name": "Organic anions",
                                    "type": "NUMBER",
                                    "min": 5.1056490807,
                                    "max": 71.299523506
                                },
                                {
                                    "name": "Submerged Vegetation Habitat Type (%)",
                                    "type": "NUMBER",
                                    "max": 80
                                },
                                {
                                    "name": "Alkalinity, Hydroxide as CaCO3",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 1
                                },
                                {
                                    "name": "RBP2, High G, Bank Stability, Left Bank (choice list)",
                                    "type": "NUMBER",
                                    "min": 8,
                                    "max": 10
                                },
                                {
                                    "name": "RBP2, High G, Riparian Vegetative Zone Width, Left Bank (choice list)",
                                    "type": "NUMBER",
                                    "min": 8,
                                    "max": 10
                                },
                                {
                                    "name": "RBP2, High G, Bank Stability, Right Bank (choice list)",
                                    "type": "NUMBER",
                                    "min": 7,
                                    "max": 10
                                },
                                {
                                    "name": "RBP2, High G, Channel Flow Status (choice list)",
                                    "type": "NUMBER",
                                    "min": 10,
                                    "max": 19
                                },
                                {
                                    "name": "RBP2, High G, Epifaunal Substrate/Available Cover (choice list)",
                                    "type": "NUMBER",
                                    "min": 14,
                                    "max": 18
                                },
                                {
                                    "name": "RBP2, High G, Riparian Vegetative Zone Width, Right Bank (choice list)",
                                    "type": "NUMBER",
                                    "min": 7,
                                    "max": 10
                                },
                                {
                                    "name": "RBP2, High G, Channel Alteration (choice list)",
                                    "type": "NUMBER",
                                    "min": 20,
                                    "max": 20
                                },
                                {
                                    "name": "RBP2, High G, Vegetative Protection, Left Bank (choice list)",
                                    "type": "NUMBER",
                                    "min": 9,
                                    "max": 10
                                },
                                {
                                    "name": "RBP2, High G, Sediment Deposition (choice list)",
                                    "type": "NUMBER",
                                    "min": 18,
                                    "max": 20
                                },
                                {
                                    "name": "RBP2, High G, Vegetative Protection, Right Bank (choice list)",
                                    "type": "NUMBER",
                                    "min": 9,
                                    "max": 10
                                },
                                {
                                    "name": "RBP2, Low G, habitat assessment total score",
                                    "type": "NUMBER",
                                    "min": 113,
                                    "max": 191
                                },
                                {
                                    "name": "Hydromorphone",
                                    "type": "NUMBER",
                                    "max": 116
                                },
                                {
                                    "name": "Buprenorphine",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Butylparaben",
                                    "type": "NUMBER",
                                    "max": 494
                                },
                                {
                                    "name": "Mevastatin",
                                    "type": "NUMBER",
                                    "max": 83.2
                                },
                                {
                                    "name": "Dehydroaripiprazole",
                                    "type": "NUMBER",
                                    "max": 95.7
                                },
                                {
                                    "name": "Ritalinic acid",
                                    "type": "NUMBER",
                                    "max": 128
                                },
                                {
                                    "name": "Chloramphenicol",
                                    "type": "NUMBER",
                                    "max": 109
                                },
                                {
                                    "name": "Naproxen",
                                    "type": "NUMBER",
                                    "max": 118
                                },
                                {
                                    "name": "Sulfamethazine",
                                    "type": "NUMBER",
                                    "max": 150
                                },
                                {
                                    "name": "Meperidine",
                                    "type": "NUMBER",
                                    "max": 151
                                },
                                {
                                    "name": "Methamphetamine",
                                    "type": "NUMBER",
                                    "max": 138
                                },
                                {
                                    "name": "Gemfibrozil",
                                    "type": "NUMBER",
                                    "max": 116
                                },
                                {
                                    "name": "Escitalopram",
                                    "type": "NUMBER",
                                    "max": 115
                                },
                                {
                                    "name": "Oxcarbazepine",
                                    "type": "NUMBER",
                                    "max": 107
                                },
                                {
                                    "name": "Diuron Metabolite",
                                    "type": "NUMBER",
                                    "max": 101
                                },
                                {
                                    "name": "Dry Solids at 105 C",
                                    "type": "NUMBER",
                                    "min": 33.9,
                                    "max": 77.2
                                },
                                {
                                    "name": "Morpholine, 3-methyl-2-phenyl-",
                                    "type": "NUMBER",
                                    "max": 125
                                },
                                {
                                    "name": "Dimethachlor",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Zolpidem phenyl-4-carboxylic acid",
                                    "type": "NUMBER",
                                    "max": 129
                                },
                                {
                                    "name": "Quetiapine",
                                    "type": "NUMBER",
                                    "max": 118
                                },
                                {
                                    "name": "Benzeneacetic acid, _alpha_-methyl-4-(2-methylpropyl)-",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Erythromycin-anhydro",
                                    "type": "NUMBER",
                                    "max": 115
                                },
                                {
                                    "name": "Phenobarbital",
                                    "type": "NUMBER",
                                    "max": 123
                                },
                                {
                                    "name": "Pravastatin",
                                    "type": "NUMBER",
                                    "max": 107
                                },
                                {
                                    "name": "Montelukast",
                                    "type": "NUMBER",
                                    "max": 147
                                },
                                {
                                    "name": "Tadalafil",
                                    "type": "NUMBER",
                                    "max": 84.2
                                },
                                {
                                    "name": "Pioglitazone",
                                    "type": "NUMBER",
                                    "max": 119
                                },
                                {
                                    "name": "Modafinil acid",
                                    "type": "NUMBER",
                                    "max": 99.2
                                },
                                {
                                    "name": "Hydroxybupropion",
                                    "type": "NUMBER",
                                    "max": 112
                                },
                                {
                                    "name": "2-ethylidene-1,5-dimethyl-3,3-diphenylpyrrolidine",
                                    "type": "NUMBER",
                                    "max": 116
                                },
                                {
                                    "name": "Methylphenidate",
                                    "type": "NUMBER",
                                    "max": 108
                                },
                                {
                                    "name": "Tylosin",
                                    "type": "NUMBER",
                                    "max": 156
                                },
                                {
                                    "name": "Desmethylcitalopram",
                                    "type": "NUMBER",
                                    "max": 123
                                },
                                {
                                    "name": "Atraton",
                                    "type": "NUMBER",
                                    "max": 112
                                },
                                {
                                    "name": "Trazodone",
                                    "type": "NUMBER",
                                    "max": 133
                                },
                                {
                                    "name": "Amitriptyline (+/-)-E-10-hydroxylated",
                                    "type": "NUMBER",
                                    "max": 123
                                },
                                {
                                    "name": "Lamotrigine",
                                    "type": "NUMBER",
                                    "max": 127
                                },
                                {
                                    "name": "Perfluorononanoic acid",
                                    "type": "NUMBER",
                                    "max": 97.6
                                },
                                {
                                    "name": "Benzoylecgonine",
                                    "type": "NUMBER",
                                    "max": 113
                                },
                                {
                                    "name": "Propachlor ESA",
                                    "type": "NUMBER",
                                    "max": 120
                                },
                                {
                                    "name": "Perfluorooctanoic acid",
                                    "type": "NUMBER",
                                    "max": 67.7
                                },
                                {
                                    "name": "Monuron",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Valsartan",
                                    "type": "NUMBER",
                                    "max": 108
                                },
                                {
                                    "name": "Perfluorooctanesulfonate",
                                    "type": "NUMBER",
                                    "max": 137
                                },
                                {
                                    "name": "Diclofenac",
                                    "type": "NUMBER",
                                    "max": 351
                                },
                                {
                                    "name": "Acebutolol",
                                    "type": "NUMBER",
                                    "max": 141
                                },
                                {
                                    "name": "Furosemide",
                                    "type": "NUMBER",
                                    "max": 135
                                },
                                {
                                    "name": "Bezafibrate",
                                    "type": "NUMBER",
                                    "max": 127
                                },
                                {
                                    "name": "2-Choro-6-ethylamino-4-amino-s-triazine",
                                    "type": "NUMBER",
                                    "max": 123
                                },
                                {
                                    "name": "_alpha_,_alpha_-Dimethylphenethylamine",
                                    "type": "NUMBER",
                                    "max": 119
                                },
                                {
                                    "name": "Methylparaben",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Clothianidin",
                                    "type": "NUMBER",
                                    "max": 128
                                },
                                {
                                    "name": "Cocaine",
                                    "type": "NUMBER",
                                    "max": 106
                                },
                                {
                                    "name": "Thiamethoxam",
                                    "type": "NUMBER",
                                    "max": 179
                                },
                                {
                                    "name": "Celecoxib",
                                    "type": "NUMBER",
                                    "max": 119
                                },
                                {
                                    "name": "Mecoprop",
                                    "type": "NUMBER",
                                    "max": 147
                                },
                                {
                                    "name": "Propachlor OA",
                                    "type": "NUMBER",
                                    "max": 119
                                },
                                {
                                    "name": "(+/-)11-nor-9-carboxy-delta-THC",
                                    "type": "NUMBER",
                                    "max": 105
                                },
                                {
                                    "name": "Oxymorphone",
                                    "type": "NUMBER",
                                    "max": 182
                                },
                                {
                                    "name": "Monoethylglycinexylidide",
                                    "type": "NUMBER",
                                    "max": 97.8
                                },
                                {
                                    "name": "Modafinil",
                                    "type": "NUMBER",
                                    "max": 98.6
                                },
                                {
                                    "name": "Normeperidine",
                                    "type": "NUMBER",
                                    "max": 121
                                },
                                {
                                    "name": "Benzenemethanol, _alpha_-[(1S)-1-(methylamino)ethyl]-, (_alpha_S)-",
                                    "type": "NUMBER",
                                    "max": 106
                                },
                                {
                                    "name": "Chromium(III)",
                                    "type": "NUMBER",
                                    "max": 0.0114
                                },
                                {
                                    "name": "Biomass/chlorophyll ratio",
                                    "type": "NUMBER",
                                    "min": 312,
                                    "max": 1530
                                },
                                {
                                    "name": "Pregabalin",
                                    "type": "NUMBER",
                                    "max": 115
                                },
                                {
                                    "name": "Phenylpropanolamine",
                                    "type": "NUMBER",
                                    "max": 120
                                },
                                {
                                    "name": "Phenytoin",
                                    "type": "NUMBER",
                                    "max": 121
                                },
                                {
                                    "name": "m-Hydroxybenzoylecgonine",
                                    "type": "NUMBER",
                                    "max": 256
                                },
                                {
                                    "name": "1-Phenethyl-4-(phenylpropionylamino)piperidine",
                                    "type": "NUMBER",
                                    "max": 122
                                },
                                {
                                    "name": "Norquetiapine",
                                    "type": "NUMBER",
                                    "max": 153
                                },
                                {
                                    "name": "Simvastatin",
                                    "type": "NUMBER",
                                    "max": 103
                                },
                                {
                                    "name": "Hydrochlorothiazide",
                                    "type": "NUMBER",
                                    "max": 102
                                },
                                {
                                    "name": "Omeprazole",
                                    "type": "NUMBER",
                                    "max": 201
                                },
                                {
                                    "name": "Sotalol",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Zolpidem",
                                    "type": "NUMBER",
                                    "max": 126
                                },
                                {
                                    "name": "Ketoprofen",
                                    "type": "NUMBER",
                                    "max": 101
                                },
                                {
                                    "name": "MDMA",
                                    "type": "NUMBER",
                                    "max": 127
                                },
                                {
                                    "name": "N-Phenyl-N-(4-piperidinyl)propanamide",
                                    "type": "NUMBER",
                                    "max": 154
                                },
                                {
                                    "name": "Mefenamic acid",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Metolachlor ESA",
                                    "type": "NUMBER",
                                    "max": 132
                                },
                                {
                                    "name": "Sumatriptan",
                                    "type": "NUMBER",
                                    "max": 159
                                },
                                {
                                    "name": "Triclocarban",
                                    "type": "NUMBER",
                                    "max": 138
                                },
                                {
                                    "name": "Sildenafil",
                                    "type": "NUMBER",
                                    "max": 152
                                },
                                {
                                    "name": "6-Acetylmorphine",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Dextrorphan",
                                    "type": "NUMBER",
                                    "max": 107
                                },
                                {
                                    "name": "Aripiprazole",
                                    "type": "NUMBER",
                                    "max": 105
                                },
                                {
                                    "name": "Primidone",
                                    "type": "NUMBER",
                                    "max": 66.5
                                },
                                {
                                    "name": "Diclofenac, 4-hydroxy",
                                    "type": "NUMBER",
                                    "max": 123
                                },
                                {
                                    "name": "Lederfen",
                                    "type": "NUMBER",
                                    "max": 145
                                },
                                {
                                    "name": "Carbamazepine 10,11 epoxide",
                                    "type": "NUMBER",
                                    "max": 112
                                },
                                {
                                    "name": "10,11-Dihydro-10-hydroxy Carbamazepine",
                                    "type": "NUMBER",
                                    "max": 87.3
                                },
                                {
                                    "name": "Calcium carbonate",
                                    "type": "NUMBER",
                                    "max": 330
                                },
                                {
                                    "name": "Cloud cover",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "Cyanides amenable to chlorination (HCN & CN)",
                                    "type": "NUMBER",
                                    "max": 0.04
                                },
                                {
                                    "name": "Settleable solids",
                                    "type": "NUMBER",
                                    "min": 0.98,
                                    "max": 53100
                                },
                                {
                                    "name": "Wind direction (direction from, expressed 0-360 deg)",
                                    "type": "NUMBER",
                                    "max": 320
                                },
                                {
                                    "name": "Halides",
                                    "type": "NUMBER",
                                    "min": 56,
                                    "max": 225
                                },
                                {
                                    "name": "Nitrate as N",
                                    "type": "NUMBER",
                                    "max": 294
                                },
                                {
                                    "name": "Heterotrophic bacteria",
                                    "type": "NUMBER",
                                    "min": 800,
                                    "max": 160000
                                },
                                {
                                    "name": "Sulfate as S",
                                    "type": "NUMBER",
                                    "max": 10053
                                },
                                {
                                    "name": "Selenium-78",
                                    "type": "NUMBER",
                                    "min": 0.745361846,
                                    "max": 0.745361846
                                },
                                {
                                    "name": "Iron-56",
                                    "type": "NUMBER",
                                    "min": 309.4080394,
                                    "max": 309.4080394
                                },
                                {
                                    "name": "Zinc-68",
                                    "type": "NUMBER",
                                    "min": 6.36809854,
                                    "max": 6.36809854
                                },
                                {
                                    "name": "Floating foam/suds - severity (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "NONE",
                                        "MILD",
                                        "MODERATE"
                                    ]
                                },
                                {
                                    "name": "Oil and Grease, surface slick/sheen - severity (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "NONE"
                                    ]
                                },
                                {
                                    "name": "Selenium-82",
                                    "type": "NUMBER",
                                    "min": 1.376610391,
                                    "max": 1.376610391
                                },
                                {
                                    "name": "Iron-54",
                                    "type": "NUMBER",
                                    "min": 225.326123,
                                    "max": 225.326123
                                },
                                {
                                    "name": "Zinc-67",
                                    "type": "NUMBER",
                                    "min": 5.784765098,
                                    "max": 5.784765098
                                },
                                {
                                    "name": "Weather condition (WMO code 4677) (choice list)",
                                    "type": "NUMBER",
                                    "max": 70
                                },
                                {
                                    "name": "Floating Garbage Severity (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "NONE",
                                        "MILD"
                                    ]
                                },
                                {
                                    "name": "Odor severity (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "NONE",
                                        "MILD"
                                    ]
                                },
                                {
                                    "name": "Chromium-52",
                                    "type": "NUMBER",
                                    "min": 2.184305876,
                                    "max": 2.184305876
                                },
                                {
                                    "name": "Velocity - stream",
                                    "type": "NUMBER",
                                    "max": 8.42
                                },
                                {
                                    "name": "Chromium-53",
                                    "type": "NUMBER",
                                    "min": 0.298146117,
                                    "max": 0.298146117
                                },
                                {
                                    "name": "Soluble Reactive Phosphorus (SRP)",
                                    "type": "NUMBER",
                                    "max": 0.989
                                },
                                {
                                    "name": "Inorganic nitrogen (ammonia, nitrate and nitrite)",
                                    "type": "NUMBER",
                                    "max": 243.88
                                },
                                {
                                    "name": "Bromine",
                                    "type": "NUMBER",
                                    "max": 2.13
                                },
                                {
                                    "name": "Ammonium as NH4",
                                    "type": "NUMBER",
                                    "max": 4.21
                                },
                                {
                                    "name": "Weight",
                                    "type": "NUMBER",
                                    "min": 10,
                                    "max": 25.2
                                },
                                {
                                    "name": "Particle distribution",
                                    "type": "NUMBER",
                                    "max": 84
                                },
                                {
                                    "name": "Di(2-ethylhexyl) phthalate",
                                    "type": "NUMBER",
                                    "max": 61
                                },
                                {
                                    "name": "Total carbon",
                                    "type": "NUMBER",
                                    "min": 3.7,
                                    "max": 7
                                },
                                {
                                    "name": "Stream width measure",
                                    "type": "NUMBER",
                                    "min": 0.247,
                                    "max": 170
                                },
                                {
                                    "name": "Distance from/to",
                                    "type": "NUMBER",
                                    "max": 1500
                                },
                                {
                                    "name": "Bacteria, iron+sulfur fixers",
                                    "type": "NUMBER",
                                    "min": 4,
                                    "max": 4
                                },
                                {
                                    "name": "Polyphosphate",
                                    "type": "NUMBER",
                                    "min": 0.05,
                                    "max": 0.05
                                },
                                {
                                    "name": "2,4,5-T isooctyl ester",
                                    "type": "NUMBER",
                                    "min": 59,
                                    "max": 59
                                },
                                {
                                    "name": "Ammonia as NH3",
                                    "type": "NUMBER",
                                    "max": 618
                                },
                                {
                                    "name": "Total fixed solids",
                                    "type": "NUMBER",
                                    "min": 1400,
                                    "max": 2800
                                },
                                {
                                    "name": "Total Kjeldahl nitrogen (Organic N & NH3)",
                                    "type": "NUMBER",
                                    "max": 117
                                },
                                {
                                    "name": "Oxygen-18",
                                    "type": "NUMBER",
                                    "min": -19.08,
                                    "max": -12.48
                                },
                                {
                                    "name": "Ammonia uptake",
                                    "type": "NUMBER",
                                    "max": 1.5
                                },
                                {
                                    "name": "Nitrite as N",
                                    "type": "NUMBER",
                                    "max": 2.43
                                },
                                {
                                    "name": "Cations-Anions",
                                    "type": "NUMBER",
                                    "min": -9.6,
                                    "max": 33.3
                                },
                                {
                                    "name": "Gasoline range organics",
                                    "type": "NUMBER",
                                    "max": 1.08
                                },
                                {
                                    "name": "Volatile dissolved solids",
                                    "type": "NUMBER",
                                    "min": 281,
                                    "max": 281
                                },
                                {
                                    "name": "Density of water at 20 deg C",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 1
                                },
                                {
                                    "name": "Carbonaceous biochemical oxygen demand, non-standard conditions",
                                    "type": "NUMBER",
                                    "min": 5.8,
                                    "max": 17
                                },
                                {
                                    "name": "Ferric ion",
                                    "type": "NUMBER",
                                    "max": 856
                                },
                                {
                                    "name": "Acidity, hydrogen ion (H+)",
                                    "type": "NUMBER",
                                    "min": 0.08,
                                    "max": 4.8
                                },
                                {
                                    "name": "Floating vegetation severity, choice list",
                                    "type": "STRING",
                                    "values": [
                                        "Mild"
                                    ]
                                },
                                {
                                    "name": "Cardiocladius",
                                    "type": "NUMBER",
                                    "min": 8,
                                    "max": 8
                                },
                                {
                                    "name": "Tanytarsus",
                                    "type": "NUMBER",
                                    "min": 4,
                                    "max": 4
                                },
                                {
                                    "name": "Pteronarcys",
                                    "type": "NUMBER",
                                    "min": 3,
                                    "max": 3
                                },
                                {
                                    "name": "Helicopsyche",
                                    "type": "NUMBER",
                                    "min": 20,
                                    "max": 150
                                },
                                {
                                    "name": "Hemerodromia",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 1
                                },
                                {
                                    "name": "Rhyacophila",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 3
                                },
                                {
                                    "name": "Eriocera",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 8
                                },
                                {
                                    "name": "Strontium-90",
                                    "type": "NUMBER",
                                    "max": 26
                                },
                                {
                                    "name": "Phaenopsectra",
                                    "type": "NUMBER",
                                    "min": 4,
                                    "max": 4
                                },
                                {
                                    "name": "Holorusia",
                                    "type": "NUMBER",
                                    "min": 4,
                                    "max": 4
                                },
                                {
                                    "name": "Cricotopus",
                                    "type": "NUMBER",
                                    "min": 27,
                                    "max": 200
                                },
                                {
                                    "name": "Brillia",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 1
                                },
                                {
                                    "name": "Symbiocladius",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 1
                                },
                                {
                                    "name": "Odontomesa",
                                    "type": "NUMBER",
                                    "min": 4,
                                    "max": 20
                                },
                                {
                                    "name": "Trichocladius",
                                    "type": "NUMBER",
                                    "min": 4,
                                    "max": 47
                                },
                                {
                                    "name": "Orthocladius",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 27
                                },
                                {
                                    "name": "Polypedilum",
                                    "type": "NUMBER",
                                    "min": 14,
                                    "max": 14
                                },
                                {
                                    "name": "Rheotanytarsus",
                                    "type": "NUMBER",
                                    "min": 41,
                                    "max": 120
                                },
                                {
                                    "name": "Arctopsyche",
                                    "type": "NUMBER",
                                    "min": 3,
                                    "max": 8
                                },
                                {
                                    "name": "Ochrotrichia",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 9
                                },
                                {
                                    "name": "Leucotrichia",
                                    "type": "NUMBER",
                                    "min": 2,
                                    "max": 12
                                },
                                {
                                    "name": "Depth of pond or reservoir in feet",
                                    "type": "NUMBER",
                                    "min": 6.9,
                                    "max": 266
                                },
                                {
                                    "name": "Pacifastacus",
                                    "type": "NUMBER",
                                    "min": 2,
                                    "max": 2
                                },
                                {
                                    "name": "Procladius",
                                    "type": "NUMBER",
                                    "min": 2,
                                    "max": 2
                                },
                                {
                                    "name": "Pentaneura",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 14
                                },
                                {
                                    "name": "Pseudochironomus",
                                    "type": "NUMBER",
                                    "min": 8,
                                    "max": 8
                                },
                                {
                                    "name": "Polycentropus",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 6
                                },
                                {
                                    "name": "Hexatoma",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 1
                                },
                                {
                                    "name": "Athripsodes",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 1
                                },
                                {
                                    "name": "Tipulidae",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 1
                                },
                                {
                                    "name": "Simulium",
                                    "type": "NUMBER",
                                    "min": 2,
                                    "max": 1000
                                },
                                {
                                    "name": "Atherix",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 53
                                },
                                {
                                    "name": "Diamesa",
                                    "type": "NUMBER",
                                    "min": 11,
                                    "max": 80
                                },
                                {
                                    "name": "Nanocladius",
                                    "type": "NUMBER",
                                    "min": 2,
                                    "max": 95
                                },
                                {
                                    "name": "Microtendipes",
                                    "type": "NUMBER",
                                    "min": 3,
                                    "max": 64
                                },
                                {
                                    "name": "Hydropsyche",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 160
                                },
                                {
                                    "name": "Cheumatopsyche",
                                    "type": "NUMBER",
                                    "min": 9,
                                    "max": 130
                                },
                                {
                                    "name": "Oecetis",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 10
                                },
                                {
                                    "name": "Brachycentrus",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 60
                                },
                                {
                                    "name": "Pteronarcella",
                                    "type": "NUMBER",
                                    "min": 1,
                                    "max": 150
                                },
                                {
                                    "name": "Potassium-40",
                                    "type": "NUMBER",
                                    "max": 570
                                },
                                {
                                    "name": "Chemical oxygen demand, (low level)",
                                    "type": "NUMBER",
                                    "max": 350
                                },
                                {
                                    "name": "Fixed dissolved solids",
                                    "type": "NUMBER",
                                    "min": 588,
                                    "max": 588
                                },
                                {
                                    "name": "Solids",
                                    "type": "NUMBER",
                                    "max": 68
                                },
                                {
                                    "name": "Sum of cations",
                                    "type": "NUMBER",
                                    "min": 0.39,
                                    "max": 7768.27
                                },
                                {
                                    "name": "Sum of anions",
                                    "type": "NUMBER",
                                    "min": 0.24,
                                    "max": 7719.53
                                },
                                {
                                    "name": "Alkalinity, Bicarbonate as CaCO3",
                                    "type": "NUMBER",
                                    "max": 161
                                },
                                {
                                    "name": "Light attenuation at measurement depth",
                                    "type": "NUMBER",
                                    "min": 29,
                                    "max": 99
                                },
                                {
                                    "name": "Sulfur-35",
                                    "type": "NUMBER",
                                    "min": 1.4,
                                    "max": 40
                                },
                                {
                                    "name": "Vernolate",
                                    "type": "NUMBER",
                                    "max": 0.1
                                },
                                {
                                    "name": "2,4,6-Trimethylphenol",
                                    "type": "NUMBER",
                                    "min": 30,
                                    "max": 35
                                },
                                {
                                    "name": "m-Nitrophenol",
                                    "type": "NUMBER",
                                    "min": 35,
                                    "max": 35
                                },
                                {
                                    "name": "Temperature, air, deg F",
                                    "type": "NUMBER",
                                    "max": 71.6
                                },
                                {
                                    "name": "2-(p-tert-Butylphenoxy)cyclohexanol",
                                    "type": "NUMBER",
                                    "min": 0.03,
                                    "max": 0.03
                                },
                                {
                                    "name": "Barban",
                                    "type": "NUMBER",
                                    "min": 58.1,
                                    "max": 139
                                },
                                {
                                    "name": "Caffeine-13C",
                                    "type": "NUMBER",
                                    "min": 49.8,
                                    "max": 197
                                },
                                {
                                    "name": "Ice cover, floating or solid - severity (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "None",
                                        "Serious",
                                        "Mild",
                                        "Moderate",
                                        "Extreme"
                                    ]
                                },
                                {
                                    "name": "Sulfur hexafluoride",
                                    "type": "NUMBER",
                                    "min": 13.6,
                                    "max": 1192
                                },
                                {
                                    "name": "Lead-210",
                                    "type": "NUMBER",
                                    "min": -0.1,
                                    "max": 1.5
                                },
                                {
                                    "name": "Polonium-210",
                                    "type": "NUMBER",
                                    "max": 0.23
                                },
                                {
                                    "name": "Radium-224",
                                    "type": "NUMBER",
                                    "min": 0.17,
                                    "max": 0.71
                                },
                                {
                                    "name": "Radium-228",
                                    "type": "NUMBER",
                                    "max": 1.75
                                },
                                {
                                    "name": "Neon-20/Neon-22 ratio",
                                    "type": "NUMBER",
                                    "min": 9.8,
                                    "max": 9.84
                                },
                                {
                                    "name": "Argon-40/Argon-36 ratio",
                                    "type": "NUMBER",
                                    "min": 294.2,
                                    "max": 297.1
                                },
                                {
                                    "name": "Krypton-86/Krypton-84 ratio",
                                    "type": "NUMBER",
                                    "min": 0.3037,
                                    "max": 0.305
                                },
                                {
                                    "name": "Xenon-130/Xenon-132 ratio",
                                    "type": "NUMBER",
                                    "min": 0.149,
                                    "max": 0.152
                                },
                                {
                                    "name": "Neon-20/Neon-22 error",
                                    "type": "NUMBER",
                                    "min": 0.016,
                                    "max": 0.049
                                },
                                {
                                    "name": "Argon-40/Argon-36 error",
                                    "type": "NUMBER",
                                    "min": 1.4,
                                    "max": 1.4
                                },
                                {
                                    "name": "Krypton-86/Krypton-84 error",
                                    "type": "NUMBER",
                                    "min": 0.0007,
                                    "max": 0.0028
                                },
                                {
                                    "name": "Xenon-130/Xenon-132 error",
                                    "type": "NUMBER",
                                    "min": 0.005,
                                    "max": 0.0051
                                },
                                {
                                    "name": "Helium-3/helium-4 error",
                                    "type": "NUMBER",
                                    "min": 1.37e-08,
                                    "max": 1.62e-08
                                },
                                {
                                    "name": "1-Bromo-3-chloropropane-d6",
                                    "type": "NUMBER",
                                    "min": 70.8,
                                    "max": 90.8
                                },
                                {
                                    "name": "Tetrahydrofuran-d8",
                                    "type": "NUMBER",
                                    "min": 79.9,
                                    "max": 128
                                },
                                {
                                    "name": "Coliphage",
                                    "type": "NUMBER",
                                    "max": 12000
                                },
                                {
                                    "name": "Germanium",
                                    "type": "NUMBER",
                                    "max": 0.841314011
                                },
                                {
                                    "name": "Rhenium",
                                    "type": "NUMBER",
                                    "min": 0.18,
                                    "max": 1.49
                                },
                                {
                                    "name": "Tellurium",
                                    "type": "NUMBER",
                                    "max": 0.21
                                },
                                {
                                    "name": "Hexamethylenetetramine",
                                    "type": "NUMBER",
                                    "max": 16
                                },
                                {
                                    "name": "1-(Aminomethyl)cyclohexaneacetic acid",
                                    "type": "NUMBER",
                                    "max": 561
                                },
                                {
                                    "name": "Chlorsulfuron",
                                    "type": "NUMBER",
                                    "max": 126
                                },
                                {
                                    "name": "Imazaquin",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Imazethapyr",
                                    "type": "NUMBER",
                                    "max": 122
                                },
                                {
                                    "name": "Azoxystrobin",
                                    "type": "NUMBER",
                                    "max": 111
                                },
                                {
                                    "name": "Morphine",
                                    "type": "NUMBER",
                                    "max": 129
                                },
                                {
                                    "name": "Propiconazole",
                                    "type": "NUMBER",
                                    "max": 264
                                },
                                {
                                    "name": "Tebuconazole",
                                    "type": "NUMBER",
                                    "max": 104
                                },
                                {
                                    "name": "Acetaminophen",
                                    "type": "NUMBER",
                                    "max": 102
                                },
                                {
                                    "name": "Bupropion",
                                    "type": "NUMBER",
                                    "max": 107
                                },
                                {
                                    "name": "Carbamazepine",
                                    "type": "NUMBER",
                                    "max": 113
                                },
                                {
                                    "name": "Cimetidine",
                                    "type": "NUMBER",
                                    "max": 150
                                },
                                {
                                    "name": "Codeine",
                                    "type": "NUMBER",
                                    "max": 129
                                },
                                {
                                    "name": "1,7-Dimethylxanthine",
                                    "type": "NUMBER",
                                    "max": 27
                                },
                                {
                                    "name": "Ethanamine, 2-(diphenylmethoxy)-N,N-dimethyl-",
                                    "type": "NUMBER",
                                    "max": 120
                                },
                                {
                                    "name": "Duloxetine",
                                    "type": "NUMBER",
                                    "max": 112
                                },
                                {
                                    "name": "Erythromycin",
                                    "type": "NUMBER",
                                    "max": 118
                                },
                                {
                                    "name": "Fluoxetine",
                                    "type": "NUMBER",
                                    "max": 111
                                },
                                {
                                    "name": "Norfluoxetine",
                                    "type": "NUMBER",
                                    "max": 120
                                },
                                {
                                    "name": "Ranitidine",
                                    "type": "NUMBER",
                                    "max": 181
                                },
                                {
                                    "name": "Sulfamethoxazole",
                                    "type": "NUMBER",
                                    "max": 123
                                },
                                {
                                    "name": "Thiabendazole",
                                    "type": "NUMBER",
                                    "max": 116
                                },
                                {
                                    "name": "Trimethoprim",
                                    "type": "NUMBER",
                                    "max": 142
                                },
                                {
                                    "name": "Warfarin",
                                    "type": "NUMBER",
                                    "max": 133
                                },
                                {
                                    "name": "Amphetamine",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Acetamide, 2-(diethylamino)-N-(2,6-dimethylphenyl)-",
                                    "type": "NUMBER",
                                    "max": 116
                                },
                                {
                                    "name": "Meprobamate",
                                    "type": "NUMBER",
                                    "max": 141
                                },
                                {
                                    "name": "Dextromethorphan",
                                    "type": "NUMBER",
                                    "max": 116
                                },
                                {
                                    "name": "Oxazepam",
                                    "type": "NUMBER",
                                    "max": 111
                                },
                                {
                                    "name": "Lorazepam",
                                    "type": "NUMBER",
                                    "max": 126
                                },
                                {
                                    "name": "Temazepam",
                                    "type": "NUMBER",
                                    "max": 196
                                },
                                {
                                    "name": "Verapamil",
                                    "type": "NUMBER",
                                    "max": 122
                                },
                                {
                                    "name": "Triamterene",
                                    "type": "NUMBER",
                                    "max": 162
                                },
                                {
                                    "name": "Fluconazole",
                                    "type": "NUMBER",
                                    "max": 96.1
                                },
                                {
                                    "name": "Loratadine",
                                    "type": "NUMBER",
                                    "max": 177
                                },
                                {
                                    "name": "Metformin",
                                    "type": "NUMBER",
                                    "max": 386
                                },
                                {
                                    "name": "Theophylline",
                                    "type": "NUMBER",
                                    "max": 107
                                },
                                {
                                    "name": "Morphinan-6-one, 4,5-epoxy-14-hydroxy-3-methoxy-17-methyl-, (5_alpha_)-",
                                    "type": "NUMBER",
                                    "max": 119
                                },
                                {
                                    "name": "Phendimetrazine",
                                    "type": "NUMBER",
                                    "max": 85.5
                                },
                                {
                                    "name": "Chlorpheniramine",
                                    "type": "NUMBER",
                                    "max": 178
                                },
                                {
                                    "name": "Carisoprodol",
                                    "type": "NUMBER",
                                    "max": 138
                                },
                                {
                                    "name": "Diazepam",
                                    "type": "NUMBER",
                                    "max": 116
                                },
                                {
                                    "name": "Methadone",
                                    "type": "NUMBER",
                                    "max": 109
                                },
                                {
                                    "name": "Atenolol",
                                    "type": "NUMBER",
                                    "max": 119
                                },
                                {
                                    "name": "Metaxalone",
                                    "type": "NUMBER",
                                    "max": 106
                                },
                                {
                                    "name": "Hydrocodone",
                                    "type": "NUMBER",
                                    "max": 125
                                },
                                {
                                    "name": "Propranol",
                                    "type": "NUMBER",
                                    "max": 123
                                },
                                {
                                    "name": "Tramadol",
                                    "type": "NUMBER",
                                    "max": 107
                                },
                                {
                                    "name": "Clonidine",
                                    "type": "NUMBER",
                                    "max": 95.2
                                },
                                {
                                    "name": "Diltiazem",
                                    "type": "NUMBER",
                                    "max": 123
                                },
                                {
                                    "name": "Amitriptyline",
                                    "type": "NUMBER",
                                    "max": 125
                                },
                                {
                                    "name": "Metoprolol",
                                    "type": "NUMBER",
                                    "max": 143
                                },
                                {
                                    "name": "Methotrexate",
                                    "type": "NUMBER",
                                    "max": 108
                                },
                                {
                                    "name": "Paroxetine",
                                    "type": "NUMBER",
                                    "max": 135
                                },
                                {
                                    "name": "Sertraline",
                                    "type": "NUMBER",
                                    "max": 105
                                },
                                {
                                    "name": "Fluticasone propionate",
                                    "type": "NUMBER",
                                    "max": 102
                                },
                                {
                                    "name": "Norsertraline",
                                    "type": "NUMBER",
                                    "max": 101
                                },
                                {
                                    "name": "Venlafaxine",
                                    "type": "NUMBER",
                                    "max": 106
                                },
                                {
                                    "name": "Famotidine",
                                    "type": "NUMBER",
                                    "max": 126
                                },
                                {
                                    "name": "Glipizide",
                                    "type": "NUMBER",
                                    "max": 167
                                },
                                {
                                    "name": "Glyburide",
                                    "type": "NUMBER",
                                    "max": 101
                                },
                                {
                                    "name": "Norverapamil",
                                    "type": "NUMBER",
                                    "max": 118
                                },
                                {
                                    "name": "Ketoconazole",
                                    "type": "NUMBER",
                                    "max": 105
                                },
                                {
                                    "name": "Nevirapine",
                                    "type": "NUMBER",
                                    "max": 128
                                },
                                {
                                    "name": "1-(3,4-dichlorophenyl)-3-methyl urea",
                                    "type": "NUMBER",
                                    "max": 9.74
                                },
                                {
                                    "name": "2-Aminobenzimidazole",
                                    "type": "NUMBER",
                                    "max": 17.4
                                },
                                {
                                    "name": "Alprazolam",
                                    "type": "NUMBER",
                                    "max": 104
                                },
                                {
                                    "name": "Desmethylvenlafaxine",
                                    "type": "NUMBER",
                                    "max": 125
                                },
                                {
                                    "name": "Imidacloprid",
                                    "type": "NUMBER",
                                    "max": 149
                                },
                                {
                                    "name": "Acetochlor OA",
                                    "type": "NUMBER",
                                    "max": 104
                                },
                                {
                                    "name": "Alachlor OA",
                                    "type": "NUMBER",
                                    "max": 99
                                },
                                {
                                    "name": "2-Chloro-4,6-diamino-s-triazine",
                                    "type": "NUMBER",
                                    "max": 1020
                                },
                                {
                                    "name": "Carbendazim",
                                    "type": "NUMBER",
                                    "max": 157
                                },
                                {
                                    "name": "Dimethenamid",
                                    "type": "NUMBER",
                                    "max": 116
                                },
                                {
                                    "name": "Dimethenamid ESA",
                                    "type": "NUMBER",
                                    "max": 126
                                },
                                {
                                    "name": "Methoxyfenozide",
                                    "type": "NUMBER",
                                    "max": 1.68
                                },
                                {
                                    "name": "Metolachlor OA",
                                    "type": "NUMBER",
                                    "max": 0.78
                                },
                                {
                                    "name": "Metochlor ESA",
                                    "type": "NUMBER",
                                    "max": 1320
                                },
                                {
                                    "name": "Siduron",
                                    "type": "NUMBER",
                                    "max": 0.01
                                },
                                {
                                    "name": "Sulfometuron methyl",
                                    "type": "NUMBER",
                                    "max": 122
                                },
                                {
                                    "name": "Alachlor ESA",
                                    "type": "NUMBER",
                                    "max": 120
                                },
                                {
                                    "name": "Chlorimuron-ethyl",
                                    "type": "NUMBER",
                                    "max": 124
                                },
                                {
                                    "name": "Lorazepam-D4",
                                    "type": "NUMBER",
                                    "min": 106,
                                    "max": 134
                                },
                                {
                                    "name": "Oxazepam-d5",
                                    "type": "NUMBER",
                                    "min": 138,
                                    "max": 178
                                },
                                {
                                    "name": "Tamoxifen-d5",
                                    "type": "NUMBER",
                                    "min": 227,
                                    "max": 254
                                },
                                {
                                    "name": "3-Phenoxybenzoic acid-13C6",
                                    "type": "NUMBER",
                                    "min": 93.6,
                                    "max": 123
                                },
                                {
                                    "name": "Acetochlor-d11",
                                    "type": "NUMBER",
                                    "min": 91,
                                    "max": 119
                                },
                                {
                                    "name": "Alachlor-d13",
                                    "type": "NUMBER",
                                    "min": 38.2,
                                    "max": 97.3
                                },
                                {
                                    "name": "Carbaryl-d7",
                                    "type": "NUMBER",
                                    "min": 85.9,
                                    "max": 135
                                },
                                {
                                    "name": "Carbendazim-d4",
                                    "type": "NUMBER",
                                    "min": 81.1,
                                    "max": 118
                                },
                                {
                                    "name": "Carbofuran-D3",
                                    "type": "NUMBER",
                                    "min": 82.1,
                                    "max": 112
                                },
                                {
                                    "name": "Deethylatrazine-d6",
                                    "type": "NUMBER",
                                    "min": 76.3,
                                    "max": 110
                                },
                                {
                                    "name": "Diflubenzuron-d4",
                                    "type": "NUMBER",
                                    "min": 92.3,
                                    "max": 113
                                },
                                {
                                    "name": "Hexazinone-d6",
                                    "type": "NUMBER",
                                    "min": 86.2,
                                    "max": 114
                                },
                                {
                                    "name": "Linuron-d6",
                                    "type": "NUMBER",
                                    "min": 98.2,
                                    "max": 108
                                },
                                {
                                    "name": "Malathion-D10",
                                    "type": "NUMBER",
                                    "min": 26.6,
                                    "max": 160
                                },
                                {
                                    "name": "Metolachlor-d6",
                                    "type": "NUMBER",
                                    "min": 79.5,
                                    "max": 106
                                },
                                {
                                    "name": "Nicosulfuron-d6",
                                    "type": "NUMBER",
                                    "min": 90.1,
                                    "max": 122
                                },
                                {
                                    "name": "Tebuconazole-d6",
                                    "type": "NUMBER",
                                    "min": 85.1,
                                    "max": 133
                                },
                                {
                                    "name": "Thiobencarb-d10",
                                    "type": "NUMBER",
                                    "min": 92.2,
                                    "max": 117
                                },
                                {
                                    "name": "cis-Permethrin-13C6",
                                    "type": "NUMBER",
                                    "min": 39.5,
                                    "max": 132
                                },
                                {
                                    "name": "Butachlor ESA",
                                    "type": "NUMBER",
                                    "max": 182
                                },
                                {
                                    "name": "Dimethachlor sulfonic acid",
                                    "type": "NUMBER",
                                    "min": 79.9,
                                    "max": 116
                                },
                                {
                                    "name": "Diuron-d6",
                                    "type": "NUMBER",
                                    "min": 91,
                                    "max": 113
                                },
                                {
                                    "name": "Thiabendazole-d4",
                                    "type": "NUMBER",
                                    "min": 86.5,
                                    "max": 109
                                },
                                {
                                    "name": "Albuterol-d9",
                                    "type": "NUMBER",
                                    "min": 121,
                                    "max": 177
                                },
                                {
                                    "name": "Diltiazem-d3",
                                    "type": "NUMBER",
                                    "min": 115,
                                    "max": 133
                                },
                                {
                                    "name": "Trimethoprim-d9",
                                    "type": "NUMBER",
                                    "min": 99.2,
                                    "max": 107
                                },
                                {
                                    "name": "Acetaminophen-d3",
                                    "type": "NUMBER",
                                    "min": 100,
                                    "max": 288
                                },
                                {
                                    "name": "Norfluoxetine-d6",
                                    "type": "NUMBER",
                                    "min": 67.1,
                                    "max": 90.5
                                },
                                {
                                    "name": "Methadone-d9",
                                    "type": "NUMBER",
                                    "min": 122,
                                    "max": 137
                                },
                                {
                                    "name": "Oxycodone-d3",
                                    "type": "NUMBER",
                                    "min": 124,
                                    "max": 141
                                },
                                {
                                    "name": "Hydrocodone-d3",
                                    "type": "NUMBER",
                                    "min": 102,
                                    "max": 115
                                },
                                {
                                    "name": "Temazepam-d5",
                                    "type": "NUMBER",
                                    "min": 105,
                                    "max": 116
                                },
                                {
                                    "name": "Caffeine-trimethyl-13C3",
                                    "type": "NUMBER",
                                    "max": 126
                                },
                                {
                                    "name": "Sulfamethoxazole-13C6",
                                    "type": "NUMBER",
                                    "max": 252
                                },
                                {
                                    "name": "Cotinine-d3",
                                    "type": "NUMBER",
                                    "min": 89.2,
                                    "max": 112
                                },
                                {
                                    "name": "Amphetamine-d6",
                                    "type": "NUMBER",
                                    "min": 73,
                                    "max": 124
                                },
                                {
                                    "name": "Codeine-d6",
                                    "type": "NUMBER",
                                    "min": 128,
                                    "max": 172
                                },
                                {
                                    "name": "Pseudoephedrine-d3",
                                    "type": "NUMBER",
                                    "min": 85.2,
                                    "max": 130
                                },
                                {
                                    "name": "Diphenhydramine-d3",
                                    "type": "NUMBER",
                                    "min": 127,
                                    "max": 141
                                },
                                {
                                    "name": "Fluoxetine-d6",
                                    "type": "NUMBER",
                                    "min": 73,
                                    "max": 108
                                },
                                {
                                    "name": "Diazepam-D5",
                                    "type": "NUMBER",
                                    "max": 106
                                },
                                {
                                    "name": "2,4-D-d3",
                                    "type": "NUMBER",
                                    "min": 74.9,
                                    "max": 94.3
                                },
                                {
                                    "name": "Organic phosphorus",
                                    "type": "NUMBER",
                                    "max": 0.06
                                },
                                {
                                    "name": "Inorganic nitrogen (nitrate and nitrite and ammoni",
                                    "type": "NUMBER",
                                    "min": 4.3,
                                    "max": 4.3
                                },
                                {
                                    "name": "Depth, bottom",
                                    "type": "NUMBER",
                                    "min": 0.1,
                                    "max": 134
                                },
                                {
                                    "name": "Lipids",
                                    "type": "NUMBER",
                                    "min": 2.5,
                                    "max": 12
                                },
                                {
                                    "name": "Axiothella",
                                    "type": "NUMBER",
                                    "min": 10,
                                    "max": 10
                                },
                                {
                                    "name": "Strontium-87/Strontium-86, ratio",
                                    "type": "NUMBER",
                                    "min": 0.72712,
                                    "max": 0.73247
                                },
                                {
                                    "name": "2,2',3,4,4',5,6,6'-Octachlorobiphenyl",
                                    "type": "NUMBER",
                                    "min": 40,
                                    "max": 110
                                },
                                {
                                    "name": "3,5-Dichlorobiphenyl",
                                    "type": "NUMBER",
                                    "max": 120
                                },
                                {
                                    "name": "cis-Nonachlor",
                                    "type": "NUMBER",
                                    "max": 15
                                },
                                {
                                    "name": "Oxychlordane",
                                    "type": "NUMBER",
                                    "max": 18
                                },
                                {
                                    "name": "o,p'-DDD",
                                    "type": "NUMBER",
                                    "max": 39
                                },
                                {
                                    "name": "o,p'-DDE",
                                    "type": "NUMBER",
                                    "max": 85
                                },
                                {
                                    "name": "o,p'-DDT",
                                    "type": "NUMBER",
                                    "max": 27
                                },
                                {
                                    "name": "2,2'-Biquinoline",
                                    "type": "NUMBER",
                                    "max": 13
                                },
                                {
                                    "name": "Phenanthridine",
                                    "type": "NUMBER",
                                    "max": 30
                                },
                                {
                                    "name": "3,5-Dimethylphenol",
                                    "type": "NUMBER",
                                    "max": 46
                                },
                                {
                                    "name": "Acridine",
                                    "type": "NUMBER",
                                    "max": 49
                                },
                                {
                                    "name": "Dibenzothiophene",
                                    "type": "NUMBER",
                                    "max": 113.75
                                },
                                {
                                    "name": "DDT/DDD/DDE, sum of p,p' & o,p' isomers",
                                    "type": "NUMBER",
                                    "max": 2100
                                },
                                {
                                    "name": "Chlordane, technical, and/or chlordane metabolites",
                                    "type": "NUMBER",
                                    "max": 88
                                },
                                {
                                    "name": "Plutonium-239 and Plutonium-240 combined",
                                    "type": "NUMBER",
                                    "min": -0.001,
                                    "max": 0.02
                                },
                                {
                                    "name": "Uranium-234",
                                    "type": "NUMBER",
                                    "max": 19
                                },
                                {
                                    "name": "Uranium-235",
                                    "type": "NUMBER",
                                    "max": 0.6
                                },
                                {
                                    "name": "Gallium",
                                    "type": "NUMBER",
                                    "max": 94
                                },
                                {
                                    "name": "Yttrium",
                                    "type": "NUMBER",
                                    "max": 120
                                },
                                {
                                    "name": "Pentachloronitrobenzene",
                                    "type": "NUMBER",
                                    "max": 38
                                },
                                {
                                    "name": "cis-Chlordane",
                                    "type": "NUMBER",
                                    "max": 24
                                },
                                {
                                    "name": "trans-Chlordane",
                                    "type": "NUMBER",
                                    "max": 15
                                },
                                {
                                    "name": "trans-Nonachlor",
                                    "type": "NUMBER",
                                    "max": 36
                                },
                                {
                                    "name": "Nonachlorobiphenyl",
                                    "type": "NUMBER",
                                    "min": 77.6,
                                    "max": 122
                                },
                                {
                                    "name": "Bifenthrin",
                                    "type": "NUMBER",
                                    "max": 0.5
                                },
                                {
                                    "name": "Cycloate",
                                    "type": "NUMBER",
                                    "max": 0.1
                                },
                                {
                                    "name": "Resmethrin",
                                    "type": "NUMBER",
                                    "max": 38.3
                                },
                                {
                                    "name": "Stream stage",
                                    "type": "NUMBER",
                                    "max": 0.02
                                },
                                {
                                    "name": "Radon-222",
                                    "type": "NUMBER",
                                    "min": -4,
                                    "max": 5100
                                },
                                {
                                    "name": "Oxidation reduction potential (ORP)",
                                    "type": "NUMBER",
                                    "min": -280,
                                    "max": 760
                                },
                                {
                                    "name": "Chlorophyll b",
                                    "type": "NUMBER",
                                    "max": 16.7
                                },
                                {
                                    "name": "Propachlor",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Butylate",
                                    "type": "NUMBER",
                                    "max": 1.1
                                },
                                {
                                    "name": "MCPB",
                                    "type": "NUMBER",
                                    "max": 0.22
                                },
                                {
                                    "name": "Methiocarb",
                                    "type": "NUMBER",
                                    "max": 148
                                },
                                {
                                    "name": "Propoxur",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Bentazon",
                                    "type": "NUMBER",
                                    "max": 150
                                },
                                {
                                    "name": "2,4-DB",
                                    "type": "NUMBER",
                                    "max": 132
                                },
                                {
                                    "name": "Oxamyl",
                                    "type": "NUMBER",
                                    "max": 158
                                },
                                {
                                    "name": "Triclopyr",
                                    "type": "NUMBER",
                                    "max": 106
                                },
                                {
                                    "name": "Oryzalin",
                                    "type": "NUMBER",
                                    "max": 112
                                },
                                {
                                    "name": "Neburon",
                                    "type": "NUMBER",
                                    "max": 116
                                },
                                {
                                    "name": "Diuron",
                                    "type": "NUMBER",
                                    "max": 627
                                },
                                {
                                    "name": "Chlorthal-Monomethyl",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "Chlorothalonil",
                                    "type": "NUMBER",
                                    "max": 0.18
                                },
                                {
                                    "name": "3-Hydroxycarbofuran",
                                    "type": "NUMBER",
                                    "max": 145
                                },
                                {
                                    "name": "Bromoxynil",
                                    "type": "NUMBER",
                                    "max": 122
                                },
                                {
                                    "name": "Aldicarb",
                                    "type": "NUMBER",
                                    "max": 112
                                },
                                {
                                    "name": "Aldicarb sulfone",
                                    "type": "NUMBER",
                                    "max": 161
                                },
                                {
                                    "name": "Aldicarb sulfoxide",
                                    "type": "NUMBER",
                                    "max": 112
                                },
                                {
                                    "name": "Ethalfluralin",
                                    "type": "NUMBER",
                                    "max": 0.073
                                },
                                {
                                    "name": "Terbacil",
                                    "type": "NUMBER",
                                    "max": 0.085
                                },
                                {
                                    "name": "Linuron",
                                    "type": "NUMBER",
                                    "max": 112
                                },
                                {
                                    "name": "Pebulate",
                                    "type": "NUMBER",
                                    "max": 0.1
                                },
                                {
                                    "name": "Triallate",
                                    "type": "NUMBER",
                                    "max": 0.0061
                                },
                                {
                                    "name": "Napropamide",
                                    "type": "NUMBER",
                                    "max": 0.012
                                },
                                {
                                    "name": "4-Bromo-3,5-dimethylphenyl N-Methylcarbamate",
                                    "type": "NUMBER",
                                    "max": 123
                                },
                                {
                                    "name": "Sodium plus potassium",
                                    "type": "NUMBER",
                                    "min": 0.3,
                                    "max": 24000
                                },
                                {
                                    "name": "Surface area",
                                    "type": "NUMBER",
                                    "max": 30600
                                },
                                {
                                    "name": "Picloram",
                                    "type": "STRING",
                                    "max": 0.08
                                },
                                {
                                    "name": "Dicamba",
                                    "type": "NUMBER",
                                    "max": 1.45
                                },
                                {
                                    "name": "_beta_-Endosulfan",
                                    "type": "NUMBER",
                                    "max": 1.1
                                },
                                {
                                    "name": "_beta_-Hexachlorocyclohexane",
                                    "type": "NUMBER",
                                    "max": 0.8
                                },
                                {
                                    "name": "_delta_-Hexachlorocyclohexane",
                                    "type": "NUMBER",
                                    "max": 0.95
                                },
                                {
                                    "name": "Endrin aldehyde",
                                    "type": "NUMBER",
                                    "max": 2
                                },
                                {
                                    "name": "_alpha_-Hexachlorocyclohexane",
                                    "type": "NUMBER",
                                    "max": 0.87
                                },
                                {
                                    "name": "Aroclor 1242",
                                    "type": "NUMBER",
                                    "max": 0.1
                                },
                                {
                                    "name": "Aroclor 1248",
                                    "type": "NUMBER",
                                    "max": 0.1
                                },
                                {
                                    "name": "Aroclor 1254",
                                    "type": "NUMBER",
                                    "max": 5.4
                                },
                                {
                                    "name": "Aroclor 1260",
                                    "type": "NUMBER",
                                    "max": 4.3
                                },
                                {
                                    "name": "Propazine",
                                    "type": "NUMBER",
                                    "max": 136
                                },
                                {
                                    "name": "Methomyl",
                                    "type": "NUMBER",
                                    "max": 111
                                },
                                {
                                    "name": "Methane",
                                    "type": "NUMBER",
                                    "max": 68
                                },
                                {
                                    "name": "Iodide",
                                    "type": "NUMBER",
                                    "max": 3.1
                                },
                                {
                                    "name": "Solar irradiation, local",
                                    "type": "NUMBER",
                                    "min": 0.5,
                                    "max": 8.5
                                },
                                {
                                    "name": "Biochemical oxygen demand, non-standard conditions",
                                    "type": "NUMBER",
                                    "max": 140
                                },
                                {
                                    "name": "o-Fluorophenol",
                                    "type": "NUMBER",
                                    "min": 0.0112,
                                    "max": 94.4
                                },
                                {
                                    "name": "Methylmercury(1+)",
                                    "type": "NUMBER",
                                    "max": 3.04
                                },
                                {
                                    "name": "Carbon-14",
                                    "type": "NUMBER",
                                    "min": 0.15,
                                    "max": 101.8
                                },
                                {
                                    "name": "Xylene",
                                    "type": "NUMBER",
                                    "max": 2.3
                                },
                                {
                                    "name": "1,2-Dimethylnaphthalene",
                                    "type": "NUMBER",
                                    "max": 24
                                },
                                {
                                    "name": "1,6-Dimethylnaphthalene",
                                    "type": "NUMBER",
                                    "max": 110
                                },
                                {
                                    "name": "1-Methylfluorene",
                                    "type": "NUMBER",
                                    "max": 56
                                },
                                {
                                    "name": "1-Methylphenanthrene",
                                    "type": "NUMBER",
                                    "max": 972.13
                                },
                                {
                                    "name": "1-Methylpyrene",
                                    "type": "NUMBER",
                                    "max": 270
                                },
                                {
                                    "name": "2,3,6-Trimethylnaphthalene",
                                    "type": "NUMBER",
                                    "max": 110
                                },
                                {
                                    "name": "2-Ethylnaphthalene",
                                    "type": "NUMBER",
                                    "max": 22
                                },
                                {
                                    "name": "2-Methylanthracene",
                                    "type": "NUMBER",
                                    "max": 150
                                },
                                {
                                    "name": "4H-Cyclopenta[def]phenanthrene",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "Benzo[e]pyrene",
                                    "type": "NUMBER",
                                    "max": 780
                                },
                                {
                                    "name": "Perylene",
                                    "type": "NUMBER",
                                    "max": 287.36
                                },
                                {
                                    "name": "Methylnaphthalene",
                                    "type": "NUMBER",
                                    "max": 14415.96
                                },
                                {
                                    "name": "C1-Phenanthrenes/anthracenes",
                                    "type": "NUMBER",
                                    "max": 4483.37
                                },
                                {
                                    "name": "C1-Fluoranthenes/pyrenes",
                                    "type": "NUMBER",
                                    "max": 381.82
                                },
                                {
                                    "name": "C1-MW 228 PAH",
                                    "type": "NUMBER",
                                    "max": 160
                                },
                                {
                                    "name": "C1-Benzopyrenes/perylenes",
                                    "type": "NUMBER",
                                    "max": 130
                                },
                                {
                                    "name": "C2-Naphthalenes",
                                    "type": "NUMBER",
                                    "max": 5912.56
                                },
                                {
                                    "name": "C2-Phenanthrenes/anthracenes",
                                    "type": "NUMBER",
                                    "max": 1500.24
                                },
                                {
                                    "name": "C2-Fluoranthenes/pyrenes",
                                    "type": "NUMBER",
                                    "max": 370
                                },
                                {
                                    "name": "C2-Benzo[a]anthracenes/chrysenes",
                                    "type": "NUMBER",
                                    "max": 230
                                },
                                {
                                    "name": "C3-Naphthalenes",
                                    "type": "NUMBER",
                                    "max": 4475.5
                                },
                                {
                                    "name": "C3-Phenanthrenes/anthracenes",
                                    "type": "NUMBER",
                                    "max": 852.88
                                },
                                {
                                    "name": "C3-Fluoranthenes/pyrenes",
                                    "type": "NUMBER",
                                    "max": 370
                                },
                                {
                                    "name": "C4-Naphthalenes",
                                    "type": "NUMBER",
                                    "max": 1993.31
                                },
                                {
                                    "name": "C4-Phenanthrenes/anthracenes",
                                    "type": "NUMBER",
                                    "max": 298.23
                                },
                                {
                                    "name": "C5-Phenanthrenes/anthracenes",
                                    "type": "NUMBER",
                                    "max": 90
                                },
                                {
                                    "name": "Ethinyl estradiol",
                                    "type": "NUMBER",
                                    "max": 148
                                },
                                {
                                    "name": "Estradiol",
                                    "type": "NUMBER",
                                    "max": 140
                                },
                                {
                                    "name": "Androsterone",
                                    "type": "NUMBER",
                                    "max": 0.43
                                },
                                {
                                    "name": "Estrone",
                                    "type": "NUMBER",
                                    "max": 119
                                },
                                {
                                    "name": "Progesterone",
                                    "type": "NUMBER",
                                    "max": 92.8
                                },
                                {
                                    "name": "Testosterone",
                                    "type": "NUMBER",
                                    "max": 90.2
                                },
                                {
                                    "name": "Bisphenol A-d16",
                                    "type": "NUMBER",
                                    "min": 55.2,
                                    "max": 123
                                },
                                {
                                    "name": "cis-Androsterone-2,2,3,4,4-d5",
                                    "type": "NUMBER",
                                    "min": 72.2,
                                    "max": 94.9
                                },
                                {
                                    "name": "Progesterone-13C3",
                                    "type": "NUMBER",
                                    "min": 6.3,
                                    "max": 79.5
                                },
                                {
                                    "name": "Cholesterol-d7",
                                    "type": "NUMBER",
                                    "min": 53.6,
                                    "max": 87
                                },
                                {
                                    "name": "Ethynylestradiol-d4",
                                    "type": "NUMBER",
                                    "min": 51.4,
                                    "max": 95.9
                                },
                                {
                                    "name": "trans-Diethyl-1,1,1',1'-d4-stilbestrol-3,3',5,5'-d4",
                                    "type": "NUMBER",
                                    "min": 45.9,
                                    "max": 94.1
                                },
                                {
                                    "name": "Mestranol-2,4,16,16-d4",
                                    "type": "NUMBER",
                                    "min": 57.6,
                                    "max": 94.9
                                },
                                {
                                    "name": "Estriol-2,4,16,17-d4",
                                    "type": "NUMBER",
                                    "min": 26.9,
                                    "max": 96.6
                                },
                                {
                                    "name": "16-Epiestriol-d2",
                                    "type": "NUMBER",
                                    "min": 16.6,
                                    "max": 94.2
                                },
                                {
                                    "name": "Medroxyprogesterone-d3",
                                    "type": "NUMBER",
                                    "min": 48.5,
                                    "max": 114
                                },
                                {
                                    "name": "Nandrolone-d3",
                                    "type": "NUMBER",
                                    "min": 67,
                                    "max": 98
                                },
                                {
                                    "name": "17_beta_-Estradiol-13,14,15,16,17,18-13C6",
                                    "type": "NUMBER",
                                    "min": 63,
                                    "max": 86.2
                                },
                                {
                                    "name": "Estrone-13,14,15,16,17,18-13C6",
                                    "type": "NUMBER",
                                    "min": 69.3,
                                    "max": 96.2
                                },
                                {
                                    "name": "Ethanol, 2-(4-nonylphenoxy)-",
                                    "type": "NUMBER",
                                    "max": 0.25
                                },
                                {
                                    "name": "4,4'-Isopropylidenediphenol",
                                    "type": "NUMBER",
                                    "max": 845
                                },
                                {
                                    "name": "3,4-Dichlorophenyl isocyanate",
                                    "type": "NUMBER",
                                    "max": 0.11
                                },
                                {
                                    "name": "Bisphenol A-d14",
                                    "type": "NUMBER",
                                    "max": 129
                                },
                                {
                                    "name": "Ferrous ion",
                                    "type": "NUMBER",
                                    "max": 66500
                                },
                                {
                                    "name": "Isobutyl alcohol-d6",
                                    "type": "NUMBER",
                                    "min": 81.4,
                                    "max": 155
                                },
                                {
                                    "name": "tert-Butanol",
                                    "type": "NUMBER",
                                    "max": 3.04
                                },
                                {
                                    "name": "Sulfur",
                                    "type": "NUMBER",
                                    "max": 1030
                                },
                                {
                                    "name": "Chloromethane",
                                    "type": "NUMBER",
                                    "max": 4.3
                                },
                                {
                                    "name": "trans-1,3-Dichloropropene",
                                    "type": "NUMBER",
                                    "max": 3.6
                                },
                                {
                                    "name": "cis-1,3-Dichloropropene",
                                    "type": "NUMBER",
                                    "max": 12
                                },
                                {
                                    "name": "tert-Amyl methyl ether",
                                    "type": "NUMBER",
                                    "max": 0.15
                                },
                                {
                                    "name": "Carbon disulfide",
                                    "type": "NUMBER",
                                    "max": 0.2
                                },
                                {
                                    "name": "cis-1,2-Dichloroethylene",
                                    "type": "NUMBER",
                                    "max": 7.4
                                },
                                {
                                    "name": "Styrene",
                                    "type": "NUMBER",
                                    "max": 0.152
                                },
                                {
                                    "name": "o-Xylene",
                                    "type": "NUMBER",
                                    "max": 2
                                },
                                {
                                    "name": "o-Ethyltoluene",
                                    "type": "NUMBER",
                                    "max": 0.004
                                },
                                {
                                    "name": "1,2,4-Trimethylbenzene",
                                    "type": "NUMBER",
                                    "max": 0.6
                                },
                                {
                                    "name": "1,3,5-Trimethylbenzene",
                                    "type": "NUMBER",
                                    "max": 0.2
                                },
                                {
                                    "name": "p-Cymene",
                                    "type": "NUMBER",
                                    "max": 0.2
                                },
                                {
                                    "name": "Methyl iodide",
                                    "type": "NUMBER",
                                    "max": 0.02
                                },
                                {
                                    "name": "CFC-113",
                                    "type": "NUMBER",
                                    "max": 84
                                },
                                {
                                    "name": "Methyl tert-butyl ether",
                                    "type": "NUMBER",
                                    "max": 8.98
                                },
                                {
                                    "name": "Methyl isobutyl ketone",
                                    "type": "NUMBER",
                                    "max": 0.54
                                },
                                {
                                    "name": "Acetone",
                                    "type": "NUMBER",
                                    "max": 110
                                },
                                {
                                    "name": "Methyl ethyl ketone",
                                    "type": "NUMBER",
                                    "max": 2.5
                                },
                                {
                                    "name": "1,2-Dichloroethane-d4",
                                    "type": "NUMBER",
                                    "min": 94.5,
                                    "max": 173
                                },
                                {
                                    "name": "m,p-Xylene",
                                    "type": "NUMBER",
                                    "max": 4
                                },
                                {
                                    "name": "Toluene-d8",
                                    "type": "NUMBER",
                                    "min": 79.3,
                                    "max": 118
                                },
                                {
                                    "name": "p-Bromofluorobenzene",
                                    "type": "NUMBER",
                                    "min": 0.0977,
                                    "max": 128
                                },
                                {
                                    "name": "Reservoir storage",
                                    "type": "NUMBER",
                                    "min": 25690,
                                    "max": 42960
                                },
                                {
                                    "name": "Terbuthylazine",
                                    "type": "NUMBER",
                                    "max": 214
                                },
                                {
                                    "name": "Hexazinone",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Bromacil",
                                    "type": "NUMBER",
                                    "max": 127
                                },
                                {
                                    "name": "Simazine",
                                    "type": "NUMBER",
                                    "max": 117
                                },
                                {
                                    "name": "Prometryn",
                                    "type": "NUMBER",
                                    "max": 29
                                },
                                {
                                    "name": "Prometon",
                                    "type": "NUMBER",
                                    "max": 113
                                },
                                {
                                    "name": "2-Chloro-4-isopropylamino-6-amino-s-triazine",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Cyanazine",
                                    "type": "NUMBER",
                                    "max": 130
                                },
                                {
                                    "name": "Fonofos",
                                    "type": "NUMBER",
                                    "max": 0.046
                                },
                                {
                                    "name": "Acenaphthylene",
                                    "type": "NUMBER",
                                    "max": 35.83
                                },
                                {
                                    "name": "Acenaphthene",
                                    "type": "NUMBER",
                                    "max": 86.05
                                },
                                {
                                    "name": "Anthracene",
                                    "type": "NUMBER",
                                    "max": 154.65
                                },
                                {
                                    "name": "Benzo(b)fluoranthene",
                                    "type": "NUMBER",
                                    "max": 1700
                                },
                                {
                                    "name": "Benzo[k]fluoranthene",
                                    "type": "NUMBER",
                                    "max": 570
                                },
                                {
                                    "name": "Benzo[a]pyrene",
                                    "type": "NUMBER",
                                    "max": 640
                                },
                                {
                                    "name": "Bis(2-chloroethoxy)methane",
                                    "type": "NUMBER",
                                    "max": 7
                                },
                                {
                                    "name": "Butyl benzyl phthalate",
                                    "type": "NUMBER",
                                    "max": 78
                                },
                                {
                                    "name": "Chrysene",
                                    "type": "NUMBER",
                                    "max": 840
                                },
                                {
                                    "name": "Diethyl phthalate",
                                    "type": "NUMBER",
                                    "max": 53
                                },
                                {
                                    "name": "Dimethyl phthalate",
                                    "type": "NUMBER",
                                    "max": 8000
                                },
                                {
                                    "name": "Fluoranthene",
                                    "type": "NUMBER",
                                    "max": 1400
                                },
                                {
                                    "name": "Fluorene",
                                    "type": "NUMBER",
                                    "max": 1030.21
                                },
                                {
                                    "name": "Indeno[1,2,3-cd]pyrene",
                                    "type": "NUMBER",
                                    "max": 610
                                },
                                {
                                    "name": "Isophorone",
                                    "type": "NUMBER",
                                    "max": 110
                                },
                                {
                                    "name": "N-Nitrosodiphenylamine",
                                    "type": "NUMBER",
                                    "max": 800
                                },
                                {
                                    "name": "Nitrobenzene",
                                    "type": "NUMBER",
                                    "max": 98.4
                                },
                                {
                                    "name": "Phenanthrene",
                                    "type": "NUMBER",
                                    "max": 3745.54
                                },
                                {
                                    "name": "Pyrene",
                                    "type": "NUMBER",
                                    "max": 1000
                                },
                                {
                                    "name": "Benzo[ghi]perylene",
                                    "type": "NUMBER",
                                    "max": 500
                                },
                                {
                                    "name": "Benz[a]anthracene",
                                    "type": "NUMBER",
                                    "max": 440
                                },
                                {
                                    "name": "o-Dichlorobenzene",
                                    "type": "NUMBER",
                                    "max": 0.023
                                },
                                {
                                    "name": "Dibenz[a,h]anthracene",
                                    "type": "NUMBER",
                                    "max": 260
                                },
                                {
                                    "name": "1,3-Dichlorobenzene",
                                    "type": "NUMBER",
                                    "max": 7
                                },
                                {
                                    "name": "p-Dichlorobenzene",
                                    "type": "NUMBER",
                                    "max": 80.5
                                },
                                {
                                    "name": "2-Chloronaphthalene",
                                    "type": "NUMBER",
                                    "max": 6
                                },
                                {
                                    "name": "Di-n-octyl phthalate",
                                    "type": "NUMBER",
                                    "max": 140
                                },
                                {
                                    "name": "2,4-Dichlorophenol",
                                    "type": "NUMBER",
                                    "max": 0.1
                                },
                                {
                                    "name": "2,4,6-Trichlorophenol",
                                    "type": "NUMBER",
                                    "max": 39
                                },
                                {
                                    "name": "p-Nitrophenol",
                                    "type": "NUMBER",
                                    "max": 0.67
                                },
                                {
                                    "name": "Phenol",
                                    "type": "NUMBER",
                                    "max": 1300
                                },
                                {
                                    "name": "Naphthalene",
                                    "type": "NUMBER",
                                    "max": 5765.84
                                },
                                {
                                    "name": "Dichlorvos",
                                    "type": "NUMBER",
                                    "max": 111
                                },
                                {
                                    "name": "Chlorpyrifos",
                                    "type": "NUMBER",
                                    "max": 108
                                },
                                {
                                    "name": "Pentachlorophenol",
                                    "type": "NUMBER",
                                    "max": 424
                                },
                                {
                                    "name": "Di(2-ethoxylhexyl) phthalate",
                                    "type": "NUMBER",
                                    "max": 2200
                                },
                                {
                                    "name": "Dibutyl phthalate",
                                    "type": "NUMBER",
                                    "max": 10000
                                },
                                {
                                    "name": "Metolachlor",
                                    "type": "NUMBER",
                                    "max": 119
                                },
                                {
                                    "name": "Atrazine",
                                    "type": "NUMBER",
                                    "max": 116
                                },
                                {
                                    "name": "Hexachlorobenzene",
                                    "type": "NUMBER",
                                    "max": 9
                                },
                                {
                                    "name": "Alachlor",
                                    "type": "NUMBER",
                                    "max": 115
                                },
                                {
                                    "name": "Acetochlor",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "1-Naphthol",
                                    "type": "NUMBER",
                                    "max": 0.0516
                                },
                                {
                                    "name": "Caffeine",
                                    "type": "NUMBER",
                                    "max": 118
                                },
                                {
                                    "name": "Endosulfan sulfate",
                                    "type": "NUMBER",
                                    "max": 4.6
                                },
                                {
                                    "name": "Metalaxyl",
                                    "type": "NUMBER",
                                    "max": 113
                                },
                                {
                                    "name": "Myclobutanil",
                                    "type": "NUMBER",
                                    "max": 6.15
                                },
                                {
                                    "name": "Oxyfluorfen",
                                    "type": "NUMBER",
                                    "max": 0.1
                                },
                                {
                                    "name": "3,4-Dichloroaniline",
                                    "type": "NUMBER",
                                    "max": 0.0731
                                },
                                {
                                    "name": "4-Chloro-2-methylphenol",
                                    "type": "NUMBER",
                                    "max": 0.0249
                                },
                                {
                                    "name": "Disulfoton sulfone",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "2-[2-[4-(1,1,3,3-Tetramethylbutyl)phenoxy]ethoxy]ethanol",
                                    "type": "NUMBER",
                                    "max": 61
                                },
                                {
                                    "name": "2-[4-(1,1,3,3-Tetramethylbutyl)phenoxy]ethanol",
                                    "type": "NUMBER",
                                    "max": 1.6
                                },
                                {
                                    "name": "Cotinine",
                                    "type": "NUMBER",
                                    "max": 142
                                },
                                {
                                    "name": "1-Methylnaphthalene",
                                    "type": "NUMBER",
                                    "max": 4959.96
                                },
                                {
                                    "name": "2,6-Dimethylnaphthalene",
                                    "type": "NUMBER",
                                    "max": 1400
                                },
                                {
                                    "name": "2-Methylnaphthalene",
                                    "type": "NUMBER",
                                    "max": 9456
                                },
                                {
                                    "name": "Coprosterol",
                                    "type": "NUMBER",
                                    "max": 1.5
                                },
                                {
                                    "name": "3-Methylindole",
                                    "type": "NUMBER",
                                    "max": 212
                                },
                                {
                                    "name": "Phenol, 2-(1,1-dimethylethyl)-4-methoxy-",
                                    "type": "NUMBER",
                                    "max": 0.1
                                },
                                {
                                    "name": "p-Cumylphenol",
                                    "type": "NUMBER",
                                    "max": 109
                                },
                                {
                                    "name": "p-Octylphenol",
                                    "type": "NUMBER",
                                    "max": 118
                                },
                                {
                                    "name": "p-(1,1,3,3-Tetramethylbutyl)phenol",
                                    "type": "NUMBER",
                                    "max": 103
                                },
                                {
                                    "name": "5-Tolyltriazole",
                                    "type": "NUMBER",
                                    "max": 1.7
                                },
                                {
                                    "name": "Acetophenone",
                                    "type": "NUMBER",
                                    "max": 1130
                                },
                                {
                                    "name": "AHTN",
                                    "type": "NUMBER",
                                    "max": 107
                                },
                                {
                                    "name": "(1R,2S,5R)-Menthol",
                                    "type": "NUMBER",
                                    "max": 117
                                },
                                {
                                    "name": "Anthraquinone",
                                    "type": "NUMBER",
                                    "max": 248
                                },
                                {
                                    "name": "Benzophenone",
                                    "type": "NUMBER",
                                    "max": 264
                                },
                                {
                                    "name": "_beta_-Sitosterol",
                                    "type": "NUMBER",
                                    "max": 23600
                                },
                                {
                                    "name": "Camphor",
                                    "type": "NUMBER",
                                    "max": 1330
                                },
                                {
                                    "name": "Carbazole",
                                    "type": "NUMBER",
                                    "max": 104
                                },
                                {
                                    "name": "Cholesterol",
                                    "type": "NUMBER",
                                    "max": 2130
                                },
                                {
                                    "name": "D-Limonene",
                                    "type": "NUMBER",
                                    "max": 965
                                },
                                {
                                    "name": "1,3,4,6,7,8-Hexahydro-4,6,6,7,8,8-hexamethylcyclopenta[g]-2-benzopyran",
                                    "type": "NUMBER",
                                    "max": 103
                                },
                                {
                                    "name": "Indole",
                                    "type": "NUMBER",
                                    "max": 1150
                                },
                                {
                                    "name": "Isoborneol",
                                    "type": "NUMBER",
                                    "max": 116
                                },
                                {
                                    "name": "Cumene",
                                    "type": "NUMBER",
                                    "max": 0.34
                                },
                                {
                                    "name": "Isoquinoline",
                                    "type": "NUMBER",
                                    "max": 103
                                },
                                {
                                    "name": "Methyl salicylate",
                                    "type": "NUMBER",
                                    "max": 136
                                },
                                {
                                    "name": "N,N-Diethyl-m-toluamide",
                                    "type": "NUMBER",
                                    "max": 109
                                },
                                {
                                    "name": "Nonylphenol diethoxylate",
                                    "type": "NUMBER",
                                    "max": 1300
                                },
                                {
                                    "name": "p-Cresol",
                                    "type": "NUMBER",
                                    "max": 8160
                                },
                                {
                                    "name": "4-Nonylphenols",
                                    "type": "NUMBER",
                                    "max": 2700
                                },
                                {
                                    "name": "Stigmastan-3_beta_-ol",
                                    "type": "NUMBER",
                                    "max": 2750
                                },
                                {
                                    "name": "Tris(2-chloroethyl) phosphate",
                                    "type": "NUMBER",
                                    "max": 113
                                },
                                {
                                    "name": "Tris(1,3-dichloro-2-propyl)phosphate",
                                    "type": "NUMBER",
                                    "max": 169
                                },
                                {
                                    "name": "Tributyl phosphate",
                                    "type": "NUMBER",
                                    "max": 112
                                },
                                {
                                    "name": "Triclosan",
                                    "type": "NUMBER",
                                    "max": 133
                                },
                                {
                                    "name": "Triethyl citrate",
                                    "type": "NUMBER",
                                    "max": 146
                                },
                                {
                                    "name": "Triphenyl phosphate",
                                    "type": "NUMBER",
                                    "max": 107
                                },
                                {
                                    "name": "Tris(2-butoxyethyl) phosphate",
                                    "type": "NUMBER",
                                    "max": 1920
                                },
                                {
                                    "name": "Fipronil",
                                    "type": "NUMBER",
                                    "max": 106
                                },
                                {
                                    "name": "Fipronil Sulfide",
                                    "type": "NUMBER",
                                    "max": 114
                                },
                                {
                                    "name": "Fipronil Sulfone",
                                    "type": "NUMBER",
                                    "max": 116
                                },
                                {
                                    "name": "Desulfinylfipronil amide",
                                    "type": "NUMBER",
                                    "max": 0.004
                                },
                                {
                                    "name": "Fipronil Desulfinyl",
                                    "type": "NUMBER",
                                    "max": 0.015
                                },
                                {
                                    "name": "Metribuzin",
                                    "type": "NUMBER",
                                    "max": 109
                                },
                                {
                                    "name": "2,6-Diethylaniline",
                                    "type": "NUMBER",
                                    "max": 0.001
                                },
                                {
                                    "name": "Trifluralin",
                                    "type": "NUMBER",
                                    "max": 0.11
                                },
                                {
                                    "name": "Dimethoate",
                                    "type": "NUMBER",
                                    "max": 0.0173
                                },
                                {
                                    "name": "Phorate",
                                    "type": "NUMBER",
                                    "max": 0.6
                                },
                                {
                                    "name": "S-Ethyl dipropylthiocarbamate",
                                    "type": "NUMBER",
                                    "max": 124
                                },
                                {
                                    "name": "Tebuthiuron",
                                    "type": "NUMBER",
                                    "max": 119
                                },
                                {
                                    "name": "Molinate",
                                    "type": "NUMBER",
                                    "max": 0.1
                                },
                                {
                                    "name": "Ethoprop",
                                    "type": "NUMBER",
                                    "max": 128
                                },
                                {
                                    "name": "Benfluralin",
                                    "type": "NUMBER",
                                    "max": 0.1
                                },
                                {
                                    "name": "Carbofuran",
                                    "type": "NUMBER",
                                    "max": 119
                                },
                                {
                                    "name": "Terbufos",
                                    "type": "NUMBER",
                                    "max": 0.56
                                },
                                {
                                    "name": "Pronamide",
                                    "type": "NUMBER",
                                    "max": 0.045
                                },
                                {
                                    "name": "Disulfoton",
                                    "type": "NUMBER",
                                    "max": 0.041
                                },
                                {
                                    "name": "Propanil",
                                    "type": "NUMBER",
                                    "max": 0.006
                                },
                                {
                                    "name": "Carbaryl",
                                    "type": "NUMBER",
                                    "max": 144
                                },
                                {
                                    "name": "Chlorthal-dimethyl",
                                    "type": "NUMBER",
                                    "max": 105
                                },
                                {
                                    "name": "Pendimethalin",
                                    "type": "NUMBER",
                                    "max": 46.3
                                },
                                {
                                    "name": "Propargite",
                                    "type": "NUMBER",
                                    "max": 2.3
                                },
                                {
                                    "name": "Azinphos-methyl",
                                    "type": "NUMBER",
                                    "max": 0.067
                                },
                                {
                                    "name": "1rs Cis-Permethrin",
                                    "type": "NUMBER",
                                    "max": 0.015
                                },
                                {
                                    "name": "Isodrin",
                                    "type": "NUMBER",
                                    "max": 106
                                },
                                {
                                    "name": "Phenol-d5",
                                    "type": "NUMBER",
                                    "min": 0.00711,
                                    "max": 72.7
                                },
                                {
                                    "name": "2,4,6-Tribromophenol",
                                    "type": "NUMBER",
                                    "min": 0.0248,
                                    "max": 117
                                },
                                {
                                    "name": "Caffeine-d9",
                                    "type": "NUMBER",
                                    "max": 139
                                },
                                {
                                    "name": "Nitrobenzene-D5",
                                    "type": "NUMBER",
                                    "min": 0.0188,
                                    "max": 116
                                },
                                {
                                    "name": "p-Terphenyl-d14",
                                    "type": "NUMBER",
                                    "min": 7.6,
                                    "max": 120
                                },
                                {
                                    "name": "2-Fluorobiphenyl",
                                    "type": "NUMBER",
                                    "min": 0.0214,
                                    "max": 121
                                },
                                {
                                    "name": "Decafluorobiphenyl",
                                    "type": "NUMBER",
                                    "max": 104
                                },
                                {
                                    "name": "Fluoranthene-d10",
                                    "type": "NUMBER",
                                    "max": 143
                                },
                                {
                                    "name": "2,2',3,3',4,4',5,6,6'-Nonachlorobiphenyl",
                                    "type": "NUMBER",
                                    "min": 76.2,
                                    "max": 116
                                },
                                {
                                    "name": "Diazinon-D10",
                                    "type": "NUMBER",
                                    "min": 45.2,
                                    "max": 188
                                },
                                {
                                    "name": "_alpha_-1,2,3,4,5,6-Hexachlorocyclohexane-D6 or alpha-HCH D6",
                                    "type": "NUMBER",
                                    "max": 170
                                },
                                {
                                    "name": "Volatile suspended solids",
                                    "type": "NUMBER",
                                    "max": 808
                                },
                                {
                                    "name": "Fixed suspended solids",
                                    "type": "NUMBER",
                                    "max": 164000
                                },
                                {
                                    "name": "Chemical oxygen demand, (high level)",
                                    "type": "NUMBER",
                                    "max": 1700
                                },
                                {
                                    "name": "Dichlorobromomethane",
                                    "type": "NUMBER",
                                    "max": 7.8
                                },
                                {
                                    "name": "Carbon tetrachloride",
                                    "type": "NUMBER",
                                    "max": 6.4
                                },
                                {
                                    "name": "1,2-Dichloroethane",
                                    "type": "NUMBER",
                                    "max": 7.4
                                },
                                {
                                    "name": "Tribromomethane",
                                    "type": "NUMBER",
                                    "max": 9.6
                                },
                                {
                                    "name": "Chlorodibromomethane",
                                    "type": "NUMBER",
                                    "max": 9.1
                                },
                                {
                                    "name": "Chloroform",
                                    "type": "NUMBER",
                                    "max": 9.5
                                },
                                {
                                    "name": "Toluene",
                                    "type": "NUMBER",
                                    "max": 6.9
                                },
                                {
                                    "name": "Benzene",
                                    "type": "NUMBER",
                                    "max": 6.6
                                },
                                {
                                    "name": "Chlorobenzene",
                                    "type": "NUMBER",
                                    "max": 7.7
                                },
                                {
                                    "name": "Chloroethane",
                                    "type": "NUMBER",
                                    "max": 4.7
                                },
                                {
                                    "name": "Ethylbenzene",
                                    "type": "NUMBER",
                                    "max": 7.7
                                },
                                {
                                    "name": "Methyl bromide",
                                    "type": "NUMBER",
                                    "max": 5.1
                                },
                                {
                                    "name": "Methylene chloride",
                                    "type": "NUMBER",
                                    "max": 8.5
                                },
                                {
                                    "name": "Tetrachloroethylene",
                                    "type": "NUMBER",
                                    "max": 6.9
                                },
                                {
                                    "name": "CFC-11",
                                    "type": "NUMBER",
                                    "max": 640
                                },
                                {
                                    "name": "1,1-Dichloroethane",
                                    "type": "NUMBER",
                                    "max": 7.2
                                },
                                {
                                    "name": "1,1-Dichloroethene",
                                    "type": "NUMBER",
                                    "max": 4.6
                                },
                                {
                                    "name": "1,1,1-Trichloroethane",
                                    "type": "NUMBER",
                                    "max": 5.3
                                },
                                {
                                    "name": "1,1,2-Trichloroethane",
                                    "type": "NUMBER",
                                    "max": 8.2
                                },
                                {
                                    "name": "1,1,2,2-Tetrachloroethane",
                                    "type": "NUMBER",
                                    "max": 8.4
                                },
                                {
                                    "name": "1,2-Dichloropropane",
                                    "type": "NUMBER",
                                    "max": 6.9
                                },
                                {
                                    "name": "trans-1,2-Dichloroethylene",
                                    "type": "NUMBER",
                                    "max": 7.6
                                },
                                {
                                    "name": "2-Chloroethyl vinyl ether",
                                    "type": "NUMBER",
                                    "max": 9
                                },
                                {
                                    "name": "CFC-12",
                                    "type": "NUMBER",
                                    "max": 330
                                },
                                {
                                    "name": "Vinyl chloride",
                                    "type": "NUMBER",
                                    "max": 4.3
                                },
                                {
                                    "name": "Trichloroethylene",
                                    "type": "NUMBER",
                                    "max": 6.5
                                },
                                {
                                    "name": "Trihalomethanes",
                                    "type": "NUMBER",
                                    "max": 36
                                },
                                {
                                    "name": "Alpha emitting radium isotopes",
                                    "type": "NUMBER",
                                    "max": 1.1
                                },
                                {
                                    "name": "Color",
                                    "type": "NUMBER",
                                    "max": 250
                                },
                                {
                                    "name": "Carbonaceous biochemical oxygen demand, standard conditions",
                                    "type": "NUMBER",
                                    "max": 62
                                },
                                {
                                    "name": "Carbon-13/Carbon-12 ratio",
                                    "type": "NUMBER",
                                    "min": -14.88,
                                    "max": 2.2
                                },
                                {
                                    "name": "Alpha particle",
                                    "type": "NUMBER",
                                    "min": -1.1,
                                    "max": 11000
                                },
                                {
                                    "name": "Beta particle",
                                    "type": "NUMBER",
                                    "max": 7600
                                },
                                {
                                    "name": "Flow rate, instantaneous",
                                    "type": "NUMBER",
                                    "max": 610
                                },
                                {
                                    "name": "Phenols",
                                    "type": "NUMBER",
                                    "max": 80
                                },
                                {
                                    "name": "Phytoplankton",
                                    "type": "NUMBER",
                                    "max": 300000
                                },
                                {
                                    "name": "Algal growth potential",
                                    "type": "NUMBER",
                                    "max": 375
                                },
                                {
                                    "name": "Depth, from ground surface to well water level",
                                    "type": "NUMBER",
                                    "max": 251
                                },
                                {
                                    "name": "Depth to water level below land surface",
                                    "type": "NUMBER",
                                    "max": 824
                                },
                                {
                                    "name": "Hydrolyzable phosphorus",
                                    "type": "NUMBER",
                                    "max": 1.1
                                },
                                {
                                    "name": "Ethylan",
                                    "type": "NUMBER",
                                    "max": 3500
                                },
                                {
                                    "name": "gamma-HCH (Lindane)",
                                    "type": "NUMBER",
                                    "max": 0.9
                                },
                                {
                                    "name": "Chlordane, technical",
                                    "type": "NUMBER",
                                    "max": 3
                                },
                                {
                                    "name": "_alpha_-Endosulfan",
                                    "type": "NUMBER",
                                    "max": 2
                                },
                                {
                                    "name": "Polychlorinated biphenyls",
                                    "type": "NUMBER",
                                    "max": 180
                                },
                                {
                                    "name": "Dichlorprop",
                                    "type": "NUMBER",
                                    "max": 110
                                },
                                {
                                    "name": "Nitrogen ion",
                                    "type": "NUMBER",
                                    "max": 3.39
                                },
                                {
                                    "name": "Hydrogen cyanide",
                                    "type": "NUMBER",
                                    "min": 64,
                                    "max": 64
                                },
                                {
                                    "name": "Tritium",
                                    "type": "NUMBER",
                                    "min": -0.1,
                                    "max": 35000
                                },
                                {
                                    "name": "Erbium",
                                    "type": "NUMBER",
                                    "max": 0.88
                                },
                                {
                                    "name": "Gadolinium",
                                    "type": "NUMBER",
                                    "max": 2.5
                                },
                                {
                                    "name": "Holmium",
                                    "type": "NUMBER",
                                    "max": 4
                                },
                                {
                                    "name": "Neodymium",
                                    "type": "NUMBER",
                                    "max": 160
                                },
                                {
                                    "name": "Praseodymium",
                                    "type": "NUMBER",
                                    "max": 3.1
                                },
                                {
                                    "name": "Thulium",
                                    "type": "NUMBER",
                                    "max": 0.086
                                },
                                {
                                    "name": "Helium-3/helium-4 ratio",
                                    "type": "NUMBER",
                                    "max": 1.444e-06
                                },
                                {
                                    "name": "Neon",
                                    "type": "NUMBER",
                                    "min": 4.3e-09,
                                    "max": 2.34e-07
                                },
                                {
                                    "name": "Helium-4",
                                    "type": "NUMBER",
                                    "min": 6e-10,
                                    "max": 9.92e-08
                                },
                                {
                                    "name": "Argon",
                                    "type": "NUMBER",
                                    "min": 7.027e-06,
                                    "max": 1.517
                                },
                                {
                                    "name": "Krypton",
                                    "type": "NUMBER",
                                    "min": 2.3e-09,
                                    "max": 8.6e-08
                                },
                                {
                                    "name": "Xenon",
                                    "type": "NUMBER",
                                    "min": 3e-10,
                                    "max": 1.26e-08
                                },
                                {
                                    "name": "Temperature, water, deg F",
                                    "type": "NUMBER",
                                    "min": 3.4,
                                    "max": 9.8
                                },
                                {
                                    "name": "RBP2, Instream Features, Channelized (Y/N) (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "NO",
                                        "YES"
                                    ]
                                },
                                {
                                    "name": "RBP2, Aquatic vegetation, portion of reach with AV (%)",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "Depth, Secchi disk depth",
                                    "type": "NUMBER",
                                    "max": 216
                                },
                                {
                                    "name": "Bank erosion stability (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "MDST",
                                        "UNST",
                                        "STAB",
                                        "MDUS"
                                    ]
                                },
                                {
                                    "name": "Riparian Width RDB",
                                    "type": "NUMBER",
                                    "max": 700
                                },
                                {
                                    "name": "Chlorophyll a - Periphyton (attached)",
                                    "type": "NUMBER",
                                    "min": 0.0974099612742749,
                                    "max": 217.085056554099
                                },
                                {
                                    "name": "RBP2, Habitat type, vegetated banks (%)",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "RBP2, Instream features, high water mark",
                                    "type": "NUMBER",
                                    "max": 217
                                },
                                {
                                    "name": "Kick Time",
                                    "type": "NUMBER",
                                    "min": 48,
                                    "max": 240
                                },
                                {
                                    "name": "Chlorophyll a, corrected for pheophytin",
                                    "type": "NUMBER",
                                    "min": 0.71,
                                    "max": 60.89
                                },
                                {
                                    "name": "RBP2, Habitat type, riffle (%)",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "RBP2, Substrate, organic, muck-mud, black-fine (FPOM)",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "RBP2, Habitat type, snags (%)",
                                    "type": "NUMBER",
                                    "max": 80
                                },
                                {
                                    "name": "RBP2, Aquatic Vegetation, Dominant Type & Species (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "ROOTED EMERG",
                                        "ATTACHED ALG",
                                        "ROOTED FLOAT",
                                        "ROOTED SUBME",
                                        "FREE FLOATIN"
                                    ]
                                },
                                {
                                    "name": "RBP2, Habitat type, run (%)",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "RBP2, Instream features, est_ stream depth",
                                    "type": "NUMBER",
                                    "max": 59
                                },
                                {
                                    "name": "Riparian Width LDB",
                                    "type": "NUMBER",
                                    "max": 1000
                                },
                                {
                                    "name": "RBP2, Watershed, Local Erosion (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "MODERATE",
                                        "NONE",
                                        "HEAVY"
                                    ]
                                },
                                {
                                    "name": "RBP2, Substrate, Inorganic, boulder, >256 mm",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "Total Nitrogen, mixed forms",
                                    "type": "NUMBER",
                                    "max": 691
                                },
                                {
                                    "name": "RBP2, Instream Features, Canopy Cover (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "PARTLY OPEN",
                                        "SHADED",
                                        "PART SHADED"
                                    ]
                                },
                                {
                                    "name": "Kick Depth",
                                    "type": "NUMBER",
                                    "min": -9,
                                    "max": 317
                                },
                                {
                                    "name": "RBP2, Substrate, organic, marl, grey shell fragments",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "RBP2, Habitat type, pools (%)",
                                    "type": "NUMBER",
                                    "max": 95
                                },
                                {
                                    "name": "RBP2, Substrate, organic, detritus, sticks, wood, etc_ (CPOM)",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "RBP2, Substrate, Inorganic, Silt, 0_004-0_06 mm",
                                    "type": "NUMBER",
                                    "max": 80
                                },
                                {
                                    "name": "RBP2, Instream features, est_ stream width",
                                    "type": "NUMBER",
                                    "max": 200
                                },
                                {
                                    "name": "Ash Free Dry Mass",
                                    "type": "NUMBER",
                                    "min": 0.0190367476431151,
                                    "max": 17.4916698028725
                                },
                                {
                                    "name": "Bank vegetative stability (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "G",
                                        "E",
                                        "F",
                                        "P"
                                    ]
                                },
                                {
                                    "name": "RBP2, Habitat type, sand (%)",
                                    "type": "NUMBER",
                                    "max": 200
                                },
                                {
                                    "name": "RBP2, Substrate, inorganic, sand, 0_06-2_0 mm",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "RBP2, Riparian Vegetation, Dominant Species Present (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "TREES",
                                        "SHRUBS",
                                        "GRASSES",
                                        "HERBACEOUS",
                                        "OTHER"
                                    ]
                                },
                                {
                                    "name": "Sandy Substrate (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "NO",
                                        "YES"
                                    ]
                                },
                                {
                                    "name": "RBP2, Substrate, inorganic, clay, <0_004 mm",
                                    "type": "NUMBER",
                                    "max": 80
                                },
                                {
                                    "name": "Rocky Substrate (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "YES",
                                        "NO"
                                    ]
                                },
                                {
                                    "name": "Slow Riffle",
                                    "type": "STRING",
                                    "values": [
                                        "YES",
                                        "NO"
                                    ]
                                },
                                {
                                    "name": "RBP2, Substrate, inorganic, gravel, 2-64 mm",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "RBP2, Substrate, inorganic, cobble, 64-256 mm",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "Cross-section Depth",
                                    "type": "NUMBER",
                                    "max": 37.5
                                },
                                {
                                    "name": "RBP2, Watershed, Predominant Surrounding Landuse (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "OTHER",
                                        "FOREST",
                                        "RESIDENTIAL",
                                        "FIELD/PASTUR",
                                        "AGRICULTURAL",
                                        "COMMERCIAL",
                                        "INDUSTRIAL"
                                    ]
                                },
                                {
                                    "name": "RBP2, Substrate, inorganic, bedrock",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "Fast Riffle",
                                    "type": "STRING",
                                    "values": [
                                        "NO",
                                        "YES"
                                    ]
                                },
                                {
                                    "name": "RBP2, Habitat type, gravel-cobble (%)",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "Count",
                                    "type": "NUMBER",
                                    "max": 6383
                                },
                                {
                                    "name": "Giardia",
                                    "type": "NUMBER",
                                    "max": 2.9
                                },
                                {
                                    "name": "p,p'-DDT",
                                    "type": "NUMBER",
                                    "max": 140
                                },
                                {
                                    "name": "2,4-D",
                                    "type": "NUMBER",
                                    "max": 156
                                },
                                {
                                    "name": "Aldrin",
                                    "type": "NUMBER",
                                    "max": 0.99
                                },
                                {
                                    "name": "2,4,5-T",
                                    "type": "NUMBER",
                                    "max": 134
                                },
                                {
                                    "name": "p,p'-DDE",
                                    "type": "NUMBER",
                                    "max": 2000
                                },
                                {
                                    "name": "Parathion",
                                    "type": "NUMBER",
                                    "max": 0.33
                                },
                                {
                                    "name": "Methoxychlor",
                                    "type": "NUMBER",
                                    "max": 0.12
                                },
                                {
                                    "name": "Silvex",
                                    "type": "NUMBER",
                                    "max": 137
                                },
                                {
                                    "name": "Methyl parathion",
                                    "type": "NUMBER",
                                    "max": 0.3
                                },
                                {
                                    "name": "Endrin",
                                    "type": "NUMBER",
                                    "max": 21
                                },
                                {
                                    "name": "Heptachlor",
                                    "type": "NUMBER",
                                    "max": 1.2
                                },
                                {
                                    "name": "Diazinon",
                                    "type": "NUMBER",
                                    "max": 119
                                },
                                {
                                    "name": "Dieldrin",
                                    "type": "NUMBER",
                                    "max": 79
                                },
                                {
                                    "name": "Toxaphene",
                                    "type": "NUMBER",
                                    "max": 1000
                                },
                                {
                                    "name": "Malathion",
                                    "type": "NUMBER",
                                    "max": 130
                                },
                                {
                                    "name": "p,p'-DDD",
                                    "type": "NUMBER",
                                    "max": 71
                                },
                                {
                                    "name": "Heptachlor epoxide",
                                    "type": "NUMBER",
                                    "max": 10
                                },
                                {
                                    "name": "Salinity",
                                    "type": "NUMBER",
                                    "min": 0.01,
                                    "max": 3290
                                },
                                {
                                    "name": "Hardness",
                                    "type": "NUMBER",
                                    "max": 1330
                                },
                                {
                                    "name": "Total Kjeldahl nitrogen",
                                    "type": "NUMBER",
                                    "max": 3.88
                                },
                                {
                                    "name": "Total hardness",
                                    "type": "NUMBER",
                                    "max": 592
                                },
                                {
                                    "name": "Nitrate + Nitrite",
                                    "type": "NUMBER",
                                    "max": 81
                                },
                                {
                                    "name": "Percent Solids",
                                    "type": "NUMBER",
                                    "min": 10.9,
                                    "max": 91.1
                                },
                                {
                                    "name": "Fluorine",
                                    "type": "NUMBER",
                                    "max": 6.8
                                },
                                {
                                    "name": "Organics mix, unspecified",
                                    "type": "NUMBER",
                                    "min": 5,
                                    "max": 99
                                },
                                {
                                    "name": "Terbium",
                                    "type": "NUMBER",
                                    "max": 10
                                },
                                {
                                    "name": "Tin",
                                    "type": "NUMBER",
                                    "max": 40
                                },
                                {
                                    "name": "Rubidium",
                                    "type": "NUMBER",
                                    "max": 206
                                },
                                {
                                    "name": "Tungsten",
                                    "type": "NUMBER",
                                    "max": 131
                                },
                                {
                                    "name": "Lutetium",
                                    "type": "NUMBER",
                                    "max": 11.4
                                },
                                {
                                    "name": "Weather comments (text)",
                                    "type": "STRING",
                                    "values": [
                                        "Current weather: cloudy, no precipitation, breeze, warm",
                                        "Past 24 hour weather: cloudy, rain, light breeze, warm",
                                        "Past 24 hour weather: cloudy, light rain, breeze, warm",
                                        "Current weather: cloudy, light rain, light breeze, warm",
                                        "Overcast with some drizzle",
                                        "Overcast with recent precipitation",
                                        "overcast, light drizzle",
                                        "Sunny, overcast",
                                        "Overcast and breezy",
                                        "Sunny, Breezy, hazy",
                                        "Sunny, calm",
                                        "Sunny, clear skies, calm",
                                        "HOT, LIGHT BREEZE, CLEAR SKIES",
                                        "Cold, cloudy, light breeze",
                                        "Cool, cloudy, light breeze",
                                        "WARM, LIGHT BREEZE, CLEAR SKIES",
                                        0,
                                        "Warm, partly cloudy and light breeze.",
                                        "Hot, partly cloudy and light breeze.",
                                        "Warm, cloudy and light breeze.",
                                        "Overcast, wind, rain and cold.",
                                        "Cool, cloudy, calm and medium precipitation",
                                        "partly cloudy, warm and light breeze",
                                        "Warm, clear, calm and light precipitation",
                                        "Cool, clear, light breeze, light precipitation",
                                        "Hot, clear and calm",
                                        "*Text",
                                        "Hot, cloudy, clam winds and humid."
                                    ]
                                },
                                {
                                    "name": "Niobium",
                                    "type": "NUMBER",
                                    "max": 248
                                },
                                {
                                    "name": "Samarium",
                                    "type": "NUMBER",
                                    "max": 164.6
                                },
                                {
                                    "name": "Europium",
                                    "type": "NUMBER",
                                    "max": 10.4
                                },
                                {
                                    "name": "Bismuth",
                                    "type": "NUMBER",
                                    "max": 500
                                },
                                {
                                    "name": "Lanthanum",
                                    "type": "NUMBER",
                                    "max": 1651
                                },
                                {
                                    "name": "Dysprosium",
                                    "type": "NUMBER",
                                    "max": 74
                                },
                                {
                                    "name": "Hafnium",
                                    "type": "NUMBER",
                                    "max": 209.1
                                },
                                {
                                    "name": "Gold",
                                    "type": "NUMBER",
                                    "max": 3.43
                                },
                                {
                                    "name": "Cerium",
                                    "type": "NUMBER",
                                    "max": 2511
                                },
                                {
                                    "name": "General observation (text)",
                                    "type": "STRING",
                                    "values": [
                                        "See Remark for TEXT",
                                        "*Text"
                                    ]
                                },
                                {
                                    "name": "Thorium-232",
                                    "type": "NUMBER",
                                    "max": 501.2
                                },
                                {
                                    "name": "Ytterbium",
                                    "type": "NUMBER",
                                    "max": 85.4
                                },
                                {
                                    "name": "Cesium",
                                    "type": "NUMBER",
                                    "max": 21.3
                                },
                                {
                                    "name": "Tantalum",
                                    "type": "NUMBER",
                                    "max": 36.5
                                },
                                {
                                    "name": "Scandium",
                                    "type": "NUMBER",
                                    "max": 30.7
                                },
                                {
                                    "name": "Zirconium",
                                    "type": "NUMBER",
                                    "max": 3658
                                },
                                {
                                    "name": "Alkalinity, Carbonate as CaCO3",
                                    "type": "NUMBER",
                                    "max": 177
                                },
                                {
                                    "name": "Precipitation",
                                    "type": "NUMBER",
                                    "max": 0.79
                                },
                                {
                                    "name": "Light, underwater incident",
                                    "type": "NUMBER",
                                    "min": 0.4,
                                    "max": 72
                                },
                                {
                                    "name": "Phosphate-phosphorus",
                                    "type": "NUMBER",
                                    "max": 1040
                                },
                                {
                                    "name": "Coliform/Streptococcus ratio, fecal",
                                    "type": "NUMBER",
                                    "max": 1.655
                                },
                                {
                                    "name": "Temperature, air",
                                    "type": "NUMBER",
                                    "min": -27,
                                    "max": 1833
                                },
                                {
                                    "name": "Inorganic nitrogen (nitrate and nitrite) as N",
                                    "type": "NUMBER",
                                    "max": 430
                                },
                                {
                                    "name": "Chlorine",
                                    "type": "NUMBER",
                                    "max": 97
                                },
                                {
                                    "name": "True color",
                                    "type": "NUMBER",
                                    "max": 68
                                },
                                {
                                    "name": "Orthophosphate as P",
                                    "type": "NUMBER",
                                    "max": 15.5
                                },
                                {
                                    "name": "Plutonium-239 and/or plutonium-240",
                                    "type": "NUMBER",
                                    "min": -0.0122,
                                    "max": 0.0716
                                },
                                {
                                    "name": "Plutonium-238",
                                    "type": "NUMBER",
                                    "min": -0.0268,
                                    "max": 0.0588
                                },
                                {
                                    "name": "Americium-241",
                                    "type": "NUMBER",
                                    "max": 0.141
                                },
                                {
                                    "name": "pH, lab",
                                    "type": "NUMBER",
                                    "min": 7.186,
                                    "max": 7.755
                                },
                                {
                                    "name": "Gran acid neutralizing capacity",
                                    "type": "NUMBER",
                                    "min": 63,
                                    "max": 5998.37
                                },
                                {
                                    "name": "Conductivity",
                                    "type": "NUMBER",
                                    "max": 12124.6
                                },
                                {
                                    "name": "Selenate",
                                    "type": "NUMBER",
                                    "max": 317
                                },
                                {
                                    "name": "Selenite",
                                    "type": "NUMBER",
                                    "max": 3.5
                                },
                                {
                                    "name": "Ammonium",
                                    "type": "NUMBER",
                                    "max": 10.6
                                },
                                {
                                    "name": "Uranium-238",
                                    "type": "NUMBER",
                                    "max": 230
                                },
                                {
                                    "name": "Total Phosphorus, mixed forms",
                                    "type": "NUMBER",
                                    "max": 805
                                },
                                {
                                    "name": "Moisture content",
                                    "type": "NUMBER",
                                    "min": 18,
                                    "max": 98
                                },
                                {
                                    "name": "Titanium",
                                    "type": "NUMBER",
                                    "max": 19340
                                },
                                {
                                    "name": "Fecal Streptococcus Group Bacteria",
                                    "type": "NUMBER",
                                    "max": 140000
                                },
                                {
                                    "name": "Dissolved oxygen saturation",
                                    "type": "NUMBER",
                                    "min": -9,
                                    "max": 7034.2
                                },
                                {
                                    "name": "Total solids",
                                    "type": "NUMBER",
                                    "max": 43900
                                },
                                {
                                    "name": "Phosphate-phosphorus as P",
                                    "type": "NUMBER",
                                    "max": 504
                                },
                                {
                                    "name": "Radium-226",
                                    "type": "NUMBER",
                                    "max": 300
                                },
                                {
                                    "name": "Gross alpha radioactivity, (Thorium-230 ref std)",
                                    "type": "NUMBER",
                                    "max": 224
                                },
                                {
                                    "name": "Gross beta radioactivity, (Cesium-137 ref std)",
                                    "type": "NUMBER",
                                    "max": 140
                                },
                                {
                                    "name": "Flow",
                                    "type": "NUMBER",
                                    "min": -999,
                                    "max": 33370
                                },
                                {
                                    "name": "Chemical oxygen demand",
                                    "type": "NUMBER",
                                    "max": 18000
                                },
                                {
                                    "name": "MBAS",
                                    "type": "NUMBER",
                                    "max": 10
                                },
                                {
                                    "name": "Ammonia-nitrogen",
                                    "type": "NUMBER",
                                    "max": 826
                                },
                                {
                                    "name": "Orthophosphate as PO4",
                                    "type": "NUMBER",
                                    "max": 52.34
                                },
                                {
                                    "name": "Ammonia-nitrogen as N",
                                    "type": "NUMBER",
                                    "max": 384
                                },
                                {
                                    "name": "Calcium as CaCO3",
                                    "type": "NUMBER",
                                    "min": 2,
                                    "max": 1700
                                },
                                {
                                    "name": "Total volatile solids",
                                    "type": "NUMBER",
                                    "max": 6302
                                },
                                {
                                    "name": "Fecal Coliform",
                                    "type": "NUMBER",
                                    "max": 20000000
                                },
                                {
                                    "name": "Biochemical oxygen demand, standard conditions",
                                    "type": "NUMBER",
                                    "max": 520
                                },
                                {
                                    "name": "Biomass, periphyton",
                                    "type": "NUMBER",
                                    "max": 2893
                                },
                                {
                                    "name": "Cloud cover (percent)",
                                    "type": "NUMBER",
                                    "max": 100
                                },
                                {
                                    "name": "Wind velocity",
                                    "type": "NUMBER",
                                    "max": 30
                                },
                                {
                                    "name": "Water content of snow",
                                    "type": "NUMBER",
                                    "min": 7,
                                    "max": 50
                                },
                                {
                                    "name": "Depth, snow cover",
                                    "type": "NUMBER",
                                    "min": 19,
                                    "max": 143
                                },
                                {
                                    "name": "Sulfur-34/Sulfur-32 ratio",
                                    "type": "NUMBER",
                                    "min": -22.9,
                                    "max": 15.5
                                },
                                {
                                    "name": "Beryllium",
                                    "type": "NUMBER",
                                    "max": 61.6
                                },
                                {
                                    "name": "Cobalt",
                                    "type": "NUMBER",
                                    "max": 126000
                                },
                                {
                                    "name": "Thallium",
                                    "type": "NUMBER",
                                    "max": 171000
                                },
                                {
                                    "name": "Strontium",
                                    "type": "NUMBER",
                                    "max": 13800
                                },
                                {
                                    "name": "Vanadium",
                                    "type": "NUMBER",
                                    "max": 45700
                                },
                                {
                                    "name": "Antimony",
                                    "type": "NUMBER",
                                    "max": 42500
                                },
                                {
                                    "name": "Lithium",
                                    "type": "NUMBER",
                                    "max": 9600
                                },
                                {
                                    "name": "Nitrogen-15/14 ratio",
                                    "type": "NUMBER",
                                    "min": -2.58,
                                    "max": 60.44
                                },
                                {
                                    "name": "Bromide",
                                    "type": "NUMBER",
                                    "max": 560
                                },
                                {
                                    "name": "Depth",
                                    "type": "NUMBER",
                                    "max": 8350
                                },
                                {
                                    "name": "UV 254",
                                    "type": "NUMBER",
                                    "max": 18.4
                                },
                                {
                                    "name": "Inorganic carbon",
                                    "type": "NUMBER",
                                    "max": 44.67
                                },
                                {
                                    "name": "Carbon",
                                    "type": "NUMBER",
                                    "max": 2100
                                },
                                {
                                    "name": "Nitrogen",
                                    "type": "NUMBER",
                                    "max": 1708
                                },
                                {
                                    "name": "Barium",
                                    "type": "NUMBER",
                                    "max": 941000
                                },
                                {
                                    "name": "Cyanide",
                                    "type": "NUMBER",
                                    "max": 154
                                },
                                {
                                    "name": "Chromium(VI)",
                                    "type": "NUMBER",
                                    "max": 160
                                },
                                {
                                    "name": "Inorganic nitrogen",
                                    "type": "NUMBER",
                                    "max": 8.3
                                },
                                {
                                    "name": "Suspended Sediment Concentration (SSC)",
                                    "type": "NUMBER",
                                    "max": 321000
                                },
                                {
                                    "name": "Suspended Sediment Discharge",
                                    "type": "NUMBER",
                                    "max": 395000
                                },
                                {
                                    "name": "Sediment",
                                    "type": "NUMBER",
                                    "max": 329
                                },
                                {
                                    "name": "Sulfur Sulfate",
                                    "type": "NUMBER",
                                    "max": 6030
                                },
                                {
                                    "name": "Bacteria mix, unspecified",
                                    "type": "NUMBER",
                                    "max": 13000
                                },
                                {
                                    "name": "Alkalinity, bicarbonate",
                                    "type": "NUMBER",
                                    "max": 1190
                                },
                                {
                                    "name": "Ammonia",
                                    "type": "NUMBER",
                                    "max": 140
                                },
                                {
                                    "name": "Sulfide",
                                    "type": "NUMBER",
                                    "max": 46
                                },
                                {
                                    "name": "Alkalinity, carbonate",
                                    "type": "NUMBER",
                                    "max": 240
                                },
                                {
                                    "name": "Alkalinity, Hydroxide",
                                    "type": "STRING",
                                    "max": 20
                                },
                                {
                                    "name": "Biomass, plankton",
                                    "type": "NUMBER",
                                    "min": 1270,
                                    "max": 1370
                                },
                                {
                                    "name": "Deuterium/Hydrogen ratio",
                                    "type": "NUMBER",
                                    "min": -172,
                                    "max": -48
                                },
                                {
                                    "name": "Oxygen-18/Oxygen-16 ratio",
                                    "type": "NUMBER",
                                    "min": -25.88,
                                    "max": 81.4
                                },
                                {
                                    "name": "Hardness, non-carbonate",
                                    "type": "NUMBER",
                                    "max": 7460
                                },
                                {
                                    "name": "Fluoride",
                                    "type": "NUMBER",
                                    "max": 1340
                                },
                                {
                                    "name": "Boron",
                                    "type": "NUMBER",
                                    "max": 9500
                                },
                                {
                                    "name": "Total suspended solids",
                                    "type": "NUMBER",
                                    "max": 164000
                                },
                                {
                                    "name": "Kjeldahl nitrogen",
                                    "type": "NUMBER",
                                    "max": 8000
                                },
                                {
                                    "name": "Sodium adsorption ratio [(Na)/(sq root of 1/2 Ca + Mg)]",
                                    "type": "NUMBER",
                                    "max": 220
                                },
                                {
                                    "name": "Sodium, percent total cations",
                                    "type": "NUMBER",
                                    "max": 270
                                },
                                {
                                    "name": "Sulfate",
                                    "type": "NUMBER",
                                    "max": 30300
                                },
                                {
                                    "name": "Chromium",
                                    "type": "NUMBER",
                                    "max": 37300
                                },
                                {
                                    "name": "Nickel",
                                    "type": "NUMBER",
                                    "max": 80100
                                },
                                {
                                    "name": "Temperature, air, deg C",
                                    "type": "NUMBER",
                                    "min": -100,
                                    "max": 90
                                },
                                {
                                    "name": "Height, gage",
                                    "type": "NUMBER",
                                    "min": -1.15,
                                    "max": 9375
                                },
                                {
                                    "name": "Uranium",
                                    "type": "NUMBER",
                                    "max": 2980
                                },
                                {
                                    "name": "Stream flow, mean_ daily",
                                    "type": "NUMBER",
                                    "max": 16000
                                },
                                {
                                    "name": "Organic Nitrogen",
                                    "type": "NUMBER",
                                    "max": 290
                                },
                                {
                                    "name": "Inorganic nitrogen (nitrate and nitrite)",
                                    "type": "NUMBER",
                                    "max": 823
                                },
                                {
                                    "name": "Orthophosphate",
                                    "type": "NUMBER",
                                    "max": 340
                                },
                                {
                                    "name": "Nitrate",
                                    "type": "NUMBER",
                                    "max": 12750
                                },
                                {
                                    "name": "Nitrite",
                                    "type": "NUMBER",
                                    "max": 48.05
                                },
                                {
                                    "name": "Pheophytin a",
                                    "type": "NUMBER",
                                    "max": 131300
                                },
                                {
                                    "name": "Chlorophyll a",
                                    "type": "NUMBER",
                                    "max": 227000
                                },
                                {
                                    "name": "Total Coliform",
                                    "type": "NUMBER",
                                    "max": 13000000
                                },
                                {
                                    "name": "Ammonia and ammonium",
                                    "type": "NUMBER",
                                    "max": 69.5
                                },
                                {
                                    "name": "Organic carbon",
                                    "type": "NUMBER",
                                    "max": 27000
                                },
                                {
                                    "name": "Phosphorus",
                                    "type": "NUMBER",
                                    "min": -0.0079,
                                    "max": 17000
                                },
                                {
                                    "name": "Nitrogen, mixed forms (NH3), (NH4), organic, (NO2) and (NO3)",
                                    "type": "NUMBER",
                                    "max": 14707
                                },
                                {
                                    "name": "Mercury",
                                    "type": "NUMBER",
                                    "max": 410
                                },
                                {
                                    "name": "Turbidity",
                                    "type": "NUMBER",
                                    "min": -7.8,
                                    "max": 13000
                                },
                                {
                                    "name": "Hydroxide",
                                    "type": "NUMBER",
                                    "max": 645
                                },
                                {
                                    "name": "Escherichia coli",
                                    "type": "NUMBER",
                                    "max": 130000
                                },
                                {
                                    "name": "RBP Stream width",
                                    "type": "NUMBER",
                                    "max": 1320
                                },
                                {
                                    "name": "Barometric pressure",
                                    "type": "NUMBER",
                                    "max": 1028
                                },
                                {
                                    "name": "Specific conductance",
                                    "type": "NUMBER",
                                    "min": -99,
                                    "max": 280000
                                },
                                {
                                    "name": "Acidity, (H+)",
                                    "type": "NUMBER",
                                    "max": 84400
                                },
                                {
                                    "name": "Oxygen",
                                    "type": "NUMBER",
                                    "max": 74200
                                },
                                {
                                    "name": "Carbon dioxide",
                                    "type": "NUMBER",
                                    "max": 21900
                                },
                                {
                                    "name": "Carbonate",
                                    "type": "NUMBER",
                                    "min": -4.49,
                                    "max": 543
                                },
                                {
                                    "name": "Bicarbonate",
                                    "type": "NUMBER",
                                    "max": 5090
                                },
                                {
                                    "name": "Oil and Grease",
                                    "type": "NUMBER",
                                    "max": 61
                                },
                                {
                                    "name": "Detergent, severity (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "None",
                                        "Mild",
                                        "Moderate",
                                        "Serious",
                                        "Extreme"
                                    ]
                                },
                                {
                                    "name": "Floating Garbage Severity (choice List)",
                                    "type": "STRING",
                                    "values": [
                                        "None",
                                        "Mild",
                                        "Moderate",
                                        "Extreme",
                                        "Serious"
                                    ]
                                },
                                {
                                    "name": "Floating algae mat - severity (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "NONE",
                                        "MILD",
                                        "MODERATE",
                                        "Mild",
                                        "None",
                                        "Serious",
                                        "Moderate",
                                        "Extreme"
                                    ]
                                },
                                {
                                    "name": "Odor, atmospheric",
                                    "type": "STRING",
                                    "values": [
                                        "None",
                                        "Mild",
                                        "Moderate",
                                        "Serious",
                                        "Extreme"
                                    ]
                                },
                                {
                                    "name": "Fish Kill, Severity (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "NONE",
                                        "None",
                                        "Mild",
                                        "Moderate"
                                    ]
                                },
                                {
                                    "name": "Floating debris - severity (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "NONE",
                                        "MILD",
                                        "SERIOUS",
                                        "MODERATE",
                                        "None",
                                        "Mild",
                                        "Moderate",
                                        "Extreme",
                                        "Serious"
                                    ]
                                },
                                {
                                    "name": "Turbidity severity (choice list)",
                                    "type": "STRING",
                                    "values": [
                                        "MILD",
                                        "NONE",
                                        "MODERATE",
                                        "SERIOUS",
                                        "None",
                                        "Serious",
                                        "Extreme",
                                        "Moderate",
                                        "Mild"
                                    ]
                                },
                                {
                                    "name": "Stream flow, instantaneous",
                                    "type": "NUMBER",
                                    "max": 26100
                                },
                                {
                                    "name": "Alkalinity",
                                    "type": "NUMBER",
                                    "min": -23.9,
                                    "max": 4170
                                },
                                {
                                    "name": "RBP High water mark",
                                    "type": "NUMBER",
                                    "min": -0.01,
                                    "max": 369
                                },
                                {
                                    "name": "pH",
                                    "type": "NUMBER",
                                    "min": -9,
                                    "max": 7348
                                },
                                {
                                    "name": "Hardness, Ca, Mg",
                                    "type": "NUMBER",
                                    "min": -7.99999,
                                    "max": 20762.8158
                                },
                                {
                                    "name": "Temperature, sample",
                                    "type": "NUMBER",
                                    "min": -15,
                                    "max": 43
                                },
                                {
                                    "name": "Dissolved oxygen (DO)",
                                    "type": "NUMBER",
                                    "min": -9,
                                    "max": 8096
                                },
                                {
                                    "name": "Alkalinity, Phenolphthalein (total hydroxide+1/2 carbonate)",
                                    "type": "NUMBER",
                                    "min": -3e-06,
                                    "max": 120
                                },
                                {
                                    "name": "Elevation, MSL",
                                    "type": "NUMBER",
                                    "min": 3901,
                                    "max": 9730
                                },
                                {
                                    "name": "Sulfate as SO4",
                                    "type": "NUMBER",
                                    "max": 39100
                                },
                                {
                                    "name": "Arsenic",
                                    "type": "NUMBER",
                                    "min": -10,
                                    "max": 1990000
                                },
                                {
                                    "name": "Magnesium",
                                    "type": "NUMBER",
                                    "max": 978245
                                },
                                {
                                    "name": "Chloride",
                                    "type": "NUMBER",
                                    "min": -1,
                                    "max": 38000
                                },
                                {
                                    "name": "Hardness, carbonate",
                                    "type": "NUMBER",
                                    "max": 14000
                                },
                                {
                                    "name": "Alkalinity, total",
                                    "type": "NUMBER",
                                    "min": -4.39,
                                    "max": 3800
                                },
                                {
                                    "name": "Copper",
                                    "type": "NUMBER",
                                    "min": -0.05,
                                    "max": 3720000
                                },
                                {
                                    "name": "Sodium",
                                    "type": "NUMBER",
                                    "max": 900022
                                },
                                {
                                    "name": "Total dissolved solids",
                                    "type": "NUMBER",
                                    "max": 115000
                                },
                                {
                                    "name": "Potassium",
                                    "type": "NUMBER",
                                    "min": -5,
                                    "max": 825400
                                },
                                {
                                    "name": "Aluminum",
                                    "type": "NUMBER",
                                    "min": -0.3,
                                    "max": 1920000
                                },
                                {
                                    "name": "Silica",
                                    "type": "NUMBER",
                                    "max": 71200
                                },
                                {
                                    "name": "Calcium",
                                    "type": "NUMBER",
                                    "max": 9346605
                                },
                                {
                                    "name": "Lead",
                                    "type": "NUMBER",
                                    "max": 11900000
                                },
                                {
                                    "name": "Silicon",
                                    "type": "NUMBER",
                                    "max": 43000
                                },
                                {
                                    "name": "Manganese",
                                    "type": "NUMBER",
                                    "max": 2510000
                                },
                                {
                                    "name": "Molybdenum",
                                    "type": "NUMBER",
                                    "max": 86000
                                },
                                {
                                    "name": "Cadmium",
                                    "type": "NUMBER",
                                    "max": 201000
                                },
                                {
                                    "name": "Zinc",
                                    "type": "NUMBER",
                                    "max": 3155500
                                },
                                {
                                    "name": "Iron",
                                    "type": "NUMBER",
                                    "max": 12440000
                                },
                                {
                                    "name": "Selenium",
                                    "type": "NUMBER",
                                    "max": 174000
                                },
                                {
                                    "name": "Silver",
                                    "type": "NUMBER",
                                    "min": -0.0025,
                                    "max": 53800
                                },
                                {
                                    "name": "Temperature, water",
                                    "type": "NUMBER",
                                    "min": -17.77775,
                                    "max": 805
                                }
                                ]
        }
    )


def main():
    print("Hello World")
    addMetadataToCollection()
    # db.Metadata.deleteOne({ "_id" : ObjectId("624ef2442c59c223bd7071c6")})


if __name__ == "__main__":
    main()
